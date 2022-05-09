'''
Module centrage
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import warnings
import doctest
from transformation.transformation import Transformation
from estimateur.moyenne import Moyenne


class SelctionVariables(Transformation):
    '''Sélection d'une ou plusieurs variables
    '''

    def __init__(self, liste_colonnes):
        '''Constructeur de l'objet

        Attributes
        ----------
        liste_colonnes : list[str]
            liste des noms des colonnes auquelles appliquer la transformation
        '''
        self.liste_colonnes = liste_colonnes

    def appliquer(self, table):
        '''Appliquer la transformation à plusieurs variables de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        index_conserves = []

        # On parcourt la liste des colonnes de SelectionVariables
        for col in self.liste_colonnes:
            try:
                index_conserves.append(table.variables.index(col))
            except:
                warnings.warn("Variable " + col +
                              " non trouvée dans la table " + table.nom)

        # TODO supprimer toutes les colonnes qui ne sont pas dans index_conserves

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Je suis un centrage"
