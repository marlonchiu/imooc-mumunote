
from flask import Blueprint, request, render_template

from app.config.config import config
from app.settings import env
from common import response_message
from model.article import Article
from model.user import User

article = Blueprint("article",__name__)

@article.route("/detail", methods=["GET"])
def article_detail():
  article_id = request.args.get("article_id")
  article = Article()
  # 获取文章的所有信息
  article_content = article.get_article_detail(article_id)

  # 获取文章作者信息
  user = User()
  user_info = user.find_by_user_id(article_content.user_id)

  # @todo 待办 补充获取文章的评论信息

  # @todo 待办 补充获取文章的点赞信息

  # @todo 待办 "我"是否收藏
  is_favorite = 1

  return render_template("article-info.html",
                        article_content=article_content,
                        user_info=user_info,
                        is_favorite=is_favorite
                        )
