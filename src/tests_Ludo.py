'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation


ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/synop.201301.csv",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


ma_table_csv_gz = DonneesCsv(nom="table_csv",
                             chemin_complet=os.getcwd() + "/donnees/synop.201301.csv.gz",
                             identifiants=['numer_sta', 'date'],
                             valeur_manquante="mq")

ma_table_csv_gz.afficher(nb_lignes=10,
                         nb_colonnes=12)
