from app import create_app, db

from app.models.user import User

app = create_app()

with app.app_context():
    user = User()
    user.username = 'superAdmin'
    user.password = '123456'
    user.department = '计算机学院'
    user.name = '超级管理员'
    user.auth = 3
    user.work_number = 10000
    db.session.add(user)
    db.session.commit()



