'''
Module donneesjson
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import warnings
import gzip
import json
import numpy as np
import os

from datetime import datetime
from table.tabledonnees import TableDonnees


class DonneesJson(TableDonnees):
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
        liste des types des variables
    identifiants : list[str]
        liste des noms de variables étant des identifiants
    '''

    def __init__(self, chemin_complet, nom = "", identifiants = [], valeur_manquante = None):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str = ""
            nom de la table
            si pas modifié, prend le nom du fichier sans l'extension
        variables : numpy array
            liste des variables
        identifiants : list[str] = []
            liste des noms de variables étant des identifiants
            [] par défaut
        chemin_complet : str
            Chemin complet du fichier à charger
        delimiteur : str
            delimiteur utilisé dans le fichier, point virgule par défaut
        valeur_manquante : str = None
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            None par défaut
        '''
        super().__init__(nom=nom, donnees_avec_entete = [], identifiants = identifiants)

        basename = os.path.basename(chemin_complet)
        file_name = os.path.splitext(basename)[0]
        nom_dossier=chemin_complet.split('/')[-2]

        dico = None


        if chemin_complet.endswith(".gz"):
            file_name = os.path.splitext(file_name)[0]
            with gzip.open(chemin_complet, mode = 'rt', encoding = 'utf-8') as gzfile:
                dico = json.load(gzfile)
        elif chemin_complet.endswith(".json"):
            with open(chemin_complet, mode = 'r', encoding = 'utf-8') as jsonfile:
                dico = json.load(jsonfile)
        else:
            warnings.warn("Le fichier doit être un json ou un json.gz")

        # Etape 1 recherche de toutes les variables
        variables_tmp = []
        for item in range(len(dico)):
            for cle in dico[item].get('fields').keys():
                if cle not in variables_tmp:
                    variables_tmp.append(cle)

        self.variables = np.sort(np.array(variables_tmp, dtype=object))

        # Etape 2 conversion du dictionnaire en numpy array
        donnees_json = []

        for item in range(len(dico)):
            ma_ligne = []
            for variable in self.variables:
                ma_ligne.append(dico[item].get('fields').get(variable))
            donnees_json.append(ma_ligne)

        self.donnees = np.array(donnees_json, dtype=object)

        self.donnees[self.donnees == valeur_manquante] = np.nan

        self.type_var = self.determiner_formats()

        if self.nom == "":
            self.nom = "{}_{}".format(nom_dossier, file_name)

        self.appliquer_formats()
        self.bilan_chargement()

    def appliquer_formats(self):
        super().appliquer_formats()

        # transformation des dates specifiquement pour la colonne date_heure
        for num_colonne in range(len(self.donnees[0])):
            if self.variables[num_colonne] == "date_heure":
                for num_ligne in range(len(self.donnees)):
                    date_time_obj = datetime.strptime(
                        self.donnees[num_ligne, num_colonne], '%Y-%m-%dT%H:%M:%S+01:00')
                    date_time_str_new = datetime.strftime(
                        date_time_obj, '%Y%m%d%H%M%S')
                    self.donnees[num_ligne, num_colonne] = date_time_str_new
