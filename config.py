import redis


# 定义配置类
class Config(object):
    DEBUG = True
    # 添加SQLAlchemy的配置信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/info_46'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 添加redis的配置信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session的配置信息
    SECRET_KEY = 'qwedfghnjmpoijhgfcxzuhjnasdfghjkl'
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


# 线上/生成
class ProductionConfig(Config):
    DEBUG = False


# 线下/开发
class DevelopmentConfig(Config):
    DEBUG = True


# 测试环境
class TestingConfig(Config):
    TESTING = True
