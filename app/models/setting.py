from app import db


class Settings(db.Model):
    __tablename__ = "settings"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))  # 岗位类别、职称名字等
    coefficient = db.Column(db.DECIMAL(20, 2), default=0)  # 系数

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'coefficient': self.coefficient
        }

