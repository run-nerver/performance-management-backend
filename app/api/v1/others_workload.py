import os, time

import xlrd
from flask import Blueprint, request, current_app

from app.models.others_workload import OthersWorkload

from app import db

from app.models.setting import Settings

from app.models.user import User
from app.utils.others import others_to_dict, others_to_dict_year

from app.utils.utils import float_to_decimal

from app.utils.token import auth

others_workload_bp = Blueprint('others_workload_bp', __name__)
today = time.strftime("%Y-%m-%d", time.localtime())


# 获取用户其他工作量
@others_workload_bp.route('/others_workload/fetchUserInfo', methods=['GET'])
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
    res = others_to_dict_year(infos.items, data['year'])
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 批量添加其他工作量
@others_workload_bp.route('/others_workload/UploadExcelOtherWorkload', methods=['POST'])
@auth.login_required
def upload_excel_create_user():
    year = request.args.get('year')
    file = request.files
    upload_excel = file.get('file')
    upload_excel.save(os.path.join(current_app.config['CONFIG_UPLOAD_PATH'],
                                   today + '-' + upload_excel.filename))
    excel_file = os.path.join(os.path.join(current_app.config['CONFIG_UPLOAD_PATH'],
                                           today + '-' + upload_excel.filename))
    excel_file = xlrd.open_workbook(excel_file)
    tem_money = Settings.query.filter_by(name='工作量金额').first()
    sheet = excel_file.sheet_by_name("Sheet1")
    for r in range(1, sheet.nrows):
        work_number = int(sheet.cell(r, 0).value)
        attendances = sheet.cell(r, 1).value if sheet.cell(r, 1).value else 0
        union_activities = sheet.cell(r, 2).value if sheet.cell(r, 2).value else 0
        ideological = sheet.cell(r, 3).value if sheet.cell(r, 3).value else 0
        news = sheet.cell(r, 4).value if sheet.cell(r, 4).value else 0
        counselors = sheet.cell(r, 5).value if sheet.cell(r, 5).value else 0
        characteristics_activities = sheet.cell(r, 6).value if sheet.cell(r, 6).value else 0
        mini_professional = sheet.cell(r, 7).value if sheet.cell(r, 7).value else 0
        information = sheet.cell(r, 8).value if sheet.cell(r, 8).value else 0
        undergraduatecolleges = sheet.cell(r, 9).value if sheet.cell(r, 9).value else 0
        graduation_design_manage = sheet.cell(r, 10).value if sheet.cell(r, 10).value else 0
        course_quality = sheet.cell(r, 11).value if sheet.cell(r, 11).value else 0
        organization = sheet.cell(r, 12).value if sheet.cell(r, 12).value else 0
        graduation_design_personal = sheet.cell(r, 13).value if sheet.cell(r, 13).value else 0
        professional_tab = sheet.cell(r, 14).value if sheet.cell(r, 14).value else 0
        mentor = sheet.cell(r, 15).value if sheet.cell(r, 15).value else 0
        discipline_competition = sheet.cell(r, 16).value if sheet.cell(r, 16).value else 0
        teaching_watch = sheet.cell(r, 17).value if sheet.cell(r, 17).value else 0
        competition_judges = sheet.cell(r, 18).value if sheet.cell(r, 18).value else 0
        union_work = sheet.cell(r, 19).value if sheet.cell(r, 19).value else 0
        extra_score = sheet.cell(r, 20).value if sheet.cell(r, 20).value else 0
        total_score = attendances + union_activities + ideological + news + counselors \
                      + characteristics_activities + mini_professional + information + undergraduatecolleges \
                      + graduation_design_manage + course_quality + organization + graduation_design_personal \
                      + professional_tab + mentor + discipline_competition + teaching_watch + competition_judges \
                      + union_work + extra_score
        total_money = float_to_decimal(total_score) * tem_money.coefficient
        info = User.query.filter_by(work_number=work_number).first()
        if info:
            if info.others_workload_user:
                info.others_workload_user.attendances = attendances,
                info.others_workload_user.union_activities = union_activities,
                info.others_workload_user.ideological = ideological,
                info.others_workload_user.news = news,
                info.others_workload_user.counselors = counselors,
                info.others_workload_user.characteristics_activities = characteristics_activities,
                info.others_workload_user.mini_professional = mini_professional,
                info.others_workload_user.information = information,
                info.others_workload_user.undergraduatecolleges = undergraduatecolleges,
                info.others_workload_user.graduation_design_manage = graduation_design_manage,
                info.others_workload_user.course_quality = course_quality,
                info.others_workload_user.organization = organization,
                info.others_workload_user.graduation_design_personal = graduation_design_personal,
                info.others_workload_user.professional_tab = professional_tab,
                info.others_workload_user.discipline_competition = discipline_competition,
                info.others_workload_user.teaching_watch = teaching_watch,
                info.others_workload_user.competition_judges = competition_judges,
                info.others_workload_user.union_work = union_work,
                info.others_workload_user.extra_score = extra_score,
                info.others_workload_user.year = year,
                info.others_workload_user.total_score = total_score,
                info.others_workload_user.total_money = total_money
            else:
                add_info = OthersWorkload(
                    attendances=attendances,
                    union_activities=union_activities,
                    ideological=ideological,
                    news=news,
                    counselors=counselors,
                    characteristics_activities=characteristics_activities,
                    mini_professional=mini_professional,
                    information=information,
                    undergraduatecolleges=undergraduatecolleges,
                    graduation_design_manage=graduation_design_manage,
                    course_quality=course_quality,
                    organization=organization,
                    graduation_design_personal=graduation_design_personal,
                    professional_tab=professional_tab,
                    mentor=mentor,
                    discipline_competition=discipline_competition,
                    teaching_watch=teaching_watch,
                    competition_judges=competition_judges,
                    union_work=union_work,
                    extra_score=extra_score,
                    year=year,
                    user_id=info.id,
                    total_score=total_score,
                    total_money=total_money
                )
                db.session.add(add_info)
    db.session.commit()
    infos = OthersWorkload.query.paginate(1, 10)
    res = others_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 更新用户其他工作量
@others_workload_bp.route('/others_workload/updateOthersWorkload', methods=['POST'])
@auth.login_required
def update_others_workload():
    data = request.get_json()
    id = data['oId']
    total_money = data['totalMoney']
    notes = data['notes']
    info = OthersWorkload.query.filter_by(id=id).first()
    info.total_money = total_money
    info.notes = notes
    db.session.commit()
    res = info.to_json()
    return {
        "code": 20000,
        "data": res
    }