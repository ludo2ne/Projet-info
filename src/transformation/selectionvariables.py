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

    def __init__(self, liste_var=[]):
        '''Constructeur de l'objet

        Parameters :
        ----------
        liste_var : list[str] = []
            liste des noms des colonnes à conserver;
            si la liste n'est pas saisie cela supprime les colonnes qui n'ont que des valeurs manquantes
        '''
        self.liste_var = liste_var

    def appliquer(self, table):
        '''Appliquer la transformation à plusieurs variables de la table

        Parameters :
        ----------
        table : TableDonnees
            table de données
        '''
        index_conserves = []
        if self.liste_var != []:
            print("------------------------------------------------------")
            print("Sélection des variables : " + str(self.liste_var))



            # On parcourt la liste des variables de SelectionVariables
            for var in self.liste_var:
                try:
                    index_conserves.append(table.variables.tolist().index(var))
                except:
                    warnings.warn("Variable " + var +
                                " non trouvée dans la table " + table.nom)

        else: #suppression de toutes les variables constituées uniquement de valeurs manquantes
            index_conserves = []
            for var in table.variables:
                if table.compte_na(var) != len(table.donnees):
                    index_conserves.append(table.variables.tolist().index(var))

        table.variables = table.variables[index_conserves]
        table.type_var = table.type_var[index_conserves]
        table.donnees = table.donnees[:, index_conserves]
