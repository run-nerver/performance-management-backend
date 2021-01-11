from flask import Blueprint, request, current_app, send_from_directory
import xlrd, os, time
from app import db
from app.models.rules import Rules
from app.models.setting import Settings
from app.models.teaching_workload import TeachingWorkload
from app.models.user import User
from app.utils.pinyin import get_acronym
from app.utils.response import response_data
from app.utils.teaching_workload import teaching_workload_to_dict_no_year
from app.utils.token import auth
from app.utils import response as resp
from app.utils.utils import workload_options_to_dict, coefficient_to_dict, user_to_dict

config_bp = Blueprint('config_bp', __name__)
today = time.strftime("%Y-%m-%d", time.localtime())


# 管理员设定工作量类别
@config_bp.route('/config/createWorkload', methods=['POST'])
@auth.login_required
def create_workload():
    data = request.get_json()
    info = Rules(workload_name=data['display_name'], key_name=data['display_name'], score=data['score'])
    db.session.add(info)
    db.session.commit()
    return {
        "code": 20000,
        "data": info.to_json()
    }


# 获取工作量类别
@config_bp.route('/config/workLoadOptions', methods=['GET'])
@auth.login_required
def workload_options():
    info = Rules.query.all()
    res = workload_options_to_dict(info)
    return {
        "code": 20000,
        "data": res
    }


# 获取工作量类别（分页）
@config_bp.route('/config/workLoadOptionsPaginate', methods=['GET'])
@auth.login_required
def workload_options_paginate():
    data = request.args
    infos = Rules.query.paginate(int(data['page']), int(data['limit']))
    res = workload_options_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 删除工作量类别
@config_bp.route('/config/deleteWorkloadOptions', methods=['POST'])
@auth.login_required
def workload_workloadDelete():
    id = request.args
    info = Rules.query.get(id['id'])
    db.session.delete(info)
    db.session.commit()
    return response_data(resp.SUCCESS)


# 更新工作量类别
@config_bp.route('/config/updateWorkloadOptions', methods=['POST'])
@auth.login_required
def workload_workloadUpdate():
    data = request.get_json()
    info = Rules.query.get(data['id'])
    info.workload_name = data['display_name']
    info.key_name = data['display_name']
    info.score = data['score']
    db.session.commit()
    return {
        "code": 20000,
        "data": {
            "items": info.to_json()
        }
    }


# 获取用户信息
@config_bp.route('/config/fetchUserInfo', methods=['GET'])
@auth.login_required
def fetch_UserInfo():
    param = []
    data = request.args
    if ('name' in data) and data['name']:
        param.append(User.name.like('%' + data['name'] + '%'))
    if ('jobCatecory' in data) and data['jobCatecory']:
        param.append(User.job_catecory == data['jobCatecory'])
    if ('teacherTitle' in data) and data['teacherTitle']:
        param.append(User.teacher_title == data['teacherTitle'])
    infos = User.query.filter(*param) \
        .paginate(int(data['page']), int(data['limit']))
    res = teaching_workload_to_dict_no_year(infos.items)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 添加用户
@config_bp.route('/config/addUser', methods=['POST'])
@auth.login_required
def addUser():
    data = request.get_json()
    teacher_title_num = Settings.query.filter_by(name=data['teacherTitle']).first()
    teacher_postion_num = Settings.query.filter_by(name=data['teacherPostion']).first()
    user = User(
        username=get_acronym(data['name']),
        password='123456',
        department=data['department'],
        name=data['name'],
        auth=1,
        work_number=data['workNumber'],
        teacher_title=data['teacherTitle'],
        job_catecory=data['jobCatecory'],
        teacher_postion=data['teacherPostion'],
        teacher_title_num=teacher_title_num.coefficient,
        teacher_postion_num=teacher_postion_num.coefficient,
        postion_status=data['postionStatus'] if data['postionStatus'] else '无'
    )
    db.session.add(user)
    db.session.commit()
    return {
        "code": 20000,
        "data": user.to_json()
    }


# 删除用户
@config_bp.route('/config/deleteUser', methods=['POST'])
@auth.login_required
def deleteUser():
    id = request.args
    user = User.query.get(id['id'])
    db.session.delete(user)
    db.session.commit()
    return response_data(resp.SUCCESS)


# 更新用户信息
@config_bp.route('/config/updateUser', methods=['POST'])
@auth.login_required
def updateUser():
    data = request.get_json()
    info = User.query.get(data['id'])
    info.username = get_acronym(data['name'])
    info.department = data['department']
    info.name = data['name']
    info.work_number = data['workNumber']
    info.teacher_title = data['teacherTitle']
    info.job_catecory = data['jobCatecory']
    info.teacher_postion = data['teacherPostion']
    teacher_title_num = Settings.query.filter_by(name=data['teacherTitle']).first()
    info.teacher_title_num = teacher_title_num.coefficient if teacher_title_num else 0
    teacher_postion_num = Settings.query.filter_by(name=data['teacherPostion']).first()
    info.teacher_postion_num = teacher_postion_num.coefficient if teacher_postion_num else 0
    info.postion_status = data['postionStatus']
    db.session.commit()
    return {
        "code": 20000,
        "data": {
            "items": info.to_json()
        }
    }


