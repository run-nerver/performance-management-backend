import time

from app import db

year = time.strftime("%Y", time.localtime())


class CounselorsWorkload(db.Model):
    __tablename__ = 'counselorsworkload'
    id = db.Column(db.Integer, primary_key=True)
    total_people = db.Column(db.Integer)  # 带学生总人数
    beyond_workload_people = db.Column(db.Integer)  # 超工作量人数
    months = db.Column(db.Integer)  # 月数
    counselors_beyond_workload = db.Column(db.DECIMAL(20, 2))  # 超工作量
    counselors_beyond_workload_score = db.Column(db.DECIMAL(20, 2))  # 超工作量分值
    counselors_beyond_workload_money = db.Column(db.DECIMAL(20, 2))  # 超工作量金额
    students_money = db.Column(db.DECIMAL(20, 2))  # 带学生金额
    total_money = db.Column(db.DECIMAL(20, 2))  # 总金额
    year = db.Column(db.String(4), default=year)
    notes = db.Column(db.Text)  # 备注
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键
