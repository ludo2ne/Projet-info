'''
Module lienvar
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 2.0
'''

from abc import abstractmethod


class LienVar:
    '''Classe pour étudier les liens entre deux variables d'une table donnée

    Attributes
    -----------
    var1 : str
        nom de la première variable
    var2 : str
        nom de la deuxième variable
    etude : str

    '''

    def __init__(self, var1, var2, etude=None):
        '''Constructeur de l'objet

        Parameters :
        ------------
        var1 : str
        var2 : str
        etude : str = None'''
        self.var1 = var1
        self.var2 = var2
        self.etude = etude

    def determine_etude(self, table):
        '''détermine le champ d'étude selon le type de variables'''

        print("détermination de l'étude")
        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)

        if table.type_var[numcol_var1] == "float" and table.type_var[numcol_var2] == "float":
            self.etude = "quanti/quanti"
            print(self.etude)
        if table.type_var[numcol_var1] == "str" and table.type_var[numcol_var2] == "str":
            self.etude = "quali/quali"
        if (table.type_var[numcol_var1] == "str" and table.type_var[numcol_var2] == "float") or (table.type_var[numcol_var1] == "float" and table.type_var[numcol_var2] == "str"):
            self.etude = "quali/quanti"
            if table.type_var[numcol_var1] == "float":
                transfert_var = self.var1
                self.var1 = self.var2
                self.var2 = transfert_var
        if (table.type_var[numcol_var1] == "date" and table.type_var[numcol_var2] == "float") or (table.type_var[numcol_var1] == "float" and table.type_var[numcol_var2] == "date"):
            self.etude = "temporel"
            if table.type_var[numcol_var1] == "float":
                transfert_var = self.var1
                self.var1 = self.var2
                # pour placer par défaut la variable numérique en 2ème (pour faciliter ensuite la méthode de représentation graphique)
                self.var2 = transfert_var

    @abstractmethod
    def representation(self, table):
        pass

    @abstractmethod
    def appliquer(self, table):
        pass
