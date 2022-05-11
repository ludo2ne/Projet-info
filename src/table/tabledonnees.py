'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
import gzip
import csv
import numpy as np
from tabulate import tabulate


class TableDonnees:
    '''Classe représentant une table de données

    Attributes
    ----------
    nom : str
        Nom de la table
    donnees : list[list[str]]
        données rangées dans une liste de listes
    chemin_complet : str
        Chemin complet du fichier à charger

    TODO
    liste_var : list[str]
        Liste contenant les noms des variables
        et ainsi supprimer la premiere ligne de donnees ?
    '''

    def __init__(self, nom, chemin_complet, delimiteur=";", valeur_manquante="na"):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        donnees : numpy array
            données rangées dans une liste de listes
        variables : numpy array
            liste des variables
        chemin_complet : str
            Chemin complet du fichier à charger
        delimiteur : str
            delimiteur utilisé dans le fichier, point virgule par défaut
        '''
        self.nom = nom
        self.chemin_complet = chemin_complet
        self.delimiteur = delimiteur

        # Chargement du fichier dans l'objet data
        donnees_csv = []
        with gzip.open(self.chemin_complet, mode='rt') as gzfile:
            synopreader = csv.reader(gzfile, delimiter=self.delimiteur)
            for row in synopreader:
                donnees_csv.append(row)

        self.variables = np.array(donnees_csv[0], dtype=object)

        donnees_csv.pop(0)
        self.donnees = np.array(donnees_csv, dtype=object)
        self.type_var = []

        self.donnees[self.donnees == valeur_manquante] = np.nan

        # Remplir la liste self.type_var
        for num_colonne in range(len(self.donnees[0])):
            isfloat = True
            for num_ligne in range(len(self.donnees)):
                try:
                    float(self.donnees[num_ligne, num_colonne])
                except:
                    isfloat = False
                    break

            self.type_var.append('float' if isfloat else 'str')

        # Transformer en float les donnees des variables de type float
        for num_colonne in range(len(self.donnees[0])):
            if self.type_var[num_colonne] == 'float':
                for num_ligne in range(len(self.donnees)):
                    self.donnees[num_ligne, num_colonne] = float(
                        self.donnees[num_ligne, num_colonne])

        print("------------------------------------------------------")
        print("Fichier chargé")
        print("   nombre de lignes    : " + str(self.donnees.shape[0]))
        print("   nombre de variables : " + str(len(self.variables)))
        print("------------------------------------------------------")

    def afficher(self, nb_lignes=-1, nb_colonnes=-1):
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
        if nb_lignes == -1:
            nb_lignes = len(listes_donnees) - 1
        if nb_colonnes == -1:
            nb_colonnes = len(listes_donnees[0])

        # Creation d une sous liste
        reduced_list = []
        reduced_list.append(self.variables[: nb_colonnes+1])
        for i in range(1, nb_lignes + 1):
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
