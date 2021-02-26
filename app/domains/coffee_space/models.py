from random import randint


class CoffeeSpace:
    _id = str()
    _name = str()

    def __init__(self, id: int = None, name: str = ""):
        self.setId(id)
        self.setName(name)

    def setId(self, id: int) -> None:
        if id:
            self._id = '%04d' % id
        else:
            self._id = '%04d' % randint(0, 9999)

    def getId(self) -> str:
        return self._id

    def setName(self, name: str) -> None:
        self._name = name

    def getName(self) -> str:
        return self._name

    def serialize(self) -> dict:
        return {"id": self.getId(),
                "name": self.getName()}

    def __str__(self) -> str:
        return f"{self.getId()},{self.getName()}\n"
