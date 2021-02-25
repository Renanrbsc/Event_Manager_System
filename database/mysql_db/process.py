class Process:

    def show_tables(self) -> str:
        return "SHOW TABLES"

    def insert_into(self, table: str, columns: list):
        columns_str = ', '.join(columns)
        values_str = ', '.join(['%s' for i in range(len(columns))])
        return f"INSERT INTO {table} ({columns_str}) " \
               f"VALUES ({values_str})"

    def select_id(self, table: str):
        return f"SELECT * " \
               f"FROM {table} " \
               f"WHERE (id=%s)"

    def select_all(self, table: str):
        return f"SELECT * FROM {table}"

    def update_in(self):
        pass

    def delete_from(self):
        pass
