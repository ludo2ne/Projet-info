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
    titre : str
        titre du graphique
    etude : str

    '''

    def __init__(self, var1, var2, titre):
        '''Constructeur de l'objet

        Parameters :
        ------------
        var1 : str
            nom de la première variable
        var2 : str
            nom de la deuxième variable
        titre : str = ""
            titre du graphique
        '''
        self.var1 = var1
        self.var2 = var2
        self.etude = None
        self.titre = titre

    def determine_etude(self, table):
        '''détermine le champ d'étude selon le type de variables'''

        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)
        if numcol_var1 == None or numcol_var2 == None:
            print("Vérifier l'écriture des variables saisies !")

        if (table.type_var[numcol_var1] == "float") and (table.type_var[numcol_var2] == "float"):
            self.etude = "quanti/quanti"
        if (table.type_var[numcol_var1] == "str") and (table.type_var[numcol_var2] == "str"):
            self.etude = "quali/quali"
        if ( (table.type_var[numcol_var1] == "str") and (table.type_var[numcol_var2] == "float") ) or ( (table.type_var[numcol_var1] == "float") and (table.type_var[numcol_var2] == "str") ):
            self.etude = "quali/quanti"
            if table.type_var[numcol_var1] == "float":
                transfert_var = self.var1
                self.var1 = self.var2
                self.var2 = transfert_var
        if ( (table.type_var[numcol_var1] == "date") and (table.type_var[numcol_var2] == "float") ) or ( (table.type_var[numcol_var1] == "float") and (table.type_var[numcol_var2] == "date") ):
            self.etude = "temporel"
            if table.type_var[numcol_var1] == "float":
                transfert_var = self.var1
                self.var1 = self.var2
                # pour placer par défaut la variable numérique en 2ème (pour faciliter ensuite la méthode de représentation graphique)
                self.var2 = transfert_var
        print("Etude de type :",self.etude, "entre les variables", self.var1, "et", self.var2)

    @abstractmethod
    def representation(self, table):
        pass

    @abstractmethod
    def appliquer(self, table):
        pass
