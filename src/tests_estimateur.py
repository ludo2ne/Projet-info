'''
Module tests_estimateur
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from transformation.export import Export
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from pipeline.pipeline import Pipeline
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation

# -------------------------------------------------------------------
# Test de calcul d'estimateurs à partir du table créée
# -------------------------------------------------------------------
print("exemple avec petite table ---------------------------------------")
ma_table3 = TableDonnees(nom="t3",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                              ["id1", "20120101", "160", "63"],
                                              ["id2", "20060920", "180", "90"], ["id3", "20060921", "170", "75"], ["id4", "20061020", "183", "85"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float"])


Moyenne().appliquer(ma_table3)


EcartType().appliquer(ma_table3)


# -------------------------------------------------------------------
# à partir d un fichier csv
# -------------------------------------------------------------------
print("exemple avec fichier csv----------------------------------------")
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")


SelectionVariables(liste_var=["date","numer_sta","ff", "tend","niv_bar","geop","tend24","tn24","tx12","tx24","nnuage2","ctype3","hnuage4"]).appliquer(ma_table_csv)
print(ma_table_csv.type_var)

print(ma_table_csv)


Moyenne().appliquer(ma_table_csv)


EcartType().appliquer(ma_table_csv)

# -------------------------------------------------------------------
# exemple avec pipeline
# -------------------------------------------------------------------
print("exemple avec pipeline----------------------------------------")
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

Pipeline(nom="estim&normalise",liste_operations=[SelectionVariables(freqNA=0.1),Moyenne(),EcartType(),Normalisation(),Export(),Moyenne()]).lancer(ma_table_csv)
#le dernier estimateur moyenne est pour vérifier que toutes les moyennes sont nulles après normalisation de la table
print(ma_table_csv)