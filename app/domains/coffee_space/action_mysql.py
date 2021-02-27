from app.domains.coffee_space.models import CoffeeSpace
from database.mysql_db.connect import DatabaseMySQL
from database.mysql_db.tables import Tables


class CoffeeSpaceActionMySQL:

    def __init__(self):
        self.db = DatabaseMySQL()
        self.db.start_connector()

    def create(self, data: dict):
        coffeeSpace = CoffeeSpace(name=data["name"], capacity=data["capacity"])
        if not self.db.get_id(table=Tables.names[2], id=coffeeSpace.getId()):
            self.db.create_data(table=Tables.names[2], data=coffeeSpace.serialize())
            return coffeeSpace.serialize()
        else:
            return f"{str(coffeeSpace)}" \
                    "Unsaved record."

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int = None):
        if id:
            coffeeSpace = CoffeeSpace(id=id)
            coffeeSpaces = self.db.get_id(table=Tables.names[2], id=coffeeSpace.getId())
        else:
            coffeeSpaces = self.db.get_all(table=Tables.names[2])
        print(f"{len(coffeeSpaces)} found.")
        return coffeeSpaces
