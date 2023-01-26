from tasks.db_task.models.base_model import BaseModel


class Genre(BaseModel):
    _ID_COLUMN_NAME = "genre_id"

    def __init__(self, genre_name, genre_id=None) -> None:
        self.genre_id = genre_id
        self.genre_name = genre_name
        super().__init__()

    def __repr__(self) -> str:
        return "GENRE " + "\n".join([f"{k}: {v}" for k, v in self.__dict__.items()])
