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
import warnings
import numpy as np

from table.tabledonnees import TableDonnees


class DonneesCsv(TableDonnees):
    '''Classe représentant une table de données

    Attributes
    ----------
    nom : str
        Nom de la table
    donnees : numpy array 2D
        données rangées dans un numpy array
    variables : numpy array 1D
        liste des variables
    type_var : numpy array 1D
        type des variables
    identifiants : list[str]
        liste des noms de variables étant des identifiants
    '''

    def __init__(self, nom, chemin_complet, identifiants=None, delimiteur=";", valeur_manquante="na"):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        variables : numpy array
            liste des variables
        identifiants : list[str]
            liste des noms de variables étant des identifiants
            aucun par défaut
        chemin_complet : str
            Chemin complet du fichier à charger
        delimiteur : str
            delimiteur utilisé dans le fichier, point virgule par défaut
        valeur_manquante : str
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            na par défaut
        '''
        super().__init__(nom=nom, donnees_avec_entete=[], identifiants=identifiants)

        self.chemin_complet = chemin_complet
        self.delimiteur = delimiteur

        donnees_csv = []

        # Teste si le fichier csv est dans une archive gz
        if self.chemin_complet.endswith(".gz"):
            with gzip.open(self.chemin_complet, mode='rt') as file:
                synopreader = csv.reader(file, delimiter=self.delimiteur)
                for row in synopreader:
                    donnees_csv.append(row)
        elif self.chemin_complet.endswith(".csv"):
            with open(self.chemin_complet) as file:
                synopreader = csv.reader(file, delimiter=self.delimiteur)
                for row in synopreader:
                    donnees_csv.append(row)
        else:
            warnings.warn("Le fichier doit être un csv ou un csv.gz")

        self.variables = np.array(donnees_csv[0], dtype=object)
        self.donnees = np.array(donnees_csv[1:], dtype=object)

        self.donnees[self.donnees == valeur_manquante] = np.nan

        self.type_var = self.determiner_formats()
        self.appliquer_formats()
        self.bilan_chargement()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
