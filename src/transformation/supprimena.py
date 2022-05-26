'''
Module supprimena
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

from transformation.transformation import Transformation
import numpy as np
import warnings


class SupprimeNA(Transformation):
    '''Suppression des lignes de table.donnees où il y a une valeur manquante pour au moins une des variables de la liste saisies;
    par défaut si la liste est vide cela s'applique à toutes les variables de type numérique uniquement

    Attributes
        ----------
        liste_var : list[str]
            listes de variables sur lesquelles appliquer la suppression des valeurs manquantes

    '''

    def __init__(self, liste_var = []):
        '''Constructeur de l'objet

        Parameters
        ----------
        liste_var : list[str] = []
            listes de variables sur lesquelles appliquer la suppression des valeurs manquantes

        '''
        self.liste_var = liste_var


    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        if self.liste_var == []:
            self.liste_var = table.liste_var_float()
        print("------------------------------------------------------")
        print("Suppression des na des variables " + str(self.liste_var))

        liste_numero_col = []
        for var in self.liste_var:
            # génère la liste des indices de colonne correspondant à la liste des variable données
            liste_numero_col.append(table.index_variable(var))

        indice_NA = []

        for i in liste_numero_col:
            #if table.type_var[i] != "float":
            #    warnings.warn("Impossible de supprimer les NA sur la variable " +
            #                  table.variables[i] + " qui n'est pas de type float")
            #    continue

            for j in range(len(table.donnees)):
                if type(table.donnees[j][i]) != str:
                    # Test de valeur manquante (qui ne fonctionne pas sur une chaine de caractère)
                    if np.isnan(table.donnees[j][i]):
                        indice_NA.append(j)

        # Supprime toutes les lignes dont l indice est dans la liste indice_NA
        table.donnees = np.delete(table.donnees, indice_NA, 0)
