from app.domains.coffee_space.action_mysql import CoffeeSpaceActionMySQL


class CoffeeSpaceView:

    def post(self):
        name = input("Digite o nome do espaço de café:")
        coffeeSpace = CoffeeSpaceActionMySQL().create({"name": name})
        return coffeeSpace

    def get_id(self):
        id = int(input("Digite o id(0,9999) do espaço de café:"))
        coffeeSpace = CoffeeSpaceActionMySQL().get(id)
        return coffeeSpace

    def get_all(self):
        coffeeSpaces = CoffeeSpaceActionMySQL().get()
        return coffeeSpaces

    def put(self):
        pass

    def delete(self):
        pass
