'''
Module exemple6_etude3
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 27/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from table.donneesjson import DonneesJson
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.filtre import Filtre
from transformation.jointureinterne import JointureInterne
from transformation.export import Export
from lienvar.temporel import Temporel
from transformation.moyenneglissante import MoyenneGlissante


# -------------------------------------------------------------------
# Jointure entre donnees meteo et electricite
# Filtre sur la région Hauts de France
# Température en fonction du temps
# Conso_elec en fonction du temps
# Moyenne glissante sur conso_elec puis affichage en fonction du temps
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
                                liste_operations=[Filtre(variable="region", modalites=["Hauts-de-France"])])

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


# Creation et lancement du pipeline
# observation des tendances
mon_2e_pipeline = Pipeline(nom="pipo2",
                           liste_operations=[JointureInterne(table_lien, [("numer_sta", "ID")]),
                                             Filtre(variable="Region", modalites=[
                                                    "Hauts-de-France"]),  # appliquer éventuellement un filtre temporel
                                             JointureInterne(
                                                 donnees_elec, [("Region", "region"), ("date", "date_heure")]),
                                             Export(),
                                             Temporel(var1="date", var2="temperature", var3="numer_sta",
                                                      titre="Temperature en fonction du temps (Hauts-de-France)"),
                                             Temporel(var1="date", var2="conso_elec", var3="numer_sta",
                                                      titre="Consommation électrique en fonction du temps (Hauts-de-France)"),
                                             MoyenneGlissante(
                                                 liste_colonnes=["conso_elec"], pas=15),
                                             Temporel(var1="date", var2="conso_elec", var3="numer_sta", titre="Consommation électrique en fonction du temps (Hauts-de-France)")])

mon_2e_pipeline.lancer(donnees_meteo)
