'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from transformation.moyenneglissante import MoyenneGlissante
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation
from lien2var.coefficientcorrelation import CoefficientCorrelation

# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)

# -------------------------------------------------------------------
# Creation et lancement du pipeline
# -------------------------------------------------------------------
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_transformations=[Centrage(),
                                                       SelectionVariables(['numer_sta', 'date', 'ff', 'w1', 'sw'])],
                                exporter_table=True)
mon_premier_pipeline.lancer(ma_table_csv)

ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)

# -------------------------------------------------------------------
# Creation manuelle d une table
# -------------------------------------------------------------------
ma_table = TableDonnees(nom="t1",
                        donnees=[["id", "dnais", "taille"],
                                ["id1", "20120101", "160"],
                                ["id2", "20060920", "180"]],
                        identifiants=["id"],
                        type_var=["str", "date", "float"])

ma_table.afficher(nb_lignes=10, nb_colonnes=7)

ma_table2 = TableDonnees(nom="t2",
                        donnees=[["id", "dnais", "taille", "poids"],
                                ["id1", "20120101", 160, "68"],
                                ["id2", "20060920", 180, 85],
                                ["id3", "20060921", 170, 70]],
                        identifiants=["id"])
ma_table2.determiner_formats
print(ma_table2.type_var)


# -------------------------------------------------------------------
# Normaliser une table
# -------------------------------------------------------------------
Normalisation().appliquer(ma_table)
ma_table.afficher(nb_lignes=10, nb_colonnes=7)



# -------------------------------------------------------------------
# Etude du lien entre 2 variables quantitatives
# -------------------------------------------------------------------
CoefficientCorrelation().representation(ma_table_csv,"pmer","tend")
CoefficientCorrelation().etude_lien(ma_table_csv,"pmer","tend")

# -------------------------------------------------------------------
# Moyennes glissantes d'une table
# -------------------------------------------------------------------
MoyenneGlissante().appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)