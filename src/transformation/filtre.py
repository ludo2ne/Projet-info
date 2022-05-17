'''
Module filtre
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from src.table.tabledonnees import TableDonnees
from transformation.transformation import Transformation
#from lien2var.lien2var import Lien2var  #pour la méthode num_col() à déplacer ?


class Filtre(Transformation):
    '''Appliation d'un ou plusieurs filtres (par modalité ou fenétrage temporel)
    '''

    def __init__(self, var, modalite = None, fenetrage = False, debut, fin, variable_date = "date"):
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
        variable_date : str
            nom de la variable donnant l'horodatage
        '''
        self.var = var
        self.modalite = modalite
        self.fenetrage = fenetrage
        self.debut = debut
        self.fin = fin
        self.variable_date = variable_date

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        numero_colonne = table.index_variable(self.var) #syntaxe ?
        print("------------------------------------------------------")

        if self.modalite != None:
            print("Liste des modalités selectionnées", self.modalite, "pour la variable", self.var)
            for i in range(len(table.donnees)):
                if table.donnees[i][numero_colonne] not in self.modalite:
                    table.donnees.pop(i)
                    i=i-1

        if self.fenetrage == True:
            print("Fenétrage temporel de : ", self.debut, "à", self.fin)
            num_col_date = table.index_variable(self.variable_date)
            if self.modalite != None:
                for i in range(len(table.donnees)):
                    if (table.donnees[i][num_col_date] < debut) or (table.donnees[i][num_col_date] > fin): #vérifier format date (float ou str) TODO
                        table.donnees.pop(i)
                        i=i-1
