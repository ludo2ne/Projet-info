'''
Module agregationspatialE
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from src.table.tabledonnees import TableDonnees
from transformation.transformation import Transformation


class AgregationSpatiale(Transformation):
    '''Agrégation vers un échelon plus vaste
    '''

    def __init__(self, echelon):
        '''Constructeur de l'objet

        Attributes
        ----------
        echelon : str
        '''
        self.echelon = echelon

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        #TODO
