'''
Module filtre
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''
import numpy as np
from transformation.transformation import Transformation


class Filtre(Transformation):
    '''Appliation d'un ou plusieurs filtres (par modalité ou fenétrage temporel)
    Attributes
        ----------
        var : str
            variable sur laquelle appliquer le filtre par modalités
        modalite : list[str]
            liste des modalités à conserver
        fenetrage : bool
            True si on souhaite appliquer un fêtrage temporel, False sinon
        debut : date
            Date de début
        fin : date
            Date de fin
        variable_date : str
            nom de la variable donnant l'horodatage

    '''

    def __init__(self, var, debut=0, fin=0, variable_date="date", modalites=[], fenetrage=False):
        '''Constructeur de l'objet

        Parameters
        ----------
        var : str
            variable sur laquelle appliquer le filtre par modalités
        modalite : list[str]
            liste des modalités à conserver
        fenetrage : bool = False
            True si on souhaite appliquer un fêtrage temporel, False sinon
        debut : date
            Date de début
        fin : date
            Date de fin
        variable_date : str = "date"
            nom de la variable donnant l'horodatage
        '''
        self.var = var
        self.modalites = modalites
        self.fenetrage = fenetrage
        self.debut = debut
        self.fin = fin
        self.variable_date = variable_date

    def appliquer(self, table):
        '''Appliquer le filtre à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        numero_colonne = table.index_variable(self.var)  # syntaxe ?
        print("------------------------------------------------------")
        liste_indice = []
        if self.modalites != []:
            print("Liste des modalités selectionnées ",
                  self.modalites, " pour la variable ", self.var)
            for i in range(len(table.donnees)):
                if table.donnees[i][numero_colonne] not in self.modalites:
                    liste_indice.append(i)

        if self.fenetrage == True:
            print("Fenétrage temporel de : ", self.debut, " à ", self.fin)
            num_col_date = table.index_variable(self.variable_date)
            if self.modalites != None:
                for i in range(len(table.donnees)):
                    # vérifier format date (float ou str) TODO
                    if (int(table.donnees[i][num_col_date]) < self.debut) or (int(table.donnees[i][num_col_date]) > self.fin):
                        liste_indice.append(i)

        table.donnees = np.delete(table.donnees, liste_indice, 0)
