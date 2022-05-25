'''
Module concaténation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''
import numpy as np
from transformation.transformation import Transformation


class ConcatenationLignes(Transformation):
    '''Concaténation des lignes de deux tables de données

    Attributes
    ----------
    autre_table : TableDonnees
    '''

    def __init__(self, autre_table):
        '''Constructeur de l'objet
        Parameters
        ----------
        autre_table : TableDonnees
        '''
        self.autre_table = autre_table
        print("-------------- Creation concat -------------------")

    def appliquer(self, table):
        '''Méthode pour concaténer les deux tables

        Parameters
        ----------
        table : TableDonnees
            une table de données
        '''
        print("------------------------------------------------------")
        print("Concaténation des tables " +
              table.nom + ' et ' + self.autre_table.nom)

        # Vérification que les tables ont les mêmes variables
        if not np.array_equal(table.variables, self.autre_table.variables):
            raise Exception("Erreur de concaténation",
                            "Les variables des deux tables ne sont pas identiques")
        else:
            # Concatenation des donnees
            table.donnees = np.concatenate(
                (table.donnees, self.autre_table.donnees))
            print('Les tables ' + table.nom + ' et ' +
                  self.autre_table.nom + ' ont été concaténées')
