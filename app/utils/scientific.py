import time


to_year = time.strftime("%Y", time.localtime())


# 返回单一用户对应年份的科研工作量
def single_teacher_scientific_workload_to_dict(item, year):
    lic = []
    for i in item.scientific_workload_user:
        if i.year == year:
            lic.append(
                {
                    'id': item.id,
                    'username': item.username,
                    'department': item.department,
                    'workload': item.workload,
                    'name': item.name,
                    'workNumber': item.work_number,
                    'jobCatecory': item.job_catecory,
                    'teacherTitle': item.teacher_title,
                    'teacherTitleNum': item.teacher_title_num,
                    'teacherPostion': item.teacher_postion,
                    'teacherPostionNum': item.teacher_postion_num,
                    'postionStatus': item.postion_status,
                    'notes': i.notes,
                    'scientificName': i.scientific_name,
                    'scientificType': i.scientific_type,
                    'scientificMoney': i.scientific_money,
                    'year': i.year,
                    'confirmStatus': i.confirm_status,
                    'sId': i.id  # 对应工作量的id，方便前端传参
                }
            )
    return lic


def scientific_to_dict(item):
    lic = []
    for i in item:
        lic.append(
            {
                'id': i.user.id,
                'username': i.user.username,
                'department': i.user.department,
                'workload': i.user.workload,
                'name': i.user.name,
                'workNumber': i.user.work_number,
                'jobCatecory': i.user.job_catecory,
                'teacherTitle': i.user.teacher_title,
                'teacherTitleNum': i.user.teacher_title_num,
                'teacherPostion': i.user.teacher_postion,
                'teacherPostionNum': i.user.teacher_postion_num,
                'postionStatus': i.user.postion_status,
                'notes': i.notes,
                'scientificName': i.scientific_name,
                'scientificType': i.scientific_type,
                'scientificMoney': i.scientific_money,
                'year': i.year,
                'sId': i.id
            }
        )
    return lic
