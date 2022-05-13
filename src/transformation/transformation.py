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
    # peut-être l'enlever si pas besoin
    @abstractmethod
    def __init__(self):
        '''Constructeur de l'objet'''
        pass

    @abstractmethod
    def appliquer(self):
        pass
