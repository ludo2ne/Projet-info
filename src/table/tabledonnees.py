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
        self.type_var = type_var

        if self.__class__.__name__ == "TableDonnees":
            self.variables = donnees[0]
            self.donnees = donnees[1:]
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

        # Gestion des valeurs par defaut des parametres
        if nb_lignes == None:
            nb_lignes = len(listes_donnees)
        if nb_colonnes == None:
            nb_colonnes = len(listes_donnees[0])

        # Creation d une sous liste
        reduced_list = []
        reduced_list.append(self.variables[: nb_colonnes+1])
        reduced_list.append(self.type_var[: nb_colonnes+1])
        for i in range(nb_lignes):
            list_row = listes_donnees[i][: nb_colonnes+1]
            reduced_list.append(list_row)

        # Affichage
        print(
            "\n" + tabulate(tabular_data=reduced_list[1:],
                            headers=reduced_list[0],
                            floatfmt=".2f") + "\n")                 # 2 decimales pour les float

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Table de données : {}".format(self.nom)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
