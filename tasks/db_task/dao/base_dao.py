from abc import ABC
from typing import List

from tasks.db_task.models.base_model import BaseModel
from tasks.db_task.utils.execute_data import ExecuteData
from tasks.db_task.exeptions.custom_sql_exeption import NoDataError
from tasks.db_task.connection.connection import DBConnection
from tasks.db_task.utils.logger import Logger
from psycopg2.extras import execute_values, RealDictCursor


class BaseDAO(ABC):
    _MODEL_CLASS = None
    _TABLE_NAME = None

    @classmethod
    def get_records_by_attributes(cls, search_data: dict = None):
        query = f"SELECT * FROM {cls._TABLE_NAME}"
        stored_values = tuple()
        if search_data:
            query += cls.__build_condition_query(search_data)
            stored_values = tuple(search_data.values())
        Logger.info(f"Query with SELECT request: {query}" % stored_values)
        return cls.__execute(ExecuteData(query, stored_values))

    @classmethod
    def add_records(cls, *models: BaseModel):
        if not models:
            error_message = "no data to insert"
            Logger.error(error_message)
            raise ValueError(error_message)

        query = cls.__create_insert_query()
        Logger.info(f"INSERT query: {query}.")
        stored_values = tuple(tuple(model.columns_without_id().values()) for model in models)
        return cls.__execute_many(ExecuteData(query, stored_values))

    @classmethod
    def update_record(cls, model_to_update: BaseModel):
        data = model_to_update.__dict__
        if not data:
            raise ValueError("empty updates")
        columns = ", ".join(data.keys())
        placeholders = ", ".join("%s" for _ in range(0, len(data)))
        update_values = model_to_update.get_updates()
        query = f"UPDATE {cls._TABLE_NAME} SET ({columns}) = ({placeholders}) " \
                f"{cls.__build_condition_query(update_values)} RETURNING *"
        stored_values = tuple(list(data.values()) + list(update_values.values()))
        return cls.__execute(ExecuteData(query, stored_values))

    @classmethod
    def delete_record(cls, data: dict) -> List[ExecuteData]:
        query = f"DELETE FROM {cls._TABLE_NAME} {cls.__build_condition_query(data)} RETURNING *"
        stored_values = tuple(data.values())
        Logger.info(f"Query with DELETE request: {query}. Values: {stored_values}")
        return cls.__execute(ExecuteData(query, stored_values))

    @classmethod
    def __create_insert_query(cls):
        data = cls._MODEL_CLASS(None).columns_without_id()
        columns = ", ".join(data.keys())
        return f"INSERT INTO {cls._TABLE_NAME} ({columns}) VALUES %s RETURNING *;"

    @classmethod
    def __execute_many(cls, execute_data: ExecuteData) -> List:
        with DBConnection.get_connection() as con:
            with con.cursor(cursor_factory=RealDictCursor) as cursor:
                Logger.info(f"Prepared data to be executed: {execute_data}")
                return [cls._MODEL_CLASS(**row)
                        for row in execute_values(cursor, execute_data.query, execute_data.stored_values, fetch=True)]

    @classmethod
    def __execute(cls, execute_data: ExecuteData):
        with DBConnection.get_connection() as con:
            with con.cursor(cursor_factory=RealDictCursor) as cursor:
                Logger.info(f"Prepared data to be executed: {execute_data}")
                cursor.execute(execute_data.query, execute_data.stored_values)
                row_count = cursor.rowcount
                Logger.info(f"Received : {row_count} rows")
                if row_count == 0:
                    Logger.error(f"received 0 rows from DB.")
                    raise NoDataError("received 0 rows from DB.")
                return [cls._MODEL_CLASS(**row) for row in cursor.fetchall()]

    @staticmethod
    def __build_condition_query(columns: dict) -> str:
        condition = " WHERE " + " AND ".join(f"{key} = %s" for key in columns.keys())
        return condition
