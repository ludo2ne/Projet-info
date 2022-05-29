'''
Module temporel
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from lienvar.lienvar import LienVar
import matplotlib.pyplot as plt


class Temporel(LienVar):
    '''Remplésentation temporelle d'une variable quantitative
    Attributes
    -----------
    var1 : str
        nom de la variable temporelle
    var2 : str
        nom de la variable quantitative à remprésenter
    titre : str
        titre du graphique
    etude : str
        champs d'étude ("temporel" à vérifier)
    '''

    def __init__(self, var1, var2, var3="", titre=""):
        '''Constructeur de l'objet
        Parameters
        ----------
        var1 : str
            variable temporelle
        var2 : str
            variable quanti
        var3 : str
            autre variable pour la coloration du graphique (facultatif)
        '''
        super().__init__(var1=var1, var2=var2, titre=titre)
        self.var3 = var3

    def representation(self, table):
        '''Représentation en fonction du temps
        Parameters
        ----------
        table : TableDonnees
        '''
        super().determine_etude(table)
        if self.titre == "":
            self.titre = "Représentation de {} en fonction du temps : {}".format(
                self.var2, table.nom)
        if self.etude == "temporel":
            numcol_var1 = table.index_variable(self.var1)
            numcol_var2 = table.index_variable(self.var2)
            if self.var3 != None:
                numcol_var3 = table.index_variable(self.var3)
                color = table.donnees[:, numcol_var3]
                plt.suptitle(
                    "Couleur en fonction de la variable {}".format(self.var3))
            else:
                color = "b"
            plt.scatter(table.donnees[:, numcol_var1],
                        table.donnees[:, numcol_var2], c=color)
            plt.title(self.titre)
            plt.xlabel('{}'.format(self.var1))
            plt.ylabel('{}'.format(self.var2))
            plt.savefig(os.getcwd() + '/donnees/exports/' + 'SérieTemporelle_{}_{}.png'.format(
                self.var2, table.nom))
            plt.show()

        else:
            quit("erreur de type de variable")

    def appliquer(self, table):
        '''série temporelle

        Parameters
        ----------
        table : TableDonnees
        '''
        self.representation(table)
