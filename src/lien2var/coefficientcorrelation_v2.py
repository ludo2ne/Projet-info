'''
Module coefficientcorrelation_v2
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 2.0
'''

import doctest
from lien2var.lien2var_v2 import Lien2varV2
import matplotlib.pyplot as plt
import numpy as np


class CoefficientCorrelationV2(Lien2varV2):
    '''Etude de la corrélation de deux variables numériques d'une table de données

    Attributes
    -----------
    var1 : str
    var2 : str
    etude : str
    '''

    def __init__(self, var1, var2):
        '''Constructeur de l'objet'''
        super().__init__(var1, var2)

    def determine_etude(self, table):
        Lien2varV2(self.var1,self.var2).determine_etude(table)
        assert self.etude == "quanti/quanti" #ça bug TODO problème à résoudre
        print(self.etude,"etude")
        if self.etude != "quanti/quanti": #TODO problème à résoudre
            print("type de variable non quantitatif") #warning TODO

    def representation(self, table):
        '''Nuage de points'''
        CoefficientCorrelationV2(self.var1,self.var2).determine_etude(table) #ça ne fonctionne pas avec self.determine_etude(table) TODO
        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)
        plt.scatter(table.donnees[:,numcol_var1], table.donnees[:,numcol_var2])
        plt.title('Nuage de points')
        plt.xlabel('{}'.format(self.var1))
        plt.ylabel('{}'.format(self.var2))
        plt.savefig('ScatterPlot_{}_{}_{}.png'.format(self.var1, self.var2, table.nom)) #comment l'enregistrer dans donnees.exports.graphique ? TODO
        plt.show()

    def etude_lien(self, table):
        '''étude de la corrélation entre les variables'''
        CoefficientCorrelationV2(self.var1,self.var2).representation(table) # syntaxe à vérifier TODO
        print("Etude du lien entre", self.var1, "et", self.var2)
        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)
        coeff_corr = np.corrcoef(table.donnees[:,numcol_var1], table.donnees[:,numcol_var2])[1,0]
        print("Le coefficient de corrélation de ces variables est : {} ".format(coeff_corr))
        if coeff_corr < 0.4:
            print("La relation entre ces variables est assez faible.")
        if coeff_corr > 0.6:
            print("La relation entre ces variables est assez forte.")
