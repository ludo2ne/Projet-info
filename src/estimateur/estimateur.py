'''Classe abstraite estimateur'''

from abc import ABC, abstractmethod
from table.tabledonnees import TableDonnees
import numpy as np


class AbstractEstimateur(ABC):
    '''Classe abstraite implémentant un estimateur
    '''

    @abstractmethod
    def __init__(self):
        '''Constructeur'''
        pass

    @abstractmethod
    def estim1var(table, numero_colonne):
        '''Calcul d'un estimateur sur la colonne d'index numero_colonne de la table
        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            index de la colonne

        Returns
        -------
        float : estimateur (écart-type ou moyenne) des valeurs de la colonne
        '''
        pass

    def appliquer(self, table):
        '''Fonction qui applique l'estimateur à toutes les colonnes de table

        Parameters
        ----------
        table : TableDonnees
            table de données déjà selectionnée pour que toutes les variables soit de type "float"

        Returns
        -------
        TableDonnees : les noms des variables et la valeur donnée par l'estimateur
        '''
        liste_estim = []
        n = len(table.variables)
        for i in range(n):
            if table.type_var[i] != "float":
                liste_estim.append(np.nan)
            else:
                liste_estim.append(self.estim1var(table, i))

        table_estim = TableDonnees(nom="{}_{}".format(table.nom,self.nom),
                            donnees_avec_entete=[table.variables, liste_estim],
                            type_var=table.type_var)

        print(self.nom, "de la table", table.nom)
        table_estim.afficher(nb_lignes = 2, nb_colonnes = n)
        return table_estim
