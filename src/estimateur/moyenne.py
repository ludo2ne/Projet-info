'''
Module moyenne
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
from ..table.tabledonnees import TableDonnees


class Moyenne:
    '''Moyenne d'une variable

    Cette classe ne contient qu'une seule méthode statique
    Il n'y a pas de constructeur car il n'est pas nécessaire d'instancier une objet de cette classe
    '''

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

        Examples
        --------

        '''
        assert(table.type_var[numero_colonne] == "float")
        somme = 0
        nb = 0
        nb_na = 0

        for i in range(1, len(table.donnees)):
            if table.donnees[i][numero_colonne] != "mq":
                somme += float(table.donnees[i][numero_colonne])
                nb += 1
            else:
                nb_na += 1

        moyenne = round(somme / nb, 2)

        print("------------------------------------------------------")
        print("Calcul de la moyenne de la variable " +
              table.variables[numero_colonne] + " : " + str(round(moyenne, 2)) +
              " (sur " + str(nb) + " valeurs renseignées et " + str(nb_na) + " valeurs manquantes)")

        return moyenne

    @staticmethod
    def table_estimateur(table):
        liste_moyenne = []
        for i in len(table.liste_var):
            liste_moyenne.append(estim1var(table, i))
        return TableDonnees(table.nom + "_moyenne", table.liste_var, table.type_var, [liste_moyenne])
