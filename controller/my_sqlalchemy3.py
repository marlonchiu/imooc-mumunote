# 导入 Flask
from operator import or_

from flask import Flask, request
from sqlalchemy import create_engine, Integer, String, Column, Table, select, func
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os

app = Flask(__name__)

# 创建一个引擎，连接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/mumushouji', echo=True)
# 打开数据库的连接会话
session = sessionmaker(engine)
# 保证线程安全
db_session = scoped_session(session)
# 获取基类
Base = declarative_base()


class User(Base):
    # 表结构的反射加载
    __table__ = Table('user', Base.metadata, autoload_with=engine)

# r = db_session.query(User).filter_by(id="1").first()
# print('_____', r.username)

# session.execute(select(User).filter_by(name="sandy")).scalar_one
# sql = select(User).filter_by(id="2")
# print(sql)
# r1 = db_session.execute(sql).scalar_one()
# print('_____', r1.username)

# 或者
# r2 = db_session.query(User).filter(or_(User.id == "1", User.id == "2")).all()
# print('_____', r2)
# for i in r2:
#     print(i.username)

# limit
# r3 = db_session.query(User).limit(4).all()
# print('_____', r3)
# for i in r3:
#     print(i.username)

# limit offset
# r3 = db_session.query(User).limit(2).offset(2).all()
# print('_____', r3)
# for i in r3:
#     print(i.username)

# 大于 大于等于
# r4 = db_session.query(User).filter(User.id > "2").all()
# print('_____', r4)
# for i in r4:
#     print(i.username)

# order by
# r5 = db_session.query(User).order_by(User.id.desc()).all()
# print('_____', r5)
# for i in r5:
#     print(i.username)

# like
# r6 = db_session.query(User).filter(User.username.like('%test%')).all()
# print('_____', r6)
# for i in r6:
#     print(i.username)

# some
# r7 = db_session.query(User).filter(User.id.in_(['1', '2'])).all()
# print('_____', r7)
# for i in r7:
#     print(i.username)

# sum
r8 = db_session.query(func.sum(User.id)).all()
print('_____', r8)


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
