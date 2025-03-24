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

    def query_user_all(self):
        sql = "select * from user"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

if __name__ == '__main__':
    my_orm = MyORM()
    result = my_orm.query_user_all()
    print(result)
