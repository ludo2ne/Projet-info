'''Classe abstraite estimateur'''

from abc import ABC, abstractmethod
from table.tabledonnees import TableDonnees


# est-ce qu'il faut modifier par AbstractEstimateur(Operation) et mettre tous les dossiers (transformation, estimateur, lien2var) dans un dossier operation ?
class AbstractEstimateur(ABC):
    '''Classe abstraite implémentant un estimateur
    '''

# ajout pour pouvoir utiliser le nom de l'estimateur dans la table de sortie finale
    @abstractmethod
    def __init__(self):
        '''Constructeur pour donner un nom à l'estimateur'''
        pass

    @abstractmethod
    # attention, ne pas changer en "appliquer" (déjà utilisé pour l'application à la table complete , cf methode suivante)
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
        for i in len(table.variables):
            liste_estim.append(self.estim1var(table, i))

        return TableDonnees(nom=table.nom + "_" + self.nom,
                            donnees=[liste_estim],
                            variables=table.variables,
                            type_var=table.type_var)
