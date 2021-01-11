import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SQLALCHEMY_TRACK_MODIFICATIONS = False

TOKEN_EXPIRATION = 30 * 24 * 3600  # 令牌过期时间

FILE_UPLOAD_PATH = os.path.join(basedir, 'uploads/files')
CONFIG_UPLOAD_PATH = os.path.join(basedir, 'uploads/configs')

SQLALCHEMY_DATABASE_URI = ''

SECRET_KEY = '123456'
