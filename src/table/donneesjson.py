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
# Lau : peut-être pas besoin de changer le nom ? on sait que les array 1D correspondent à donnees[0] et donnees[1:]?

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
        super().__init__(nom = nom, donnees_avec_entete = [], identifiants = identifiants )

        self.chemin_complet = chemin_complet
        self.delimiteur = delimiteur

        dico = None

        if self.chemin_complet.endswith(".gz"):
            with gzip.open(self.chemin_complet, mode='rt', encoding='utf-8') as gzfile:
                dico = json.load(gzfile)
        elif self.chemin_complet.endswith(".json"):
            with open(self.chemin_complet, mode='r', encoding='utf-8') as jsonfile:
                dico = json.load(jsonfile)
        else:
            warnings.warn("Le fichier doit être un json ou un json.gz")

            # Etape 1 recherche de toutes les variables
        variables_tmp = []
        for item in range(len(dico)):
            for cle in dico[item].get('fields').keys():
                if cle not in variables_tmp:
                    variables_tmp.append(cle)

        self.variables = np.array(variables_tmp, dtype=object) #TODO pourquoi avoir définie la liste des variables en array plutot qu'en liste ??

        # Etape 2 conversion du dictionnaire en numpy array
        donnees_json = []

        for item in range(len(dico)):
            ma_ligne = []
            for variable in self.variables:
                ma_ligne.append(dico[item].get('fields').get(variable))
            donnees_json.append(ma_ligne)

        self.donnees_avec_entete = np.array(donnees_json, dtype=object)

        self.donnees_avec_entete[self.donnees_avec_entete == valeur_manquante] = np.nan

        self.type_var = self.determiner_formats()
        self.appliquer_formats()
        self.bilan_chargement()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
