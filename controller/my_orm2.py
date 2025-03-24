import pymysql
# from flask import Blueprint

# 创建蓝图对象
# my_orm1 = Blueprint('my_orm1', __name__)

class MyORM:
    def __init__(self):
        # 建立与数据库的连接
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            database="mumushouji",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        # 实例化一个游标对象
        cursor = conn.cursor()
        self.cursor = cursor

    # 封装执行函数
    def execute(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

class User:
    table_name = 'user'
    def query_all(self):
        sql = "select * from %s" % self.table_name
        result = MyORM().execute(sql)
        return result
    def query_one(self):
        sql = "select * from %s limit 1" % self.table_name
        result = MyORM().execute(sql)
        return result

class Article:
    table_name = 'article'
    def query_all(self):
        sql = "select * from %s limit 5" % self.table_name
        result = MyORM().execute(sql)
        return result

if __name__ == '__main__':
    user = User()
    result1 = user.query_all()
    print(result1)
    print('-'*20)
    result3 = user.query_one()
    print(result3)
    print('-'*20)
    article = Article()
    result2 = article.query_all()
    print(result2)
