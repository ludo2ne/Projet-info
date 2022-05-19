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

    def __init__(self, nom, donnees_avec_entete, identifiants=[], type_var=[], valeur_manquante=None):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        donnees_avec_entete : numpy array
            données rangées dans un numpy array
            la première ligne contient les entêtes de colonnes (variables)
        identifiants : list[str]
            liste des noms de variables étant des identifiants
        type_var : numpy array
            type des variables
        valeur_manquante : str
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            na par défaut
        '''
        self.nom = nom
        self.identifiants = identifiants

        if self.__class__.__name__ == "TableDonnees":
            if donnees_avec_entete != []:
                self.variables = np.array(donnees_avec_entete[0], dtype=object)
                self.donnees = np.array(donnees_avec_entete[1:], dtype=object)
            else:
                self.variables = []
                self.donnees = []
            if type_var != []:
                self.type_var = np.array(type_var, dtype=object)
            else:
                self.type_var = self.determiner_formats()

            self.donnees[self.donnees == valeur_manquante] = np.nan

            self.appliquer_formats()
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

        print("------------------------------------------------------")
        print("Affichage de la table " + self.nom)

        # Pour eviter de tout refaire je reconverti le numpy array en liste de liste
        listes_donnees = self.donnees.tolist()

        # Si les parametres sont renseignes???TODO a None ou si leur valeur est trop grande
        # ils prennent simplement la valeur maximum possible
        if nb_lignes == None or nb_lignes > len(listes_donnees):
            nb_lignes = len(listes_donnees)
        if nb_colonnes == None or nb_colonnes > len(listes_donnees[0]):
            nb_colonnes = len(listes_donnees[0])

        # Creation d une sous liste
        reduced_list = [[]]

        for i in range(0, nb_colonnes):
            reduced_list[0].append(
                str(self.variables[i]) + "\n" + str(self.type_var[i]))

        for i in range(nb_lignes):
            list_row = listes_donnees[i][: nb_colonnes]
            reduced_list.append(list_row)

        # Affichage
        print(
            "\n" + tabulate(tabular_data=reduced_list[1:],
                            headers=reduced_list[0],
                            tablefmt="psql",
                            floatfmt=".2f") + "\n")    # 2 decimales pour les float

    def determiner_formats(self):
        '''Méthode qui détermine le format de chaque colonne à partir des données

        Si la variable contient le mot date, le format de cette variable sera date
        Si la variable fait parti de la liste des identifiants, celle-ci reste de type str
        Si toutes les données d'une variable sont de type float, la variable sera de type float

        Returns
        -------
        liste_formats : list[str]
            liste de formats pour alimenter ensuite l'attribut type_var
        '''

        liste_formats = []

        for num_colonne in range(len(self.variables)):

            # si il y a le mot date dans le nom de la variable elle sera de type date
            if "date" in self.variables[num_colonne]:
                liste_formats.append('date')
                continue

            # si la variable est un identifiant elle reste de type str
            if self.variables[num_colonne] in self.identifiants:
                liste_formats.append('str')
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
#                liste_formats.append('int')
            if isFloat:
                liste_formats.append('float')
            else:
                liste_formats.append('str')

        return np.array(liste_formats)

    def appliquer_formats(self):
        '''Transforme en float les données des variables de type float
        '''
        for num_colonne in range(len(self.donnees[0])):
            if self.type_var[num_colonne] == "float":
                for num_ligne in range(len(self.donnees)):
                    self.donnees[num_ligne, num_colonne] = float(
                        self.donnees[num_ligne, num_colonne])

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Table de données : {}".format(self.nom)

    def index_variable(self, nom_variable):
        return np.where(self.variables == nom_variable)[0][0]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
