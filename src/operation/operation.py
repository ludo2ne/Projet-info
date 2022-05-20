'''Classe abstraite estimateur'''

from abc import ABC, abstractmethod
from table.tabledonnees import TableDonnees


class AbstractOperation(ABC):
    '''Classe abstraite implémentant un estimateur

    '''


    @abstractmethod
    def __init__(self):
        '''Constructeur pour donner un nom à l'estimateur'''
        pass

    @abstractmethod
    def appliquer(self,table):
        pass
