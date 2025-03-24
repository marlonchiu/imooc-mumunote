from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from app.config.config import config
from app.settings import env
print('______env______',env)


def db_connect():
    # 创建一个引擎，连接数据库
    config_class = config[env]
    print(config_class)
    engine = create_engine(config_class.db_url, echo=config_class.if_echo)
    # 打开数据库的连接会话
    session = sessionmaker(engine)
    # 保证线程安全
    db_session = scoped_session(session)
    # 获取基类
    Base = declarative_base()

    return db_session, Base, engine
