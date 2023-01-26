class GenericSQLError(Exception):
    def __init__(self, message=None) -> None:
        super().__init__(message)


class NoDataError(GenericSQLError):
    pass
