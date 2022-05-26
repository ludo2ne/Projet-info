'''
Module ecarttype
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 11/05/2022
Licence : Domaine public
Version : 1.0
'''
import math
from estimateur.moyenne import Moyenne
from estimateur.estimateur import AbstractEstimateur
import numpy as np


class EcartType(AbstractEstimateur):
    '''CLasse permettant de calculer l'écart-type des variables d'une table
    '''

    def __init__(self):
        pass

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
        '''
        if table.type_var[numero_colonne] != "float":
            return None

        somme = 0
        nb = 0
        nb_na = 0
        moyenne = Moyenne.estim1var(table, numero_colonne)

        if np.isnan(moyenne):
            return np.nan

        for i in range(len(table.donnees)):
            if not np.isnan(table.donnees[i][numero_colonne]):
                somme += (float(table.donnees[i]
                          [numero_colonne]) - moyenne) ** 2
                nb += 1
            else:
                nb_na += 1
        if nb != 0:
            ecart_type = round(math.sqrt(somme / nb), 5)
        else:
            ecart_type = np.nan
            print("Toutes les valeurs de {} sont manquantes".format(
                table.variables[numero_colonne]))

        # print("------------------------------------------------------")
        # print("Calcul de l'écart-type de la variable " +
        #      table.variables[numero_colonne] + " : " + str(ecart_type) +
        #      " (sur " + str(nb) + " valeurs renseignées et " + str(nb_na) + " valeurs manquantes)")

        if ecart_type == 0:
            print(
                "Attention, l'écart-type de {} est nul".format(table.variables[numero_colonne]))

        return ecart_type
