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
# Creation a partir d un fichier csv
# -------------------------------------------------------------------
ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")
#Export().appliquer(ma_table_csv)

SelectionVariables(liste_var=["date","numer_sta","ff", "tend","niv_bar","geop","tend24","tn24","tx12","tx24","nnuage2","ctype3","hnuage4"]).appliquer(ma_table_csv)



# -------------------------------------------------------------------
# Supprimer les lignes d'une table qui contiennent au moins une valeur manquante pour une liste de variables données
# -------------------------------------------------------------------

#SupprimeNA(["vv", "ww"]).appliquer(ma_table_csv)
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




ma_table3 = TableDonnees(nom="t3",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                              ["id1", "20120101", "160", "63"],
                                              ["id2", "20060920", "180", "90"], ["id3", "20060921", "170", "75"], ["id4", "20061020", "183", "85"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float"])

ma_table4 = TableDonnees(nom="tableMixte",
                         donnees_avec_entete=[["id", "dnais", "taille", "poids", "emploi","saisfaction"],
                                              ["id1", "20120101", "160", "63","statisticien","satisfait"],
                                              ["id2", "20060920", "180", "90", "informaticien", "satisfait"], ["id3", "20060921", "170", "75","statisticien","satisfait"], ["id4", "20061020", "183", "65","na","insatisfait"],["id5", "20061025", "182", "80","informaticien","na"]],
                         identifiants=["id"],
                         type_var=["str", "date", "float", "float","str","str"], valeur_manquante="na")


# -------------------------------------------------------------------
# Etude du lien entre 2 variables quantitatives
# -------------------------------------------------------------------




SupprimeNA(["ff", "tend", "hnuage4"]).appliquer(ma_table_csv)

#ma_table_csv.afficher(nb_colonnes=7)

SelectionVariables(["numer_sta","date,""ff", "tend", "hnuage4"]).appliquer(ma_table_csv)
ma_table_csv.afficher(nb_lignes=10, nb_colonnes=7)
print(ma_table_csv.variables)
print(ma_table_csv.type_var)


CoefficientCorrelation("ff", "tend").appliquer(
    ma_table_csv)


#SelectionVariables(["numer_sta","date,""ff", "tend", "hnuage4",""]).appliquer(ma_table_csv)
#ma_table_csv.afficher(nb_lignes=10, nb_colonnes=7)
#print(ma_table_csv.variables)
#print(ma_table_csv.type_var)

print(ma_table4)
Anova("poids","satisfaction").appliquer(ma_table4) #TODO à debugger

TestChiSquare("emploi","satisfaction").appliquer(ma_table4) #TODO à debugger




# -------------------------------------------------------------------
# Creation manuelle d une table TODO à debugger
# -------------------------------------------------------------------

#ma_table2 = TableDonnees(nom="t2",donnees_avec_entete=[["id", "dnais", "taille", "poids"],["id1", "20120101", "160", "68"], ["id2", "20060920", 180, 85], ["id3", "20060921", 170, 70]],identifiants=["id"])
# bug pour ma_table2 à cause de appliquer.format() TODO ne fonctionne pas si type_var n'est pas prédéfinie, ou sil les variables sont déjà en partie de type float ?
# ma_table2.determiner_formats ne fonctionne pas
# print(ma_table2.type_var)





'''
    def appliquer(self, table):
        nom_tb_joint = "{}_{}".format(table.nom, self.autre_table.nom)
        cle1=[TableDonnees.index_variable(var) for var in self.cle[0]]
        cle2=[TableDonnees.index_variable(var) for var in self.cle[1]]
        table_donnees=[]
        list_var = table.variables + self.autre_table.variables #concaténation
        list_type = table.type_var + self.autre_table.type_var
        for i in range(len(table.donnees)):
            for j in range(len(self.autre_table.donnees)):
                if table.donnees[i,cle1] == self.autre_table.donnees[j,cle2]:
                    list_concat = table.donnees[i] + self.autre_table.donnees[j]
                    #list_concat.pop(col_cle[0]) dans l'idée de supprimer les colonnes en double, mais pop() attend un seul entier pas une liste
                    #list_concat.pop(cle1) dans l'idée de supprimer les colonnes en double, mais pop() attend un seul entier pas une liste
                    table_donnees.append(list_concat)
        #finir par transformer table_donnee en array ?
        # supprimer les colonnes (de la nouvelle table jointe) dont les numeros sont contenus dans cle1 (car en double) TODO
        table.nom = nom_tb_joint
        table.variables = list_var
        table.donnees = table_donnees
        table.type_var = list_type
'''