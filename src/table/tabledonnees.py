'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import numpy as np
from tabulate import tabulate


class TableDonnees:
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

    def __init__(self, nom, donnees_avec_entete, identifiants=[], type_var=[], valeur_manquante=None):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            nom de la table
        donnees_avec_entete : numpy array
            données rangées dans un numpy array
            la première ligne contient les entêtes de colonnes (attribut variables)
            le reste du tableau comporte les données (attribut donnees)
        identifiants : list[str]
            liste des noms de variables étant des identifiants
            [] par défaut
        type_var : numpy array
            type des variables
            [] par défaut
        valeur_manquante : str
            indique par quelle chaine de caractères sont représentées les valeurs manquantes
            None par défaut
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

            self.donnees[self.donnees == valeur_manquante] = np.nan

            if type_var != []:
                self.type_var = np.array(type_var, dtype=object)
            else:
                self.type_var = self.determiner_formats()

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

        # Codé initialement pour des listes : Pour eviter de tout refaire conversion du numpy array en liste de listes
        listes_donnees = self.donnees.tolist()

        # Si nb_lignes ou nb_colonnes ne sont pas précisés
        # OU si est demandé moins de lignes/colonnes qu'existant
        # ==> affichage de toutes les lignes/colonnes
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

    def __str__(self):
        return "{}".format(self.afficher())

    def determiner_formats(self):
        '''Méthode qui détermine le format de chaque colonne à partir des données

        Si la variable contient le mot date, le format de cette variable sera date
        Si la variable fait partie de la liste des identifiants, celle-ci reste de type str
        Si toutes les données d'une variable sont de type float, la variable sera de type float

        Returns
        -------
        liste_formats : numpy array 1D
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

            # on va maintenant tester si la variable est un float
            isFloat = True

            for num_ligne in range(len(self.donnees)):
                try:
                    float(self.donnees[num_ligne, num_colonne])
                except:
                    isFloat = False
                    break

            if isFloat:
                liste_formats.append('float')
            else:
                liste_formats.append('str')

        return np.array(liste_formats)

    def appliquer_formats(self):
        '''Transforme les données des variables en fonction du type
               date => YYYYMMDD
               "float" (float au format str) => float
        '''

        for num_colonne in range(len(self.donnees[0])):
            # transformation des float
            if self.type_var[num_colonne] == "float":
                for num_ligne in range(len(self.donnees)):
                    self.donnees[num_ligne, num_colonne] = float(
                        self.donnees[num_ligne, num_colonne])

    def index_variable(self, nom_variable):
        '''Retourne l'index de la colonne de la variable
           None si la variable n'a pas été trouvée
        Parameters :
        ----------
        nom_variable : str
        '''
        liste_index = np.where(self.variables == nom_variable)[0]
        return None if len(liste_index) == 0 else liste_index[0]

    def compte_na(self, nom_variable):
        '''Retourne le nombre de valeurs manquante d'une variable
        Parameters :
        ----------
        nom_variable : str

        Returns :
        ----------
        nb_na : int
        '''
        nb_na = 0
        num_colonne = self.index_variable(nom_variable = nom_variable)
        for i in range(len(self.donnees)):
            if type(self.donnees[i][num_colonne]) != str:
                if np.isnan(self.donnees[i][num_colonne]): #la methode np.isnan() ne s'applique pas sur une chaine de caractère
                    nb_na += 1
        return nb_na

    def liste_var_float(self):
        '''Retourne la liste des variables numériques, c'est à dire de type float
        Returns :
        --------
        liste_var : list [str]
        '''
        liste_var = []
        for i in range(len(self.variables)):
            if self.type_var[i] == "float":
                liste_var.append(self.variables[i])
        return liste_var

    def liste_var_na(self,freqNA):
        '''retourne la liste des variables qui ont moins d'une certain fréquence de valeurs manquantes
        Parameters :
        -----------
        freqNA : float
            fréquence (proportion en 0 et 1) de valeurs manquantes maximale autorisées pour une variable
        Returns :
        liste_var : list[str]
        '''
        liste_var = []
        n=len(self.donnees)
        if n == 0 :
            print("attention, la table est vide")
        for var in self.variables:
            freq = self.compte_na(var) / n
            if freq <= freqNA:
                liste_var.append(var)
        return liste_var
