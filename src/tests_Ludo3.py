import os
import numpy as np
from estimateur.moyenne import Moyenne
from estimateur.ecarttype import EcartType
from table.tabledonnees import TableDonnees
from transformation.concatenation import ConcatenationLignes
from transformation.moyenneglissante import MoyenneGlissante
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.filtre import Filtre
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation
from transformation.jointureinterne import JointureInterne
from transformation.supprimena import SupprimeNA
from transformation.export import Export
from lienvar.coefficientcorrelation import CoefficientCorrelation


# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------


ma_table_csv_01 = DonneesCsv(nom="table_csv",
                             chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                             identifiants=['numer_sta', 'date'],
                             valeur_manquante="mq")

Export().appliquer(ma_table_csv_01)

SupprimeNA(["ff", "tend"]).appliquer(ma_table_csv_01)

ma_table_csv_01.afficher(nb_lignes=10,
                         nb_colonnes=12)


# -------------------------------------------------------------------
# Creation et lancement du pipeline
# -------------------------------------------------------------------
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_operations=[Centrage(),
                                                  SelectionVariables(
                                                      ['numer_sta', 'date', 'ff', 'w1', 'sw']),
                                                  Export()])
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

Filtre(variable="code_insee_region", modalites=[
    "24", "75"]).appliquer(ma_table_json)

Filtre(variable="date_heure", debut=20130101020000,
       fin=20130101033000).appliquer(ma_table_json)

Filtre(variable="consommation_brute_gaz_terega",
       modalites=[1760.0]).appliquer(ma_table_json)

ma_table_json.afficher(nb_lignes=15,
                       nb_colonnes=7)
