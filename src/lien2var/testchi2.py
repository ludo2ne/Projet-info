'''
Module testchi2
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from lien2var.lien2var_v2 import Lien2varV2
import numpy as np
#from table.tabledonnees import TableDonnees


class Testchi2(Lien2var):
    '''Test d'indépendance du X² de deux variables qualitatives d'une table de données

    Attributes
    -----------
    var1 : str
        nom de la variable qualitative
    var2 : str
        nom de la variable qualitative
    etude : str
        champs d'étude ("quali/quanti" à vérifier)
    '''

    def __init__(self,var1,var2):
        '''Constructeur de l'objet'''
        super().__init__(var1,var2)

    def determine_etude(self, table):
        Lien2varV2(self.var1,self.var2).determine_etude(table)
        assert self.etude == "quali/quali" #ça bug TODO problème à résoudre
        if self.etude != "quali/quali": #TODO problème à résoudre
            print("erreur de type de variable") #warning TODO

    def representation(self, table):
        Testchi2(self.var1,self.var2).determine_etude(table) #TODO à debugger
        liste_modalites1 = []
        liste_modalites2 = []
        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)
        for i in len(table.donnees):
            if table.donnees[i,numcol_var1] not in liste_modalites1:
                liste_modalites1.append(table.donnees[i,numcol_var1])
            if table.donnees[i,numcol_var2] not in liste_modalites2:
                liste_modalites2.append(table.donnees[i,numcol_var2])
        tb_contingence=[["modalités"]+liste_modalites2]
        ligne=1
        for modalite1 in liste_modalites1:
            tb_contingence.append([modalite1])
            for modalite2 in liste_modalites2:
                nb=0
                for i in len(table.donnee):
                    if table.donnees[i,numcol_var1] == modalite1 and table.donnees[i,numcol_var2] == modalite2:
                        nb+=1
                tb_contingence[ligne].append(nb)
            ligne+=1
        print(tb_contingence)
