'''
Module tests_selectionvariables
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv

from transformation.selectionvariables import SelectionVariables


# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

# -------------------------------------------------------------------
# Test d'une selection d'une liste de variable
# -------------------------------------------------------------------

SelectionVariables(liste_var=["date","numer_sta","pmer", "niv_bar","geop","tend24","tn24","tx12","tx24","nnuage2","ctype3","hnuage4"]).appliquer(ma_table_csv)
print(ma_table_csv)


# -------------------------------------------------------------------
# Test consécutif d'une selection plus restrainte sans les variables qui n'ont que des valeurs manquantes
# -------------------------------------------------------------------

SelectionVariables(freqNA=0.99).appliquer(ma_table_csv)
ma_table_csv.afficher()

# -------------------------------------------------------------------
# Selection des vériables avec moins de 10% de valeurs manquantes
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

SelectionVariables(freqNA=0.1).appliquer(ma_table_csv)
ma_table_csv.afficher()