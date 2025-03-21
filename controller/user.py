from flask import Blueprint

user = Blueprint("user",__name__)

@user.route("/user/add")
def add_user():
    return"添加用户成功"


@user.route("/user/update")
def update_user():
    return"更新用户成功"
