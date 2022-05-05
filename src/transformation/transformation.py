'''
Module transformation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
from abc import abstractmethod


class Transformation:
    '''Transformation d'une ou plusieurs variables
    '''

    def __init__(self, colonnes_application):
        '''Constructeur de l'objet

        Attributes
        ----------
        colonnes_application : list[int]
            colonnes auquelles appliquer la transformation
            TODO au lieu de l'index de la colonne, modifier pour mettre le nom
        '''
        self.colonnes_application = colonnes_application

    @abstractmethod
    def appliquer(self, table):
        pass
