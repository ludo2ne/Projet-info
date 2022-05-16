'''
Module testchi2
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
import matplotlib.pyplot as plt

class CoefficientCorrelation(Lien2var):
    '''Etude de la corrélation de deux variables numériques d'une table de données'''

    def __init__(self, table, var1, var2):
        '''Constructeur de l'objet'''
        super().__init__(self, table, var1, var2)
        assert(self.etude=="quanti/quanti")

    def representation(self, table, var1, var2):
        '''Nuage de points'''
        plt.scatter(self.var1_liste,self.var1_liste)
        plt.title('Nuage de points')
        plt.xlabel('{}'.format(var1))
        plt.ylabel('{}'.format(var2))
        plt.savefig('ScatterPlot_{}_{}.png'.format(var1,var2))
        plt.show()

     def etude_lien(self, table, var1, var2):
