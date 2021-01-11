import time

from app import db

year = time.strftime("%Y", time.localtime())


class OthersWorkload(db.Model):
    __tablename__ = 'othersworkload'
    id = db.Column(db.Integer, primary_key=True)
    attendances = db.Column(db.DECIMAL(20, 2))  # 考勤
    union_activities = db.Column(db.DECIMAL(20, 2))  # 工会活动
    ideological = db.Column(db.DECIMAL(20, 2))  # 思想政治
    news = db.Column(db.DECIMAL(20, 2))  # 新闻稿
    counselors = db.Column(db.DECIMAL(20, 2))  # 辅导员专项
    characteristics_activities = db.Column(db.DECIMAL(20, 2))  # 特色活动
    mini_professional = db.Column(db.DECIMAL(20, 2))  # 微专业申办
    information = db.Column(db.DECIMAL(20, 2))  # 信息安全申报
    undergraduatecolleges = db.Column(db.DECIMAL(20, 2))  # 本科建设
    graduation_design_manage = db.Column(db.DECIMAL(20, 2))  # 毕业设计管理
    course_quality = db.Column(db.DECIMAL(20, 2))  # 优质课程
    organization = db.Column(db.DECIMAL(20, 2))  # 教学组织申报
    graduation_design_personal = db.Column(db.DECIMAL(20, 2))  # 毕业设计个人
    professional_tab = db.Column(db.DECIMAL(20, 2))  # 专业导学
    mentor = db.Column(db.DECIMAL(20, 2))  # 导师制
    discipline_competition = db.Column(db.DECIMAL(20, 2))  # 学科竞赛
    teaching_watch = db.Column(db.DECIMAL(20, 2))  # 观摩课
    competition_judges = db.Column(db.DECIMAL(20, 2))  # 竞赛评委
    union_work = db.Column(db.DECIMAL(20, 2))  # 工会组织工作
    extra_score = db.Column(db.DECIMAL(20, 2))  # 额外加分
    total_score = db.Column(db.DECIMAL(20, 2))  # 合计分数
    total_money = db.Column(db.DECIMAL(20, 2))  # 总金额
    year = db.Column(db.String(4), default=year)
    notes = db.Column(db.Text)  # 备注
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def to_json(self):
        return {
            'id': self.id,
            'attendances': self.attendances,
            'unionActivities': self.union_activities,
            'ideological': self.ideological,
            'news': self.news,
            'counselors': self.counselors,
            'characteristicsActivities': self.characteristics_activities,
            'miniProfessional': self.mini_professional,
            'information': self.information,
            'undergraduatecolleges': self.undergraduatecolleges,
            'courseQuality': self.course_quality,
            'organization': self.organization,
            'graduationDesignPersonal': self.graduation_design_personal,
            'professionalTab': self.professional_tab,
            'mentor': self.mentor,
            'disciplineCompetition': self.discipline_competition,
            'teachingWatch': self.teaching_watch,
            'competitionJudges': self.competition_judges,
            'unionWork': self.union_work,
            'extraScore': self.extra_score,
            'totalScore': self.total_score,
            'totalMoney': self.total_money,
            'notes': self.notes,
            'name': self.user.name,
            'jobCatecory': self.user.job_catecory,
            'teacherTitle': self.user.teacher_title
        }