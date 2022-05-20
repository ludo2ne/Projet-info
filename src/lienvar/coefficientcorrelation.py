'''
Module coefficientcorrelation_v2
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 2.0
'''

from lienvar.lienvar import LienVar
import matplotlib.pyplot as plt
import numpy as np
#from table.tabledonnees import TableDonnees


class CoefficientCorrelation(LienVar):
    '''Etude de la corrélation de deux variables numériques d'une table de données

    Attributes
    -----------
    var1 : str
    var2 : str
    etude : str
    '''

    def __init__(self, var1, var2):
        '''Constructeur de l'objet'''
        super().__init__(var1, var2)  # comment on note dans l'UML ? j'ai oublié TODO

#    def determine_etude(self, table):
#        Lien2varV2(self.var1, self.var2).determine_etude(table)
#        assert self.etude == "quanti/quanti"  # ça bug TODO problème à résoudre
#        print(self.etude, "etude")
#        if self.etude != "quanti/quanti":  # TODO problème à résoudre
#            print("type de variable non quantitatif")  # warning TODO

    def representation(self, table):
        '''Nuage de points'''

        print("méthode representation")

        super().determine_etude(table)
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

    def appliquer(self, table):
        '''étude de la corrélation entre les variables'''
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
        if coeff_corr < 0.4:
            print("La relation entre ces variables est assez faible.")
        if coeff_corr > 0.6:
            print("La relation entre ces variables est assez forte.")
