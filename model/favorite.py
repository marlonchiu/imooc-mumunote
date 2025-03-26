import random
from sqlalchemy import Table

from app.config.config import config
from app.settings import env
from common.database import db_connect

db_session, Base, engine = db_connect()

class Favorite(Base):
  # 表结构的反射加载
  __table__ = Table('favorite', Base.metadata, autoload_with=engine)

  def update_status(self, article_id, user_id, canceled=0):
    # 查询一下这个用户是否收藏过，如果没有收藏，那么就插入数据，如果收藏过，那么就更新数据
    # canceled的值为的意思就是收藏，为1的意思就是收藏
    favorite_data = db_session.query(Favorite).filter_by(article_id=article_id, user_id=user_id).first()
    if favorite_data is not None:
      # 更新数据
      favorite_data.canceled = canceled
    else:
      # 插入数据
      insert_data = {
        "article_id": article_id,
        "user_id": user_id,
        "canceled": canceled
      }
      favorite = Favorite(**insert_data)
      db_session.add(favorite)
    db_session.commit()

  # 查询某个用户是否收藏
  def user_if_favorite(self, user_id, article_id):
      result = db_session.query(Favorite.canceled).filter_by(
          user_id=user_id,
          article_id=article_id
      ).first()
      if result is None:
        return 1
      else:
        return result[0]
