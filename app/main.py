from database.mysql_db.connect import DatabaseMySQL

from app.domains.screen.views import ScreenView
from app.domains.screen.actions import ScreenAction
from app.domains.screen.models import Screen


class MainApp:

    def run(self) -> None:
        db = DatabaseMySQL()
        db.start_connector()
        db.start_tables()

        while True:
            Screen().menuMain()
            op = str(input("Digite a opção escolhida:"))
            if ScreenAction().exit(op):
                break
            ScreenView().optionMain(op)
