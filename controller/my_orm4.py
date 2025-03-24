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

    def __init__(self, **kwargs):
      for k,v in kwargs.items():
            self.__setattr__(k,v)
      # print(self.__dict__)
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

    # 插入用户
    def insert(self):
        # sql = "insert into user (username,nickname,email,password) values ('%s','%s','%s','%s')"% (params['username'],params['nickname'],params['email'],params['password'])
        print(self.__dict__)
        keys =[]
        values = []
        for k,v in self.__dict__.items():
            keys.append(k)
            values.append(v)

        sql = "insert into %s(%s) values('%s')" % (self.table_name, ",".join(keys), "','".join(values))
        print(sql)
        # return 0
        return MyORM().execute(sql)

if __name__ == '__main__':
    user = User(username= "test3", password="123456", email="test3@gg.com")
    user.insert()
