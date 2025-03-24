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

class Favorite(Base):
    # 表结构的反射加载
    __table__ = Table('favorite', Base.metadata, autoload_with=engine)

@app.route('/')
# http://127.0.0.1:5000/?username=2@qq.com
def my_favorite():
    username = request.args.get('username')
    print("🚀 ~ username:", username)

    all_article = db_session.query(User, Article, Favorite).outerjoin(
        Favorite, User.user_id == Favorite.user_id
        ).outerjoin(
        Article, Article.id == Favorite.article_id
    ).filter(User.username == username).all()

    print("🚀 ~ :", all_article)
    for user,article,favorite in all_article:
        print("🚀 ~ user:", user.username)
        print("🚀 ~ article:", article.title)
        print("🚀 ~ favorite:", favorite.article_id)

    return 'OK'


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
