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
    from controller.user import user
    app.register_blueprint(user)
