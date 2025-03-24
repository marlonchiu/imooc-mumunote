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


class User(Base):
    # 表结构的反射加载
    __table__ = Table('user', Base.metadata, autoload_with=engine)

# 设置secret key用于session加密
app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机密钥

@app.route('/register', methods=[ 'POST'])
def register():
    request_data = request.data
    request_data = json.loads(request_data)
    print(request_data)
    username = request_data.get('username')
    password = request_data.get('password')
    email = request_data.get('email')

    # 在正式查询数据库数据之前，我们需要做一个密码的md5格式转换
    password = hashlib.md5(password.encode()).hexdigest()
    print(username, password, email)

    insert_data = {
        'username': username,
        'password': password,
        'email': email
    }

    user = User(**insert_data)
    db_session.add(user)
    db_session.commit()

    return '注册成功'


# 数据更新
# 思路是需要先查询出来要改动的行，然后再进行删除或者是更新
row = db_session.query(User).filter_by(id="6").first()
row.username = "admin111"
db_session.commit()

# 数据删除
# row = db_session.query(User).filter_by(id="5").delete()
# db_session.commit()


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
