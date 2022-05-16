'''
Module filtre
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from transformation.transformation import Transformation


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

        print("------------------------------------------------------")
        if fenetrage == True:
            print("Fenétrage temporel de : ",self.debut,"à",self.fin)

        if modalite=!None:

        index_conserves = []

        # On parcourt la liste des colonnes de SelectionVariables
        for col in self.liste_colonnes:
            try:
                index_conserves.append(table.variables.tolist().index(col))
            except:
                warnings.warn("Variable " + col +
                              " non trouvée dans la table " + table.nom)

        table.variables = table.variables[index_conserves]
        table.type_var = table.type_var[index_conserves]
        table.donnees = table.donnees[:, index_conserves]
