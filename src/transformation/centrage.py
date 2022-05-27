'''
Module centrage
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import numpy as np
from transformation.transformation import Transformation
from estimateur.moyenne import Moyenne


class Centrage(Transformation):
    '''Centrage d'une ou plusieurs variables
    '''

    def __init__(self):
        '''Constructeur de l'objet
        '''
        pass

    def appliquer_variable(self, table, numero_colonne):
        '''Appliquer le centrage à une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer
        '''

        # Calcul de la moyenne
        moyenne = Moyenne.estim1var(table, numero_colonne)

        # Centrage de toutes les valeurs qui ne sont pas des valeurs manquantes
        for i in range(0, len(table.donnees)):
            if not np.isnan(table.donnees[i][numero_colonne]):
                old_value = table.donnees[i][numero_colonne]
                new_value = old_value - moyenne
                table.donnees[i][numero_colonne] = new_value

        return table

    def appliquer(self, table):
        '''Appliquer la transformation à toutes les variables numériques de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        print("------------------------------------------------------")
        print("Centrage de la table " + table.nom)

        for num_col in range(len(table.variables)):
            if table.type_var[num_col] == "float":
                self.appliquer_variable(table, num_col)
