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
    # def query_one(self, select_params, where_params):
    #   sql = "select %s from %s where %s limit 1"% (select_params, self.table_name, where_params)
    #   return MyORM().execute(sql)
    def query_one(self, select_params = None, **where_params):
      # sql = "select %s from %s where %s limit 1"% (select_params, self.table_name, where_params)

      # select username,nickname from user
      if select_params is not None and type(select_params) is list:
        # sql 语句拼接
        sql = "select"
        select_params = ",".join(select_params)
        sql += " %s from %s "% (select_params, self.table_name)
        print(sql)
      else:
        sql = "select * from " + self.table_name

      # select username, nickname from user where user id=1 and username='3@gg.com'
      print(where_params)
      if where_params is not None:
        # sql 语句拼接
        sql = sql + "where "
        for k,v in where_params.items():
          sql += "%s='%s' and "% (k,v)
        sql += "1=1 limit 1"
        print(sql)

      return MyORM().execute(sql)


if __name__ == '__main__':
    user = User()
    # result3 = user.query_one(["username", "nickname"])
    # result3 = user.query_one()
    # print(result3)
    # print(user.query_one(["username","nickname"],{"user_id":1}))
    result1 = user.query_one(["username","email"], id=1, username="test1")
    print(result1)
