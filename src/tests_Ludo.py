import os
import numpy as np
from table.tabledonnees import TableDonnees
from transformation.concatenation import ConcatanationLignes

# -------------------------------------------------------------------
# Creation manuelle d une table
# -------------------------------------------------------------------
ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                 ["id1", 20120101, 160, 50],
                                 ["id2", 20060920, 180, 80],
                                 ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])


print(ma_table.index_variable("poids"))

print(ma_table.donnees[:, 2])


ma_liste = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ma_liste[3:5])
