from flask import Blueprint, request

user = Blueprint("user",__name__)

# 模块拦截器
@user.before_request
def before_request():
    if request.path.startswith("/v"):
        pass
    else:
        return "模块拦截器拦截 -- 用户请登录"

@user.route("/user/add")
def add_user():
    return"添加用户成功"

@user.route("/user/update")
def update_user():
    return"更新用户成功"

@user.route("/v/user/info")
def info_user():
    return"查看用户信息"
