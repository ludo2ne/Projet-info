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

        index_lignes_a_supprimer = []
        donnees_jointes = []

        for i in range(len(table.donnees)):
            #match_found = False
            for j in range(len(self.autre_table.donnees)):
                it_is_a_match = True
                for k in range(len(self.cle)):
                    if table.donnees[i, index_cles_table[k]] != self.autre_table.donnees[j, index_cles_autre_table[k]]:
                        it_is_a_match = False
                        break
                if it_is_a_match:
                    #match_found = True
                    donnees_jointes.append(np.concatenate((
                        table.donnees[i], np.delete(self.autre_table.donnees[j], index_cles_autre_table))))
                    break
            # if not match_found:
            #    index_lignes_a_supprimer.append(i)

        table.donnees = np.array(donnees_jointes)

        # inutile
        #table.donnees = np.delete(table.donnees, index_lignes_a_supprimer, 0)

        table.variables = np.concatenate((
            table.variables, np.delete(self.autre_table.variables, index_cles_autre_table)))
        table.type_var = np.concatenate((
            table.type_var, np.delete(self.autre_table.type_var, index_cles_autre_table)))


'''
    def appliquer(self, table):
        nom_tb_joint = "{}_{}".format(table.nom, self.autre_table.nom)
        cle1=[TableDonnees.index_variable(var) for var in self.cle[0]]
        cle2=[TableDonnees.index_variable(var) for var in self.cle[1]]
        table_donnees=[]
        list_var = table.variables + self.autre_table.variables #concaténation
        list_type = table.type_var + self.autre_table.type_var
        for i in range(len(table.donnees)):
            for j in range(len(self.autre_table.donnees)):
                if table.donnees[i,cle1] == self.autre_table.donnees[j,cle2]:
                    list_concat = table.donnees[i] + self.autre_table.donnees[j]
                    #list_concat.pop(col_cle[0]) dans l'idée de supprimer les colonnes en double, mais pop() attend un seul entier pas une liste
                    #list_concat.pop(cle1) dans l'idée de supprimer les colonnes en double, mais pop() attend un seul entier pas une liste
                    table_donnees.append(list_concat)
        #finir par transformer table_donnee en array ?
        # supprimer les colonnes (de la nouvelle table jointe) dont les numeros sont contenus dans cle1 (car en double) TODO
        table.nom = nom_tb_joint
        table.variables = list_var
        table.donnees = table_donnees
        table.type_var = list_type
'''