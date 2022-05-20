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
    '''Application d'un filtre ou d'un fenétrage temporel

    Dans le cas où la variable est de type date

    Attributes
    ----------
    var : str
        variable sur laquelle appliquer le filtre
    modalite : list[str]
        liste des modalités à conserver
    debut : int
        Entier représentant une date au format YYYYMMDDHHMMSS
    fin : int
        Entier représentant une date au format YYYYMMDDHHMMSS
    '''

    def __init__(self, variable, debut=None, fin=None, modalites=[]):
        '''Constructeur de l'objet Filtre

        Parameters
        ----------
        var : str
            variable sur laquelle appliquer le filtre
        modalite : list[str]
            liste des modalités à conserver
        debut : int
            Entier représentant une date au format YYYYMMDDHHMMSS
        fin : int
            Entier représentant une date au format YYYYMMDDHHMMSS
        '''
        self.variable = variable
        self.modalites = modalites
        self.debut = debut
        self.fin = fin

    def appliquer(self, table):
        '''Appliquer le filtre à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        print("------------------------------------------------------")

        index_lignes_a_supprimer = []
        numero_colonne = table.index_variable(self.variable)

        if numero_colonne == None:
            raise Exception("Variable " + self.variable +
                            " non trouvée dans la table " + table)

        # Si la variable est une date
        if table.type_var[numero_colonne] == "date":
            print("Fenêtrage de la variable " + self.variable +
                  " - Début : " + str(self.debut) + " - Fin : " + str(self.fin))

            for i in range(len(table.donnees)):
                if self.debut != None and int(table.donnees[i][numero_colonne]) < self.debut:
                    index_lignes_a_supprimer.append(i)
                if self.fin != None and int(table.donnees[i][numero_colonne]) > self.fin:
                    index_lignes_a_supprimer.append(i)

        # Si la variable est un string ou float
        if table.type_var[numero_colonne] == "str" or table.type_var[numero_colonne] == "float":
            print("Filtrage de la variable " + self.variable +
                  " - Modalités : " + str(self.modalites))

            for i in range(len(table.donnees)):
                if table.donnees[i][numero_colonne] not in self.modalites:
                    index_lignes_a_supprimer.append(i)

        table.donnees = np.delete(table.donnees, index_lignes_a_supprimer, 0)
