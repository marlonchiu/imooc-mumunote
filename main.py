# 导入 Flask
from flask import Flask
import os

app = Flask(__name__)

# 设置secret key用于session加密
app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机密钥

@app.route('/')
def hello_world():
    return 'Hello Flask!'

# 注册蓝图
from controller.user import user
app.register_blueprint(user)

from controller.article import article
app.register_blueprint(article)

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
