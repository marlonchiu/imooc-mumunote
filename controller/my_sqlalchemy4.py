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

class Article(Base):
    # 表结构的反射加载
    __table__ = Table('article', Base.metadata, autoload_with=engine)

@app.route('/')
# http://127.0.0.1:5000/?username=2@qq.com
def my_article():
    username = request.args.get('username')
    print("🚀 ~ username:", username)
    # all_article = db_session.query(User, Article).join(Article, User.user_id == Article.user_id).filter(User.username == username).all()
    # for user, article in all_article:
    #     print("🚀 ~ user:", user)
    #     print("🚀 ~ user:", user.username)
    #     print("🚀 ~ article:", article)
    #     print("🚀 ------ article.title:", article.title)

    # all_article = db_session.query(User.username, User.nickname, Article.title).join(Article, User.user_id == Article.user_id).filter(User.username == username).all()
    # print("🚀 ~ :", all_article)
    # for u,n,a in all_article:
    #     print("🚀 ~ user.username:", u)
    #     print("🚀 ~ user.nickname:", n)
    #     print("🚀 ------ article.title:", a)

    all_article = db_session.query(User, Article.title).join(Article, User.user_id == Article.user_id).filter(User.username == username).all()
    print("🚀 ~ :", all_article)
    for user,title in all_article:
        print("🚀 ~ user.username:", user.username)
        print("🚀 ------ article.title:", title)

    return 'OK'


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
