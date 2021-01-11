import time
from decimal import Decimal

to_year = time.strftime("%Y", time.localtime())


def single_teacher_others_workload_to_dict(item, year):
    lic = []
    for i in item.others_workload_user:
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
                    'attendances': i.attendances,
                    'unionActivities': i.union_activities,
                    'ideological': i.ideological,
                    'news': i.news,
                    'counselors': i.counselors,
                    'characteristicsActivities': i.characteristics_activities,
                    'miniProfessional': i.mini_professional,
                    'information': i.information,
                    'undergraduatecolleges': i.undergraduatecolleges,
                    'graduationDesignManage': i.graduation_design_manage,
                    'courseQuality': i.course_quality,
                    'organization': i.organization,
                    'graduation_designPersonal': i.graduation_design_personal,
                    'professionalTab': i.professional_tab,
                    'mentor': i.mentor,
                    'disciplineCompetition': i.discipline_competition,
                    'teachingWatch': i.teaching_watch,
                    'competitionJudges': i.competition_judges,
                    'unionWork': i.union_work,
                    'extraScore': i.extra_score,
                    'totalScore': i.total_score,
                    'totalMoney': i.total_money,
                    'notes': i.notes,
                    'year': i.year,
                    'oId': i.id  # 对应工作量的id，方便前端传参
                }
            )
    return lic


def others_to_dict_year(item, year=to_year):
    lic = []
    for i in item:
        for a in i.others_workload_user:
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
                        'attendances': a.attendances,
                        'unionActivities': a.union_activities,
                        'ideological': a.ideological,
                        'news': a.news,
                        'counselors': a.counselors,
                        'characteristicsActivities': a.characteristics_activities,
                        'miniProfessional': a.mini_professional,
                        'information': a.information,
                        'undergraduatecolleges': a.undergraduatecolleges,
                        'graduationDesignManage': a.graduation_design_manage,
                        'courseQuality': a.course_quality,
                        'organization': a.organization,
                        'graduationDesignPersonal': a.graduation_design_personal,
                        'professionalTab': a.professional_tab,
                        'mentor': a.mentor,
                        'disciplineCompetition': a.discipline_competition,
                        'teachingWatch': a.teaching_watch,
                        'unionWork': a.union_work,
                        'extraScore': a.extra_score,
                        'totalScore': a.total_score,
                        'competitionJudges': a.competition_judges,
                        'totalMoney': a.total_money,
                        'year': a.year,
                        'oId': a.id
                    }
                )
    return lic


def others_to_dict(item):
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
                'attendances': i.attendances,
                'unionActivities': i.union_activities,
                'ideological': i.ideological,
                'news': i.news,
                'counselors': i.counselors,
                'characteristicsActivities': i.characteristics_activities,
                'miniProfessional': i.mini_professional,
                'information': i.information,
                'undergraduatecolleges': i.undergraduatecolleges,
                'graduationDesignManage': i.graduation_design_manage,
                'courseQuality': i.course_quality,
                'organization': i.organization,
                'graduationDesignPersonal': i.graduation_design_personal,
                'professionalTab': i.professional_tab,
                'mentor': i.mentor,
                'disciplineCompetition': i.discipline_competition,
                'teachingWatch': i.teaching_watch,
                'unionWork': i.union_work,
                'extraScore': i.extra_score,
                'totalScore': i.total_score,
                'competitionJudges': i.competition_judges,
                'totalMoney': i.total_money,
                'year': i.year,
                'oId': i.id
            }
        )
    return lic
