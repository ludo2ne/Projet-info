'''
Module coefficientcorrelation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 19/05/2022
Licence : Domaine public
Version : 1.0
'''

from lienvar.lienvar import LienVar
import matplotlib.pyplot as plt
import numpy as np


class CoefficientCorrelation(LienVar):
    '''Etude de la corrélation de deux variables numériques d'une table de données

    Attributes
    -----------
    var1 : str
        nom de la variable quantitative
    var2 : str
        nom de la variable quantitative
    var3 : str
        nom de la 3ème variable quantitative (facultative, utilisée pour la couleur du graphique)
    titre : str
        titre du graphique
    etude : str
        champs d'étude ("quanti/quanti" à vérifier)
    '''

    def __init__(self, var1, var2, var3 = None, titre = ""):
        '''Constructeur de l'objet
        Parameters
        ----------
        var1 : str
            nom de la variable quantitative
        var2 : str
            nom de la variable quantitative
        var3 : str
            nom de la 3ème variable quantitative (facultative, utilisée pour la couleur du graphique)
        titre : str = ""
            titre du graphique (sinon, généré automatiquement)
        '''
        super().__init__(var1 = var1, var2 = var2, titre = titre)
        self.var3 = var3


    def representation(self, table):
        '''Nuage de points et export de ce graphique
        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)
        if self.titre == "":
            self.titre = 'Nuage de points : {}'.format(table.nom)

        if self.etude == "quanti/quanti":
            numcol_var1 = table.index_variable(self.var1)
            numcol_var2 = table.index_variable(self.var2)
            if self.var3 != None:
                numcol_var3 = table.index_variable(self.var3)
                color = table.donnees[:, numcol_var3]
                plt.suptitle("Couleur en fonction de la variable {}".format(self.var3))
            else:
                color = "b"
            plt.scatter(table.donnees[:, numcol_var1],
                        table.donnees[:, numcol_var2], c = color)
            plt.title(self.titre)
            plt.xlabel('{}'.format(self.var1))
            plt.ylabel('{}'.format(self.var2))
            plt.savefig('ScatterPlot_{}_{}_{}.png'.format(
                self.var1, self.var2, table.nom)) #/donnees/exports/graphiques/ TODO
            plt.show()

        else:
            quit("erreur de type de variable")

    def appliquer(self, table):
        '''Etude de la corrélation entre les variables

        et appel à representation du nuage de points & export du graphique

        Parameters
        ----------
        table : TableDonnees
        '''
        self.representation(table)

        numcol_var1 = table.index_variable(self.var1)
        numcol_var2 = table.index_variable(self.var2)

        coeff_corr = np.corrcoef(
            table.donnees[:, numcol_var1].astype(float), table.donnees[:, numcol_var2].astype(float))[1, 0]

        print("Le coefficient de corrélation de ces variables est : {} ".format(coeff_corr))
        if abs(coeff_corr) < 0.4:
            print("La relation entre ces variables est assez faible.")
        elif abs(coeff_corr) < 0.55:
            print("La relation entre ces variables est peu significative.")
        elif abs(coeff_corr) < 0.7:
            print("La relation entre ces variables est assez significative.")
        elif abs(coeff_corr) < 0.85:
            print("La relation entre ces variables est relativement forte.")
        else:
            print("La relation entre ces variables est très forte.")
