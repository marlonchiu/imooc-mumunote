from flask import Blueprint

article = Blueprint('article', __name__)

@article.route('/article/add')
def add_article():
    return '添加文章成功'
