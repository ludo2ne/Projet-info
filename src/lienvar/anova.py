'''
Module anova
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
from lienvar.lienvar import LienVar
import matplotlib.pyplot as plt
import numpy as np
#from table.tabledonnees import TableDonnees

class Anova(LienVar):
    '''Analyse de variance d'une variable quantitative en fonction d'une variable qualitative d'une table de données
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
        LienVar(self.var1,self.var2).determine_etude(table)
        assert self.etude == "quali/quanti" #ça bug TODO problème à résoudre
        if self.etude != "quali/quanti": #TODO problème à résoudre
            print("erreur de type de variable") #warning TODO

    def representation(self, table):
        Anova(self.var1,self.var2).determine_etude(table) #TODO à debugger
        liste_modalites = []
        numcol_var_quali = table.index_variable(self.var1)
        numcol_var_quanti = table.index_variable(self.var2)
        for i in len(table.donnees):
            if table.donnees[i,numcol_var_quali] not in liste_modalites:
                liste_modalites.append(table.donnees[i,numcol_var_quali])
        matrice_boxplot=[]
        nb=0
        for modalite in liste_modalites:
            matrice_boxplot.append([])
            for i in len(table.donnees):
                if table.donnees[i,numcol_var_quali] == modalite:
                    matrice_boxplot[nb].append(table.donnees[i,numcol_var_quanti])
            nb+=1
        plt.boxplot(matrice_boxplot)
        plt.title('Boxplot')
        plt.xlabel('{}//{}'.format(self.var1,liste_modalites))
        plt.ylabel('{}'.format(self.var2))
        plt.savefig('BoxPlot_{}_{}_{}.png'.format(self.var1, self.var2, table.nom))
        plt.show()
