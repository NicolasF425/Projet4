from utilities.clear_screen import clear_screen
from time import sleep


class MenuView:

    def __init__(self, titre_vue, elements_menu):
        self.titre_vue = titre_vue
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)

    def print_view(self, nocls=False, title=True):
        if nocls is False:
            clear_screen()
        if title is True:
            print(self.titre_vue)
        for item in self.elements_menu:
            print(item)

    def input_choice(self, nocls=False, title=True):
        choix_ok = False
        while choix_ok is False:
            self.print_view(nocls, title)
            choix = input("\nSélectioner : ")
            choix_ok = self.check_choix(choix)
        return int(choix)

    def check_choix(self, choix):
        try:
            choix = int(choix)
        except ValueError:
            print("Veuillez Entrer un nombre !")
            sleep(2)
            return False
        if choix > 0 and choix <= self.nb_elements:
            return True
        else:
            print("Vous devez choisir une option de 1 à "+str(self.nb_elements))
            sleep(2)
            return False

    def print_info(info):
        print(info)
