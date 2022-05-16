'''
Module filtre
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from transformation.transformation import Transformation
from lien2var.lien2var import Lien2var  #pour la méthode num_col() à déplacer ?

class Filtre(Transformation):
    '''Appliation d'un ou plusieurs filtres (par modalité ou fenétrage temporel)
    '''

    def __init__(self, var, modalite=None, fenetrage=False,debut,fin):
        '''Constructeur de l'objet

        Attributes
        ----------
        var : str
            variable sur laquelle appliquer le filtre par modalités
        modalite : list[str]
            liste des modalités à conserver
        fenetrage : bool
            True si on souhaite appliquer un fêtrage temporel, False sinon
        debut : date
        fin : date
        '''
        self.var=var
        self.modalite=modalite
        self.fenetrage=fenetrage
        self.debut=debut
        self.fin=fin

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        numero_colonne = num_col(table, self.var)
        print("------------------------------------------------------")

        if self.modalite != None:
            print("Liste des modalités selectionnées", self.modalite, "pour la variable", self.var)
            for i in range(len(table.donnees)):
                if table.donnees[i][numero_colonne] is not in self.modalite: #syntaxe à vérifier
                    table.donnees.pop(i)
                    i=i-1

        if self.fenetrage == True:
            print("Fenétrage temporel de : ", self.debut, "à", self.fin)
            if self.modalite != None:
                for i in range(len(table.donnees)):
                    if #TODO<debut or TODO>fin:   à voir le fonctionnement des inégalités avec les dates
                        table.donnees.pop(i)
                        i=i-1
