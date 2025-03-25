from flask import Blueprint, render_template, request
import logging
from app.config.config import config
from app.settings import env

from model.article import Article

index = Blueprint("index",__name__)

@index.route("/")
def home():
    # 获取当前到底是第几页
    page = request.args.get("page")
    article_type = request.args.get("article_type")
    logging.debug("page: " + str(page))
    logging.debug("article_type: "+ str(article_type))

    if page is None:
        page = 1
    if article_type is None:
        article_type = "recommend"

    #  到数据库中查询文章数据，然后返回给前端页面
    article = Article()
    db_result = article.find_article(page, article_type)

    return render_template("index.html", result=db_result)
