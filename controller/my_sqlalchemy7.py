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
# http://127.0.0.1:5000/?keyword=flask
def my_favorite():
    keyword = request.args.get('keyword')
    print("🚀 ~ keyword:", keyword)

    all_article = db_session.query(Article).filter(or_(Article.title.like('%'+keyword+'%'), Article.article_content.like('%'+keyword+'%'))).all()

    print("🚀 ~ :", all_article)
    to_page_data = model_list(all_article)

    return to_page_data

def model_list(result):
    list_result = []
    for row in result:
        print(row.__dict__)
        my_dict = {}
        for k,v in row.__dict__.items():
            if not k.startswith('_sa'):
                my_dict[k] = v
        print(my_dict)
        list_result.append(my_dict)
    print('_________',list_result)
    return list_result

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
