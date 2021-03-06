'''
Module exemple5_etude2
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
from lienvar.coefficientcorrelation import CoefficientCorrelation
from lienvar.anova import Anova


# -------------------------------------------------------------------
# Jointure entre donnees meteo et electricite
<<<<<<< HEAD
# Filtre sur une region pour plus de rapidite
# Etude de lien avec la région (dont Boxplot)
=======
# Filtre sur 3 régions : Bretagne, Occitanie, Grand Est
# Anova : Boxplot de la consommation électrique par région
# Anova : Boxplot de la consommation électrique par région
# Correlation : Consommation électrique en fonction de la température
>>>>>>> 35e36b02a0a2bf0e5136304805e6f8b87beb2822
# -------------------------------------------------------------------

# ---------------------------------
# Import donnees electricite
# ---------------------------------

# Creation a partir d un fichier json
donnees_elec = DonneesJson(nom="electricit201301",
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
                                liste_operations=[Filtre(variable="region", modalites=["Bretagne", "Occitanie", "Grand Est"])])

mon_premier_pipeline.lancer(donnees_elec)


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

donnees_meteo.afficher(nb_lignes=10,
                       nb_colonnes=12)

# ---------------------------------
# Import table lien
# ---------------------------------

table_lien = DonneesCsv(nom="Region",
                        chemin_complet=os.getcwd() + "/donnees/geographiques/postesSynopAvecRegions.csv",
                        identifiants=['ID', 'Region'])


# Creation et lancement du pipeline  (2ème jointure un peu lente : patience...)
# observation des disparités régionales
mon_2e_pipeline = Pipeline(nom="pipo2",
                           liste_operations=[JointureInterne(table_lien, [("numer_sta", "ID")]),
                                             Filtre(variable="Region", modalites=[
                                                    "Bretagne", "Occitanie", "Grand Est"]),
                                             JointureInterne(
                                                 donnees_elec, [("Region", "region"), ("date", "date_heure")]),
                                             SupprimeNA(
                                                 liste_var=["temperature", "conso_elec", "vitesse_vent", "Region"]),
                                             Anova(
                                                 var1="Region", var2="conso_elec", titre="Boxplot de la consommation électrique par région"),
                                             Anova(
                                                 var1="Region", var2="temperature", titre="Boxplot de la température par région"),
                                             CoefficientCorrelation(var1="temperature", var2="conso_elec", var3="code_insee_region", titre="Consommation électrique en fonction de la température")])

mon_2e_pipeline.lancer(donnees_meteo)
