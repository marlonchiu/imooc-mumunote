import random
from sqlalchemy import Table

from app.config.config import config
from app.settings import env
from common.database import db_connect
from common.utils import model_to_json
from model.user import User

db_session, Base, engine = db_connect()

class Feedback(Base):
  # 表结构的反射加载
  __table__ = Table('comment', Base.metadata, autoload_with=engine)

  """
    我们需要最终给前端返回一个完整的数据
    那么最终的数据样式
    final_data_list=[{
    最上层评论的数据以及用户数据，
    replay_list:[{
        from_user:"",
        to_user:"",
        reply:""
    },{},{}]
    },{},{}]

  """
  # 查询文章的评论列表
  def get_feedback_user_list(self, article_id):
    final_data_list = []
    # 查询文章的一级评论 ，就是那些带有楼层的，新开的评论
    feedback_list = self.find_feedback_by_article_id(article_id)
    for feedback in feedback_list:
      user = User()
      # 根据一级评论的数据，获取回复评论的评论的内容
      all_reply = self.find_reply_by_reply_id(base_reply_id=feedback.id)
      feedback_user = user.find_by_user_id(feedback.user_id)
      reply_list = []
      # 再根据每一条回复的评论，查询用户信息
      for reply in all_reply:
          # 用于存储当前这条原始评论的所有回复评论，如果没有回复，这个值就为空
          reply_content_with_user = {}
          from_user_data = user.find_by_user_id(reply.user_id)
          # 获取回复谁的评论的用户信息
          to_user_reply_data = self.find_reply_by_id(reply.reply_id)
          to_user_data = user.find_by_user_id(to_user_reply_data[0].user_id)

          reply_content_with_user["from_user"] = model_to_json(from_user_data)
          reply_content_with_user["to_user"] = model_to_json(to_user_data)
          reply_content_with_user["content"] = model_to_json(reply)
          reply_list.append(reply_content_with_user)

      # 存储每一个回复下的所有数据
      every_feedback_data = model_to_json(feedback)
      every_feedback_data.update(model_to_json(feedback_user))
      every_feedback_data["reply_list"] = reply_list
      final_data_list.append(every_feedback_data)

    return final_data_list

  # 查询文章的一级评论
  def find_feedback_by_article_id(self, article_id):
    result = db_session.query(Feedback).filter_by(
      article_id = article_id,
      reply_id = 0,
      base_reply_id = 0
      ).order_by(
        Feedback.id.desc()
      ).all()
    return result

  # 获取回复评论的评论
  def find_reply_by_reply_id(self, base_reply_id):
    result = db_session.query(Feedback).filter_by(
      base_reply_id = base_reply_id
      ).order_by(
        Feedback.id.desc()
      ).all()
    return result

  # 获取回复评论的评论
  def find_reply_by_id(self, id):
    result = db_session.query(Feedback).filter(
      Feedback.id == id
      ).order_by(
        Feedback.id.desc()
      ).all()
    return result

  # 获取评论数量
  def get_article_feedback_count(self, article_id):
    result = db_session.query(Feedback).filter_by(
      article_id=article_id,
      reply_id=0,
      base_reply_id=0
      ).count()
    return result
