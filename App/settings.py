import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
# print(BASE_DIR)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# print(STATIC_DIR)
MEDIA_DIR = os.path.join(STATIC_DIR, 'user_avatar')


# print(MEDIA_DIR)


class Config():
    ENV = 'development'
    DEBUG = True

    # 配置数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.39:3306/tpp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置邮箱
    MAIL_SERVER = 'smtp.163.com'  # 邮箱服务器
    MAIL_USERNAME = '13572155829@163.com'
    MAIL_PASSWORD = 'DQming888'  # 授权码

    # 设置session相关参数
    SECRET_KEY = 'MING'
