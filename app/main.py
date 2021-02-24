from app.domains.screen.views import ScreenView
from app.domains.screen.actions import ScreenAction
from app.domains.screen.models import Screen


class MainApp:

    def run(self):
        while True:
            Screen().menuMain()
            op = str(input("Digite a opção escolhida:"))
            if ScreenAction().exit(op):
                break
            ScreenView().optionMain(op)
