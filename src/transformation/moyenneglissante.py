'''
Module moyenneglissante
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 16/05/2022
Licence : Domaine public
Version : 1.0
'''

import numpy as np
from transformation.transformation import Transformation
import statistics


class MoyenneGlissante(Transformation):
    '''Moyenne glissante d'une ou plusieurs variables
    Attributes
        ----------
        liste_colonnes : list[str]
            liste des noms des colonnes auxquelles appliquer la transformation (colonnes de type "float")
        pas : int
            taille des sous-listes sur lesquelles on calcule la moyenne
    '''

    def __init__(self, liste_colonnes = "all", pas = 3):
        '''Constructeur de l'objet

        Parameters
        ----------
        liste_colonnes : list[str]
            liste des noms des colonnes auxquelles appliquer la transformation (colonnes de type "float")
        pas : int = 3
            taille des sous-listes sur lesquelles on calcule la moyenne
        '''
        self.liste_colonnes = liste_colonnes
        self.pas = pas

    @staticmethod
    def moyenne_glissante(table, numero_colonne, pas):
        '''Calculer la liste des moyennes glissantes d'une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer
        pas : int
        '''
        liste_valeurs = table.donnees[:, numero_colonne]
        liste_moyennes = []

        if pas % 2 == 1:  # cas impair
            demi_pas = int((pas-1) / 2)
        else:
            demi_pas = int(pas / 2)

        for i in range(demi_pas):
            liste_moyennes.append(np.nan)  # pour les premières valeurs (qui n'ont pas assez de lignes précédentes)
        for i in range(demi_pas, len(table.donnees) - demi_pas):
            ss_liste = liste_valeurs[i - demi_pas: i + demi_pas + 1]
            if pas % 2 ==0:
                print(ss_liste)
                ss_liste = np.delete(ss_liste, demi_pas, None) #suppresion de l'élément central de la sous-liste quand le pas est pair
                print(ss_liste)
            moyenne = statistics.mean(ss_liste) #renvoie une valeur manquante si la liste contient au moins une valeur manquante
            liste_moyennes.append(moyenne)
        for i in range(demi_pas):
            liste_moyennes.append(np.nan)  # pour les dernières valeurs (qui n'ont pas assez de lignes suivantes)

        return liste_moyennes

    def appliquer_variable(self, table, numero_colonne, pas):
        '''Appliquer la moyenne glissante à une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer
        pas : int
        '''
        liste_moyennes = MoyenneGlissante.moyenne_glissante(
            table, numero_colonne, pas)
        for i in range(len(table.donnees)):
            table.donnees[i][numero_colonne] = liste_moyennes[i]

    def appliquer(self, table):
        '''Appliquer la transformation à toutes les variables numériques de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        print("------------------------------------------------------")
        print("Moyenne glissante de la table " + table.nom)

        for num_col in range(len(table.variables)):
            if table.type_var[num_col] == "float" and ((table.variables[num_col] in self.liste_colonnes) or self.liste_colonnes == "all"):
                self.appliquer_variable(table, num_col, self.pas)
