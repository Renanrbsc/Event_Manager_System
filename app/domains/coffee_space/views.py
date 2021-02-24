from app.domains.coffee_space.actions import CoffeeSpaceAction


class CoffeeSpaceView:

    def post(self):
        name = input("Digite o nome do espaço de café:")
        coffeeSpace = CoffeeSpaceAction().create({"name": name})
        return coffeeSpace

    def get_id(self):
        id = int(input("Digite o id(0,9999) do espaço de café:"))
        coffeeSpace = CoffeeSpaceAction().get(id)
        return coffeeSpace

    def get_all(self):
        coffeeSpaces = CoffeeSpaceAction().get()
        return coffeeSpaces

    def put(self):
        pass

    def delete(self):
        pass