# 批量添加用户信息
@config_bp.route('/config/UploadExcelCreateUser', methods=['POST'])
@auth.login_required
def upload_excel_create_user():
    file = request.files
    upload_excel = file.get('file')
    upload_excel.save(os.path.join(current_app.config['CONFIG_UPLOAD_PATH'],
                                   today + '-' + upload_excel.filename))
    excel_file = os.path.join(os.path.join(current_app.config['CONFIG_UPLOAD_PATH'],
                                           today + '-' + upload_excel.filename))
    excel_file = xlrd.open_workbook(excel_file)
    sheet = excel_file.sheet_by_name("Sheet1")
    for r in range(1, sheet.nrows):
        work_number = int(sheet.cell(r, 0).value)
        name = sheet.cell(r, 1).value
        job_catecory = sheet.cell(r, 2).value
        teacher_title = sheet.cell(r, 3).value
        teacher_postion = sheet.cell(r, 4).value if sheet.cell(r, 4).value else '无'
        department = sheet.cell(r, 5).value
        teacher_title_num = Settings.query.filter_by(name=teacher_title).first()  # 职称系数
        teacher_postion_num = teacher_title_num if job_catecory == '教学辅助岗' \
            else Settings.query.filter_by(name=teacher_postion).first()  # 职级系数
        info = User.query.filter_by(work_number=work_number).first()
        if info:
            info.name = name
            info.job_catecory = job_catecory
            info.teacher_title = teacher_title
            info.department = department
            info.teacher_postion = teacher_postion
            info.teacher_title_num = teacher_title_num.coefficient
            info.teacher_postion_num = teacher_postion_num.coefficient
        else:
            add_info = User(
                username=get_acronym(name),
                work_number=work_number,
                name=name,
                job_catecory=job_catecory,
                teacher_title=teacher_title,
                password=str(work_number),
                department=department,
                teacher_postion=teacher_postion,
                teacher_title_num=teacher_title_num.coefficient,
                teacher_postion_num=teacher_postion_num.coefficient
            )
            db.session.add(add_info)
    db.session.commit()
    infos = User.query.paginate(1, 10)
    res = user_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "items": res
        }
    }


# 获取系数（分页）
@config_bp.route('/config/coefficientPaginate', methods=['GET'])
@auth.login_required
def coefficient_paginate():
    param = []
    data = request.args
    if ('name' in data) and data['name']:
        param.append(Settings.name.like('%' + data['name'] + '%'))
    infos = Settings.query.filter(*param) \
        .paginate(int(data['page']), int(data['limit']))
    res = coefficient_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 添加系数
@config_bp.route('/config/createCoefficient', methods=['POST'])
@auth.login_required
def create_coefficient():
    data = request.get_json()
    info = Settings(name=data['name'], coefficient=data['coefficient'])
    db.session.add(info)
    db.session.commit()
    return {
        "code": 20000,
        "data": info.to_json()
    }


# 更新系数
@config_bp.route('/config/updateCoefficient', methods=['POST'])
@auth.login_required
def update_coefficient():
    data = request.get_json()
    info = Settings.query.get(data['id'])
    info.name = data['name']
    info.coefficient = data['coefficient']
    db.session.commit()
    return {
        "code": 20000,
        "data": {
            "items": info.to_json()
        }
    }


# 删除系数
@config_bp.route('/config/deleteCoefficient', methods=['POST'])
@auth.login_required
def delete_coefficient():
    id = request.args
    user = Settings.query.get(id['id'])
    db.session.delete(user)
    db.session.commit()
    return response_data(resp.SUCCESS)


# 确认教师教学工作量
@config_bp.route('/config/confirmModifyStatus', methods=['POST'])
@auth.login_required
def confirm_modify_status():
    id = request.args.get('id')
    info = TeachingWorkload.query.filter_by(id=id).first()
    if info.confirm_status == '未确认':
        info.confirm_status = '已确认'
        db.session.commit()
        return response_data(resp.SUCCESS)
    if info.confirm_status == '已确认':
        info.confirm_status = '未确认'
        db.session.commit()
        return response_data(resp.SUCCESS)


# 下载模板文件
@config_bp.route('/config/templateDownload', methods=['POST', 'GET'])
def download():
    filename = request.args.get('filename')
    from jixiao import app
    dirpath = os.path.join(app.root_path, 'uploads/configs')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True,
                               mimetype='text/csv')  # as_attachment=True 一定要写，不然会变成打开，而不是下载
