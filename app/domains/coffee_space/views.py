from app.domains.coffee_space.action_mysql import CoffeeSpaceActionMySQL


class CoffeeSpaceView:

    def __init__(self):
        self.action = CoffeeSpaceActionMySQL()

    def post(self):
        name = input("Digite o nome do espaço de café:")
        capacity = int(input("Digite a capacidade maxima do espaço de café:"))
        coffee_space = self.action.create({"name": name, "capacity": capacity})
        return coffee_space

    def get_id(self):
        id = int(input("Digite o id(0,9999) do espaço de café:"))
        coffee_space = self.action.get(id)
        return coffee_space

    def get_all(self):
        coffee_spaces = self.action.get()
        return coffee_spaces

    def put_id(self):
        id = int(input("Digite o id(0,9999) do espaço de café:"))
        name = input("Digite o novo nome do espaço de café:")
        capacity = int(input("Digite a nova capacidade maxima do espaço de café:"))
        coffee_space = self.action.update_id({"name": name, "capacity": capacity}, id)
        return coffee_space

    def delete_id(self):
        id = int(input("Digite o id(0,9999) do espaço de café:"))
        coffee_space = self.action.delete_id(id)
        return coffee_space
