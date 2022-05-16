
from table.tabledonnees import TableDonnees
import numpy as np

ma_table = TableDonnees(nom="t1",
                        donnees=[["id", "dnais", "taille", "poids"],
                                 ["id1", 20120101, 160, 50],
                                 ["id2", 20060920, 180, 80],
                                 ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])


# Numero colonne
print(ma_table.index_variable("taille"))
print(np.where(ma_table.variables == "taille")[0][0])

# colonne -> liste
print(ma_table.donnees[:, 2])

# sous liste
print(ma_table.variables[1:3])
