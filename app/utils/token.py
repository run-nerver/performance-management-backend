from collections import namedtuple

from flask import current_app, g, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired


from app.utils.error_code import AuthFailed, Forbidden

from flask_httpauth import HTTPBasicAuth

from app.utils.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'scope'])


@auth.verify_password
def verify_password(token, password):
    token = request.headers.get('X-Token')
    user_info = varify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def get_token(uid, scope):
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(
        uid,
        scope,
        expiration
    )
    t = {
        'token': token.decode('ascii')
    }
    return t


def generate_auth_token(uid, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'scope': scope
    })


# 验证token
def varify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed()
    except SignatureExpired:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    uid = data['uid']
    scope = data['scope']
    blueprint = request.blueprint
    split = blueprint.split('_')
    allow = is_in_scope(scope, request.endpoint, split[0])
    if not allow:
        raise Forbidden()
    return User(uid, scope)
