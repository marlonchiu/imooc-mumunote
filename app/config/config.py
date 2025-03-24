# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://root:123456@127.0.0.1:3306/mumushouji"

# 测试环境
class TestConfig(Config):
    # db_url = ""
    if_echo=True

class ProductionConfig(Config):
    if_echo=False

config = {
    "test": TestConfig,
    "prop": ProductionConfig
}
