'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
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

    def __init__(self, nom, donnees, identifiants=None, valeur_manquante="na"):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        donnees : numpy array
            données rangées dans un numpy array
        variables : numpy array
            liste des variables
        identifiants : list[str]
            liste des noms de variables étant des identifiants
        valeur_manquante : str
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            na par défaut
        '''
        self.nom = nom
        self.identifiants = identifiants

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
        reduced_list.append(self.type_var[: nb_colonnes+1])
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
