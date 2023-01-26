from abc import ABC
from typing import Any


class BaseModel(ABC):
    _ID_COLUMN_NAME = None
    _UPDATE_DICT = dict()

    def __init__(self) -> None:
        self._UPDATE_DICT.clear()

    def __setattr__(self, name: str, value: Any) -> None:
        previous_value = self.__dict__.get(name)
        self._UPDATE_DICT.update({name: previous_value})
        super.__setattr__(self, name, value)

    def columns_without_id(self) -> dict:
        return {key: value for key, value in self.__dict__.items() if key != self._ID_COLUMN_NAME}

    def get_updates(self):
        return self._UPDATE_DICT

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.__dict__ == o.__dict__
        else:
            return False
