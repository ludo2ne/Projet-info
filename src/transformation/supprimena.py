'''
Module supprimena
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from transformation.transformation import Transformation
#from lien2var.lien2var import Lien2var  #pour la méthode num_col() à déplacer ?  à supprimer

class SupprimeNA(Transformation):
    '''Suppression des valeurs manques pour une liste de variables
    '''

    def __init__(self, liste_var):
        '''Constructeur de l'objet

        Attributes
        ----------
        liste_var : list[str]
            listes de variables sur lesquelles appliquer la suppression des valeurs manquantes

        '''
        self.liste_var=liste_var

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        liste_numero_col=[]
        for var in self.liste_var:
            #liste_numero_col.append(num_col(table, var))
            liste_numero_col.append(table.idex_variable(var))

        for i in liste_numero_col:
            for j in range(len(table.donnees)):
                if table.donnees[j][i] == "na": #c'est "na" ou "nan" ? TODO
                    table.donnees.pop(j)
                    j=j-1
