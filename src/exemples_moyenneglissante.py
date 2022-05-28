'''
Module exemples_moyenneglissante
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from transformation.moyenneglissante import MoyenneGlissante
from table.donneescsv import DonneesCsv
from transformation.export import Export

# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

Export().appliquer(ma_table_csv)
print(ma_table_csv.type_var)
print(ma_table_csv.variables)
# affichage de la table initiale
ma_table_csv.afficher(nb_colonnes=12)

# -------------------------------------------------------------------
# Moyennes glissantes d'une table (sur toutes les variables numériques de la table)
# -------------------------------------------------------------------
MoyenneGlissante().appliquer(ma_table_csv)
ma_table_csv.afficher(nb_colonnes=12)

# -------------------------------------------------------------------
# Moyennes glissantes d'une liste de variable d'une table (autre test)
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")  # réinitialisation de la table

MoyenneGlissante(["tend", "dd"],pas = 5).appliquer(ma_table_csv)
ma_table_csv.afficher(nb_colonnes=12)
