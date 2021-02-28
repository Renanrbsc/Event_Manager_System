from app.domains.coffee_space.models import CoffeeSpace
from app.domains.coffee_space.db_mysql import CoffeeRoomMySQL


class CoffeeSpaceActionMySQL:

    def __init__(self):
        self.db = CoffeeRoomMySQL()

    def create(self, data: dict):
        coffee_space = CoffeeSpace(name=data["name"],
                                   capacity=data["capacity"])
        if not self.db.get_by_id(id=coffee_space.getId()):
            row = self.db.post(data=coffee_space.serialize())
            return f"{coffee_space.serialize()}\n{row}"
        else:
            return f"{coffee_space.serialize()}\nRegistro não salvo."

    def update_id(self, data: dict, id: int):
        coffee_space = CoffeeSpace(id=id,
                                   name=data["name"],
                                   capacity=data["capacity"])
        if self.db.get_by_id(id=coffee_space.getId()):
            row = self.db.put_id(data=coffee_space.serialize())
            return f"{coffee_space.serialize()}\n{row}"
        else:
            return f"{coffee_space.serialize()}\nRegistro não encontrado."

    def delete_id(self, id: int = None):
        coffee_space = CoffeeSpace(id=id)
        if self.db.get_by_id(id=coffee_space.getId()):
            return self.db.remove_id(id=coffee_space.getId())
        else:
            return f"Registro não encontrado."

    def get(self, id: int = None):
        if id:
            coffee_space = CoffeeSpace(id=id)
            coffee_spaces = self.db.get_by_id(id=coffee_space.getId())
        else:
            coffee_spaces = self.db.get_all()
        print(f"{len(coffee_spaces)} encontrado(s).")
        return coffee_spaces
