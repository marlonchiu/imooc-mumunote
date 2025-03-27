from sqlalchemy import Table, or_, distinct

from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User
from model.favorite import Favorite
from model.feedback import Feedback

db_session, Base, engine = db_connect()

class Article(Base):
    __table__ = Table("article", Base.metadata, autoload_with=engine)
    # 查询出所有文章，但是不要草稿
    def find_article(self, page, article_type="recommend"):
      #  一页显示多少内容呢, 我们默认为一个10, page默认应该是从1开始
      if int(page) < 1:
        page = 1
      count = int(page) * config[env].page_count
      # 这就证明是来到了推荐的分类下边
      if article_type == "recommend":
        result = db_session.query(Article, User.nickname).join(
          User, User.user_id == Article.user_id
        ).filter(
          Article.drafted == 1
        ).order_by(
          Article.browse_num.desc()
        ).limit(count).all()
      else:
        result = db_session.query(Article, User.nickname).join(
          User, User.user_id == Article.user_id
        ).filter(
          Article.label_name == article_type,
          Article.drafted == 1
        ).order_by(
          Article.browse_num.desc()
        ).limit(count).all()

      return result

    # 搜索按钮查询文章
    def search_article(self, page, keyword):
      if int(page) < 1:
        page = 1
      count = int(page) * config[env].page_count

      result = db_session.query(Article, User.nickname).join(
        User, User.user_id == Article.user_id
      ).filter(
        or_(Article.title.like("%"+keyword+"%"),
          Article.article_content.like("%"+keyword+"%"))
      ).order_by(
        Article.browse_num.desc()
      ).limit(count).all()

      return result

    # 获取文章详情
    def get_article_detail(self, article_id):
      result = db_session.query(Article).filter_by(id=article_id).first()
      # 浏览次数+1
      result.browse_num += 1
      db_session.commit()
      return db_session.query(Article).filter_by(id=article_id).first()
      # return db_session.query(Article).filter(Article.id==article_id)

    # 相关文章
    def find_about_article(self, label_name):
      result = db_session.query(Article).filter_by(label_name=label_name).order_by(
        Article.browse_num.desc()
      ).limit(5)

      return result

    # 获取某一个用户所有的不是草稿的文章
    def get_article_by_user_id(self, user_id):
      result = db_session.query(Article).filter_by(
        user_id=user_id,
        drafted=1
      ).all()

      return self.app_path(result)

    # 获取某个用户所有的收藏的文章
    def get_favorite_article_by_user_id(self, user_id):
      result = db_session.query(Article).join(
        Favorite,
        Favorite.article_id == Article.id
      ).filter(
        Favorite.user_id == user_id
      ).order_by(
        Favorite.create_time.desc()
      ).all()

      return self.app_path(result)

    # 获取所有用户评论过的文章
    def get_feedback_article_by_user_id(self,user_id):
      # 用子查询解决查询结果的问题
      article_id_list = db_session.query(
        distinct(Feedback.article_id)
      ).filter_by(user_id=user_id).subquery()
      # 再通过文章id的集合查询到所有文章数据
      result = db_session.query(Article).filter(
        Article.id.in_(article_id_list)
      ).all()

      return self.app_path(result)


    # 添加文章中所有头部图片的路径
    def app_path(self, article_list):
      for article in article_list:
        article.article_image = config[env].article_header_image_path + article.article_image

      return article_list
