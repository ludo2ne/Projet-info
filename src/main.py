'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
from table.tabledonnees import TableDonnees
from transformation.centrage import Centrage


# tests des fonctionnalités

data = TableDonnees(nom="table_test",
                    chemin_complet="C:/Users/Ludo/Downloads/Projet info/src/tests/donnees/synop.201301.csv.gz")

data.afficher(nb_lignes=5,
              nb_colonnes=15)

Centrage.appliquer(table=data, numero_colonne=6)

data.afficher(nb_lignes=5,
              nb_colonnes=15)
