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

class Model:
    # 这个构造方法里边的代码是给数据插入的时候用的
    def __init__(self, **kwargs):
      for k,v in kwargs.items():
            self.__setattr__(k,v)

    # 通过链式操作来指定查询的列，就是一顿.然后调用各种方法
    def field(self, select_params):
      self.columns = ','.join(select_params)
      return self

    def query(self, **where_params):
       table = self.__class__.__getattribute__(self, 'table_name')
       if hasattr(self, 'columns'):
          sql = "select %s from %s "% (self.columns, table)
       else:
          sql = "select * from %s "% (table)

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
      table = self.__class__.__getattribute__(self, 'table_name')
      keys =[]
      values = []
      for k,v in self.__dict__.items():
          keys.append(k)
          values.append(v)

      sql = "insert into %s(%s) values('%s')" % (table, ",".join(keys), "','".join(values))

      return MyORM().execute(sql)

class User(Model):
    table_name = 'user'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Article(Model):
    table_name = 'article'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':

  # user = User()
  #  print(user.query())
  # print(user.field(["id", "username","email"]).query(username="test1"))

  # user = User(username= "test4", password="123456", email="test4@qq.com")
  # user.insert()


  article = Article()
  # print(article.query())
  print(article.field(["id", "title"]).query(id="1"))
