import time

from app import db

year = time.strftime("%Y", time.localtime())


class TeachingWorkload(db.Model):
    __tablename__ = "teachingworkload"
    id = db.Column(db.Integer, primary_key=True)
    teaching_workload = db.Column(db.DECIMAL(20, 2), default=0)  # 教学工作量
    teaching_qualified_workload = db.Column(db.DECIMAL(20, 2), default=0)  # 教学合格工作量
    teaching_excellent_workload = db.Column(db.DECIMAL(20, 2), default=0)  # 教学考评优秀奖励
    teaching_beyond_workload = db.Column(db.DECIMAL(20, 2), default=0)  # 教学超工作量
    teaching_beyond_workload_num = db.Column(db.DECIMAL(20, 2), default=0)  # 教学超工作量乘系数
    teaching_beyond_workload_money = db.Column(db.DECIMAL(20, 2), default=0)  # 教学超工作量金额
    manage_beyond_workload_money = db.Column(db.DECIMAL(20, 2), default=0)  # 管理岗超工作量金额

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键
    user_workload = db.relationship('User')  # 返回此工作量对应的user
    total_money = db.Column(db.DECIMAL(20, 2), default=0)  # 总金额

    year = db.Column(db.String(4), default=year)
    notes = db.Column(db.Text)  # 备注

    confirm_status = db.Column(db.String(10), default='未确认')

    def to_json(self):
        return {
            'id': self.id,
            'teachingWorkload': self.teaching_workload,
            'teachingQualifiedWorkload': self.teaching_qualified_workload,
            'teachingExcellentWorkload': self.teaching_excellent_workload,
            'teachingBeyondWorkload': self.teaching_beyond_workload,
            'teachingBeyondWorkloadNum': self.teaching_beyond_workload_num,
            'teachingBeyondWorkloadMoney': self.teaching_beyond_workload_money,
            'userWorkload': self.user_workload,
            'totalMoney': self.total_money,
            'year': self.year
        }
