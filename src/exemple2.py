'''
Module exemple2
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.centrage import Centrage
from transformation.export import Export
from transformation.moyenneglissante import MoyenneGlissante

# -------------------------------------------------------------------
# Import d une table a partir d un fichier csv
# Selection de variables
# Moyenne Glissante
# Centrage
# Export
# -------------------------------------------------------------------


# Creation a partir d un fichier csv
ma_table_csv = DonneesCsv(
                          chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


# Creation et lancement du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_operations=[SelectionVariables(['numer_sta', 'date', 'pmer', 'tend', 'cod_tend', 'dd', 'ff', 't', 'vv', 'ww']),
                                                  MoyenneGlissante(pas=7),
                                                  Centrage(),
                                                  Export()])

mon_premier_pipeline.lancer(ma_table_csv)

ma_table_csv.afficher(nb_lignes=20,
                      nb_colonnes=12)
