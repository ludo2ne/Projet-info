'''
Module main
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date	: 13/05/2022
Licence : Domaine public
Version : 1.0
'''
import os
import numpy as np
from table.tabledonnees import TableDonnees
from transformation.concatenation import ConcatanationLignes

# -------------------------------------------------------------------
# Creation manuelle d une table
# -------------------------------------------------------------------
ma_table = TableDonnees(nom="t1",
                        donnees=[["id", "dnais", "taille", "poids"],
                                 ["id1", 20120101, 160, 50],
                                 ["id2", 20060920, 180, 80],
                                 ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])

mon_autre_table = TableDonnees(nom="t2",
                               donnees=[["id", "dnais", "taille", "poids"],
                                        ["id1", 20100101, 130, 40]],
                               identifiants=["id"],
                               type_var=["str", "date", "float", "float"])


ma_table.afficher()
#
mon_autre_table.afficher()
#
# #
#
# #
#
# # -------------------------------------------------------------------
#
# # Test de la concaténation
#
# # -------------------------------------------------------------------
#

'''
ma_table_concatenee = ConcatanationLignes(mon_autre_table).appliquer(ma_table)
ma_table_concatenee.afficher()
'''
ConcatanationLignes(mon_autre_table).appliquer(ma_table)
ma_table.afficher()


# exemple qui marche : (mais type final obtenu un peu bizarre, liste de tableaux..? )
# donnees = [[] for k in range(
#    len(ma_table.donnees) + len(mon_autre_table.donnees) + 1)]
# print(donnees)
#donnees[0] = np.asarray(ma_table.variables)
# print(donnees)
# donnees_conc = np.concatenate(
#    (ma_table.donnees, mon_autre_table.donnees))
# print(donnees_conc)
# print(len(donnees))
# print(len(donnees_conc))
# for k in range(len(donnees_conc)):
#    donnees[k+1] = donnees_conc[k]
#    print(donnees)

# avec tentative de changer de type :
# donnees = [[] for k in range(
#    len(ma_table.donnees) + len(mon_autre_table.donnees) + 1)]
# print(donnees)
#donnees[0] = list(ma_table.variables)
# print(donnees)
# donnees_conc = np.concatenate(
#    (ma_table.donnees, mon_autre_table.donnees))
# print(donnees_conc)
# print(len(donnees))
# print(len(donnees_conc))
# for k in range(len(donnees_conc)):
#    donnees[k+1] = list(donnees_conc[k])
#    print(donnees)
#donnees = np.asarray(donnees)
# print(donnees)
