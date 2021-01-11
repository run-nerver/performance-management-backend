import time

to_year = time.strftime("%Y", time.localtime())


#  返回单一用户信息，传入的是user实例
def single_counselors_to_dict_with_user(item, year=to_year):
    lic = []
    for i in item.counselors_workload_user:
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
                    'totalPeople': i.total_people,
                    'beyondWorkloadPeople': i.beyond_workload_people,
                    'months': i.months,
                    'counselorsBeyondWorkload': i.counselors_beyond_workload,
                    'counselorsBeyondWorkloadScore': i.counselors_beyond_workload_score,
                    'counselorsBeyondWorkloadMoney': i.counselors_beyond_workload_money,
                    'studentsMoney': i.students_money,
                    'totalMoney': i.total_money,
                    'cId': i.id,
                    'year': i.year
                }
            )
            return lic



# 返回单一用户更新信息 传入的是counselors实例
def single_counselors_to_dict(item):
    lic = []
    lic.append(
        {
            'id': item.user.id,
            'username': item.user.username,
            'department': item.user.department,
            'workload': item.user.workload,
            'name': item.user.name,
            'workNumber': item.user.work_number,
            'jobCatecory': item.user.job_catecory,
            'teacherTitle': item.user.teacher_title,
            'teacherTitleNum': item.user.teacher_title_num,
            'teacherPostion': item.user.teacher_postion,
            'teacherPostionNum': item.user.teacher_postion_num,
            'postionStatus': item.user.postion_status,
            'notes': item.notes,
            'totalPeople': item.total_people,
            'beyondWorkloadPeople': item.beyond_workload_people,
            'months': item.months,
            'counselorsBeyondWorkload': item.counselors_beyond_workload,
            'counselorsBeyondWorkloadScore': item.counselors_beyond_workload_score,
            'counselorsBeyondWorkloadMoney': item.counselors_beyond_workload_money,
            'studentsMoney': item.students_money,
            'totalMoney': item.total_money,
            'cId': item.id,
            'year': item.year
        }
    )
    return lic


def counselors_to_dict(item):
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
                'totalPeople': i.total_people,
                'beyondWorkloadPeople': i.beyond_workload_people,
                'months': i.months,
                'counselorsBeyondWorkload': i.counselors_beyond_workload,
                'counselorsBeyondWorkloadScore': i.counselors_beyond_workload_score,
                'counselorsBeyondWorkloadMoney': i.counselors_beyond_workload_money,
                'studentsMoney': i.students_money,
                'totalMoney': i.total_money,
                'cId': i.id,
                'year': i.year
            }
        )
    return lic
