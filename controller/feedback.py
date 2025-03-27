import json
from flask import Blueprint, request, session, make_response, jsonify
import logging
import time

from app.config.config import config
from app.settings import env
from common import response_message
from model.feedback import Feedback
from common.utils import compress_image, model_to_json
from app.config.ue_config import FEEDBACK_UECONFIG

# 创建蓝图对象
feedback = Blueprint('feedback', __name__)

@feedback.route("/feedback/list", methods=["get","post"])
def article_feedback_list():
  request_data = json.loads(request.data)
  article_id = request_data.get("article_id")

  try:
    feedback = Feedback()
    result = feedback.get_feedback_user_list(article_id=article_id)
    return response_message.FeedbackMessage.success(result)
  except Exception as e:
    logging.error(e)
    return response_message.FeedbackMessage.error("评论获取失败")

@feedback.route("/feedback", methods=["get","post"])
def ueditor():
  param = request.args.get("action")
  print('ueditor_______________', param)

  if request.method == "GET" and param == "config":
    return make_response(FEEDBACK_UECONFIG)
  # 下边是我们做图片上传的代码
  # elif param == "uploadimage":
  elif param == "image":
    f = request.files.get("file")
    filename = f.filename
    # 文件的后缀名
    suffix = filename.split(".")[-1]
    newname = time.strftime("%Y%m%d_%H%M%S."+suffix)
    f.save("resource/upload/"+newname)
    # 大图片压缩
    source = dest = "resource/upload" + newname
    compress_image(source, dest, 1200)

    # 构造响应数据
    result = {}
    result["state"] = "SUCCESS"
    result['url'] = "/upload/" + newname
    result["title"]= filename
    result["original"] = filename
    return jsonify(result)
