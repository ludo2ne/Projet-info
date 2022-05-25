import os
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation
from transformation.export import Export
from transformation.supprimena import SupprimeNA

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
                                liste_operations=[SelectionVariables(['numer_sta', 'date', 'pmer', 'ff', 'ww', 'w1']),
                                                  Normalisation(),
                                                  SupprimeNA(['w1']),
                                                  Export()])

mon_premier_pipeline.lancer(ma_table_csv)

ma_table_csv.afficher(nb_lignes=20,
                      nb_colonnes=12)
