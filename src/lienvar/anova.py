'''
Module anova
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 1.0
'''

import os
import matplotlib.pyplot as plt
from lienvar.lienvar import LienVar


class Anova(LienVar):
    '''Analyse de variance d'une variable quantitative en fonction d'une variable qualitative d'une table de données

    Attributes
    -----------
    var1 : str
        nom de la variable qualitative
    var2 : str
        nom de la variable quantitative
    etude : str
        champs d'étude ("quali/quanti" à vérifier)
    '''

    def __init__(self, var1, var2, titre=""):
        '''Constructeur de l'objet

        Parameters
        ----------
        var1 : str
            nom de la variable qualitative
        var2 : str
            nom de la variable quantitative
        titre : str = ""
            titre du graphique (sinon, généré automatiquement)
        '''
        super().__init__(var1=var1, var2=var2, titre=titre)

    def representation(self, table):
        '''Boxplot et export de ce graphique

        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)
        if self.titre == "":
            self.titre = 'Boxplot  : {}'.format(table.nom)

        if self.etude == "quali/quanti":
            liste_modalites = []
            numcol_var_quali = table.index_variable(self.var1)
            numcol_var_quanti = table.index_variable(self.var2)
            for i in range(len(table.donnees)):
                if table.donnees[i, numcol_var_quali] not in liste_modalites:
                    liste_modalites.append(table.donnees[i, numcol_var_quali])

            matrice_boxplot = []
            nb_lignes = 0
            for modalite in liste_modalites:
                matrice_boxplot.append([])
                for i in range(len(table.donnees)):
                    if table.donnees[i, numcol_var_quali] == modalite:
                        matrice_boxplot[nb_lignes].append(
                            table.donnees[i, numcol_var_quanti])
                nb_lignes += 1

            plt.boxplot(matrice_boxplot)
            plt.title(self.titre)
            plt.xlabel('Modalités de {} : {}'.format(
                self.var1, liste_modalites))
            plt.ylabel('{}'.format(self.var2))
            plt.savefig(os.getcwd() + '/donnees/exports/' + 'BoxPlot_{}_{}_{}.png'.format(
                self.var1, self.var2, table.nom))
            plt.show()

        else:
            quit("erreur de type de variable")

    def appliquer(self, table):
        '''analyse de variance : étude du rapport de corrélation
        et appel à representation du Boxplot & export du graphique

        Parameters
        ----------
        table : TableDonnees
        '''
        self.representation(table)
        print("voir le boxplot affiché et exporté")
        # prolongement possible (test d'analyse de variance)
