'''
Module jointureinterne
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import numpy as np
from transformation.transformation import Transformation


class JointureInterne(Transformation):
    '''Joiinture entre deux tables selon une clé (liste de variables)
        Attributes
        ----------
        cle : list [tuple(str)]
            Liste de tuples contenant chacun un attribut de chaque table permettant de faire la jointure
        autre_table : TableDonnees

    '''

    def __init__(self, autre_table, cle):
        '''Constructeur de l'objet

        Parameters
        ----------
        cle : list [tuple(str)]
            Liste de tuples contenant chacun un attribut de chaque table permettant de faire la jointure
        autre_table : TableDonnees
            La table à joindre
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

        print("------------------------------------------------------")
        print("Jointure de la table " +
              table.nom + ' avec la table ' + self.autre_table.nom)

        index_cles_table = [table.index_variable(
            var[0]) for var in self.cle]
        index_cles_autre_table = [self.autre_table.index_variable(
            var[1]) for var in self.cle]

        donnees_jointes = []

        # on commence par une double boucle pour tester toutes les combinaisons possibles
        # entre les donnees des deux tables
        for i in range(len(table.donnees)):
            for j in range(len(self.autre_table.donnees)):
                it_is_a_match = True
                # on parcourt la liste des cles pour comparer les valeurs
                for k in range(len(self.cle)):
                    # des qu il y a une difference entre deux cles, on sort de la boucle
                    if table.donnees[i, index_cles_table[k]] != self.autre_table.donnees[j, index_cles_autre_table[k]]:
                        it_is_a_match = False
                        break
                # si toutes les cles sont egales, on fait la jointure
                if it_is_a_match:
                    donnees_jointes.append(np.concatenate((
                        table.donnees[i], np.delete(self.autre_table.donnees[j], index_cles_autre_table))))
                    break

        table.donnees = np.array(donnees_jointes)

        table.variables = np.concatenate((
            table.variables, np.delete(self.autre_table.variables, index_cles_autre_table)))
        table.type_var = np.concatenate((
            table.type_var, np.delete(self.autre_table.type_var, index_cles_autre_table)))
        table.nom = "{}_{}".format(table.nom, self.autre_table.nom)
