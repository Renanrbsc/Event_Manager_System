from random import randint


class CoffeeSpace:
    _id = str()
    _name = str()
    _capacity = str()

    def __init__(self, id: int = None, name: str = "", capacity: int = None):
        self.setId(id)
        self.setName(name)
        self.setCapacity(capacity)

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

    def setCapacity(self, capacity: int) -> None:
        if capacity:
            self._capacity = '%03d' % capacity
        else:
            self._capacity = '%03d' % 0

    def getCapacity(self) -> str:
        return self._capacity

    def serialize(self) -> dict:
        return {"id": self.getId(),
                "name": self.getName(),
                "capacity": self.getCapacity()}

    def __str__(self) -> str:
        return f"{self.getId()},{self.getName()},{self.getCapacity()}\n"
