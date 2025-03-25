import random
from sqlalchemy import Table

from common.database import db_connect

db_session, Base, engine = db_connect()

class User(Base):
  # 表结构的反射加载
  __table__ = Table('user', Base.metadata, autoload_with=engine)

  def get_one(self):
    return db_session.query(User).first()

  def find_by_username(self, username):
    print(username)
    return db_session.query(User).filter(User.username == username).all()

  def do_register(self,username,password):
    nickname = username.split("@")[0]
    # 头像
    picture_num = random.randint(1,539)
    picture = str(picture_num) + ".jpg"
    job="未定义"
    user = User(username=username,
                password=password,
                nickname=nickname,
                picture=picture,
                job=job)
    db_session.add(user)
    db_session.commit()
    return user
