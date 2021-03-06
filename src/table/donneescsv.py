'''
Module donneescsv
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import gzip
import csv
import warnings
import numpy as np
import os

from table.tabledonnees import TableDonnees


class DonneesCsv(TableDonnees):
    '''Classe représentant une table de données extrait d'un fichier csv

    Attributes
    ----------
    nom : str
        Nom de la table
    donnees : numpy array 2D
        données rangées dans un numpy array
    variables : numpy array 1D
        liste des variables
    type_var : numpy array 1D
        liste des types des variables
    identifiants : list[str]
        liste des noms de variables étant des identifiants
    '''

    def __init__(self, chemin_complet, nom = "", identifiants = [], delimiteur = ";", valeur_manquante = "mq"):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str = ""
            nom de la table
            si pas saisi, prend le nom du fichier sans l'extension
        identifiants : list[str] = []
            liste des noms de variables étant des identifiants
            aucun par défaut
        chemin_complet : str
            Chemin complet du fichier à charger
        delimiteur : str = ";"
            delimiteur utilisé dans le fichier, point virgule par défaut
        valeur_manquante : str = "mq"
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            mq par défaut pour les csv
        '''
        super().__init__(nom = nom,
                         donnees_avec_entete = [],
                         identifiants = identifiants)

        donnees_csv = []

        basename = os.path.basename(chemin_complet)
        file_name = os.path.splitext(basename)[0]


        # Teste si le fichier csv est dans une archive gz
        if chemin_complet.endswith(".gz"):
            file_name = os.path.splitext(file_name)[0]

            with gzip.open(chemin_complet, mode = 'rt') as file:
                synopreader = csv.reader(file, delimiter=delimiteur)
                for row in synopreader:
                    donnees_csv.append(row)

        elif chemin_complet.endswith(".csv"):
            with open(chemin_complet) as file:
                synopreader = csv.reader(file, delimiter=delimiteur)
                for row in synopreader:
                    donnees_csv.append(row)
        else:
            warnings.warn("Le fichier doit être un csv ou un csv.gz")

        self.variables = np.array(donnees_csv[0], dtype=object)
        self.donnees = np.array(donnees_csv[1:], dtype=object)

        self.donnees[self.donnees == valeur_manquante] = np.nan

        self.type_var = self.determiner_formats()
        if self.nom == "":
            self.nom = file_name
        self.appliquer_formats()
        self.bilan_chargement()
