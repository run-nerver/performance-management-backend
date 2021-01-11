import os, time

import xlrd
from flask import Blueprint, request, current_app, send_from_directory, g

from app import db

from app.models.setting import Settings
from app.models.teaching_workload import TeachingWorkload
from app.models.user import User
from app.utils.teaching_workload import single_teaching_workload_to_dict, teaching_workload_to_dict

from app.utils.utils import float_to_decimal

from app.utils.token import auth

teaching_workload_bp = Blueprint('teaching_workload_bp', __name__)
today = time.strftime("%Y-%m-%d", time.localtime())


# 获取用户教学工作量
@teaching_workload_bp.route('/teaching_workload/fetchUserInfo', methods=['GET'])
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
    # 传入year，返回对应年份的工作量
    res = teaching_workload_to_dict(infos.items, data['year'])
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 批量添加教学工作量
@teaching_workload_bp.route('/teaching_workload/UploadExcelTeachingWorkload', methods=['POST'])
@auth.login_required
def upload_excel_create_user():
    year = request.args.get('0')
    file = request.files
    upload_excel = file.get('file')
    teaching_qualified_workload = Settings.query.filter_by(name='教学合格工作量').first()
    teacher_postion_status_workload = Settings.query.filter_by(name='教研室主任').first()
    manage_beyond_workload = Settings.query.filter_by(name='管理岗超工作量').first()
    counsellor_beyond_workload = Settings.query.filter_by(name='辅导员岗超工作量').first()
    teaching_assistant_beyond_workload = Settings.query.filter_by(name='教辅岗超工作量').first()
    upload_excel.save(os.path.join(current_app.config['CONFIG_UPLOAD_PATH'],
                                   today + '-' + upload_excel.filename))
    excel_file = os.path.join(os.path.join(current_app.config['CONFIG_UPLOAD_PATH'],
                                           today + '-' + upload_excel.filename))
    excel_file = xlrd.open_workbook(excel_file)
    sheet = excel_file.sheet_by_name("Sheet1")
    for r in range(1, sheet.nrows):
        work_number = int(sheet.cell(r, 0).value)
        name = sheet.cell(r, 1).value
        teaching_workload = float_to_decimal(sheet.cell(r, 2).value if sheet.cell(r, 2).value else 0)
        teaching_excellent_workload = float_to_decimal(
            sheet.cell(r, 3).value if sheet.cell(r, 3).value else 0)
        info = User.query.filter_by(work_number=work_number).first()
        if info:
            if info.job_catecory == '教学岗':
                if info.postion_status == '教研室主任':
                    add_info = TeachingWorkload(
                        user_id=info.id,
                        teaching_workload=teaching_workload,
                        teaching_qualified_workload=teacher_postion_status_workload.coefficient,
                        teaching_excellent_workload=teaching_excellent_workload,
                        teaching_beyond_workload=teaching_workload - teacher_postion_status_workload.coefficient + teaching_excellent_workload,
                        year=year
                    )
                    db.session.add(add_info)
                else:
                    # 非教研室主任
                    add_info = TeachingWorkload(
                        user_id=info.id,
                        teaching_workload=teaching_workload,
                        teaching_qualified_workload=teaching_qualified_workload.coefficient,
                        teaching_excellent_workload=teaching_excellent_workload,
                        teaching_beyond_workload=teaching_workload - teaching_qualified_workload.coefficient + teaching_excellent_workload,
                        year=year
                    )
                    db.session.add(add_info)
            elif info.job_catecory == '管理岗':
                temp_teaching_beyond_workload = teaching_workload if teaching_workload < manage_beyond_workload.coefficient else manage_beyond_workload.coefficient
                add_info = TeachingWorkload(
                    user_id=info.id,
                    teaching_workload=teaching_workload,
                    teaching_qualified_workload=float_to_decimal(0),
                    teaching_excellent_workload=teaching_excellent_workload,
                    teaching_beyond_workload=temp_teaching_beyond_workload - 0 + teaching_excellent_workload,
                    year=year
                )
                db.session.add(add_info)
            elif info.job_catecory == '辅导员管理岗':
                temp_teaching_beyond_workload = teaching_workload if teaching_workload < counsellor_beyond_workload.coefficient else counsellor_beyond_workload.coefficient
                add_info = TeachingWorkload(
                    user_id=info.id,
                    teaching_workload=teaching_workload,
                    teaching_qualified_workload=float_to_decimal(0),
                    teaching_excellent_workload=teaching_excellent_workload,
                    teaching_beyond_workload=temp_teaching_beyond_workload - 0 + teaching_excellent_workload,
                    year=year
                )
                db.session.add(add_info)
            elif info.job_catecory == '教学辅助岗':
                temp_teaching_beyond_workload = teaching_workload if teaching_workload < teaching_assistant_beyond_workload.coefficient else teaching_assistant_beyond_workload.coefficient
                add_info = TeachingWorkload(
                    user_id=info.id,
                    teaching_workload=teaching_workload,
                    teaching_qualified_workload=float_to_decimal(0),
                    teaching_excellent_workload=teaching_excellent_workload,
                    teaching_beyond_workload=temp_teaching_beyond_workload - 0 + teaching_excellent_workload,
                    year=year
                )
                db.session.add(add_info)

    db.session.commit()
    infos = User.query.paginate(1, 10)
    res = teaching_workload_to_dict(infos.items, year)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 计算教学工作量
