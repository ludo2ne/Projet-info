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

    def __init__(self, nom, chemin_complet, delimiteur=";"):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        donnees : list[list[str]]
            données rangées dans une liste de listes
        chemin_complet : str
            Chemin complet du fichier à charger
        delimiteur : str
            delimiteur utilisé dans le fichier, point virgule par défaut
        '''
        self.nom = nom
        self.donnees = []
        self.chemin_complet = chemin_complet
        self.delimiteur = delimiteur

        # Chargement du fichier dans l'objet data
        with gzip.open(self.chemin_complet, mode='rt') as gzfile:
            synopreader = csv.reader(gzfile, delimiter=self.delimiteur)
            for row in synopreader:
                self.donnees.append(row)

        print("------------------------------------------------------")
        print("Fichier chargé")
        print("   nombre de lignes    : " + str(len(self.donnees) - 1))
        print("   nombre de variables : " + str(len(self.donnees[0])))
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

        # Gestion des valeurs par defaut des parametres
        if nb_lignes == -1:
            nb_lignes = len(self.donnees) - 1
        if nb_colonnes == -1:
            nb_colonnes = len(self.donnees[0])

        # Creation d une sous liste
        reduced_list = []
        for i in range(0, nb_lignes + 1):
            list_row = self.donnees[i][:nb_colonnes+1]
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
