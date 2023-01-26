class ExecuteData:
    def __init__(self, query: str, stored_values: tuple) -> None:
        self.query = query
        self.stored_values = stored_values

    def __repr__(self) -> str:
        return f"QUERY: {self.query}   VALUES: {self.stored_values}"
