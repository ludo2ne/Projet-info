import os
import numpy as np
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
from transformation.supprimena import SupprimeNA
from lienvar.coefficientcorrelation import CoefficientCorrelation

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
# Creation manuelle d une table
# -------------------------------------------------------------------
ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                             ["id1", 20120101, 160, 50],
                                             ["id2", 20060920, 180, 80],
                                             ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])


print(ma_table.index_variable("poids"))

print(ma_table.donnees[:, 2])


ma_liste = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ma_liste[3:5])


# -------------------------------------------------------------------
# Etude du lien entre 2 variables quantitatives
# -------------------------------------------------------------------
SupprimeNA(["ff", "tend"]).appliquer(ma_table_csv)


CoefficientCorrelation("ff", "tend").appliquer(
    ma_table_csv)  # TODO à debugger (autre version)

# -------------------------------------------------------------------
# Creation manuelle d une table TODO à debugger
# -------------------------------------------------------------------

ma_table2 = TableDonnees(nom="t2",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                              ["id1", "20120101", 160, 68],
                                              ["id2", "20060920", 180, 85],
                                              ["id3", "20060921", 170, 70]],
                         identifiants=["id"])
# bug pour ma_table2 à cause de appliquer.format() TODO ne fonctionne pas si type_var n'est pas prédéfinie, ou sil les variables sont déjà en partie de type float ?
# ma_table2.determiner_formats ne fonctionne pas ?
print(ma_table2.type_var)