@teaching_workload_bp.route('/teaching_workload/CalcWorkload', methods=['POST'])
@auth.login_required
def calc_workload():
    year = request.args.get('0')  # 获取计算年份
    info = TeachingWorkload.query.filter_by(year=year).all()
    tem_money = Settings.query.filter_by(name='工作量金额').first()
    man_1 = Settings.query.filter_by(name='管理岗系数1').first()
    man_2 = Settings.query.filter_by(name='管理岗系数2').first()
    for i in info:
        temp_teaching_beyond_workload = i.teaching_beyond_workload
        if i.user_workload.job_catecory == '教学岗':
            if temp_teaching_beyond_workload > 500:
                i.teaching_beyond_workload_num = (500 + (temp_teaching_beyond_workload - 500) / 2) * \
                                                 i.user_workload.teacher_title_num
                i.teaching_beyond_workload_money = (500 + (temp_teaching_beyond_workload - 500) / 2) * \
                                                   i.user_workload.teacher_title_num * tem_money.coefficient
                i.total_money = (500 + (temp_teaching_beyond_workload - 500) / 2) * \
                                i.user_workload.teacher_title_num * tem_money.coefficient
                i.confirm_status = '未确认'
            else:
                i.teaching_beyond_workload_num = temp_teaching_beyond_workload * \
                                                 i.user_workload.teacher_title_num
                i.teaching_beyond_workload_money = temp_teaching_beyond_workload * \
                                                   i.user_workload.teacher_title_num * tem_money.coefficient
                i.total_money = temp_teaching_beyond_workload * \
                                i.user_workload.teacher_title_num * tem_money.coefficient
                i.confirm_status = '未确认'
        # 非教学岗
        elif i.user_workload.job_catecory == '管理岗' or i.user_workload.job_catecory == '教学辅助岗' or i.user_workload.job_catecory == '辅导员管理岗':
            i.teaching_beyond_workload_num = temp_teaching_beyond_workload * \
                                             i.user_workload.teacher_title_num
            i.teaching_beyond_workload_money = temp_teaching_beyond_workload * \
                                               i.user_workload.teacher_title_num * tem_money.coefficient
            i.manage_beyond_workload_money = man_1.coefficient * man_2.coefficient * tem_money.coefficient * i.user_workload.teacher_postion_num
            i.total_money = (
                                    temp_teaching_beyond_workload * i.user_workload.teacher_title_num * tem_money.coefficient) + \
                            (
                                    man_1.coefficient * man_2.coefficient * tem_money.coefficient * i.user_workload.teacher_postion_num)
            i.confirm_status = '未确认'
    db.session.commit()
    infos = User.query.paginate(1, 10)
    res = teaching_workload_to_dict(infos.items, year)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 更新用户工作量
