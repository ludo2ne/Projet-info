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
                        donnees=np.asarray([["id", "dnais", "taille", "poids"], [
                            "id1", 20120101, 160, 50], ["id2", 20060920, 180, 80], ["id3", 20010815, 155, 45]]),
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])

mon_autre_table = TableDonnees(nom="t2",
                               donnees=np.asarray([["id", "dnais", "taille", "poids"], [
                                   "id1", 20100101, 130, 40]]),
                               identifiants=["id"],
                               type_var=["str", "date", "float", "float"])

ma_table.afficher()
mon_autre_table.afficher()

# -------------------------------------------------------------------
# Test de la concaténation
# -------------------------------------------------------------------
ma_table_concatenee = ConcatanationLignes(mon_autre_table).appliquer(ma_table)
# TODO : comment prendre en compte les headers ? erreur avec concatenate
