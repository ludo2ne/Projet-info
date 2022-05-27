import os
from transformation.moyenneglissante import MoyenneGlissante
from table.donneescsv import DonneesCsv
from transformation.export import Export
from table.tabledonnees import TableDonnees

ma_table = TableDonnees(nom="table_test",
                        donnees_avec_entete=[["region", "date", "consommation", "meteo"],
                                             ["R1", 20130101000000, 100, 50],
                                             ["R2", 20130101000000, 180, 80],
                                             ["R3", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 55],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R1", 20010815, 200, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])
MoyenneGlissante(pas=4).appliquer(ma_table)
print(ma_table)
