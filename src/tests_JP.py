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
from transformation.supprimena import SupprimeNA
# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")



# -------------------------------------------------------------------
# Supprimer les lignes d'une table qui contiennent au moins une valeur manquante pour une liste de variables données
# -------------------------------------------------------------------

SupprimeNA(["vv","ww"]).appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)

# -------------------------------------------------------------------
# Creation manuelle d une table
# -------------------------------------------------------------------
ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille"],
                                 ["id1", "20120101", "160"],
                                 ["id2", "20060920", "180"]],
                        identifiants=["id"],
                        type_var=["str", "date", "float"])

ma_table.afficher(nb_lignes=10, nb_colonnes=7)

ma_table2 = TableDonnees(nom="t2",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                ["id1", "20120101", 160, "68"],
                                ["id2", "20060920", 180, 85],
                                ["id3", "20060921", 170, 70]],
                        identifiants=["id"])
#ma_table2.determiner_formats ne fonctionne pas
#print(ma_table2.type_var)

# -------------------------------------------------------------------
# Normaliser une table
# -------------------------------------------------------------------
Normalisation().appliquer(ma_table)
ma_table.afficher(nb_lignes=10, nb_colonnes=7)