'''
Module testchisquare
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from lienvar.lienvar import LienVar
import numpy as np
import matplotlib.pyplot as plt


class TestChiSquare(LienVar):
    '''Test d'indépendance du X² de deux variables qualitatives d'une table de données

    Attributes
    -----------
    var1 : str
        nom de la variable qualitative
    var2 : str
        nom de la variable qualitative
    titre : str
        titre du tableau de contigence
    etude : str
        champs d'étude ("quali/quali" à vérifier)
    '''

    def __init__(self, var1, var2, titre=""):
        '''Constructeur de l'objet

        Parameters
        ----------
        var1 : str
            nom de la variable qualitative
        var2 : str
            nom de la variable qualitative
        titre : str = ""
            titre du tableau de contigence (sinon, automatique)
        '''
        super().__init__(var1=var1, var2=var2, titre=titre)

    def representation(self, table):
        '''Tableau de contignence

        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)
        if self.titre == "":
            self.titre = 'Tableau de contingence : {}'.format(table.nom)
        if self.etude == "quali/quali":
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

            tableau = np.array(tb_contingence)

            fig, ax = plt.subplots(1, 1)
            ax.axis('off')
            ax.table(cellText=tableau, loc="center")
            plt.savefig(os.getcwd() + '/donnees/export/' + 'TabContingence_{}_{}_{}.png'.format(
                self.var1, self.var2, table.nom))
            plt.title(self.titre)
            plt.show()

        else:
            print("erreur de type de variable")

        return tableau

    def appliquer(self, table):
        '''étude de la corrélation entre les variables
        et appel à representation du nuage de points & export du graphique

        Parameters
        ----------
        table : TableDonnees
        '''
        self.representation(table)
        # prolongement possible : test du X²
