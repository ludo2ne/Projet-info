'''
Module agregationspatialE
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 17/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from src.table.tabledonnees import TableDonnees
from transformation.transformation import Transformation


class AgregationSpatiale(Transformation):
    '''Agrégation vers un échelon plus vaste
    '''

    def __init__(self, echelon):
        '''Constructeur de l'objet

        Attributes
        ----------
        echelon : str
        '''
        self.echelon = echelon

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        #TODO

        #algorithme (brouillon) :
        #1ere étape : à partir d'une table_station qui associe une variable num_stat à une region,
        # créer une liste de listes qui contient une 1ere liste entête avec chaque nom de régions (sans doublon)
        # puis pour chaque région une liste de liste de numéro de station (éventuellement sans doublons)
        #
        # 2ème étape : dans la table.donnees extraire une sous-matrice des données de type numérique pour chaque date et pour chaque liste de station d'une même région
        # pour une région et une date, calculer la moyenne de chaque variable numerique

        #la table récupérée (en sortie) aura la même structure que table.donnee mais avec une variable region à la place de la variable num_stat
