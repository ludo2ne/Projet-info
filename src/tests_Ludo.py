import numpy as np
from table.tabledonnees import TableDonnees

print(np.isnan(float("160.00")))


ma_table = TableDonnees(nom="t1",
                        donnees=np.array([["id", "dnais", "taille"],
                                          ["id1", "20120101", "160"],
                                          ["id2", "20060920", "180"]]),
                        identifiants=["id"],
                        type_var=["str", "date", "float"])


print(type(ma_table.donnees[0, 2]))
