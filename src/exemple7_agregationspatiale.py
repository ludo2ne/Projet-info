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
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.export import Export
from transformation.agregationspatiale import AgregationSpatiale


# ----------------------------------------------------------------------------
# Import d'une table JSON
# Sélection des variables
# SupprimeNA
# Agrégation spatiale par date
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Import d'une table JSON : données d'électricité pour le mois de janvier 2013
# ----------------------------------------------------------------------------
donnees_elec1 = DonneesJson(nom="electricit201301",
                            chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                            identifiants=["code_insee_region", "date", "heure"])
# Export().appliquer(donnees_elec1)

# ----------------------------------------------------------------------------
# Définition du Pipeline
# ----------------------------------------------------------------------------

pipeline_agregation1 = Pipeline(nom="pipeline_agreg",
                                liste_operations=[SelectionVariables(liste_var=['consommation_brute_electricite_rte', 'date', 'region']),
                                                  SupprimeNA(
                                                      liste_var=['consommation_brute_electricite_rte']),
                                                  AgregationSpatiale('date', 'region', 'national', ['consommation_brute_electricite_rte'])])

pipeline_agregation1.lancer(donnees_elec1)
print(donnees_elec1)
