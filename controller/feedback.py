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
def article_feedback_list():
  request_data = json.loads(request.data)
  article_id = request_data.get("article_id")

  try:
    feedback = Feedback()
    result = feedback.get_feedback_user_list(article_id=article_id)
    return response_message.FeedbackMessage.success(result)
  except Exception as e:
    logging.error(e)
    return response_message.FeedbackMessage.error("评论失败")
