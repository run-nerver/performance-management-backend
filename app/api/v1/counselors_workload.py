import os, time

import xlrd
from flask import Blueprint, request, current_app

from app.models.counselors_workload import CounselorsWorkload
from app.models.others_workload import OthersWorkload

from app import db

from app.models.setting import Settings

from app.models.user import User
from app.utils.counselors import counselors_to_dict, single_counselors_to_dict
from app.utils.others import others_to_dict, others_to_dict_year

from app.utils.utils import float_to_decimal

from app.utils.token import auth

counselors_workload_bp = Blueprint('counselors_workload_bp', __name__)
today = time.strftime("%Y-%m-%d", time.localtime())


# 获取辅导员工作量
@counselors_workload_bp.route('/counselors_workload/fetchUserInfo', methods=['GET'])
@auth.login_required
def fetch_UserInfo():
    param = []
    data = request.args
    if ('year' in data) and data['year']:
        param.append(CounselorsWorkload.year == data['year'])
    infos = CounselorsWorkload.query.filter(*param) \
        .paginate(int(data['page']), int(data['limit']))
    res = counselors_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "items": res
        }
    }


# 批量导入辅导员工作量
@counselors_workload_bp.route('/counselors_workload/UploadExcelCounselorsWorkload', methods=['POST'])
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
    sheet = excel_file.sheet_by_name("Sheet1")
    tem_money = Settings.query.filter_by(name='工作量金额').first()
    for r in range(1, sheet.nrows):
        work_number = int(sheet.cell(r, 0).value) if sheet.cell(r, 0).value else 0
        total_people = sheet.cell(r, 2).value if sheet.cell(r, 2).value else 0
        beyond_workload_people = sheet.cell(r, 3).value if sheet.cell(r, 3).value else 0
        months = sheet.cell(r, 4).value if sheet.cell(r, 4).value else 0
        counselors_beyond_workload = sheet.cell(r, 5).value if sheet.cell(r, 5).value else 0
        counselors_beyond_workload_score = sheet.cell(r, 6).value if sheet.cell(r, 6).value else 0
        students_money = sheet.cell(r, 7).value if sheet.cell(r, 7).value else 0
        counselors_beyond_workload_money = float_to_decimal(counselors_beyond_workload_score) * tem_money.coefficient
        total_money = counselors_beyond_workload_money + float_to_decimal(students_money)

        info = User.query.filter_by(work_number=work_number).first()
        if info:
            if info.counselors_workload_user:
                info.counselors_workload_user.total_people = total_people
                info.counselors_workload_user.beyond_workload_people = beyond_workload_people
                info.counselors_workload_user.months = months
                info.counselors_workload_user.counselors_beyond_workload = counselors_beyond_workload
                info.counselors_workload_user.counselors_beyond_workload_score = counselors_beyond_workload_score
                info.counselors_workload_user.students_money = students_money
                info.counselors_workload_user.total_money = total_money
                info.counselors_workload_user.counselors_beyond_workload_money = counselors_beyond_workload_money
                db.session.commit()
            else:
                add_info = CounselorsWorkload(
                    total_people=total_people,
                    beyond_workload_people=beyond_workload_people,
                    months=months,
                    counselors_beyond_workload=counselors_beyond_workload,
                    counselors_beyond_workload_score=counselors_beyond_workload_score,
                    students_money=students_money,
                    counselors_beyond_workload_money=counselors_beyond_workload_money,
                    total_money=total_money,
                    year=year,
                    user_id=info.id
                )
                db.session.add(add_info)
    db.session.commit()
    infos = CounselorsWorkload.query.paginate(1, 10)
    res = counselors_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "items": res
        }
    }

# 更新辅导员工作量
@counselors_workload_bp.route('/counselors_workload/updateCounselorsWorkload', methods=['POST'])
@auth.login_required
def update_counselors_workload():
    data = request.get_json()
    info = CounselorsWorkload.query.get(data['cId'])
    info.total_people = data['totalPeople']
    info.beyond_workload_people = data['beyondWorkloadPeople']
    info.counselors_beyond_workload = data['counselorsBeyondWorkload']
    info.counselors_beyond_workload_score = data['counselorsBeyondWorkloadScore']
    info.counselors_beyond_workload_money = data['counselorsBeyondWorkloadMoney']
    info.students_money = data['studentsMoney']
    info.total_money = data['totalMoney']
    info.notes = data['notes']
    db.session.commit()
    res = single_counselors_to_dict(info)
    return {
        "code": 20000,
        "data": res[0]

    }
