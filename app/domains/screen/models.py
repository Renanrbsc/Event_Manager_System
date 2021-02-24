

class Screen:

    def menuMain(self):
        print("#------------ MENU PRINCIPAL ------------------#")
        print("#------------ 1 - Estudantes ------------------#")
        print("#------------ 2 - Salas do Evento -------------#")
        print("#------------ 3 - Espaços de Café -------------#")
        print("#------------ exit - Sair ---------------------#")
        print("#----------------------------------------------#")

    def menuStudent(self):
        print("#------------ MENU ESTUDANTE ------------------#")
        print("#------------ 1 - Create ----------------------#")
        print("#------------ 2 - Get ID ----------------------#")
        print("#------------ 3 - Get All ---------------------#")
        print("#------------ 4 - Put -------------------------#")
        print("#------------ 5 - Delete ----------------------#")
        print("#------------ back - Menu Principal -----------#")
        print("#----------------------------------------------#")

    def menuCoffeeSpace(self):
        print("#------------ MENU ESPAÇO DE CAFE -------------#")
        print("#------------ 1 - Create ----------------------#")
        print("#------------ 2 - Get ID ----------------------#")
        print("#------------ 3 - Get All ---------------------#")
        print("#------------ 4 - Put -------------------------#")
        print("#------------ 5 - Delete ----------------------#")
        print("#------------ back - Menu Principal -----------#")
        print("#----------------------------------------------#")

    def menuEventRoom(self):
        print("#------------ MENU SALA DE EVENTOS -------------#")
        print("#------------ 1 - Create ----------------------#")
        print("#------------ 2 - Get ID ----------------------#")
        print("#------------ 3 - Get All ---------------------#")
        print("#------------ 4 - Put -------------------------#")
        print("#------------ 5 - Delete ----------------------#")
        print("#------------ back - Menu Principal -----------#")
        print("#----------------------------------------------#")

    def __str__(self) -> str:
        return f"menu"
