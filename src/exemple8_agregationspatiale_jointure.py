'''
Module exemple7_agregationspatiale
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 28/05/2022
Licence : Domaine public
Version : 1.0
'''

import os
from transformation.supprimena import SupprimeNA
from table.donneesjson import DonneesJson
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.export import Export
from transformation.agregationspatiale import AgregationSpatiale
from transformation.jointureinterne import JointureInterne

# -------------------------------------------------------------------
# Jointure entre donnees meteo et electricite
# Sélections de quelques variables
# Agregation spatiale
# -------------------------------------------------------------------

# ---------------------------------
# Import donnees electricite
# ---------------------------------

# Creation a partir d un fichier json
donnees_elec = DonneesJson(nom="electricit201301",
                           chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                           identifiants=["code_insee_region", "date", "heure"])


# ---------------------------------
# Import donnees meteo
# ---------------------------------

# Creation a partir d un fichier csv
donnees_meteo = DonneesCsv(nom="meteo201301",
                           chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz",
                           identifiants=['numer_sta', 'date'],
                           valeur_manquante="mq")

# ---------------------------------
# Import table lien
# ---------------------------------

table_lien = DonneesCsv(nom="Region",
                        chemin_complet=os.getcwd() + "/donnees/geographiques/postesSynopAvecRegions.csv",
                        identifiants=['ID', 'Region'])


# Creation et lancement du pipeline
# relations entre température et electricite (et impact du vent)
mon_2e_pipeline = Pipeline(nom="pipo2",
                           liste_operations=[JointureInterne(autre_table=table_lien, cle=[("numer_sta", "ID")]),
                                             SelectionVariables(
                                                 liste_var=['numer_sta', 'date', 'Nom', 'Region', 't', 'u']),
                                             JointureInterne(autre_table=donnees_elec, cle=[
                                                             ("Region", "region"), ("date", "date_heure")]),
                                             SelectionVariables(liste_var=[
                                                                'date', 'Region', 't', 'u', 'consommation_brute_electricite_rte']),
                                             SupprimeNA(
                                                 liste_var=['t', 'u', 'consommation_brute_electricite_rte']),
                                             AgregationSpatiale('date', 'Region', 'national', liste_var_cum=['consommation_brute_electricite_rte'], liste_var_moy=['t', 'u'])])
# TODO attention il y a un pbm dans les noms de variables, ne correspondent pas aux données ><
mon_2e_pipeline.lancer(donnees_meteo)
donnees_meteo.bilan_chargement()
print(donnees_meteo.variables)
donnees_meteo.afficher()
