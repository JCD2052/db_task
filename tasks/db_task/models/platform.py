from tasks.db_task.models.base_model import BaseModel


class Platform(BaseModel):
    _ID_COLUMN_NAME = "platform_id"

    def __init__(self, platform_name, platform_id=None) -> None:
        self.platform_id = platform_id
        self.platform_name = platform_name
        super().__init__()

    def __repr__(self) -> str:
        return "PLATFORM " + "\n".join([f"{k}: {v}" for k, v in self.__dict__.items()])
