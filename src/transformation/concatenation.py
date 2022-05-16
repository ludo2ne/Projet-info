'''
Module concaténation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 13/05/2022
Licence : Domaine public
Version : 1.0
'''
import numpy as np
from transformation.transformation import Transformation
from table.tabledonnees import TableDonnees


class ConcatanationLignes(Transformation):
    '''Concaténation des lignes de deux tables de données'''

    def __init__(self, autre_table):
        '''Constructeur'''
        self.autre_table = autre_table

    def appliquer(self, table):
        '''Méthode pour concaténer les deux tables

        Parameters
        ----------
        table : TableDonnees
            une table de données
        autre_table : TableDonnees
            une autre table de données

        Returns
        -------
        TableDonnees : Contenant les données des deux tables

        Examples
        --------
        '''
        # assert(table.variables == self.autre_table.variables)
        # assert(table.type_var == self.autre_table.type_var)

        '''
        if np.array_equal(table.variables, self.autre_table.variables):
            # liste vide avec "la bonne taille"
            donnees = [[] for k in range(
                len(table.donnees) + len(self.autre_table.donnees) + 1)]
            # 1er element : nom des variables
            donnees[0] = np.asarray(table.variables)
            donnees_conc = np.concatenate(
                (table.donnees, self.autre_table.donnees))  # concaténation des données
            for k in range(len(donnees_conc)):
                donnees[k+1] = donnees_conc[k]  # ajout des lignes

            # donnees = np.asarray(table.variables)
            # table.donnees = np.concatenate((table.donnees, self.autre_table.donnees))

            print('Les tables ' + table.nom + ' et ' +
                  self.autre_table.nom + ' ont été concaténées')

            return TableDonnees(table.nom + '_' + self.autre_table.nom,
                                donnees=np.asarray(donnees),
                                identifiants=None,
                                type_var=table.type_var,
                                valeur_manquante="na")
        else:
            print("erreur de concatenation")
            return None
        '''

        print("------------------------------------------------------")
        print("Concaténation des tables " +
              table.nom + ' et ' + self.autre_table.nom)

        if not np.array_equal(table.variables, self.autre_table.variables):
            raise Exception("Erreur de concaténation",
                            "Les variables des deux tables ne sont pas identiques")
        else:
            # Concatenation des donnees
            donnees_conc = np.concatenate(
                (table.donnees, self.autre_table.donnees))
            # Ajout en premiere position de la liste des variables
            donnees_conc = np.concatenate(([table.variables], donnees_conc))

            return TableDonnees(table.nom + '_' + self.autre_table.nom,
                                donnees=donnees_conc,
                                identifiants=None,
                                type_var=table.type_var,
                                valeur_manquante="na")
