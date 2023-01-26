from tasks.db_task.dao.base_dao import BaseDAO
from tasks.db_task.models.genre import Genre


class GenreDAO(BaseDAO):
    _TABLE_NAME = "GAME_GENRE"
    _MODEL_CLASS = Genre
