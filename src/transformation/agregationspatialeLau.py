'''
Module agregationspatialE
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''

import doctest
from src.table.tabledonnees import TableDonnees
from transformation.transformation import Transformation


class AgregationSpatialeLau(Transformation):
    '''Agrégation vers un échelon plus vaste

    Attributes
        ----------
        echelon : str
            nom de la variable d'agrégation dont on va regrouper les modalités
        type_agregation : str
            type d'agrégation : 'moyenne' ou 'cumul'
        table_correspondance : TableDonnees
    '''

    def __init__(self, echelon, type_agregation='cumul', table_correspondance=None):
        '''Constructeur de l'objet

        Parameters
        ----------
        echelon : str
        table_correspondance : TableDonnees
        '''
        self.echelon = echelon
        self.type_agregation = type_agregation
        self.table_correspondance = table_correspondance

    def appliquer(self, table, var_tri=None):
        '''Appliquer la transformation à la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        var_tri : str
            nom de la variable selon laquelle va se faire l'agrégation
        '''
        # vérfiier que var_tri est une variable de table

        liste_tri = set(var_tri)
        for modalite in liste_tri:  # pour chaque date

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
