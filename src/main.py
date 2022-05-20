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
from lien2var.coefficientcorrelation_v2 import CoefficientCorrelationV2
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
                                                       SelectionVariables(
                                                           ['numer_sta', 'date', 'ff', 'w1', 'sw'])],
                                exporter_table=True)
mon_premier_pipeline.lancer(ma_table_csv_01)

ma_table_csv_01.afficher(nb_colonnes=12)
