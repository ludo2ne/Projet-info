'''
Module exemple7_agregationspatiale
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 02/06/2022
Licence : Domaine public
Version : 1.0
'''

import os
from transformation.supprimena import SupprimeNA
from table.donneesjson import DonneesJson
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.agregationspatiale import AgregationSpatiale
from transformation.jointureinterne import JointureInterne
from transformation.filtre import Filtre
from lienvar.coefficientcorrelation import CoefficientCorrelation
from lienvar.temporel import Temporel
from transformation.concatenation import ConcatenationLignes
from transformation.export import Export
from estimateur.moyenne import Moyenne

# -------------------------------------------------------------------
# Jointure entre donnees meteo et electricite
<<<<<<< HEAD
# Sélections de quelques variables
# Agregation spatiale de régions à l'Ouest / + représentation série temporelle
=======
# Filtre sur 3 régions Nouvelle-Aquitaine, Occitanie, Bretagne
# Agregation spatiale
#   cumul : consommation_brute_electricite_rte
#   moyenne : temperature, humidite
# Temporel : Consommation électrique en fonction du temps
>>>>>>> 35e36b02a0a2bf0e5136304805e6f8b87beb2822
# -------------------------------------------------------------------

# ---------------------------------
# Import donnees electricite
# ---------------------------------

# Creation a partir d un fichier json
donnees_elec = DonneesJson(nom="electricit201301",
                           chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                           identifiants=["code_insee_region", "date", "heure"])

Filtre(variable="region", modalites=[
       "Nouvelle-Aquitaine", "Occitanie", "Bretagne"]).appliquer(donnees_elec)

# ---------------------------------
# Import donnees meteo
# ---------------------------------

# Creation a partir d un fichier csv
donnees_meteo = DonneesCsv(nom="meteo201301",
                           chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz",
                           identifiants=['numer_sta', 'date'],
                           valeur_manquante="mq")

# Renommage d'une variable peu explicite
donnees_meteo.variables[donnees_meteo.variables ==
                        "t"] = "temperature"
donnees_meteo.variables[donnees_meteo.variables ==
                        "ff"] = "vitesse_vent"
donnees_meteo.variables[donnees_meteo.variables ==
                        "u"] = "humidite"

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
                                             Filtre(variable="Region", modalites=[
                                                    "Nouvelle-Aquitaine", "Occitanie", "Bretagne"]),

                                             SelectionVariables(
                                                 liste_var=['numer_sta', 'date', 'Nom', 'Region', 'temperature', 'vitesse_vent']),
                                             JointureInterne(autre_table=donnees_elec, cle=[
                                                             ("Region", "region"), ("date", "date_heure")]),

                                             SelectionVariables(liste_var=[
<<<<<<< HEAD
                                                                'date', 'Region', 'temperature', 'vitesse_vent', 'consommation_brute_electricite_rte']),
                                             Moyenne(),

                                             SupprimeNA(
                                                 liste_var=['temperature', 'vitesse_vent', 'consommation_brute_electricite_rte']),
                                             AgregationSpatiale('date', 'Region', 'Ouest', liste_var_cum=['consommation_brute_electricite_rte'], liste_var_moy=['temperature', 'vitesse_vent']),

                                             Temporel(var1="date", var2="consommation_brute_electricite_rte", var3="temperature", titre="Consommation électrique en fonction du temps (Ouest)"),

                                             CoefficientCorrelation(var1="vitesse_vent", var2="consommation_brute_electricite_rte", var3="temperature", titre="Consommation électrique en fonction de la vitesse du vent (Ouest)")
=======
                                                                'date', 'Region', 'temperature', 'humidite', 'consommation_brute_electricite_rte']),
                                             SupprimeNA(
                                                 liste_var=['temperature', 'humidite', 'consommation_brute_electricite_rte']),
                                             AgregationSpatiale('date', 'Region', 'Ouest', liste_var_cum=[
                                                                'consommation_brute_electricite_rte'], liste_var_moy=['temperature', 'humidite']),

                                             Temporel(var1="date", var2="consommation_brute_electricite_rte",
                                                      var3="temperature", titre="Consommation électrique en fonction du temps (Ouest)")
>>>>>>> 35e36b02a0a2bf0e5136304805e6f8b87beb2822

                                             ])


mon_2e_pipeline.lancer(donnees_meteo)
donnees_meteo.bilan_chargement()
print(donnees_meteo.variables)
donnees_meteo.afficher()
