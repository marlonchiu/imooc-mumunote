# 导入 Flask
from flask import Flask, request, session
import os

app = Flask(__name__, template_folder="template")

# 设置secret key用于session加密
app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机密钥

@app.route('/')
def hello_world():
    return 'Hello Flask!'

# 注册蓝图
# from controller.index import index
# app.register_blueprint(index)
# from controller.index2 import index2
# app.register_blueprint(index2)
# from controller.index3 import index3
# app.register_blueprint(index3)
# from controller.index4 import index4
# app.register_blueprint(index4)
# from controller.index5 import index5
# app.register_blueprint(index5)
# from controller.index6 import index6
# app.register_blueprint(index6)
# from controller.my_orm1 import my_orm1
# app.register_blueprint(my_orm1)
# from controller.my_sqlalchemy import my_sqlalchemy
# app.register_blueprint(my_sqlalchemy)

# 自定义过滤器
@app.template_filter('add_double')
def add_double(value):
    return value * 2

# 全局函数
def global_sum(a,b):
    return a+b
app.jinja_env.globals['global_sum'] = global_sum
# app.jinja_env.globals.update(global_sum=global_sum)


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=8080, debug=True)
