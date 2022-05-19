'''
Module jointureinterne
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import numpy as np
from table.tabledonnees import TableDonnees
from transformation.transformation import Transformation


class JointureInterne(Transformation):
    '''Joiinture entre deux tables selon une clé (liste de variables)
    '''

    def __init__(self, autre_table, cle):
        '''Constructeur de l'objet

        Attributes
        ----------
        cle : list [tuple(str)]
            Liste de tuples contenant chacun un attribut de chaque table permettant de faire la jointure
        autre_table : TableDonnees
        '''
        self.autre_table = autre_table
        self.cle = cle

    def appliquer(self, table):
        '''Appliquer la jointure à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        index_cles_table = [table.index_variable(
            var[0]) for var in self.cle]
        index_cles_autre_table = [self.autre_table.index_variable(
            var[1]) for var in self.cle]

        index_lignes_a_supprimer = []
        donnees_jointes = []

        for i in range(len(table.donnees)):
            match_found = False
            for j in range(len(self.autre_table.donnees)):
                it_is_a_match = True
                for k in range(len(self.cle)):
                    if table.donnees[i, index_cles_table[k]] != self.autre_table.donnees[j, index_cles_autre_table[k]]:
                        it_is_a_match = False
                        break
                if it_is_a_match:
                    match_found = True
                    donnees_jointes.append(np.concatenate((
                        table.donnees[i], np.delete(self.autre_table.donnees[j], index_cles_autre_table[k]))))
                    break
            if not match_found:
                index_lignes_a_supprimer.append(i)

        table.donnees = np.array(donnees_jointes)
        #table.donnees = np.delete(table.donnees, index_lignes_a_supprimer, 0)
        table.variables = np.concatenate((
            table.variables, self.autre_table.variables))
        table.type_var = np.concatenate((
            table.type_var, self.autre_table.type_var))
