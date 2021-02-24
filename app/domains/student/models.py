from random import randint


class Student:
    _id = str()
    _name = str()
    _lastname = str()

    def __init__(self, id: int = None, name: str = "", lastname: str = ""):
        self.setId(id)
        self.setName(name)
        self.setLastname(lastname)

    def setId(self, id: int) -> None:
        if id:
            self._id = '%04d' % id
        else:
            self._id = '%04d' % randint(0, 9999)

    def getId(self) -> str:
        return self._id

    def setLastname(self, lastname: str) -> None:
        self._lastname = lastname

    def getLastname(self) -> str:
        return self._lastname

    def setName(self, name: str) -> None:
        self._name = name

    def getName(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"{self.getId()},{self.getName()},{self.getLastname()}\n"
