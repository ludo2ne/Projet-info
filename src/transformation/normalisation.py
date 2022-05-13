'''
Module normalisation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''

from matplotlib.pyplot import table
from transformation.transformation import Transformation
from transformation.reduction import Reduction
from transformation.centrage import Centrage


class Normalisation(Transformation):
    '''Normalisation (ou standardisation) d'une table de données,
    ne prend en compte que les variables numériques "float" sans modifier les autres'''

    def __init__(self):
        '''Constructeur de l'objet
        '''
        pass

    def appliquer(self, table):
        '''Appliquer la transformation à toutes les variables numériques de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        Centrage().appliquer(table)
        Reduction().appliquer(table)

        print("------------------------------------------------------")
        print("Normalisation (standardisation) de la table " + table.nom)
