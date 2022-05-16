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
mon_autre_table.afficher()

ma_table_concatenee = ConcatanationLignes(mon_autre_table).appliquer(ma_table)

ma_table_concatenee.afficher()
