
from flask import Blueprint, request, render_template, session

from app.config.config import config
from app.settings import env
from common import response_message
from model.article import Article
from model.favorite import Favorite
from model.user import User
from model.feedback import Feedback

article = Blueprint("article",__name__)
label_types = config[env].label_types
article_types = config[env].article_types
article_tags = config[env].article_tags

@article.route("/detail", methods=["GET"])
def article_detail():
  article_id = request.args.get("article_id")
  article = Article()
  # 获取文章的所有信息
  article_content = article.get_article_detail(article_id)
  article_tag_string = article_content.article_tag
  article_tag_list = article_tag_string.split(",")

  # 获取文章作者信息
  user = User()
  user_info = user.find_by_user_id(article_content.user_id)

  # @todo 待办 补充获取文章的评论信息
  feedback_data_list = Feedback().get_feedback_user_list(article_id)
  feedback_count = Feedback().get_article_feedback_count(article_id)

  # @todo 待办 "我"是否收藏
  is_favorite = 1
  # 判断我是否登录
  if session.get("is_login") == "true":
    user_id = session.get("user_id")
    is_favorite = Favorite().user_if_favorite(user_id,article_id)

  # 相关文章（label_name 相同）
  about_article = article.find_about_article(article_content.label_name)

  return render_template("article-info.html",
                        article_content=article_content,
                        user_info=user_info,
                        is_favorite=is_favorite,
                        article_tag_list=article_tag_list,
                        about_article=about_article,
                        feedback_data_list=feedback_data_list,
                        feedback_count=feedback_count,
                        )


@article.route("/article/new")
def article_new():
  print("🚀 ~ article_new:")
  # user_id = session.get("user_id")
  return render_template("new-article.html",
                        label_types=label_types,
                        article_types=article_types,
                        article_tags=article_tags,)
