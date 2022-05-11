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
                        chemin_complet="P:/projet-info-sources/Projet-info/donnees/synop.201301.csv.gz",
                        valeur_manquante="mq")

ma_table.afficher(nb_lignes=10, 
                  nb_colonnes=15)

# Creation du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_transformations=[Centrage(['ff', 't', 'xxxxx']),
                                                       SelectionVariables(['numer_sta', 'ff', 'w1'])])
mon_premier_pipeline.lancer(ma_table)

ma_table.afficher(nb_lignes=10,
                  nb_colonnes=15)
