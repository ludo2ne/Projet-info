from datetime import datetime
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
import os
import numpy as np
import statistics
import matplotlib.pyplot as plt

ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                             ["id1", 20120101, 160, 50],
                                             ["id2", 20060920, 180, 80],
                                             ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])


date_time_str = '20170921085519'
date_time_obj = datetime.strptime(date_time_str, '%Y%m%d%H%M%S')
date_time_str_new = datetime.strftime(date_time_obj, '%Y%m%d%H%M%S')

print(date_time_obj)
print(type(date_time_obj))
print(date_time_str_new)
print(type(date_time_str_new))
