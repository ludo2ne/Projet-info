'''
Module reduction
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''

import numpy as np
import warnings
from transformation.transformation import Transformation
from estimateur.ecarttype import EcartType


class Reduction(Transformation):
    '''Reduction d'une ou plusieurs variables
    '''

    def __init__(self):
        '''Constructeur de l'objet
        '''
        pass

    def appliquer_variable(self, table, numero_colonne): # cob=vertir en staticmethode ?
        '''Appliquer la réduction à une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer
        '''

        # Calcul de l'écart-type
        ecartype = EcartType.estim1var(table, numero_colonne)

        # Réduction de toutes les valeurs qui ne sont pas NaN
        if ecartype != 0 and not np.isnan(ecartype):
            for i in range(0, len(table.donnees)):
                if not np.isnan(table.donnees[i][numero_colonne]):
                    old_value = table.donnees[i][numero_colonne]
                    new_value = old_value/ecartype
                    table.donnees[i][numero_colonne] = new_value
        else:
            warnings.warn("Attention, la variable " +
                          table.variables[numero_colonne] + " n'est pas réduite")

    def appliquer(self, table):
        '''Appliquer la réduction à toutes les variables numériques de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        print("------------------------------------------------------")
        print("Réduction de la table " + table.nom)

        for num_col in range(len(table.variables)):
            if table.type_var[num_col] == "float":
                self.appliquer_variable(table, num_col)
