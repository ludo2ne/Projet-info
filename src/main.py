'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
from table.tabledonnees import TableDonnees
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.selectionvariables import SelectionVariables


# tests des fonctionnalités

ma_table = TableDonnees(nom="table_test",
                        chemin_complet="P:/projet-info-sources/Projet-info/src/tests/donnees/synop.201301.csv.gz")

ma_table.afficher(nb_lignes=5,
                  nb_colonnes=15)


mon_centrage = Centrage(['ff', 't', 'xxxxx'])
ma_selection = SelectionVariables(['numer_sta', 'ff'])

mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_transformations=[mon_centrage, ma_selection])
mon_premier_pipeline.lancer(ma_table)

ma_table.afficher(nb_lignes=5,
                  nb_colonnes=15)
