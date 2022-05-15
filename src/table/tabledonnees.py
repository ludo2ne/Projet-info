'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
import numpy as np
from tabulate import tabulate


class TableDonnees:
    '''Classe représentant une table de données

    Attributes
    ----------
    nom : str
        Nom de la table
    donnees : numpy array
        données rangées dans un numpy array
    variables : numpy array
        liste des variables
    type_var : numpy array
        type des variables
    identifiants : list[str]
        liste des noms de variables étant des identifiants
    '''

    def __init__(self, nom, donnees, identifiants=None, type_var=[], valeur_manquante="na"):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        donnees : numpy array
            données rangées dans un numpy array
            la première ligne contient les entêtes de colonnes (variables)
        identifiants : list[str]
            liste des noms de variables étant des identifiants
        type_var : numpy array
            type des variables
        valeur_manquante : str
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            na par défaut

        Examples
        --------
        '''
        self.nom = nom
        self.identifiants = identifiants

        if self.__class__.__name__ == "TableDonnees":
            self.variables = np.array(donnees[0], dtype=object)
            self.type_var = np.array(type_var, dtype=object)
            self.donnees = np.array(donnees[1:], dtype=object)
            self.appliquer_format()
            self.bilan_chargement()

    def bilan_chargement(self):
        print("------------------------------------------------------")
        print("Table " + self.nom + " chargée : ")
        print("   nombre de lignes    : " + str(len(self.donnees)))
        print("   nombre de variables : " + str(len(self.variables)))
        print("------------------------------------------------------")

    def afficher(self, nb_lignes=None, nb_colonnes=None):
        '''Affiche sous forme de tableau un extrait de la table

        Parameters
        ----------
        nb_lignes : int
            nombre de lignes à afficher
            si non renseigné, toutes les lignes sont affichées
        nb_colonnes : int
            nombre de colonnes à afficher
            si non renseigné, toutes les colonnes sont affichées

        Returns
        -------
        None
        '''

        # Pour eviter de tout refaire je reconverti le numpy array en liste de liste
        listes_donnees = self.donnees.tolist()

        # Si les parametres sont resenignes a None ou si leur valeur est trop grande
        # ils prennent simplement la valeur maximum possible
        if nb_lignes == None or nb_lignes > len(listes_donnees):
            nb_lignes = len(listes_donnees)
        if nb_colonnes == None or nb_colonnes > len(listes_donnees[0]):
            nb_colonnes = len(listes_donnees[0])

        # Creation d une sous liste
        reduced_list = [[]]

        for i in range(0, nb_colonnes):
            reduced_list[0].append(str(self.variables[i]) + "\n" + str(self.type_var[i]))

        for i in range(nb_lignes):
            list_row = listes_donnees[i][: nb_colonnes]
            reduced_list.append(list_row)

        # Affichage
        print(
            "\n" + tabulate(tabular_data=reduced_list[1:],
                            headers=reduced_list[0],
                            tablefmt="psql",
                            floatfmt=".2f") + "\n")    # 2 decimales pour les float

    def appliquer_format(self):
        '''Transforme en float les données des variables de type float
        '''
        for num_colonne in range(len(self.donnees[0])):
            if self.type_var[num_colonne] == "float":
                for num_ligne in range(len(self.donnees)):
                    self.donnees[num_ligne, num_colonne] = float(
                        self.donnees[num_ligne, num_colonne])

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Table de données : {}".format(self.nom)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
