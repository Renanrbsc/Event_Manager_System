class Process:

    def show_tables(self) -> str:
        return "SHOW TABLES"

    def insert_into(self, table: str, columns: list) -> str:
        columns_str = ', '.join(columns)
        values_str = ', '.join(['%s' for i in range(len(columns))])
        return f"INSERT INTO {table} ({columns_str}) " \
               f"VALUES ({values_str});"

    def select_id(self, table: str) -> str:
        return f"SELECT * " \
               f"FROM {table} " \
               f"WHERE (id=%s);"

    def select_all(self, table: str) -> str:
        return f"SELECT * FROM {table};"

    def update_id(self, table: str, columns: list) -> str:
        sql = f"UPDATE {table} " \
              f"SET {columns[1]}=%s, " \
              f"SET {columns[2]}=%s " \
              f"WHERE {columns[0]}=%s;"
        return sql

    def delete_id(self):
        pass


print(Process().update_id("aaaaaaa", ["ssss", "ssssssss"]))