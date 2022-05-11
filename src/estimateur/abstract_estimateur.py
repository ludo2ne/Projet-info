'''Classe abstraite estimateur'''

from abc import ABC, abstractmethod
from table.tabledonnees import TableDonnees


class AbstractEstimateur(ABC):
    '''Classe abstraite implémentant un estimateur

    Attributes
    ----------
    nom : 'str'
        nom de l'estimateur
    '''

# ajout pour pouvoir utiliser le nom de l'estimateur dans la table de sortie finale
    @abstractmethod
    def __init__(self):
        '''Constructeur pour donner un nom à l'estimateur'''
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

        Examples
        --------
        '''
        pass

    def table_estimateur(self, table):
        '''Fonction qui applique l'estimateur à toutes les colonnes de table

        Parameters
        ----------
        table : TableDonnees
            table de données

        Returns
        -------
        TableDonnees : les variables et la valeur donnée par l'estimateur

        Examples
        --------
        '''
        liste_estim = []
        for i in len(table.liste_var):
            liste_estim.append(estim1var(table, i))
        return TableDonnees(table.nom + "_" + self.nom, table.liste_var, table.type_var, [liste_estim])
