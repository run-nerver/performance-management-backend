import time

to_year = time.strftime("%Y", time.localtime())

# 返回单一用户对应年份的教学工作量
def single_teaching_workload_to_dict(item, year):
    lic = []
    for i in item.teaching_workload_user:
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
                    'teachingWorkload': i.teaching_workload,
                    'teachingQualifiedWorkload': i.teaching_qualified_workload,
                    'teachingExcellentWorkload': i.teaching_excellent_workload,
                    'teachingBeyondWorkload': i.teaching_beyond_workload,
                    'teachingBeyondWorkloadNum': i.teaching_beyond_workload_num,
                    'teachingBeyondWorkloadMoney': i.teaching_beyond_workload_money,
                    'manageBeyondWorkloadMoney': i.manage_beyond_workload_money,
                    'totalMoney': i.total_money,
                    'year': i.year,
                    'confirmStatus': i.confirm_status,
                    'tId': i.id  # 对应工作量的id，方便前端传参
                }
            )
    return lic


# 返回不带年份的查询，只返回user表信息，不返回对应的教学工作量
def teaching_workload_to_dict_no_year(item):
    lic = []
    for i in item:
        lic.append(
            {
                'id': i.id,
                'username': i.username,
                'department': i.department,
                'workload': i.workload,
                'name': i.name,
                'workNumber': i.work_number,
                'jobCatecory': i.job_catecory,
                'teacherTitle': i.teacher_title,
                'teacherTitleNum': i.teacher_title_num,
                'teacherPostion': i.teacher_postion,
                'teacherPostionNum': i.teacher_postion_num,
                'postionStatus': i.postion_status,
            }
        )
    return lic


# 返回带年份的查询对应教学工作量
def teaching_workload_to_dict(item, year=to_year):
    lic = []
    for i in item:
        for a in i.teaching_workload_user:
            # 传入year，返回对应年份的工作量
            if a.year == year:
                lic.append(
                    {
                        'id': i.id,
                        'username': i.username,
                        'department': i.department,
                        'workload': i.workload,
                        'name': i.name,
                        'workNumber': i.work_number,
                        'jobCatecory': i.job_catecory,
                        'teacherTitle': i.teacher_title,
                        'teacherTitleNum': i.teacher_title_num,
                        'teacherPostion': i.teacher_postion,
                        'teacherPostionNum': i.teacher_postion_num,
                        'postionStatus': i.postion_status,
                        'notes': a.notes,
                        'teachingWorkload': a.teaching_workload,
                        'teachingQualifiedWorkload': a.teaching_qualified_workload,
                        'teachingExcellentWorkload': a.teaching_excellent_workload,
                        'teachingBeyondWorkload': a.teaching_beyond_workload,
                        'teachingBeyondWorkloadNum': a.teaching_beyond_workload_num,
                        'teachingBeyondWorkloadMoney': a.teaching_beyond_workload_money,
                        'manageBeyondWorkloadMoney': a.manage_beyond_workload_money,
                        'totalMoney': a.total_money,
                        'confirmStatus': a.confirm_status,
                        'tId': a.id,
                        'year': a.year
                    }
                )
    return lic
