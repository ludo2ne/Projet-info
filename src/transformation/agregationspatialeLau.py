'''
Module agregationspatialE
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''

from transformation.transformation import Transformation
import numpy as np
from table.tabledonnees import TableDonnees
from estimateur.moyenne import Moyenne


class AgregationSpatialeLau(Transformation):
    '''Agrégation vers un échelon plus vaste

    L'agrégation peut se faire par cumul (somme, définie par défaut) ou moyenne.

    Attributes
    ----------
    '''

    def __init__(self, var_tri, echelon_init, echelon_final, liste_var_cum=[], liste_var_moy=[]):
        '''Constructeur de l'objet

        Parameters
        ----------
        var_tri : str ou date
            nom de la variable par laquelle sont triées les données avant agrégation
        echelon_init : str
            nom de la variable correspondant à l'échelon initial
        echelon_final : str
            nom de l'échelon final
        liste_var_cum : list
            liste des variables qu'on agrège par cumul (somme)
            par défaut : liste vide
        liste_var_moy : list
            liste des variables qu'on agrège par moyenne
            par défaut : liste vide
        table_correspondance : TableDonnees
        '''
        self.var_tri = var_tri
        self.echelon_init = echelon_init
        self.echelon_final = echelon_final
        self.liste_var_cum = liste_var_cum
        self.liste_var_moy = liste_var_moy

    def agregation(self, table, var_tri_prev):
        '''Fonction d'agregation

        Parameters
        ----------
        table : numpy array 
            table comportant les noms de variables et les données
        var_tri_prev : float ou date
            valeur de la variable de tri pour cette agrégation
        '''
        objetTable = TableDonnees(nom='objet',
                                  donnees_avec_entete=table,
                                  bilanchargement=False)  # pour ne pas que ça s'affiche à chaque passage dans la boucle
        # par défaut on cumule toutes les variables
        if self.liste_var_cum == [] and self.liste_var_moy == []:
            liste_var_cum = objetTable.variables

        # La table obtenue commence par afficher la valeur de var_tri et l'échelon final :
        result = [var_tri_prev, self.echelon_final]
        for k in range(len(objetTable.donnees[0])):
            if objetTable.variables[k] not in [self.var_tri, self.echelon_init]:
                if objetTable.type_var[k] == 'float' and objetTable.variables[k] in self.liste_var_cum:
                    result.append(np.cumsum(objetTable.donnees[:, k])[
                        len(objetTable.donnees[:, k])-1])
                elif objetTable.type_var[k] == 'float' and objetTable.variables[k] in self.liste_var_moy:
                    result.append(Moyenne().estim1var(objetTable, k))
                    print(Moyenne().estim1var(objetTable, k))
                elif objetTable.type_var[k] != 'float':
                    result.append('nan')
        return result

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        # TODO vérifier que var_tri et echelon_init sont des variables de table

        # récupérer l'index de var_tri et echelon_init
        index_var_tri = table.index_variable(self.var_tri)
        index_echelon_init = table.index_variable(self.echelon_init)
        # tri de la table par var_tri
        table.donnees = table.donnees[table.donnees[:,
                                                    index_var_tri].argsort()]

        # initialisation de la liste finale avec le nom des variables (dans le "bon" ordre)
        liste_finale_variables = [self.var_tri, self.echelon_final]
        for var in table.variables:
            if var not in [self.var_tri, self.echelon_init]:
                liste_finale_variables.append(var)
        liste_finale = [liste_finale_variables]
        # TODO on devrait plutot mettre : table.variables = ?

        # initialisation de la sous-liste correspondant à la première valeur de var_tri
        k = 0
        donnees_extraites = list(table.donnees[k])
        var_tri_current = donnees_extraites[index_var_tri]

        # on conserve les noms de variables en en-tête
        tmp_liste = [table.variables]
        var_tri_prev = donnees_extraites[index_var_tri]
        while k < len(table.donnees):
            donnees_extraites = list(table.donnees[k])
            var_tri_current = donnees_extraites[index_var_tri]
            if var_tri_current == var_tri_prev:
                tmp_liste.append(donnees_extraites)
            else:
                result = self.agregation(tmp_liste, var_tri_prev)
                liste_finale.append(result)
                var_tri_prev = donnees_extraites[index_var_tri]
                tmp_liste = [table.variables]
                tmp_liste.append(donnees_extraites)
            k += 1
        result = self.agregation(tmp_liste, var_tri_prev)
        liste_finale.append(result)

        print('la liste finale est :')
        print(np.asarray(liste_finale))

# TODO à la fin on renvoie une nouvelle table : juste redéfinir self.donnees et self.variables? (mais du coup self.type_var.. ?)
