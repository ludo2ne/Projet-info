'''
Module lien2var
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 16/05/2022
Licence : Domaine public
Version : 1.0
'''

from abc import abstractmethod
import doctest


class Lien2var:
    '''Classe (abstraite ?) pour étudier les liens entre deux variables d'une table donnée'''

    def __init__(self, table, var1, var2): # pas sûr que ça soit la meilleure façon de faire, à vérifier TODO
        '''Constructeur de l'objet'''
        numcol_var1 = table.index_variable(var1)
        numcol_var2 = table.index_variable(var2)
        self.var1_liste = table.donnees[:,numcol_var1]
        self.var2_liste = table.donnees[:,numcol_var2] #au lieu de liste_colonne(table, numcol_var2)
        if table.type_var[numcol_var1] == "float" and table.type_var[numcol_var2] == "float":
            self.etude = "quanti/quanti"
        if table.type_var[numcol_var1] == "str" and table.type_var[numcol_var2] == "str":
            self.etude = "quali/quali"
        if (table.type_var[numcol_var1] == "str" and table.type_var[numcol_var2] == "float") or (table.type_var[numcol_var1] == "float" and table.type_var[numcol_var2] == "str"):
            self.etude = "quanti/quali"

    @abstractmethod
    def representation(self, table, var1, var2):
        pass

    @abstractmethod
    def etude_lien(self, table, var1, var2):
        pass
