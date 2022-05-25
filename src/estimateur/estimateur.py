'''Classe abstraite estimateur'''

from abc import ABC, abstractmethod
from table.tabledonnees import TableDonnees


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
        float : écart-type des valeurs de la colonne
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
        TableDonnees : les variables et la valeur donnée par l'estimateur
        '''
        liste_estim = []
        for i in range(len(table.variables)):
            if table.type_var[i] != "float":
                liste_estim.append("na")
            else:
                liste_estim.append(self.estim1var(table, i))

        return TableDonnees(nom=table.nom,
                            donnees_avec_entete=[table.variables, liste_estim],
                            type_var=table.type_var)
