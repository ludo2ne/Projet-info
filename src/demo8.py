'''
Module exemple4_etude1
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from transformation.supprimena import SupprimeNA
from table.donneesjson import DonneesJson
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.filtre import Filtre
from transformation.jointureinterne import JointureInterne
from transformation.export import Export
from lienvar.coefficientcorrelation import CoefficientCorrelation


# -------------------------------------------------------------------
# Consommation de gaz en fonction de la température
#   janvier 2013
#   Montpellier
# -------------------------------------------------------------------

# ---------------------------------
# Import donnees electricite
# ---------------------------------

mois = "01"

# Creation a partir d un fichier json
donnees_elec = DonneesJson(nom="electricit201301",
                           chemin_complet=os.getcwd() + "/donnees/electricite/2013-" + mois + ".json.gz",
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
                                liste_operations=[Filtre(variable="region", modalites=["Occitanie"])])

mon_premier_pipeline.lancer(donnees_elec)


# ---------------------------------
# Import donnees meteo
# ---------------------------------

# Creation a partir d un fichier csv
donnees_meteo = DonneesCsv(nom="meteo201301",
                           chemin_complet=os.getcwd() + "/donnees/meteo/synop.2013" + mois + ".csv.gz",
                           identifiants=['numer_sta', 'date'],
                           valeur_manquante="mq")

# Renommage d'une variable peu explicite
donnees_meteo.variables[donnees_meteo.variables ==
                        "t"] = "temperature"
donnees_meteo.variables[donnees_meteo.variables ==
                        "ff"] = "vitesse_vent"

donnees_meteo.afficher(nb_lignes=10,
                       nb_colonnes=12)

# ---------------------------------
# Import table lien
# ---------------------------------

table_lien = DonneesCsv(nom="Region",
                        chemin_complet=os.getcwd() + "/donnees/geographiques/postesSynopAvecRegions.csv",
                        identifiants=['ID', 'Region'])


annuel = DonneesCsv(nom="annuel",
                    chemin_complet=os.getcwd() + "/donnees/exports/annuel.csv",
                    identifiants=['numer_sta', 'date'],
                    valeur_manquante="nan")

# Creation et lancement du pipeline
# relations entre température et electricite (et impact du vent)
mon_2e_pipeline = Pipeline(nom="pipo2",
                           liste_operations=[JointureInterne(autre_table=table_lien, cle=[("numer_sta", "ID")]),
                                             Filtre(variable="Region",
                                                    modalites=["Occitanie"]),
                                             Filtre(variable="Nom",
                                                    modalites="MONTPELLIER"),
                                             JointureInterne(
                                                 autre_table=donnees_elec, cle=[("Region", "region"), ("date", "date_heure")]),
                                             Filtre(variable="heure",
                                                    modalites="12:00"),
                                             CoefficientCorrelation(var1="temperature", var2="conso_gaz",
                                                                    titre="Consommation gaz en fonction de la température"),
                                             Export()])

mon_2e_pipeline.lancer(donnees_meteo)
