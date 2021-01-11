from flask import Blueprint, request, g

from app.models.user import User
from app.utils.token import get_token, varify_auth_token, auth
from app.utils import response as resp
from app.utils.response import response_data

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    current_user = User.verify(data['username'], data['password'])
    if current_user:
        token = get_token(current_user['uid'], current_user['scope'])
        return {
            "code": 20000,
            "data": token
        }


@login_bp.route('/user/info', methods=['GET'])
@auth.login_required
def get_info():
    # token = request.args.get('token')
    # uid = varify_auth_token(token)
    # if uid:
    #     g.uid = uid
    info = User.query.filter_by(id=g.user.uid).first()
    return {
        "code": 20000,
        "data": {
            "roles": [info.auth],
            "introduction": "introduction",
            "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            "name": info.name
        }
    }


@login_bp.route('/user/logout', methods=['POST'])
def logout():
    return response_data(resp.SUCCESS)
