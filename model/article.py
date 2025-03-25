from sqlalchemy import Table, or_
from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User

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
