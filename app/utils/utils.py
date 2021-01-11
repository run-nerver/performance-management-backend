# 教师总表转dict
import time
from decimal import Decimal

to_year = time.strftime("%Y", time.localtime())


# 教师总表转dict（管理员查看）
def teacher_workload_to_dict(item, year=to_year, confirm_status=''):
    lic = []
    total_money = 0
    temp = {}
    scientific_money = 0
    for i in item:
        if confirm_status == '':
            if i.teaching_workload_user:
                for a in i.teaching_workload_user:
                    if a.year == year:
                        total_money += a.total_money
                        temp.update({
                            'id': i.id,
                            'username': i.name,
                            'workNumber': i.work_number,
                            'jobCatecory': i.job_catecory,
                            'teacherTitle': i.teacher_title,
                            'teachingWorkloadTotalMoney': a.total_money,
                            'confirmStatus': a.confirm_status
                        })
                    if i.scientific_workload_user:
                        for a in i.scientific_workload_user:
                            if a.year == year:
                                total_money += a.scientific_money
                                scientific_money += a.scientific_money
                                temp.update({'scientificWorkloadTotalMoney': scientific_money})
                    if i.others_workload_user:
                        for a in i.others_workload_user:
                            if a.year == year:
                                total_money += a.total_money
                                temp.update({'othersWorkloadTotalMoney': a.total_money})
                    if i.counselors_workload_user:
                        for a in i.counselors_workload_user:
                            if a.year == year:
                                total_money += a.total_money
                                temp.update({'counselorsWorkloadTotalMoney': a.total_money})
                    temp.update({'totalMoney': total_money})
                    lic.append(temp)
                    total_money = 0
                    temp = {}
                    scientific_money = 0
        else:
            if i.teaching_workload_user:
                for a in i.teaching_workload_user:
                    if a.year == year and a.confirm_status == confirm_status:
                        total_money += a.total_money
                        temp.update({
                            'id': i.id,
                            'username': i.name,
                            'workNumber': i.work_number,
                            'jobCatecory': i.job_catecory,
                            'teacherTitle': i.teacher_title,
                            'teachingWorkloadTotalMoney': a.total_money,
                            'confirmStatus': a.confirm_status
                        })
                        if i.scientific_workload_user:
                            for a in i.scientific_workload_user:
                                if a.year == year:
                                    total_money += a.scientific_money
                                    scientific_money += a.scientific_money
                                    temp.update({'scientificWorkloadTotalMoney': scientific_money})
                        if i.others_workload_user:
                            for a in i.others_workload_user:
                                if a.year == year:
                                    total_money += a.total_money
                                    temp.update({'othersWorkloadTotalMoney': a.total_money})
                        temp.update({'totalMoney': total_money})
                        lic.append(temp)
                        total_money = 0
                        temp = {}
                        scientific_money = 0

    return lic


# 工作量参数转dict
def workload_options_to_dict(item):
    lic = []
    for i in item:
        lic.append(
            {
                'id': i.id,
                'key': i.key_name,
                'score': i.score,
                'display_name': i.workload_name
            }
        )
    return lic


# 教学工作量转dict
def teaching_workload_to_dict(item):
    lic = []
    for i in item:
        lic.append(
            {
                'id': i.id,
                'teachingWorkload': i.teaching_workload,
                'teachingQualifiedWorkload': i.teaching_qualified_workload,
                'teachingExcellentWorkload': i.teaching_excellent_workload,
                'teachingBeyondWorkload': i.teaching_beyond_workload,
                'teachingBeyondWorkloadNum': i.teaching_beyond_workload_num,
                'teachingBeyondWorkloadMoney': i.teaching_beyond_workload_money,
                'userWorkload': i.user_workload,
                'totalMoney': i.total_money,
                'year': i.year,
                'confirmStatus': i.confirm_status
            }
        )
    return lic


# 系数表转dict
def coefficient_to_dict(item):
    lic = []
    for i in item:
        lic.append(
            {
                'id': i.id,
                'name': i.name,
                'coefficient': i.coefficient
            }
        )
    return lic


# float转decimal
def float_to_decimal(data):
    return Decimal.from_float(data).quantize(Decimal('0.00'))


# 用户信息转dict
def user_to_dict(item):
    lic = []
    for i in item:
        lic.append(
            {
               'id': i.id,
               'name': i.name,
               'work_number': i.work_number,
               'job_catecory': i.job_catecory,
               'teacher_title': i.teacher_title,
               'teacher_title_num': i.teacher_title_num,
               'teacher_postion': i.teacher_postion,
               'teacher_postion_num': i.teacher_postion_num,
               'notes': i.notes,
            }
        )
