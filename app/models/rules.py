from app import db


class Rules(db.Model):
    __tablename__ = "rules"
    id = db.Column(db.Integer, primary_key=True)
    workload_name = db.Column(db.String(120), unique=True, nullable=False)
    key_name = db.Column(db.String(20))
    score = db.Column(db.DECIMAL(20, 2))
    infos = db.relationship('Information', backref='rules.id')

    def to_json(self):
        return {
            'id': self.id,
            'display_name': self.workload_name,
            'key_name': self.key_name,
            'score': self.score
        }
