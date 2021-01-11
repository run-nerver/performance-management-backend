import time

from app import db

year = time.strftime("%Y", time.localtime())


class ScientificWorkload(db.Model):
    __tablename__ = 'scientificworkload'
    id = db.Column(db.Integer, primary_key=True)
    scientific_name = db.Column(db.String(128))  #名称
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键
    scientific_type = db.Column(db.String(64))  # 类型
    scientific_money = db.Column(db.DECIMAL(20, 2), default=0)  # 金额
    year = db.Column(db.String(4), default=year)
    notes = db.Column(db.Text)  # 备注

    confirm_status = db.Column(db.String(10))  # 状态
