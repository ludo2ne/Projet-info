'''
Module tests_normalisation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
from pipeline.pipeline import Pipeline
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from transformation.normalisation import Normalisation
import numpy as np

# -------------------------------------------------------------------
# Normalisation d'une table créée à partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

print(ma_table_csv.type_var) #type de variables

print(ma_table_csv.nom, "avant normalisation")
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=7) #après normalisation

Normalisation().appliquer(ma_table_csv)
print(ma_table_csv.nom, "aprés normalisation")
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=7) #après normalisation



# -------------------------------------------------------------------
# Normalisation d'une table manuellement créée (avec valeur manquante)
# -------------------------------------------------------------------


ma_table3 = TableDonnees(nom="t3",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                              ["id1", "20120101", np.nan , "63"],
                                              ["id2", "20060920", "180", "90"], ["id3", "20060921", "170", "75"], ["id4", "20061020", "183", "85"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float"])
print(ma_table3.nom, "avant normalisation")
ma_table3.afficher(nb_lignes=10, nb_colonnes=7) #avant normalisation

Normalisation().appliquer(ma_table3)
print(ma_table3.nom, "après normalisation")
ma_table3.afficher(nb_lignes=10, nb_colonnes=7) #après normalisation

# -------------------------------------------------------------------
# Autre procédé testé avec Pipeline (pour verifier la coherence : même résultat que le test précédent)
# -------------------------------------------------------------------
from transformation.centrage import Centrage
from transformation.reduction import Reduction #imports faits volontairement ici pour montrer qu'ils n'étaients pas nécessaires aux tests précédents

ma_table3 = TableDonnees(nom="t3",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                              ["id1", "20120101", np.nan , "63"],
                                              ["id2", "20060920", "180", "90"], ["id3", "20060921", "170", "75"], ["id4", "20061020", "183", "85"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float"]) #réinitialisation de la table précédente


Pipeline(nom="standard", liste_operations=[Centrage(),Reduction()]).lancer(ma_table3)
print(ma_table3.nom, "après centrage et réduction par Pipeline")
ma_table3.afficher(nb_lignes=10, nb_colonnes=7) #après normalisation v2
