class ListView:
    '''Classe pour l'affichage d'un menu dans une vue'''

    SPACES = "                                                                                "
    largeurs_colonnes = []

    def __init__(self):
        pass

    def print_line(self, elements, largeurs_colonnes):
        '''Ecrit une liste d'éléments textes
        Attention le nombre de colonnes doit égaler celui d'éléments'''

        line = "|"
        i = 0
        for element in elements:
            if type(element) is int:
                element = str(element)
            delta_longueur = len(element)-largeurs_colonnes[i]
            if delta_longueur < 0:   # element plus court que largeur colonne
                element = element + self.SPACES[0:-delta_longueur]
            else:
                element = element[0:largeurs_colonnes[i]]
            element = element + "|"
            if largeurs_colonnes[i] > 0:
                line = line + element
            i += 1
            if i > len(elements):
                break
        print(line)

    def print_list(self, listes_elements, largeurs_colonnes):
        '''Ecrit plusieurs lignes de plusieurs éléments'''

        for elements in listes_elements:
            self.print_line(elements, largeurs_colonnes)
