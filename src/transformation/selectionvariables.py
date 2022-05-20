'''
Module centrage
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import warnings
import doctest

from sqlalchemy import desc
from transformation.transformation import Transformation


class SelectionVariables(Transformation):
    '''Sélection d'une ou plusieurs variables
    Attributes :
    ----------
        liste_var : list[str]
            liste des noms des colonnes à conserver
    '''

    def __init__(self, liste_var):
        '''Constructeur de l'objet

        Parameters :
        ----------
        liste_var : list[str]
            liste des noms des colonnes à conserver
        '''
        self.liste_var = liste_var

    def appliquer(self, table):
        '''Appliquer la transformation à plusieurs variables de la table

        Parameters :
        ----------
        table : TableDonnees
            table de données
        '''

        print("------------------------------------------------------")
        print("Sélection des variables : " + str(self.liste_var))

        index_conserves = []

        # On parcourt la liste des colonnes de SelectionVariables
        for col in self.liste_var:
            try:
                index_conserves.append(table.variables.tolist().index(col))
            except:
                warnings.warn("Variable " + col +
                              " non trouvée dans la table " + table.nom)

        table.variables = table.variables[index_conserves]
        table.type_var = table.type_var[index_conserves]
        table.donnees = table.donnees[:, index_conserves]
