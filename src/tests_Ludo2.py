import os
import numpy as np
from estimateur.moyenne import Moyenne
from estimateur.ecarttype import EcartType
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
from transformation.jointureinterne import JointureInterne
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
# Creation et lancement du pipeline
# -------------------------------------------------------------------
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_transformations=[SelectionVariables(['numer_sta', 'date', 'pmer', 'w1', 'sw']),
                                                       Normalisation()],
                                exporter_table=True)
mon_premier_pipeline.lancer(ma_table_csv)


print(Moyenne.estim1var(ma_table_csv, 2))
print(EcartType.estim1var(ma_table_csv, 2))

# -------------------------------------------------------------------
# tests tranformations
# -------------------------------------------------------------------

# SupprimeNA(["vv", "numer_sta"]).appliquer(ma_table_csv)


ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id",  "matricule", "dnais",    "taille"],
                                             ["id1", "A",         "20120101", "160"],
                                             ["id2", "B",         "20060920", "180"],
                                             ["id3", "C",         "20060920", "na"],
                                             ["id4", "D",         "20010525", "165"]],
                        identifiants=["id", "matricule"],
                        type_var=["str", "str", "date", "float"],
                        valeur_manquante="na")

ma_table_emploi = TableDonnees(nom="t1bis",
                               donnees_avec_entete=[["ident", "code", "emploi"],
                                                    ["id2", "B", "statisticien"],
                                                    ["id1", "Z", "informaticien"],
                                                    ["id3", "C", "prof"]],
                               identifiants=["ident", "code"],
                               type_var=["str", "str", "str"],
                               valeur_manquante="na")

JointureInterne(autre_table=ma_table_emploi,
                cle=[("id", "ident"), ("matricule", "code")]).appliquer(ma_table)


ma_table.afficher(nb_lignes=10, nb_colonnes=7)
