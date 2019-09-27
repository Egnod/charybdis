from ..config import conf


class DramatiqConfig:
    REDIS_HOST = conf.get_credential("redis_host", "localhost")
    REDIS_PORT = conf.get_credential("redis_port", "34007")
    REDIS_PASSWORD = conf.get_credential("redis_password", "charybdis_secrets")

    DRAMATIQ_BROKER = "dramatiq.brokers.redis:RedisBroker"
    DRAMATIQ_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/"
