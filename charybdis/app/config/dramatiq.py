from .credentials import get_credential


class DramatiqConfig(object):
    REDIS_HOST = get_credential("redis_host", "localhost")
    REDIS_PORT = get_credential("redis_port", "34007")
    REDIS_PASSWORD = get_credential("redis_password", "charybdis_secrets")

    DRAMATIQ_BROKER = "dramatiq.brokers.redis:RedisBroker"
    DRAMATIQ_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/"
