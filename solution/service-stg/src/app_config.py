import os

from lib.kafka_connect import KafkaConsumer, KafkaProducer
from lib.pg import PgConnect
from lib.redis import RedisClient


class AppConfig:
    CERTIFICATE_PATH = '/crt/YandexInternalRootCA.crt'
    DEFAULT_JOB_INTERVAL = 25

    def __init__(self) -> None:

        self.kafka_host = str(os.getenv('KAFKA_HOST') or "")
        self.kafka_port = int(str(os.getenv('KAFKA_PORT')) or 0)
        self.kafka_consumer_username = str(os.getenv('KAFKA_CONSUMER_USERNAME') or "")
        self.kafka_consumer_password = str(os.getenv('KAFKA_CONSUMER_PASSWORD') or "")
        self.kafka_consumer_group = str(os.getenv('KAFKA_CONSUMER_GROUP') or "")
        self.kafka_consumer_topic = str(os.getenv('KAFKA_SOURCE_TOPIC') or "")
        self.kafka_producer_username = str(os.getenv('KAFKA_CONSUMER_USERNAME') or "")
        self.kafka_producer_password = str(os.getenv('KAFKA_CONSUMER_PASSWORD') or "")
        self.kafka_producer_topic = str(os.getenv('KAFKA_DESTINATION_TOPIC') or "")

        self.redis_host = str(os.getenv('REDIS_HOST') or "")
        self.redis_port = int(str(os.getenv('REDIS_PORT')) or 0)
        self.redis_password = str(os.getenv('REDIS_PASSWORD') or "")

        self.pg_warehouse_host = str(os.getenv('PG_WAREHOUSE_HOST') or "")
        self.pg_warehouse_port = int(str(os.getenv('PG_WAREHOUSE_PORT') or 0))
        self.pg_warehouse_dbname = str(os.getenv('PG_WAREHOUSE_DBNAME') or "")
        self.pg_warehouse_user = str(os.getenv('PG_WAREHOUSE_USER') or "")
        self.pg_warehouse_password = str(os.getenv('PG_WAREHOUSE_PASSWORD') or "")

    def kafka_producer(self):
        print(f"KAFKA DESTINATION TOPIC: {self.kafka_producer_topic}")
        return KafkaProducer(
            self.kafka_host,
            self.kafka_port,
            self.kafka_producer_username,
            self.kafka_producer_password,
            self.kafka_producer_topic,
            self.CERTIFICATE_PATH
        )

    def kafka_consumer(self):
        print(f"KAFKA_HOST: {self.kafka_host}")
        print(f"KAFKA_PORT: {self.kafka_port}")
        print(f"KAFKA_CONSUMER_USERNAME: {self.kafka_consumer_username}")
        print(f"KAFKA_CONSUMER_PASSWORD: {self.kafka_consumer_password}")
        print(f"KAFKA_TOPIC: {self.kafka_consumer_topic}")
        print(f"KAFKA_GROUP: {self.kafka_consumer_group}")
        print(f"KAFKA_CERTIFICATE_PATH: {self.CERTIFICATE_PATH}")
        return KafkaConsumer(
            self.kafka_host,
            self.kafka_port,
            self.kafka_consumer_username,
            self.kafka_consumer_password,
            self.kafka_consumer_topic,
            self.kafka_consumer_group,
            self.CERTIFICATE_PATH
        )

    def redis_client(self) -> RedisClient:
        return RedisClient(
            self.redis_host,
            self.redis_port,
            self.redis_password,
            self.CERTIFICATE_PATH
        )

    def pg_warehouse_db(self):
        return PgConnect(
            self.pg_warehouse_host,
            self.pg_warehouse_port,
            self.pg_warehouse_dbname,
            self.pg_warehouse_user,
            self.pg_warehouse_password
        )
