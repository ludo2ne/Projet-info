'''
Module jointureinterne
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from typing_extensions import Concatenate

from numpy import concatenate
from src.table.tabledonnees import TableDonnees
from transformation.transformation import Transformation


class JointureInterne(Transformation):
    '''Joiinture entre deux tables selon une clé (liste de variables)
    '''

    def __init__(self, autre_table, cle):
        '''Constructeur de l'objet

        Attributes
        ----------
        cle : list [ liste [] ] ou array
            matrice à deux lignes où la 1ère ligne est la liste de clés de table, et la 2ème ligne est la liste de clés de autre_table (dans le même ordre de correspondance)
        autre_table : TableDonnees
        '''
        self.autre_table = autre_table
        self.cle = cle

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
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
                    table_donnees.append(list_concat)
        #finir par transformer table_donnee en array ?
        # supprimer les colonnes de numeros contenus dans cle1 car en double TODO
        table.nom = nom_tb_joint
        table.variables = list_var
        table.donnees = table_donnees
        table.type_var = list_type
