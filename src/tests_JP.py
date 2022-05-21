'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from lienvar.coefficientcorrelation import CoefficientCorrelation
from lienvar.anova import Anova
from transformation.moyenneglissante import MoyenneGlissante
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.selectionvariables import SelectionVariables
from transformation.normalisation import Normalisation
from lienvar.coefficientcorrelation import CoefficientCorrelation
from transformation.supprimena import SupprimeNA
from lienvar.testchisquare import TestChiSquare
# -------------------------------------------------------------------
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")


# -------------------------------------------------------------------
# Supprimer les lignes d'une table qui contiennent au moins une valeur manquante pour une liste de variables données
# -------------------------------------------------------------------

SupprimeNA(["vv", "ww"]).appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)

# -------------------------------------------------------------------
# Creation manuelle d une table
# -------------------------------------------------------------------
ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille"],
                                             ["id1", "20120101", "160"],
                                             ["id2", "20060920", "180"]],
                        identifiants=["id"],
                        type_var=["str", "date", "float"])

ma_table.afficher(nb_lignes=10, nb_colonnes=7)


# -------------------------------------------------------------------
# Normaliser une table
# -------------------------------------------------------------------
Normalisation().appliquer(ma_table)
ma_table.afficher(nb_lignes=10, nb_colonnes=7)

ma_table3 = TableDonnees(nom="t3",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                              ["id1", "20120101", "160", "63"],
                                              ["id2", "20060920", "180", "90"], ["id3", "20060921", "170", "75"], ["id4", "20061020", "183", "85"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float"])

Normalisation().appliquer(ma_table3)
ma_table3.afficher(nb_lignes=10, nb_colonnes=7)

Normalisation().appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=7)


# -------------------------------------------------------------------
# Etude du lien entre 2 variables quantitatives
# -------------------------------------------------------------------
SupprimeNA(["ff", "tend", "hnuage4"]).appliquer(ma_table_csv)

ma_table_csv.afficher(nb_colonnes=7)



CoefficientCorrelation("ff", "tend").appliquer(
    ma_table_csv)  # TODO à debugger

Anova("tend","hnuage4").appliquer(ma_table_csv) #TODO à debugger




# -------------------------------------------------------------------
# Creation manuelle d une table TODO à debugger
# -------------------------------------------------------------------

#ma_table2 = TableDonnees(nom="t2",donnees_avec_entete=[["id", "dnais", "taille", "poids"],["id1", "20120101", "160", "68"], ["id2", "20060920", 180, 85], ["id3", "20060921", 170, 70]],identifiants=["id"])
# bug pour ma_table2 à cause de appliquer.format() TODO ne fonctionne pas si type_var n'est pas prédéfinie, ou sil les variables sont déjà en partie de type float ?
# ma_table2.determiner_formats ne fonctionne pas
# print(ma_table2.type_var)

# -------------------------------------------------------------------
# Moyennes glissantes d'une table
# -------------------------------------------------------------------
MoyenneGlissante().appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=7)
