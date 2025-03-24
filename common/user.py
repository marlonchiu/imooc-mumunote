from sqlalchemy import Table

from common.database import db_connect

db_session, Base, engine = db_connect()

class User(Base):
  # 表结构的反射加载
  __table__ = Table('user', Base.metadata, autoload_with=engine)

  def get_one(self):
    return db_session.query(User).first()
