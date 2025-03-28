import json
import time
import random

from flask import Blueprint, request, render_template, session, jsonify
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from common.utils import compress_image
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
  user_id = session.get("user_id")
  return render_template("new-article.html",
                        label_types=label_types,
                        article_types=article_types,
                        article_tags=article_tags,
                        )


def get_article_request_param(request_data):
  user = User().find_by_user_id(session.get("user_id"))
  title = request_data.get("title")
  article_content = request_data.get("article_content")
  return user, title, article_content

# 草稿或文章存储
@article.route("/article/save",methods=["post"])
def article_save():
  request_data = json.loads(request.data)
  # 我们根据article_id来判断是不是第一次保存，如果没有这个id就存储为草稿，如果有那么就文章发布
  # 其实文章发布就是文章更新
  article_id = request_data.get("article_id")
  # 取出是否是草稿
  drafted = request_data.get("drafted")
  # 必须让前端传一个article_id，那么这个值如果是-1我们就认为是草稿
  if article_id == -1 and drafted == 0:
    user, title, article_content = get_article_request_param(request_data)
    if title == "":
      return response_message.ArticleMessage.other("请输入文章头信息")
    # 存储草稿的时候一定要返回一个article_id回来
    article_id = Article().insert_article(user.user_id,title,article_content,drafted)
    return response_message.ArticleMessage.save_success(article_id, "草稿存储成功")

  elif article_id > -1:
    user, title, article_content = get_article_request_param(request_data)
    if title == "":
        return response_message.ArticleMessage.other("请输入文章头信息")
    # 图片信息就不在这里获取了，当用户点击上传头像的时候，这个头像信息就应该已经更新到数据库里了
    # 所以图片上传这个动作应该发生在文章发布的前边
    label_name = request_data.get("label_name")
    article_tag = request_data.get("article_tag")
    article_type = request_data.get("article_type")

    article_id = Article().update_article(
      article_id=article_id,
      title=title,
      article_content=article_content,
      drafted=drafted,
      label_name=label_name,
      article_tag=article_tag,
      article_type=article_type
    )

    return response_message.ArticleMessage.save_success(article_id, "发布文章成功")


# 上传文章头部图片
@article.route("/article/upload/article_header_image", methods=["POST"])
def upload_article_header_image():
  # 获取前端图片文件
  f = request.files.get("header-image-file")
  filename = f.filename

  # 文件的后缀名
  suffix = filename.split(".")[-1]
  newname = time.strftime("%Y%m%d_%H%M%S." + suffix)
  newname = "article-header-" + newname
  f.save("resource/upload/" + newname)
  # 大图片压缩
  source = dest = "resource/upload/" + newname
  compress_image(source, dest, 1200)

  # 更新数据库
  article_id = request.form.get("article_id")
  Article().update_article_header_image(article_id, newname)

  # 构造响应数据
  result = {}
  result["state"] = "SUCCESS"
  result['url'] = "/upload/" + newname
  result["title"] = filename
  result["original"] = filename
  return jsonify(result)


# 随机文章头部图片
@article.route("/article/random/article_header_image", methods=["POST"])
def random_article_header_image():
  name = random.randint(1,100)
  newname = str(name) + ".jpg"

  # 更新数据库
  article_id = request.form.get("article_id")
  Article().update_article_header_image(article_id, newname)

  # 构造响应数据
  result = {}
  result["state"] = "SUCCESS"
  result['url'] = "/upload/" + newname
  result["title"] = newname
  result["original"] = newname
  return jsonify(result)
