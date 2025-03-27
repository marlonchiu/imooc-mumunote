import redis
from datetime import datetime
from app.config.config import config
from app.settings import env

def redis_connect():
    redis_config = config[env]
    pool = redis.ConnectionPool(
        host=redis_config.REDIS_HOST,
        port=redis_config.REDIS_PORT,
        # password=redis_config.REDIS_PASSWORD,
        max_connections=redis_config.REDIS_POLL,
        db=redis_config.REDIS_DB,
        decode_responses=redis_config.REDIS_DECODE_RESPONSES,
    )
    return redis.Redis(connection_pool=pool)



# 一次性把mysql中的用户数据初始化到redis中
from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User

db_session, Base, engine = db_connect()

def model_list(result):
  list = []
  for row in result:
    dict = {}
    for k, v in row.__dict__.items():
      if not k.startswith("_sa_"):
        if isinstance(v, datetime):
          v = v.strftime("%Y-%m-%d %H:%M:%S")
        dict[k] = v
    list.append(dict)
  return list


def mysql_to_redis_string():
  redis_client = redis_connect()
  result = db_session.query(User).all()
  # 把这个result需要转换成 [{},{},{}]
  user_list = model_list(result)
  for user in user_list:
    redis_client.set("user:"+user["username"],str(user))

# mysql_to_redis_string()

def mysql_to_redis_hash():
  redis_client = redis_connect()
  result = db_session.query(User).all()
  # 把这个result需要转换成 [{},{},{}]
  user_list = model_list(result)
  for user in user_list:
    redis_client.hset("hash_user:" + user["username"], user["username"], user["password"])

# mysql_to_redis_hash()
