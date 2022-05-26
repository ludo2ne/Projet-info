'''
Module test_moyenneglissante
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from transformation.moyenneglissante import MoyenneGlissante
from table.donneescsv import DonneesCsv

# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")


print(ma_table_csv.type_var)
print(ma_table_csv.variables)
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=12) #affichage de la table initiale

# -------------------------------------------------------------------
# Moyennes glissantes d'une table (sur toutes les variables numériques de la table)
# -------------------------------------------------------------------
MoyenneGlissante().appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=12)

# -------------------------------------------------------------------
# Moyennes glissantes d'une liste de variable d'une table (autre test)
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq") #réinitialisation de la table

MoyenneGlissante(["tend","dd"]).appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=12)
