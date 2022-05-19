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
from transformation.concatenation import ConcatanationLignes
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation

from transformation.moyenneglissante import MoyenneGlissante
from lien2var.coefficientcorrelation import CoefficientCorrelation
from transformation.supprimena import SupprimeNA

# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv_01 = DonneesCsv(nom="table_csv",
                             chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                             identifiants=['numer_sta', 'date'],
                             valeur_manquante="mq")

ma_table_csv_01.afficher(nb_lignes=10,
                         nb_colonnes=12)

ma_table_csv_02 = DonneesCsv(nom="table_csv",
                             chemin_complet=os.getcwd() + "/donnees/test/synop.201302.csv",
                             identifiants=['numer_sta', 'date'],
                             valeur_manquante="mq")

# -------------------------------------------------------------------
# Creation et lancement du pipeline
# -------------------------------------------------------------------
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_transformations=[Centrage(),
                                                       ConcatanationLignes(
                                                           ma_table_csv_02),
                                                       SelectionVariables(['numer_sta', 'date', 'ff', 'w1', 'sw'])],
                                exporter_table=True)
mon_premier_pipeline.lancer(ma_table_csv_01)

ma_table_csv_01.afficher(nb_colonnes=12)


# -------------------------------------------------------------------
# Creation a partir d un fichier json
# -------------------------------------------------------------------
ma_table_json = DonneesJson(nom="table_json",
                            chemin_complet=os.getcwd() + "/donnees/test/2013-01.json.gz",
                            identifiants=["code_insee_region", "date", "heure"])

ma_table_json.afficher(nb_lignes=10,
                       nb_colonnes=7)


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


# -------------------------------------------------------------------
# Normaliser une table
# -------------------------------------------------------------------
Normalisation().appliquer(ma_table)
ma_table.afficher(nb_lignes=10, nb_colonnes=7)
