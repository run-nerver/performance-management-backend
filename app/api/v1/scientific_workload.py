import os, time

import xlrd
from flask import Blueprint, request, current_app

from app import db

from app.models.scientific_workload import ScientificWorkload

from app.models.user import User

from app.utils.scientific import scientific_to_dict

from app.utils.utils import float_to_decimal

from app.utils.token import auth

scientific_workload_bp = Blueprint('scientific_workload_bp', __name__)
today = time.strftime("%Y-%m-%d", time.localtime())


# 获取用户科研工作量
@scientific_workload_bp.route('/scientific_workload/fetchUserInfo', methods=['GET'])
@auth.login_required
def fetch_UserInfo():
    param = []
    data = request.args
    if ('scientificName' in data) and data['scientificName']:
        param.append(ScientificWorkload.scientific_name.like('%' + data['scientificName'] + '%'))
    if ('scientificType' in data) and data['scientificType']:
        param.append(ScientificWorkload.scientific_type.like('%' + data['scientificType'] + '%'))
    if ('year' in data) and data['year']:
        param.append(ScientificWorkload.year == data['year'])
    infos = ScientificWorkload.query.filter(*param) \
        .paginate(int(data['page']), int(data['limit']))
    res = scientific_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }


# 批量添加科研工作量
@scientific_workload_bp.route('/scientific_workload/UploadExcelScientificWorkload', methods=['POST'])
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
    for r in range(1, sheet.nrows):
        work_number = int(sheet.cell(r, 0).value)
        scientific_name = sheet.cell(r, 2).value
        scientific_type = sheet.cell(r, 3).value
        scientific_money = float_to_decimal(sheet.cell(r, 4).value)
        info = User.query.filter_by(work_number=work_number).first()
        if info:
            if info.scientific_workload_user:
                info.scientific_workload_user.scientific_name = scientific_name,
                info.scientific_workload_user.scientific_type = scientific_type,
                info.scientific_workload_user.scientific_money = scientific_money,
                info.scientific_workload_user.year = year,
            else:
                add_info = ScientificWorkload(
                    scientific_name=scientific_name,
                    scientific_type=scientific_type,
                    scientific_money=scientific_money,
                    year=year,
                    user_id=info.id
                )
                db.session.add(add_info)
    db.session.commit()
    infos = ScientificWorkload.query.paginate(1, 10)
    res = scientific_to_dict(infos.items)
    return {
        "code": 20000,
        "data": {
            "total": infos.total,
            "items": res
        }
    }
