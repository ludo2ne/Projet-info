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

    Attributes
        ----------
        echelon : str
        table_correspondance : TableDonnees
    '''

    def __init__(self, echelon, table_correspondance):
        '''Constructeur de l'objet

        Parameters
        ----------
        echelon : str
        table_correspondance : TableDonnees
        '''
        self.echelon = echelon
        self.table_correspondance = table_correspondance

    def appliquer(self, table):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        # TODO il faudrait voir un peu plus la "tête"  des tables et de la table d'association (région/station) pour comprendre la mise en oeuvre

        # algorithme (brouillon) :
        # 1ere étape : à partir d'une table_station qui associe une variable num_stat à une region,
        # créer une liste (entête) qui contient chaque nom de régions (sans doublon)
        #  une liste de [ liste de numéros de station (éventuellement sans doublons) pour une région ] par région
        #
        # 2ème étape : dans la table.donnees extraire une sous-matrice des données de type numérique pour chaque date et pour chaque liste de station d'une même région
        # pour une région et une date, calculer la moyenne de chaque variable numerique : recuperer cette liste et la mettre (append) dans une liste de donnees

        # la table récupérée (en sortie) aura la même structure que table.donnees mais avec une variable region à la place de la variable num_stat ,
        # il n'y aura pas de doublons des couples d'identifiants (region, date)
