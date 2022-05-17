'''
Module jointureinterne
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from src.table.tabledonnees import TableDonnees
from transformation.transformation import Transformation


class JointureInterne(Transformation):
    '''Joiinture entre deux tables selon une clé (liste de variables)
    '''

    def __init__(self, autre_table, cle):
        '''Constructeur de l'objet

        Attributes
        ----------
        cle : list[str]
        autre_table : TableDonnees
        '''
        self.autre_table = autre_table
        self.cle = cle

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        #TODO
