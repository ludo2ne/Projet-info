'''
Module coefficientcorrelation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 16/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from lien2var.lien2var import Lien2var
import matplotlib.pyplot as plt
import numpy as np
from lien2var.lien2var import Lien2var


class CoefficientCorrelation(Lien2var):
    '''Etude de la corrélation de deux variables numériques d'une table de données'''

    def __init__(self, table, var1, var2):
        '''Constructeur de l'objet'''
        super().__init__(table, var1, var2)
        assert(self.etude == "quanti/quanti")

    def representation(self, table, var1, var2):  # bug d'indentation ? TODO
        '''Nuage de points'''
        plt.scatter(self.var1_liste, self.var1_liste)
        plt.title('Nuage de points')
        plt.xlabel('{}'.format(var1))
        plt.ylabel('{}'.format(var2))
        plt.savefig('ScatterPlot_{}_{}_{}.png'.format(var1, var2, table.nom))
        plt.show()

    def etude_lien(self, table, var1, var2):
        '''étude de la corrélation entre les variables'''
        print("Etude du lien entre", var1, "et", var2)
        coeff_corr = np.corrcoef(self.var1_liste, self.var2_liste)
        print("le coefficient de corrélation de ces variables est :", coeff_corr)
        if coeff_corr < 0.4:
<<<<<<< HEAD
           print("la relation entre ces variables est assez faible")
=======
            print("la relation entre ces variables est assez faible")
>>>>>>> e6db8536ebe266fbb922489f22858c07a6bf44ec
        if coeff_corr > 0.6:
            print("la relation entre ces variables est assez forte")
