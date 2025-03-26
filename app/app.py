from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder="../template", static_url_path="/", static_folder="../resource")

    # 注册蓝图
    init_blueprint(app)

    # 设置secret key用于session加密
    app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机密钥

    return app

def init_blueprint(app):
    from controller.index import index
    app.register_blueprint(index)

    from controller.user import user
    app.register_blueprint(user)

    from controller.article import article
    app.register_blueprint(article)

    from controller.favorite import favorite
    app.register_blueprint(favorite)

    from controller.feedback import feedback
    app.register_blueprint(feedback)
