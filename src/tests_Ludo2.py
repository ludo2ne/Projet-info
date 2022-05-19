import os
import numpy as np
from estimateur.moyenne import Moyenne
from table.tabledonnees import TableDonnees
from transformation.concatenation import ConcatanationLignes
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
from lien2var.coefficientcorrelation_v2 import CoefficientCorrelationV2

# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------

ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


# -------------------------------------------------------------------
# tests tranformations
# -------------------------------------------------------------------

SupprimeNA(["vv", "numer_sta"]).appliquer(ma_table_csv)
# TODO ajouter un test si la colonne n'est pas de type float

ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


# Normalisation().appliquer(ma_table_csv)
#print(Moyenne.estim1var(ma_table_csv, 2))
#
# ma_table_csv.afficher(nb_lignes=10,
#                      nb_colonnes=12)
