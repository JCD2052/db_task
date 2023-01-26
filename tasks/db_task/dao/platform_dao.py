from tasks.db_task.dao.base_dao import BaseDAO
from tasks.db_task.models.platform import Platform


class PlatformDAO(BaseDAO):
    _MODEL_CLASS = Platform
    _TABLE_NAME = "PLATFORM"
