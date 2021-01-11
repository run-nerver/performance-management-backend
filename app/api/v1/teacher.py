import os, json

from flask import Blueprint, request, current_app, send_from_directory, g
from sqlalchemy import func
from app.models.rules import Rules

from app import db

from app.models.information import Information
from app.models.teaching_workload import TeachingWorkload
from app.models.user import User
from app.utils.counselors import single_counselors_to_dict_with_user
from app.utils.others import single_teacher_others_workload_to_dict
from app.utils.response import response_data
from app.utils.scientific import single_teacher_scientific_workload_to_dict
from app.utils.teaching_workload import single_teaching_workload_to_dict

from app.utils.utils import teacher_workload_to_dict
from app.utils import response as resp
from app.utils.token import auth

teacher_bp = Blueprint('teacher_bp', __name__)


# 个人教师工作量
@teacher_bp.route('/teacher/workload', methods=['GET'])
@auth.login_required
def teacher_workload():
    data = request.args
    totalNumber = Information.query.filter(Information.user_id == g.user.uid, Information.status == 1).count()
    totalScore = db.session.query(func.sum(Information.score)).filter(Information.status == 1,
                                                                      Information.user_id == g.user.uid).scalar()
    param = []
    param.append(Information.user_id == g.user.uid)
    if ('type' in data) and (data['type']):
        param.append(Information.type == data['type'])
    if ('title' in data) and (data['title']):
        param.append(Information.name.like('%' + data['title'] + '%'))
    if ('status' in data) and (data['status']):
        param.append(Information.status == int(data['status']))
    info = Information.query.filter(*param).paginate(int(data['page']), int(data['limit']))
    res = teacher_workload_to_dict(info.items)
    return {
        "code": 20000,
        "data": {
            "total": info.total,
            "items": res,
            "totalNumber": totalNumber,
            "totalScore": totalScore

        }
    }


# 教师上传支撑材料
@teacher_bp.route('/teacher/createInfo', methods=['POST'])
@auth.login_required
def teacher_createInfo():
    fileList = []
    file = request.files
    for f in file.getlist('file'):
        filename = f.filename
        f.save(os.path.join(current_app.config['FILE_UPLOAD_PATH'], filename))
        fileList.append(filename)
    data = request.form
    data = json.loads(data['body'])
    rule = Rules.query.filter_by(key_name=data['type']).first()
    info = Information(name=data['title'], type=data['type'], user_id=g.user.uid, status=0, rule_id=rule.id,
                       score=rule.score, filesUrl=','.join(fileList))
    db.session.add(info)
    db.session.commit()
    return {
        "code": 20000,
        "data": {
            "items": info.to_json(),
            "attList": info.file_to_list()
        }
    }


# 修改教师工作量
# todo 编辑初始点击后默认显示附件，如上传新附件后覆盖原有附件，没有上传直接修改对应表单值
@teacher_bp.route('/teacher/workloadUpdate', methods=['POST'])
@auth.login_required
def teacher_workloadUpdate():
    data = request.get_json()
    info = Information.query.get(data['id'])
    if info.type == data['type']:
        info.name = data['title']
    else:
        info.name = data['title']
        info.type = data['type']
        key = Rules.query.filter_by(key_name=data['type']).first()
        info.score = key.score
    db.session.commit()
    return {
        "code": 20000,
        "data": {
            "items": info.to_json()
        }
    }


# 删除教师工作量
# todo 删除对应附件
@teacher_bp.route('/teacher/deleteWorkload', methods=['POST'])
@auth.login_required
def teacher_workloadDelete():
    id = request.args
    info = Information.query.get(id['id'])
    db.session.delete(info)
    db.session.commit()
    return response_data(resp.SUCCESS)


# 上传文件 目测没用 测试
@teacher_bp.route('/teacher/fileUpload', methods=['POST'])
@auth.login_required
def teacher_fileUpload():
    file = request.files
    for f in file.getlist('file'):
        print(f)
        filename = f.filename
        f.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
    return "hello"


# 下载文件
@teacher_bp.route('/teacher/download', methods=['POST', 'GET'])
def download():
    filename = request.args.get('filename')
    from jixiao import app
    dirpath = os.path.join(app.root_path, 'uploads')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True,
                               mimetype='text/csv')  # as_attachment=True 一定要写，不然会变成打开，而不是下载


# 获取单独教师工作量（教师查看）
@teacher_bp.route('/teacher/singleUserInfo', methods=['POST'])
@auth.login_required
def single_user_info():
    r = request.args
    year = r.get('year')
    id = g.user.uid
    user_info = User.query.get(id)
    res = single_teaching_workload_to_dict(user_info, year)
    return {
        "code": 20000,
        "data": res
    }


# 获取单独教师所有工作量（教师首页）
@teacher_bp.route('/teacher/singleUserAllInfo', methods=['POST'])
@auth.login_required
def single_user_all_info():
    r = request.args
    year = r.get('year')
    id = g.user.uid
    user_info = User.query.get(id)
    scientific_workload = []
    others_workload = []
    teaching_workload = []
    counselors_workload= []
    total_workload = {}
    total_money = 0
    if user_info.teaching_workload_user:
        teaching_workload = single_teaching_workload_to_dict(user_info, year)
        if teaching_workload:
            total_money += teaching_workload[0]['totalMoney']
            total_workload['teachingWorkloadTotalMoney'] = teaching_workload[0]['totalMoney']
            total_workload['confirmStatus'] = teaching_workload[0]['confirmStatus']
            total_workload['totalId'] = teaching_workload[0]['tId']

    if user_info.scientific_workload_user:
        scientific_workload = single_teacher_scientific_workload_to_dict(user_info, year)
        if scientific_workload:
            res = [i['scientificMoney'] for i in scientific_workload]  # 列表返回当前教师当年科研奖励金额
            total_money += sum(res)
            total_workload['scientificWorkloadTotalMoney'] = sum(res)
    if user_info.others_workload_user:
        others_workload = single_teacher_others_workload_to_dict(user_info, year)
        if others_workload:
            total_money += others_workload[0]['totalMoney']
            total_workload['othersWorkloadTotalMoney'] = others_workload[0]['totalMoney']
    if user_info.counselors_workload_user:
        counselors_workload = single_counselors_to_dict_with_user(user_info, year)
        if counselors_workload:
            total_money += counselors_workload[0]['totalMoney']
            total_workload['counselorsWorkloadTotalMoney'] = counselors_workload[0]['totalMoney']
    total_workload['totalMoney'] = total_money
    total_workload['workNumber'] = user_info.work_number
    total_workload['name'] = user_info.name
    total_workload['jobCatecory'] = user_info.job_catecory
    total_workload['teacherTitle'] = user_info.teacher_title

    return {
        "code": 20000,
        "data": {
            "teachingWorkload": teaching_workload,
            "scientificWorkload": scientific_workload,
            "othersWorkload": others_workload,
            'counselorsWorkload': counselors_workload,
            "totalWorkload": [total_workload]
        }
    }


# 教师确认教学工作量
@teacher_bp.route('/teacher/confirmTeachingWorkload', methods=['POST'])
@auth.login_required
def confirm_teaching_workload():
    id = request.args.get('id')
    info = TeachingWorkload.query.filter_by(id=id).first()
    info.confirm_status = '已确认'
    db.session.commit()
    return response_data(resp.SUCCESS)
