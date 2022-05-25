'''
Module coefficientcorrelation_v2
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 1.0
'''

from ast import Break
from lienvar.lienvar import LienVar
import matplotlib.pyplot as plt
import numpy as np
#from table.tabledonnees import TableDonnees


class CoefficientCorrelation(LienVar):
    '''Etude de la corrélation de deux variables numériques d'une table de données

    Attributes
    -----------
    var1 : str
        nom de la variable qualitative
    var2 : str
        nom de la variable qualitative
    etude : str
        champs d'étude ("quanti/quanti" à vérifier)
    '''

    def __init__(self, var1, var2):
        '''Constructeur de l'objet
        Parameters
        ----------
        var1 : str
        var2 : str
        '''
        super().__init__(var1, var2)  # comment on note dans l'UML ? j'ai oublié TODO

    def representation(self, table):
        '''Nuage de points et export de ce graphique
        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)

        if self.etude == "quanti/quanti":  # ça bug TODO problème à résoudre
            numcol_var1 = table.index_variable(self.var1)
            numcol_var2 = table.index_variable(self.var2)
            plt.scatter(table.donnees[:, numcol_var1],
                        table.donnees[:, numcol_var2])
            plt.title('Nuage de points')
            plt.xlabel('{}'.format(self.var1))
            plt.ylabel('{}'.format(self.var2))
            # comment l'enregistrer dans donnees.exports.graphique ? TODO
            plt.savefig('ScatterPlot_{}_{}_{}.png'.format(
                self.var1, self.var2, table.nom))
            plt.show()
        else:
            print("erreur de type de variable")
            Break

    def appliquer(self, table):
        '''étude de la corrélation entre les variables
        et appel à representation du nuage de points & export du graphique

        Parameters
        ----------
        table : TableDonnees
        '''
        self.representation(table)  # syntaxe à vérifier TODO
        print("Etude du lien entre", self.var1, "et", self.var2)
        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)
        ma_liste_test = table.donnees[:, numcol_var1]
        print(table.donnees[:, numcol_var1])
        print(table.donnees[:, numcol_var2])
        step1 = np.corrcoef(
            table.donnees[:, numcol_var1].astype(float), table.donnees[:, numcol_var2].astype(float))
        print(step1)
        coeff_corr = np.corrcoef(
            table.donnees[:, numcol_var1].astype(float), table.donnees[:, numcol_var2].astype(float))[1, 0]
        print("Le coefficient de corrélation de ces variables est : {} ".format(coeff_corr))
        if abs(coeff_corr) < 0.4:
            print("La relation entre ces variables est assez faible.")
        if abs(coeff_corr) > 0.6:
            print("La relation entre ces variables est assez forte.")
