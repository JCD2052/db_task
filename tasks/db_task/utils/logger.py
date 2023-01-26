import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Union


class LoggerConfig:
    LOGS_DIR_NAME = "tasks/db_task"
    LOGGER_NAME = "Logger"
    LOGS_FILE_NAME = LOGS_DIR_NAME + os.sep + "logs.log"
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = "[%(asctime)s - %(levelname)s] - %(message)s"
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler = RotatingFileHandler(LoggerConfig.LOGS_FILE_NAME, maxBytes=LoggerConfig.MAX_BYTES,
                                    backupCount=LoggerConfig.BACKUP_COUNT)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __handler.setFormatter(__formatter)
    __logger.addHandler(__handler)

    @staticmethod
    def set_level(level: Union[str, int]) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        Logger.__logger.info(msg=message)

    @staticmethod
    def debug(message: str) -> None:
        Logger.__logger.debug(msg=message)

    @staticmethod
    def warning(message: str) -> None:
        Logger.__logger.warning(msg=message)

    @staticmethod
    def error(message: str) -> None:
        Logger.__logger.error(msg=message)

    @staticmethod
    def fatal(message: str) -> None:
        Logger.__logger.fatal(msg=message)

    @staticmethod
    def step(message: str) -> None:
        Logger.__logger.info(msg=message)
