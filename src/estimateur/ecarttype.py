'''
Module ecarttype
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 11/05/2022
Licence : Domaine public
Version : 1.0
'''
import math
from moyenne import Moyenne
from estimateur.estimateur import AbstractEstimateur
from table.tabledonnees import TableDonnees


class EcartType(AbstractEstimateur):
    '''Ecart-type calculé sur chaque variable d'une table

    Attributes
    ----------
    nom : str = 'ecart_type'
    '''

    def __init__(self):
        self.nom = 'ecart_type'

    @staticmethod
    def estim1var(table, numero_colonne):
        '''Calculer l'écart-type d'une colonne de la table

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
        assert (table.type_var[numero_colonne] == 'float')

        somme = 0
        nb = 0
        nb_na = 0
        moyenne = Moyenne.estim1var(table, numero_colonne)

        for i in range(1, len(table.donnees)):
            if table.donnees[i][numero_colonne] != "mq":
                somme += (float(table.donnees[i]
                          [numero_colonne]) - moyenne) ** 2
                nb += 1
            else:
                nb_na += 1

        ecart_type = round(math.sqrt(somme / nb), 2)

        print("------------------------------------------------------")
        print("Calcul de l'écart-type de la variable " +
              table.variables[numero_colonne] + " : " + str(ecart_type) +
              " (sur " + str(nb) + " valeurs renseignées et " + str(nb_na) + " valeurs manquantes)")

        return ecart_type
