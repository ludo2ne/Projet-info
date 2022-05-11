'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.selectionvariables import SelectionVariables

# tests des fonctionnalités

ma_table = DonneesCsv(nom="table_test",
                      chemin_complet=os.getcwd() + "/donnees/synop.201301.csv.gz",
                      identifiants=['numer_sta', 'date'],
                      valeur_manquante="mq")

ma_table.afficher(nb_lignes=10,
                  nb_colonnes=15)

# Creation du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_transformations=[Centrage(),
                                                       SelectionVariables(['numer_sta', 'date', 'ff', 'w1', 'sw'])])
mon_premier_pipeline.lancer(ma_table)

ma_table.afficher(nb_lignes=10,
                  nb_colonnes=15)
