'''
Module exemple3
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.filtre import Filtre
from transformation.concatenation import ConcatenationLignes
from transformation.export import Export


# -------------------------------------------------------------------
# Import d une table a partir d un fichier json
# Mise en forme de 2 tables puis concatentation
# Filtre
# Selection de variables
# Concatenation avec la 2e table
# Export
# -------------------------------------------------------------------

# Creation a partir d un fichier json
ma_table_json_01 = DonneesJson(nom="table_json_01",
                               chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                               identifiants=["code_insee_region", "date", "heure"])

ma_table_json_01.afficher(nb_lignes=15,
                          nb_colonnes=7)

# Renommage de deux variables aux noms un peu trop longs
ma_table_json_01.variables[ma_table_json_01.variables ==
                           "consommation_brute_electricite_rte"] = "conso_elec"
ma_table_json_01.variables[ma_table_json_01.variables ==
                           "consommation_brute_gaz_terega"] = "conso_gaz"

# Creation et lancement du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_operations=[Filtre(variable="code_insee_region", modalites=["24", "75"]),
                                                  Filtre(
                                                      variable="date_heure", debut=20130101020000, fin=20130101040000),
                                                  SelectionVariables(
                                                      ['region', 'date', 'heure', 'conso_gaz', 'conso_elec'])])

mon_premier_pipeline.lancer(ma_table_json_01)

ma_table_json_01.afficher(nb_lignes=20,
                          nb_colonnes=7)


# -------------------------------------------------------------------
# Import d une seconde table a partir d un fichier json
# -------------------------------------------------------------------
ma_table_json_02 = DonneesJson(nom="table_json_02",
                               chemin_complet=os.getcwd() + "/donnees/electricite/2013-02.json.gz",
                               identifiants=["code_insee_region", "date", "heure"])


# Renommage de deux variables aux noms un peu trop longs
ma_table_json_02.variables[ma_table_json_02.variables ==
                           "consommation_brute_electricite_rte"] = "conso_elec"
ma_table_json_02.variables[ma_table_json_02.variables ==
                           "consommation_brute_gaz_terega"] = "conso_gaz"


ma_table_json_02.afficher(nb_lignes=30,
                          nb_colonnes=7)

# Creation et lancement du pipeline
mon_2e_pipeline = Pipeline(nom="pipo2",
                           liste_operations=[Filtre(variable="code_insee_region", modalites=["24", "75"]),
                                             Filtre(
                                                 variable="date_heure", debut=20130201020000, fin=20130201040000),
                                             SelectionVariables(
                                                 ['region', 'date', 'heure', 'conso_gaz', 'conso_elec']),
                                             ConcatenationLignes(
                                                 ma_table_json_01),
                                             Export()])

mon_2e_pipeline.lancer(ma_table_json_02)

ma_table_json_02.afficher(nb_colonnes=7)
