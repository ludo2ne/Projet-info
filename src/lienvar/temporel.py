'''
Module temporel
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''

from lienvar.lienvar import LienVar
import numpy as np
from table.tabledonnees import TableDonnees


class Temporel(LienVar):
    '''Remplésentation temporelle d'une variable quantitative
    Attributes
    -----------
    var1 : str
        nom de la variable temporelle
    list_var2 : list[str]
        liste de noms des variables quantitatives à remprésenter sur la même période
    etude : str
        champs d'étude ("temporel" à vérifier)
    '''

    def __init__(self, var1, var2, var3):
        '''Constructeur de l'objet
        Parameters
        ----------
        var1 : str
            variable temporelle
        var2 : str
            variable quanti
        var3 : str
            variable quali pour grouper var2 en liste
        '''
        super().__init__(var1, var2)
        self.init = var3

    def representation(self, table):
        '''Représentation en fonction du temps
        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)
        if self.etude == "temporel":
            pass