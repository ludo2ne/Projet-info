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
from transformation.filtre import Filtre
from transformation.concatenation import ConcatenationLignes
from transformation.export import Export
from transformation.agregationspatialeLau import AgregationSpatialeLau

#
# -------------------------------------------------------------------
# Import d'une table JSON
# Sélection des variables
# SupprimeNA
# Agrégation spatiale par date
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Import de deux tables JSON
# -------------------------------------------------------------------
donnees_elec1 = DonneesJson(nom="electricit201301",
                            chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz",
                            identifiants=["code_insee_region", "date", "heure"])
# Export().appliquer(donnees_elec1)

# -------------------------------------------------------------------
# Sélection des variables
# -------------------------------------------------------------------
SelectionVariables(liste_var=[
                   'consommation_brute_electricite_rte', 'date', 'region']).appliquer(donnees_elec1)

# -------------------------------------------------------------------
# SupprimeNA
# -------------------------------------------------------------------
SupprimeNA(liste_var=['consommation_brute_electricite_rte']
           ).appliquer(donnees_elec1)
# donnees_elec1.bilan_chargement()

# -------------------------------------------------------------------
# Agrégation spatiale par date
# -------------------------------------------------------------------
AgregationSpatialeLau('date', 'region', 'national', [
                      'consommation_brute_electricite_rte']).appliquer(donnees_elec1)
