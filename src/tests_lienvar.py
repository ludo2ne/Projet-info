'''
Module tests_lienvar
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from lienvar.coefficientcorrelation import CoefficientCorrelation
from lienvar.anova import Anova
from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
from table.donneesjson import DonneesJson
from pipeline.pipeline import Pipeline
from transformation.centrage import Centrage
from transformation.selectionvariables import SelectionVariables
from lienvar.coefficientcorrelation import CoefficientCorrelation
from transformation.supprimena import SupprimeNA
from lienvar.testchisquare import TestChiSquare
from transformation.export import Export

# -------------------------------------------------------------------
# création d'une table de données qui mixe le données qualitatives et quantitative
# -------------------------------------------------------------------

ma_table4 = TableDonnees(nom="tableMixte",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids", "emploi","satisfaction"],
                                              ["id1", "20120101", "160", "63","statisticien","satisfait"],
                                              ["id2", "20060920", "180", "90", "informaticien", "satisfait"], ["id3", "20060921", "170", "75","statisticien","satisfait"], ["id4", "20061020", "183", "65","na","insatisfait"],["id5", "20061025", "182", "80","informaticien","na"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float","str","str"], valeur_manquante="na")
print(ma_table4)

# -------------------------------------------------------------------
# Etude du lien entre 2 variables quantitatives
# -------------------------------------------------------------------
CoefficientCorrelation(var1="taille",var2="poids").appliquer(ma_table4)

# -------------------------------------------------------------------
# Autre test quanti/quanti sur une plus grande table, en passant par un pipeline
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")

Pipeline(nom="étude2varQuantitatives", liste_operations = [SupprimeNA(liste_var = ["pmer", "tend"]), SelectionVariables(liste_var = ["date", "numer_sta", "pmer", "tend"]), CoefficientCorrelation(var1 = "pmer", var2 = "tend")]).lancer(ma_table_csv)
print(ma_table_csv)

# -------------------------------------------------------------------
# Etude du lien entre une variable quali et une variable quanti
# -------------------------------------------------------------------
ma_table4 = TableDonnees(nom="tableMixte",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids", "emploi","satisfaction"],
                                              ["id1", "20120101", "160", "63","statisticien","satisfait"],
                                              ["id2", "20060920", "180", "90", "informaticien", "satisfait"], ["id3", "20060921", "170", "75","statisticien","satisfait"], ["id4", "20061020", "183", "65","mq","insatisfait"],["id5", "20061025", "182", "80","informaticien","mq"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float","str","str"], valeur_manquante="na") #j'ai volantairement renommé les na pour ne pas les convertir en np.nan en attendant de résoudre le pb

Anova(var1="satisfaction",var2="poids").appliquer(ma_table4)

# -------------------------------------------------------------------
# Etude du lien entre deux variables quali
# -------------------------------------------------------------------
TestChiSquare(var1="satisfaction",var2="emploi").appliquer(ma_table4) #erreur de test d'égalité avec les valeurs manquantes TODO