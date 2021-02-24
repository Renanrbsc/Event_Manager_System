from app.domains.screen.models import Screen
from app.domains.screen.actions import ScreenAction

from app.domains.student.views import StudentView
from app.domains.coffee_space.views import CoffeeSpaceView
from app.domains.event_room.views import EventRoomView


class ScreenView:

    def optionMain(self, op: str):
        screen = Screen()
        if op == "1":
            menu = screen.menuStudent
            self.renderScreen(menu, StudentView())
        elif op == "2":
            menu = screen.menuEventRoom
            self.renderScreen(menu, EventRoomView())
        elif op == "3":
            menu = screen.menuCoffeeSpace
            self.renderScreen(menu, CoffeeSpaceView())

    def renderScreen(self, menu, view):
        while True:
            menu()
            op = str(input("Digite a opção escolhida:"))
            if ScreenAction().back(op):
                break
            ScreenAction().option(op, view)
