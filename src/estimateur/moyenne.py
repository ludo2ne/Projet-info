'''
Module moyenne
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import numpy as np
from estimateur.estimateur import AbstractEstimateur


class Moyenne(AbstractEstimateur):
    '''CLasse permettant de calculer la moyenne des variables d'une table
    '''

    def __init__(self):
        '''Constructeur'''
        self.nom = "moyenne"

    @staticmethod
    def estim1var(table, numero_colonne):
        '''Calculer la moyenne d'une colonne de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            index de la colonne

        Returns
        -------
        float : moyenne des valeurs de la colonne
        '''
        if table.type_var[numero_colonne] != "float":
            return None

        somme = 0
        nb = 0
        nb_na = 0

        for i in range(len(table.donnees)):
            if not np.isnan(table.donnees[i][numero_colonne]):
                somme += float(table.donnees[i][numero_colonne])
                nb += 1
            else:
                nb_na += 1

        moyenne = round(somme / nb, 2) if nb != 0 else np.nan

        # print("------------------------------------------------------")
        # print("Calcul de la moyenne de la variable " +
        #      table.variables[numero_colonne] + " : " + str(round(moyenne, 2)) +
        #      " (sur " + str(nb) + " valeurs renseignées et " + str(nb_na) + " valeurs manquantes)")

        return moyenne
