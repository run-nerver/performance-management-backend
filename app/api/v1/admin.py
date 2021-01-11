from flask import Blueprint, request

from app import db

from app.models.user import User
from app.models.information import Information
from app.utils.counselors import single_counselors_to_dict_with_user
from app.utils.others import single_teacher_others_workload_to_dict
from app.utils.response import response_data
from app.utils.scientific import single_teacher_scientific_workload_to_dict
from app.utils.teaching_workload import single_teaching_workload_to_dict
from app.utils.token import auth

from app.utils.utils import teacher_workload_to_dict
from app.utils import response as resp

admin_bp = Blueprint('admin_bp', __name__)


# 教师工作量总表
@admin_bp.route('/admin/list', methods=['GET'])
@auth.login_required
def teacher_list():
    param = []
    data = request.args
    year = data.get('year')
    confirm_status = ''
    if ('name' in data) and data['name']:
        param.append(User.name.like('%' + data['name'] + '%'))
    if ('jobCatecory' in data) and data['jobCatecory']:
        param.append(User.job_catecory == data['jobCatecory'])
    if ('teacherTitle' in data) and data['teacherTitle']:
        param.append(User.teacher_title == data['teacherTitle'])
    if ('confirmStatus' in data) and data['confirmStatus']:
        confirm_status = data['confirmStatus']
    infos = User.query.filter(*param) \
        .paginate(int(data['page']), int(data['limit']))
    res = teacher_workload_to_dict(infos.items, year, confirm_status)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 管理员查看教师个人页面
@admin_bp.route('/admin/singleTeacher', methods=['POST'])
@auth.login_required
def single_teacher():
    data = request.args
    year = data.get('year')
    id = data.get('id')
    user_info = User.query.get(id)
    scientific_workload = []
    others_workload = []
    teaching_workload = []
    counselors_workload = []
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
            "totalWorkload": [total_workload],
            'counselorsWorkload': counselors_workload,
        }
    }


# 修改教师工作量状态
@admin_bp.route('/admin/modifyStatus/<id>', methods=['POST'])
@auth.login_required
def modifyStatus(id):
    uid = request.args.get('uid')
    info = Information.query.filter(Information.id == int(uid)).first()
    info.status = not info.status
    user = User.query.filter_by(id=id).first()
    if info.status == 1:
        user.workload += info.score
    if info.status == 0:
        user.workload -= info.score
    db.session.add(info, user)
    db.session.commit()

    return response_data(resp.SUCCESS)


# 批量审核教师工作量
@admin_bp.route('/admin/batchCheck/<id>', methods=['POST'])
@auth.login_required
def batchCheck(id):
    data = request.args
    for key, value in data.to_dict().items():
        info = Information.query.filter_by(id=value).first()
        if info.status == 0:
            info.status = 1
            user = User.query.filter_by(id=id).first()
            user.workload += info.score
            db.session.add(info, user)
            db.session.commit()
    return response_data(resp.SUCCESS)
