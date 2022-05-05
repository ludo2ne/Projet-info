'''
Module centrage
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from estimateur.moyenne import Moyenne


class Centrage():
    '''Centrage d'une ou plusieurs variables
    '''

    def __init__(self, colonnes_application):
        '''Constructeur de l'objet

        Attributes
        ----------
        colonnes_application : list[int]
            colonnes auquelles appliquer la transformation
            TODO au lieu de l'index de la colonne, modifier pour mettre le nom
        '''
        # super().__init__(colonnes_application)
        self.colonnes_application = colonnes_application

    def appliquer_variable(self, table, numero_colonne):
        '''Appliquer le centrage à une variable de la table

        Cette méthode est statique, elle peut être utilisée sans 

        Parameters
        ----------
        table : TableDonnees
            table de données

        Examples
        --------

        '''

        print("------------------------------------------------------")
        print("Centrage de la variable " + table.donnees[0][numero_colonne])

        # Calcul de la moyenne
        moyenne = Moyenne.appliquer(table, numero_colonne)

        # Centrage de toutes les valeurs
        for i in range(1, len(table.donnees)):
            if table.donnees[i][numero_colonne] != "mq":
                old_value = float(table.donnees[i][numero_colonne])
                new_value = str(old_value - moyenne)
                table.donnees[i][numero_colonne] = new_value

        return table

    def appliquer(self, table):
        '''Appliquer la transformation à plusieurs variables de la table
        '''
        for col in self.colonnes_application:
            self.appliquer_variable(table, col)

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Je suis un centrage"
