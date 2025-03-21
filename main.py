# 导入 Flask
from flask import Flask, request, session
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

@app.route('/login')
def login():
    session["islogin"] = True
    print(session)
    return '登录成功'

@app.route("/update_user")
def update_user():
    return"修改用户信息成功"

# # 全局拦截器,不管请求的url是什么，都会先执行这个函数
# @app.before_request
# def before_request():

#     # 获取请求的url
#     # 拦截器，如果用户没有登录，则跳转到登录页面
#     url = request.path
#     print(url)

#     # 定义白名单
#     pass_path = ['/', '/login']
#     #定义一个可通过的后缀名
#     suffix = url.endswith("png") or url.endswith("jpg") or url.endswith("css") or url.endswith("js")

#     print(session)
#     print(session.get("islogin"))

#     # 如果是白名单中的url，则放行
#     if url in pass_path or suffix:
#       pass
#     else:
#       # 判断用户是否登录
#       if not session.get("islogin"): # 如果用户没有登录，则跳转到登录页面
#         return "请登录"
#       else: # 如果用户登录，则放行
#         return "用户已经登陆了~ 放行"

# 定制页面的错误处理
@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return "输入网址错误，页面不存在~~~~"

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
