from app.domains.coffee_space.models import CoffeeSpace
from database.text_db.process import read_all, read_id, append_model


class CoffeeSpaceActionText:

    def create(self, data: dict):
        coffeeSpace = CoffeeSpace(name=data["name"], capacity=data["capacity"])

        if not read_id(local_name="coffee_space", model=coffeeSpace):
            append_model(local_name="coffee_space", model=coffeeSpace)
            return coffeeSpace
        else:
            return f"Registro não salvo!\n"

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int = None):
        if id:
            coffeeSpaces = read_id(local_name="coffee_space", model=CoffeeSpace(id=id))
        else:
            coffeeSpaces = read_all(local_name="coffee_space")
        return coffeeSpaces
