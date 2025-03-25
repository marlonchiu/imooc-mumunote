import random
from sqlalchemy import Table

from app.config.config import config
from app.settings import env
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

  def find_by_user_id(self, user_id):
    # user_info = db_session.query(User).filter(User.user_id == user_id).first()
    user_info = db_session.query(User).filter_by(user_id = user_id).first()

    # 这个代码是为了方便调用者自己不用拼接用户头像的路径了
    if user_info.picture.startswith(config[env].user_header_image_path):
      return user_info
    else:
      user_info.picture = config[env].user_header_image_path + user_info.picture
      return user_info
