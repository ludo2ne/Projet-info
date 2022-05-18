'''
Module supprimena
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from transformation.transformation import Transformation
import numpy as np

class SupprimeNA(Transformation):
    '''Suppression des lignes de table.donnees où il y a des valeurs manquantes pour la liste de variables saisie

    Attributes
        ----------
        liste_var : list[str]
            listes de variables sur lesquelles appliquer la suppression des valeurs manquantes

    '''

    def __init__(self, liste_var):
        '''Constructeur de l'objet

        Parameters
        ----------
        liste_var : list[str]
            listes de variables sur lesquelles appliquer la suppression des valeurs manquantes

        '''
        self.liste_var = liste_var

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        liste_numero_col=[]
        for var in self.liste_var:
            liste_numero_col.append(table.index_variable(var)) #génère la liste des indices de colonne correspondant à la liste des variable données

        indice_NA=[]
        for i in liste_numero_col:
            for j in range(len(table.donnees)):
                if np.isnan(table.donnees[j][i]): #test de valeur manquante
                    indice_NA.append(j)

        table.donnees = np.delete(table.donnees, indice_NA, 0) #supprime toutes les lignes dont l'indice est dans la liste indice_NA
        table.variables = np.delete(table.variables, indice_NA, 0)
        table.type_var = np.delete(table.type_var, indice_NA, 0)
