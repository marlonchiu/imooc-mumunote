import json
import random
import time
from flask import Blueprint, request, session, make_response, url_for, render_template

import logging

from app.config.config import config
from app.settings import env
from common import response_message
from model.article import Article
from model.user import User

# 创建蓝图对象
personal = Blueprint('personal', __name__)

@personal.before_request
def personal_before_request():
  url = request.path
  is_login = session.get("is_login")
  if url.startswith("/personal") and is_login != 'true':
    response = make_response("登录重定向", 302)
    response.headers["Location"] = url_for("index.home")
    return response

@personal.route("/personal")
def personal_center():
    # url ?type=我的评论、 我的收藏
    type_name = request.args.get("type")
    if type_name is None:
      type_name = "article"
    user_id = session.get("user_id")
    # user_id = 1

    # 如果是文章
    article = Article()
    if type_name == "article":
      article_data = article.get_article_by_user_id(user_id)

    # 如果是收藏
    elif type_name == "favorite":
      article_data = article.get_favorite_article_by_user_id(user_id)

    # 如果是评论
    elif type_name == "feedback":
      article_data = article.get_feedback_article_by_user_id(user_id)

    else:
      return response_message.PersonalMessage.error("参数传递错误")

    user = User().find_by_user_id(user_id)
    return render_template("personal_center.html",
                          article_data=article_data,
                          type_name=type_name,
                          active=type_name,
                          user=user)
