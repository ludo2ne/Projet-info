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
        super().__init__(nom=nom, donnees=[], identifiants=identifiants)

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

        self.donnees[self.donnees == valeur_manquante] = np.nan

        self.type_var = []

        # Remplir la liste self.type_var
        for num_colonne in range(len(self.donnees[0])):

            # si il y a le mot date dans le nom de la variable elle sera de type date
            if "date" in self.variables[num_colonne]:
                self.type_var.append('date')
                continue

            # si la variable est un identifiant elle reste de type str
            if self.variables[num_colonne] in self.identifiants:
                self.type_var.append('str')
                continue

            # on va maintenant tester si la variable est un int, un float ou aucun des deux
#            isInt = True
            isFloat = True

            for num_ligne in range(len(self.donnees)):
                #                try:
                #                    int(self.donnees[num_ligne, num_colonne])
                #                except:
                #                    if not np.isnan(self.donnees[num_ligne, num_colonne]):
                #                        isInt = False

                try:
                    float(self.donnees[num_ligne, num_colonne])
                except:
                    isFloat = False
                    break

#            if isInt:
#                self.type_var.append('int')
            if isFloat:
                self.type_var.append('float')
            else:
                self.type_var.append('str')

        self.type_var = np.array(self.type_var)

        self.appliquer_format()
        self.bilan_chargement()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
