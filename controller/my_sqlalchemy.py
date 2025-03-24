# 导入 Flask
import hashlib
import json

from flask import Flask, request
from sqlalchemy import create_engine, Integer, String, Column, Table
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


# sqlclchemy是支持使用代码进行表结构创建的 （可以测试创建表）
# class User(Base):
#   __tablename__="userssss"
#   user_id = Column(Integer,primary_key=True)
#   username = Column(String(255))
#
# User.metadata.create_all(engine)

class User(Base):
    # 表结构的反射加载
    __table__ = Table('user', Base.metadata, autoload_with=engine)

# 设置secret key用于session加密
app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机密钥

@app.route('/login', methods=[ 'POST'])
def login():
    # result = db_session.query(User).all()
    # # print(result)
    # for i in result:
    #     print(i.username)

    # result = db_session.query(User).first()
    # print(result)
    # print(result.username)

    request_data = request.data
    request_data = json.loads(request_data)
    print(request_data)
    user_input_name = request_data.get('username')
    user_input_password = request_data.get('password')
    print(user_input_name, user_input_password)
    # filter方法，比较写的不是我们之前那种参数，它支持 == > < >= <= 这些运算符号
    # result = db_session.query(User).filter(User.username == user_input_name).first()

    # 之前给参数赋值的运算符是=
    # result = db_session.query(User).filter_by(username=user_input_name).first()

    # 在正式查询数据库数据之前，我们需要做一个密码的md5格式转换
    user_input_password = hashlib.md5(user_input_password.encode()).hexdigest()
    print(user_input_password)
    result = db_session.query(User).filter_by(username=user_input_name, password=user_input_password).first()

    print(result.username)

    return '登陆成功'


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
