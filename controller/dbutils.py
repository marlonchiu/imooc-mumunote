# 导入pymysqL模块
import pymysql

# 建立与数据库的连接
conn = pymysql.connect(
  host="192.168.1.129",
  port=3306,
  user="admin1",
  password="123",
  database="mumushouji",
  charset="utf8",
  cursorclass=pymysql.cursors.DictCursor
)

# 执行sql语句
sql = "select * from user"

# 实例化一个游标对象
cursor = conn.cursor()
cursor.execute(sql)

# 获取查询结果
result = cursor.fetchall()
print(result)

# 遍历结果
for row in result:
  print(row)
  print(row[0],row[1],row[2],row[3])

# 关闭连接
cursor.close()
conn.close()
