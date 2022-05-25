'''
Module testchisquare
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from lienvar.lienvar import LienVar
import numpy as np
from table.tabledonnees import TableDonnees


class TestChiSquare(LienVar):
    '''Test d'indépendance du X² de deux variables qualitatives d'une table de données

    Attributes
    -----------
    var1 : str
        nom de la variable qualitative
    var2 : str
        nom de la variable qualitative
    etude : str
        champs d'étude ("quali/quali" à vérifier)
    '''

    def __init__(self, var1, var2):
        '''Constructeur de l'objet
        Parameters
        ----------
        var1 : str
        var2 : str
        '''
        super().__init__(var1, var2)

    def representation(self, table):
        '''Tableau de contignence
        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)
        if self.etude == "quali/quali":  # ça bug TODO problème à résoudre
            liste_modalites1 = []
            liste_modalites2 = []
            numcol_var1 = table.index_variable(self.var1)
            numcol_var2 = table.index_variable(self.var2)
            for i in range(len(table.donnees)):
                if table.donnees[i, numcol_var1] not in liste_modalites1:
                    liste_modalites1.append(table.donnees[i, numcol_var1])
                if table.donnees[i, numcol_var2] not in liste_modalites2:
                    liste_modalites2.append(table.donnees[i, numcol_var2])
            tb_contingence = [["modalités"]+liste_modalites2]
            ligne = 1
            for modalite1 in liste_modalites1:
                tb_contingence.append([modalite1])
                for modalite2 in liste_modalites2:
                    nb = 0
                    for i in range(len(table.donnees)):
                        if table.donnees[i, numcol_var1] == modalite1 and table.donnees[i, numcol_var2] == modalite2:
                            nb += 1
                    tb_contingence[ligne].append(nb)
                ligne += 1
            print(tb_contingence)
        else:
            print("erreur de type de variable")
        return tb_contingence

    def appliquer(self, table):
        '''étude de la corrélation entre les variables
        et appel à representation du nuage de points & export du graphique

        Parameters
        ----------
        table : TableDonnees
        '''
        self.representation(table)
        print("Etude du lien entre", self.var1, "et", self.var2)
        # TODO inachevé