@teaching_workload_bp.route('/teaching_workload/updateUserWorkload', methods=['POST'])
@auth.login_required
def update_user_workload():
    data = request.get_json()
    year = data['year']
    info = User.query.get(data['id'])
    t_info = TeachingWorkload.query.filter_by(id=data['tId']).first()
    tem_money = Settings.query.filter_by(name='工作量金额').first()
    man_1 = Settings.query.filter_by(name='管理岗系数1').first()
    man_2 = Settings.query.filter_by(name='管理岗系数2').first()
    manage_beyond_workload = Settings.query.filter_by(name='管理岗超工作量').first()
    counsellor_beyond_workload = Settings.query.filter_by(name='辅导员岗超工作量').first()
    teaching_assistant_beyond_workload = Settings.query.filter_by(name='教辅岗超工作量').first()
    temp_teaching_beyond_workload = float_to_decimal(data['teachingWorkload']) - \
                                    float_to_decimal(data['teachingQualifiedWorkload']) + \
                                    float_to_decimal(data['teachingExcellentWorkload'])
    temp_teaching_workload = float_to_decimal(data['teachingWorkload'])  # 非教学岗教学工作量（非教学岗只看这个值超不超即可）
    if info.job_catecory == '教学岗':
        if temp_teaching_beyond_workload > 500:
            temp_teaching_beyond_workload_num = (500 + (
                    temp_teaching_beyond_workload - 500) / 2) * info.teacher_title_num
        else:
            temp_teaching_beyond_workload_num = temp_teaching_beyond_workload * info.teacher_title_num
        t_info.teaching_workload = float_to_decimal(data['teachingWorkload'])
        t_info.teaching_qualified_workload = float_to_decimal(data['teachingQualifiedWorkload'])
        t_info.teaching_excellent_workload = float_to_decimal(data['teachingExcellentWorkload'])
        t_info.notes = data['notes']
        t_info.teaching_beyond_workload = temp_teaching_beyond_workload
        t_info.teaching_beyond_workload_num = temp_teaching_beyond_workload_num
        t_info.teaching_beyond_workload_money = temp_teaching_beyond_workload_num * tem_money.coefficient
        t_info.total_money = temp_teaching_beyond_workload_num * tem_money.coefficient
    elif info.job_catecory == '管理岗':
        temp_teaching_beyond_workload = temp_teaching_workload if temp_teaching_workload < manage_beyond_workload.coefficient else manage_beyond_workload.coefficient
        t_info.teaching_workload = float_to_decimal(data['teachingWorkload'])
        t_info.teaching_qualified_workload = float_to_decimal(data['teachingQualifiedWorkload'])
        t_info.teaching_excellent_workload = float_to_decimal(data['teachingExcellentWorkload'])
        t_info.notes = data['notes']
        t_info.teaching_beyond_workload = temp_teaching_beyond_workload
        t_info.teaching_beyond_workload_num = temp_teaching_beyond_workload * info.teacher_title_num
        t_info.teaching_beyond_workload_money = temp_teaching_beyond_workload * info.teacher_title_num * tem_money.coefficient
        t_info.total_money = (temp_teaching_beyond_workload * info.teacher_title_num * tem_money.coefficient) + (
                man_1.coefficient * man_2.coefficient * tem_money.coefficient * info.teacher_postion_num)
    elif info.job_catecory == '辅导员管理岗':
        temp_teaching_beyond_workload = temp_teaching_workload if temp_teaching_workload < counsellor_beyond_workload.coefficient else counsellor_beyond_workload.coefficient
        t_info.teaching_workload = float_to_decimal(data['teachingWorkload'])
        t_info.teaching_qualified_workload = float_to_decimal(data['teachingQualifiedWorkload'])
        t_info.teaching_excellent_workload = float_to_decimal(data['teachingExcellentWorkload'])
        t_info.notes = data['notes']
        t_info.teaching_beyond_workload = temp_teaching_beyond_workload
        t_info.teaching_beyond_workload_num = temp_teaching_beyond_workload * info.teacher_title_num
        t_info.teaching_beyond_workload_money = temp_teaching_beyond_workload * info.teacher_title_num * tem_money.coefficient
        t_info.total_money = (temp_teaching_beyond_workload * info.teacher_title_num * tem_money.coefficient) + (
                man_1.coefficient * man_2.coefficient * tem_money.coefficient * info.teacher_postion_num)
    elif info.job_catecory == '教学辅助岗':
        temp_teaching_beyond_workload = temp_teaching_workload if temp_teaching_workload < teaching_assistant_beyond_workload.coefficient else teaching_assistant_beyond_workload.coefficient
        t_info.teaching_workload = float_to_decimal(data['teachingWorkload'])
        t_info.teaching_qualified_workload = float_to_decimal(data['teachingQualifiedWorkload'])
        t_info.teaching_excellent_workload = float_to_decimal(data['teachingExcellentWorkload'])
        t_info.notes = data['notes']
        t_info.teaching_beyond_workload = temp_teaching_beyond_workload
        t_info.teaching_beyond_workload_num = temp_teaching_beyond_workload * info.teacher_title_num
        t_info.teaching_beyond_workload_money = temp_teaching_beyond_workload * info.teacher_title_num * tem_money.coefficient
        t_info.total_money = (temp_teaching_beyond_workload * info.teacher_title_num * tem_money.coefficient) + (
                man_1.coefficient * man_2.coefficient * tem_money.coefficient * info.teacher_postion_num)
    db.session.commit()
    res = single_teaching_workload_to_dict(info, year)
    return {
        "code": 20000,
        "data": res[0]  # res是列表 res[0]是字典 这里返回字典前端才可以实时显示
    }
