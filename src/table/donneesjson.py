'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
import gzip
import json
import numpy as np

from table.tabledonnees import TableDonnees


class DonneesJson(TableDonnees):
    '''Classe représentant une table de données

    Attributes
    ----------
    nom : str
        Nom de la table
    donnees : numpy array
        données rangées dans un numpy array
    variables : numpy array
        liste des variables
    type_var : list[str]
        type des variables
    identifiants : list[str]
        liste des noms de variables étant des identifiants
    '''
# TODO Est-ce qu'ici l'attribut donnees est en fait donnees_avec_entete ? Si oui, modifier et mettre l'ULM à jour en même temps (idem dans la classe csv)

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
        super().__init__(nom=nom, donnees=[], identifiants=identifiants)

        self.chemin_complet = chemin_complet
        self.delimiteur = delimiteur

        # Chargement du fichier dans l'objet data
        with gzip.open(self.chemin_complet, mode='rt', encoding='utf-8') as gzfile:
            dico = json.load(gzfile)

        # Etape 1 recherche de toutes les variables
        variables_tmp = []
        for item in range(len(dico)):
            for cle in dico[item].get('fields').keys():
                if cle not in variables_tmp:
                    variables_tmp.append(cle)

        self.variables = np.array(variables_tmp, dtype=object)

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
        self.appliquer_format()
        self.bilan_chargement()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
