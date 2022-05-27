import os
import numpy as np
from estimateur.moyenne import Moyenne
from estimateur.ecarttype import EcartType
from table.tabledonnees import TableDonnees
from transformation.concatenation import ConcatenationLignes
from transformation.moyenneglissante import MoyenneGlissante
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.filtre import Filtre
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation
from transformation.jointureinterne import JointureInterne
from transformation.supprimena import SupprimeNA
from transformation.export import Export
from lienvar.coefficientcorrelation import CoefficientCorrelation


# -----------------------------------------------------------------------------------------------
# Test :
# Etape 1 :  charger la table posteSynopAvecRegion.csv  (chargement classique de tableDonneesCSV)
# Etape 2 :  chargement d'une table meteo et d'une table électricité
# E ETape 3 : faire la jointure entre les trois avec JointureInterne
# -----------------------------------------------------------------------------------------------

# Etape 1 :
table_lien = DonneesCsv(nom="table_posteSynopAvecRegion",
                        chemin_complet=os.getcwd() + "/donnees/geographiques/postesSynopAvecRegions.csv")
# print(table_lien.variables)
#table_lien.afficher(nb_lignes=10, nb_colonnes=10)


# Etape 2 :
# table météo :
table_meteo = DonneesCsv(nom="table_meteo",
                         chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz")

# print(table_meteo.variables)
#table_meteo.afficher(nb_lignes=100, nb_colonnes=10)
# print(table_meteo.index_variable('date'))

# table electricité:
table_elec = DonneesJson(nom="table_elec",
                         chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz")

#table_elec.afficher(nb_lignes=10, nb_colonnes=7)
# print(table_meteo.index_variable('date'))

# Etape 3:

# Jointure table_lien avec table_meteo (clé [("ID", "numer_sta")]) et table_elec (clé [("Region", "region")])

table_jointe = table_lien
jointure1 = JointureInterne(table_meteo, [("ID", "numer_sta")])
jointure1.appliquer(table_jointe)
table_jointe.bilan_chargement()
jointure2 = JointureInterne(
    table_elec, [("Region", "region"), ("date", "date")])
jointure2.appliquer(table_jointe)

print(table_jointe.variables)
table_jointe.bilan_chargement()
#table_jointe.afficher(nb_lignes=10, nb_colonnes=10)
# ne marche pas TODO à corriger
