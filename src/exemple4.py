'''
Module exemple4
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from table.donneesjson import DonneesJson
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.filtre import Filtre
from transformation.jointureinterne import JointureInterne
from transformation.export import Export


# -------------------------------------------------------------------
# Jointure entre donnees meteo et electricite
# Filtre sur une region pour plus de rapidite
# -------------------------------------------------------------------

# ---------------------------------
# Import donnees electricite
# ---------------------------------

# Creation a partir d un fichier json
donnees_elec = DonneesJson(nom="table_json_01",
                               chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                               identifiants=["code_insee_region", "date", "heure"])


# Renommage de deux variables aux noms un peu trop longs
donnees_elec.variables[donnees_elec.variables ==
                       "consommation_brute_electricite_rte"] = "conso_elec"
donnees_elec.variables[donnees_elec.variables ==
                       "consommation_brute_gaz_terega"] = "conso_gaz"

donnees_elec.afficher(nb_lignes=15,
                      nb_colonnes=5)

# Creation et lancement du pipeline
mon_premier_pipeline = Pipeline(nom="pipo",
                                liste_operations=[Filtre(variable="region", modalites=["Hauts-de-France"])])

mon_premier_pipeline.lancer(donnees_elec)


# ---------------------------------
# Import donnees meteo
# ---------------------------------

# Creation a partir d un fichier csv
donnees_meteo = DonneesCsv(nom="table_csv",
                           chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz",
                           identifiants=['numer_sta', 'date'],
                           valeur_manquante="mq")

donnees_meteo.afficher(nb_lignes=10,
                       nb_colonnes=12)

# ---------------------------------
# Import table lien
# ---------------------------------

table_lien = DonneesCsv(nom="table_posteSynopAvecRegion",
                        chemin_complet=os.getcwd() + "/donnees/geographiques/postesSynopAvecRegions.csv",
                        identifiants=['ID', 'Region'])


# Creation et lancement du pipeline
mon_2e_pipeline = Pipeline(nom="pipo2",
                           liste_operations=[JointureInterne(table_lien, [("numer_sta", "ID")]),
                                             Filtre(variable="Region", modalites=[
                                                    "Hauts-de-France"]),
                                             Export(),
                                             JointureInterne(
                                                 donnees_elec, [("Region", "region"), ("date", "date_heure")]),
                                             Export()])

mon_2e_pipeline.lancer(donnees_meteo)
