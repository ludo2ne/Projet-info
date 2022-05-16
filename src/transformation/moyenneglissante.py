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
    '''

    def __init__(self):
        '''Constructeur de l'objet

        Attributes
        ----------
        liste_colonnes : list[str]
            liste des noms des colonnes auxquelles appliquer la transformation (colonnes de type "float")
        '''
        pass
# est-ce que la liste_colonnes est vraiment un attribut la classe de MoyenneGlissante ? si oui l'ajouter sur l'UML, sinon le supprimer de la documentation TODO

    # table.donnees[:, numero_colonne]
    def liste_colonne(self, table, numero_colonne):
        '''converti les données d'une colonne de la table en une liste'''
        liste = []
        for i in range(len(table.donnees)):
            liste.append(table.donnees[i][numero_colonne])
        return liste  # cette méthode sera utile pour la classe Lien2Var : est-ce qu'il vaut mieux la  mettre en méthode de TableDonnées ? #TODO

    # liste[debut:fin]
    def sous_liste(self, liste, debut, fin):
        '''extrait une sous liste'''
        ss_list = []
        for i in range(debut, fin+1):
            ss_list.append(liste[i])
        return ss_list

    def moyenne_glissante(self, table, numero_colonne, pas):
        '''Calculer la liste des moyennes glissantes à d'une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer
        '''
        liste_valeurs = self.liste_colonne(table, numero_colonne)
        liste_moyennes = []

        if pas % 2 == 1:  # cas impair

            demi_pas = int((pas-1) / 2)

            for i in range(demi_pas):
                liste_moyennes.append("na")  # pour les premières valeurs
            for i in range(demi_pas, len(table.donnees)-demi_pas+1):
                ss_liste = self.sous_liste(
                    liste_valeurs, i-demi_pas, i+demi_pas)
                if not np.isnan(ss_liste):
                    moyenne = statistics.mean(ss_liste)
                else:
                    moyenne = "na"
                liste_moyennes.append(moyenne)
            for i in range(demi_pas):
                liste_moyennes.append("na")  # pour les dernières valeurs

        if pas % 2 == 0:  # cas pair
            for i in range(pas/2):
                liste_moyennes.append("na")  # pour les premières valeurs
            for i in range(pas/2, len(table.donnees)-pas/2+1):
                ss_liste = self.sous_liste(liste_valeurs, i-pas/2, i+pas/2)
                ss_liste.pop(i)
                if not np.isnan(ss_liste):
                    moyenne = statistics.mean(ss_liste)
                else:
                    moyenne = "na"
                liste_moyennes.append(moyenne)
            for i in range(pas/2):
                liste_moyennes.append("na")  # pour les dernières valeurs

        return liste_moyennes

    def appliquer_variable(self, table, numero_colonne, pas=3):
        '''Appliquer la moyenne glissante à une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer
        '''
        liste_moyennes = self.moyenne_glissante(table, numero_colonne, pas)
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
            if table.type_var[num_col] == "float":
                self.appliquer_variable(table, num_col)
