import os
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.filtre import Filtre
from transformation.export import Export


# -------------------------------------------------------------------
# Import d une table a partir d un fichier json
# Filtre
# Selection de variables
# Export
# -------------------------------------------------------------------

# Creation a partir d un fichier json
ma_table_json = DonneesJson(nom="table_json",
                            chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                            identifiants=["code_insee_region", "date", "heure"])

ma_table_json.afficher(nb_lignes=15,
                       nb_colonnes=7)

# Renommage de deux variables aux noms un peu trop longs
ma_table_json.variables[ma_table_json.variables ==
                        "consommation_brute_electricite_rte"] = "conso_elec"
ma_table_json.variables[ma_table_json.variables ==
                        "consommation_brute_gaz_terega"] = "conso_gaz"

# Creation et lancement du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_operations=[Filtre(variable="code_insee_region", modalites=["24", "75"]),
                                                  Filtre(
                                                      variable="date_heure", debut=20130101020000, fin=20130101060000),
                                                  SelectionVariables(
                                                      ['region', 'date', 'heure', 'conso_gaz', 'conso_elec']),

                                                  Export()])

mon_premier_pipeline.lancer(ma_table_json)

ma_table_json.afficher(nb_lignes=15,
                       nb_colonnes=7)
