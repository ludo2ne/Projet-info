import os
import numpy as np
from estimateur.moyenne import Moyenne
from estimateur.ecarttype import EcartType
from table.tabledonnees import TableDonnees
from transformation.concatenation import ConcatanationLignes
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
# table_posteSynopAvecRegion.afficher()

# Etape 2 :
# table météo :
table_meteo = DonneesCsv(nom="table_meteo",
                         chemin_complet=os.getcwd() + "/donnees/meteo/synop.201301.csv.gz")
# print(table_meteo.variables)
#table_meteo.afficher(nb_lignes=10, nb_colonnes=15)

# table electricité:
# table_elec = DonneesJson(nom="table_elec",
#                         chemin_complet=os.getcwd() + "/donnees/electricite/2013-01.json.gz")

#table_elec.afficher(nb_lignes=10, nb_colonnes=7)

# Etape 3:

# Jointure table_lien avec table_meteo

jointure_lien_meteo = JointureInterne(table_lien, [("numer_sta", "ID")])
jointure_lien_meteo.appliquer(table=table_meteo)
#table_meteo.afficher(nb_lignes=10, nb_colonnes=10)
print(table_meteo.variables)
# ? je ne comprends pas

# déjà : on change la table_meteo c'est bof ? pourquoi ne pas retourner un nouvel objet de type TableDonnees en définissant ses attributs plutot qu'en changeant ceux de la table_meteo?
