class ScreenAction:

    def option(self, op: str, view: object):
        if op == "1":
            print(view.post())
        elif op == "2":
            print(view.get_id())
        elif op == "3":
            print(view.get_all())

    def exit(self, op: str):
        if op == "exit":
            print("Até mais!")
            return True
        return False

    def back(self, op: str):
        if op == "back":
            print("Voltando ao menu principal!")
            return True
        return False