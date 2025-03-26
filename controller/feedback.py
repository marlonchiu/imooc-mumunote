import json
from flask import Blueprint,  session, request
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from model.feedback import Feedback

# 创建蓝图对象
feedback = Blueprint('feedback', __name__)

@feedback.route("/feedback", methods=["get","post"])
def article_feedback():
  request_data = json.loads(request.data)
  article_id = request_data.get("article_id")

  try:
    feedback = Feedback()
    feedback.get_feedback_user_list(article_id=article_id)
    return response_message.FeedbackMessage.success("评论成功")
  except Exception as e:
    logging.error(e)
    return response_message.FeedbackMessage.error("评论失败")
