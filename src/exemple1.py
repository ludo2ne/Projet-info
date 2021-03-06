'''
Module exemple1
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation
from transformation.export import Export
from transformation.supprimena import SupprimeNA

# -------------------------------------------------------------------
# Import d une table a partir d un fichier csv
# Selection de variables
# Normalisation
# Suppression des NA sur la variable w1
# Export
# -------------------------------------------------------------------


# Creation a partir d un fichier csv
ma_table_csv = DonneesCsv(
                          chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

# Affichage de 10 lignes et 12 colonnes
ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


# Creation et lancement du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_operations=[SelectionVariables(['numer_sta', 'date', 'pmer', 'ff', 'vv', 'ww', 'w1']),
                                                  Normalisation(),
                                                  SupprimeNA(['w1']),
                                                  Export()])

# Lancement du pipeline
mon_premier_pipeline.lancer(ma_table_csv)

# Affichage de 10 colonnes
ma_table_csv.afficher(nb_lignes=10)
