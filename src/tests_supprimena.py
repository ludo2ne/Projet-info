'''
Module tests_supprimena
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.export import Export
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from transformation.supprimena import SupprimeNA

# -------------------------------------------------------------------
# Test du suppression de valeurs manquantes pour une liste de variable
# -------------------------------------------------------------------

ma_table = TableDonnees(nom="t1",
                            donnees_avec_entete=[["id",  "mat", "date", "taille"],
                                                 ["id1", "A", "20120101", "160"],
                                                 ["id2", "B", "20060920", "180"],
                                                 ["id3", "C", "20060920", "na"],
                                                 ["id4", "D", "20010525", "165"],
                                                 ["id5", "na", "19860525", "175"]],
                            identifiants=["id", "mat"],
                            valeur_manquante="na")
print(ma_table)

SupprimeNA(liste_var=["mat","taille"]).appliquer(ma_table)
print("Table après suppression des valeurs manquantes:", ma_table)

print("je suis ici",ma_table.liste_var_float())

# -------------------------------------------------------------------
# Autre test sur une plus grande table
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")
ma_table_csv.afficher(nb_colonnes=12)

SupprimeNA(liste_var=["pmer", "tend", "ww"]).appliquer(ma_table_csv)

ma_table_csv.afficher(nb_colonnes=12)

# -------------------------------------------------------------------
# Suppression des valeurs manquantes pour TOUTES les variables de type numérique
# -------------------------------------------------------------------

SupprimeNA().appliquer(ma_table_csv)

#Export().appliquer(ma_table_csv) #constat la table est vide car des variables n'ont que des valeurs manquantes

# -------------------------------------------------------------------
# Utilisation du Pipeline pour éliminer d'abort les variables qui n'ont que des valeurs manquantes,
# avant de supprimer les valeurs manquantes pour TOUTES les autres variables de type numérique
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")
ma_table_csv.afficher(nb_colonnes=12)

#Pipeline(nom="nettoyage",liste_operations=[SelectionVariables(),SupprimeNA(),Export()]).lancer(ma_table_csv)
# cette table est encore vide de données car aucune ligne ne contenait aucune valeur manquante
