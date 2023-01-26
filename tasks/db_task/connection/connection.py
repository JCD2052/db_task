import psycopg2

from tasks.db_task.connection.config import DB_CONFIG
from tasks.db_task.connection.singleton import MetaSingleton


class DBConnection(metaclass=MetaSingleton):

    @staticmethod
    def get_connection():
        return psycopg2.connect(**DB_CONFIG)
