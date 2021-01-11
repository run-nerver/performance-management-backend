from datetime import datetime
from app.models.user import User

from app import db


class Information(db.Model):
    __tablename__ = "information"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    pic_name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(10))
    rule_id = db.Column(db.Integer, db.ForeignKey('rules.id'))
    status = db.Column(db.Integer)  # 0 已删除 1 已审核 2未审核
    score = db.Column(db.DECIMAL(20, 2))  # 单个工作量
    filesUrl = db.Column(db.String(1024))  # 附件路径

    @staticmethod
    def modify_status(target, value, oldvalue, initiator):
        if value == 1:
            User.workload += Information.score

    def to_json(self):
        return {
            'id': self.id,
            'username': self.name,
            'pic_name': self.pic_name,
            'user_id': self.user_id,
            'timestamp': self.timestamp,
            'type': self.type,
            'status': self.status,
            'score': self.score,
            'filesUrl': self.filesUrl
        }

    # fileUrl转list
    def file_to_list(self):
        return self.filesUrl.split(',')


# db.event.listen(Information.status, 'set', Information.modify_status)
