from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.utils.error_code import AuthFailed, ParameterException


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    _password = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(60))
    auth = db.Column(db.SmallInteger, default=1)
    infos = db.relationship('Information', backref='user.id')
    workload = db.Column(db.DECIMAL(20, 2), default=0)  # 总工作量
    name = db.Column(db.String(20))  # 姓名
    work_number = db.Column(db.Integer)  # 工号
    job_catecory = db.Column(db.String(30))  # 岗位类别
    teacher_title = db.Column(db.String(30))  # 职称
    teacher_title_num = db.Column(db.DECIMAL(20, 2), default=0)  # 职称系数
    teacher_postion = db.Column(db.String(30))  # 职务级别
    teacher_postion_num = db.Column(db.DECIMAL(20, 2), default=0)  # 职级系数
    teaching_workload_user = db.relationship('TeachingWorkload', backref='user')  # 返回对应教师工作量的行数ID
    scientific_workload_user = db.relationship('ScientificWorkload', backref='user')  # 返回对应科研工作量的行数ID
    others_workload_user = db.relationship('OthersWorkload', backref='user')  # 返回对应其他工作量的行数ID
    counselors_workload_user = db.relationship('CounselorsWorkload', backref='user')  # 返回对应辅导员工作量的行数ID
    postion_status = db.Column(db.String(10))  # 职位 教研室主任等
    notes = db.Column(db.Text)  # 备注

    def to_json(self):
        return {
            'auth': self.auth,
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'workNumber': self.work_number,
            'department': self.department,
            'jobCatecory': self.job_catecory,
            'teacherTitle': self.teacher_title,
            'teacherTitleNum': self.teacher_title_num,
            'teacherPostion': self.teacher_postion,
            'teacherPostionNum': self.teacher_postion_num,
            'postionStatus': self.postion_status
        }

    # @classmethod
    # def find_by_username(cls, username):
    #     return cls.query.filter_by(username=username).first()

    @staticmethod
    def verify(workNumber, password):
        user = User.query.filter_by(work_number=int(workNumber)).first()
        if not user:
            raise AuthFailed()
        if not user.check_password(password):
            raise ParameterException()
        scope = 'SuperAdminScope' if user.auth == 3 else \
            'AdminScope' if user.auth == 2 or user.auth == 11 or user.auth == 12 or user.auth == 13 \
                else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    # def keys(self):
    #     return [
    #         'auth',
    #         'id',
    #         'username',
    #         'name',
    #         'work_number',
    #         'department',
    #         'job_catecory',
    #         'teacher_title',
    #         'teacher_titleNum',
    #         'teacher_postion',
    #         'teacher_postion_num',
    #         'postion_status',
    #         'teaching_workload_user'
    #     ]
    #
    # def __getitem__(self, item):
    #     return getattr(self, item)
