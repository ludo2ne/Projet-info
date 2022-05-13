'''
Module reduction
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''

import warnings
import statistics
import doctest
import numpy as np
from transformation.transformation import Transformation
from estimateur.ecarttype import EcartType


class Reduction(Transformation):
    '''Reduction d'une ou plusieurs variables
    '''

    def __init__(self):
        '''Constructeur de l'objet
        '''
        pass

    def appliquer_variable(self, table, numero_colonne):
        '''Appliquer la réduction à une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer

        Examples
        --------

        '''

        #colx = table.donnees[:, numero_colonne].astype(float)
        # print(type(colx))

        # Calcul de l'écart-type
        ecartype = EcartType.estim1var(table, numero_colonne)

        # Réduction de toutes les valeurs qui ne sont pas NaN
        for i in range(0, len(table.donnees)):
            if not np.isnan(table.donnees[i][numero_colonne]):
                old_value = table.donnees[i][numero_colonne]
                new_value = old_value/ecartype
                table.donnees[i][numero_colonne] = new_value

        return table #pourquoi il y a un return ? TODO

    def appliquer(self, table):
        '''Appliquer la transformation à plusieurs variables de la table

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
