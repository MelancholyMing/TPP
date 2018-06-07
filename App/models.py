# 声明数据库中表对应的模型类
from datetime import datetime
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    Migrate(app, db)


class IdBase():
    id = Column(Integer, primary_key=True, autoincrement=True)


class Letter(db.Model, IdBase):
    __tablename__ = 't_letter'

    name = Column(String(10))


class City(db.Model, IdBase):
    __tablename__ = 't_city'

    # id = Column(Integer, primary_key=True, autoincrement=True)
    parentId = Column(Integer, default=0)
    regionName = Column(String(20))
    cityCode = Column(Integer)
    pinYin = Column(String(50))

    letter_id = Column(Integer, ForeignKey(Letter.id))
    letter = relationship("Letter", backref=backref("citys", lazy=True))


class User(db.Model, IdBase):
    __tablename__ = 't_user'

    # id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    password = Column(String(50))
    nickName = Column(String(20))
    email = Column(String(50), unique=True)
    phone = Column(String(12), unique=True)
    is_active = Column(Boolean, default=False)
    is_life = Column(Boolean, default=True)
    regist_time = Column(DateTime, default=datetime.now())
    last_login_time = Column(DateTime)

    # 新增头像属性
    photo_1 = Column(String(200), nullable=True)  # 原图
    photo_2 = Column(String(200), nullable=True)  # 小图


class Movies(db.Model, IdBase):
    showname = Column(String(100))
    shownameen = Column(String(200))
    director = Column(String(50))
    leadingRole = Column(String(300))
    type = Column(String(50))
    country = Column(String(20))
    language = Column(String(20))  # 语言
    duration = Column(Integer)  # 播放时长
    screeningmodel = Column(String(20))
    openday = Column(DateTime)  # 开放时间
    backgroundpicture = Column(String(200))
    flag = Column(Integer)
    isdelete = Column(Boolean)  # 是否删除


class Cinemas(db.Model, IdBase):
    name = Column(String(50))  # 电影名
    city = Column(String(50))  # 城市
    district = Column(String(20))  # 区名
    address = Column(String(200))  # 详细地址
    phone = Column(String(50))  # 联系电话
    score = Column(Float(precision=1))  # 评分
    hallnum = Column(Integer)  # 播放厅数量
    servicecharge = Column(Float(precision=2))  # 服务费
    astrict = Column(Integer, default=5)  # 限购数量
    flag = Column(Integer)  # 营业状态
    isdelete = Column(Boolean, default=False)  # 是否删除
