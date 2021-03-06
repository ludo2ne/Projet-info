'''
Module agregationspatiale
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''

from transformation.transformation import Transformation
import numpy as np
from table.tabledonnees import TableDonnees
from estimateur.moyenne import Moyenne


class AgregationSpatiale(Transformation):
    '''Agrégation vers un échelon plus vaste

    L'agrégation peut se faire par cumul (somme, définie par défaut) ou moyenne.

    Attributes
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
        '''
        self.var_tri = var_tri
        self.echelon_init = echelon_init
        self.echelon_final = echelon_final
        self.liste_var_cum = liste_var_cum
        self.liste_var_moy = liste_var_moy

    def agregation(self, donnees_avec_entete, var_tri_prev):
        '''Fonction d'agregation

        Parameters
        ----------
        table : numpy array 
            table comportant les noms de variables et les données
        var_tri_prev : float ou date
            valeur de la variable de tri pour cette agrégation

        Returns
        -------
        result : list
            liste des valeurs agrégées pour la valeur var_tri_prev de la variable de tri  
        '''
        objetTable = TableDonnees(nom='objet',
                                  donnees_avec_entete=donnees_avec_entete,
                                  bilanchargement=False)  # pour ne pas que ça s'affiche à chaque passage dans la boucle
        # par défaut on cumule toutes les variables
        if self.liste_var_cum == [] and self.liste_var_moy == []:
            self.liste_var_cum = np.delete(objetTable.variables, [objetTable.index_variable(
                self.var_tri), objetTable.index_variable(self.echelon_init)])

        # La table obtenue commence par afficher la valeur de var_tri et l'échelon final :
        result = [var_tri_prev, self.echelon_final]
        for k in range(len(objetTable.donnees[0])):
            if objetTable.variables[k] not in [self.var_tri, self.echelon_init]:
                if objetTable.type_var[k] == 'float' and objetTable.variables[k] in self.liste_var_cum:
                    result.append(np.cumsum(objetTable.donnees[:, k])[
                        len(objetTable.donnees[:, k])-1])
                elif objetTable.type_var[k] == 'float' and objetTable.variables[k] in self.liste_var_moy:
                    result.append(Moyenne().estim1var(objetTable, k))
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
        assert(self.var_tri in table.variables and self.echelon_init in table.variables)

        # récupérer l'index de var_tri
        index_var_tri = table.index_variable(self.var_tri)
        # tri de la table par var_tri
        table.donnees = table.donnees[table.donnees[:,
                                                    index_var_tri].argsort()]

        # initialisation de la liste finale avec le nom des variables (dans le "bon" ordre)
        liste_finale_variables = [self.var_tri, self.echelon_final]
        types = [table.type_var[table.index_variable(self.var_tri)], 'srt']
        for var in table.variables:
            if var not in [self.var_tri, self.echelon_init]:
                liste_finale_variables.append(var)
                types.append(table.type_var[table.index_variable(var)])
        liste_finale = [liste_finale_variables]

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

        # Modification de la table :
        table.variables = np.asarray(liste_finale[0])
        table.donnees = np.asarray(liste_finale[1:])
        table.type_var = np.asarray(types)
