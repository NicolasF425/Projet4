from time import sleep
from utilities.clear_screen import clear_screen


class MainView:
    '''Vue menu principal'''

    TITRE_VUE = "GESTION DE TOURNOIS D'ECHECS\n"

    def __init__(self, elements_menu):
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)

    def print_view(self):
        clear_screen()
        print(self.TITRE_VUE)
        for item in self.elements_menu:
            print(item)

    def input_choice(self):
        choix_ok = False
        while choix_ok is False:
            self.print_view()
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
