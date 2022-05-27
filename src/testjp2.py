from table.tabledonnees import TableDonnees



ma_table = TableDonnees(nom="t1",
                            donnees_avec_entete=[["id",  "mat", "date", "taille"],
                                                 ["id1", "A", "20120101", "160"],
                                                 ["id2", "B", "20060920", "180"],
                                                 ["id3", "C", "20060920", "na"],
                                                 ["id4", "D", "20010525", "165"],
                                                 ["id5", "na", "19860525", "175"]],
                            identifiants=["id", "mat"],
                            valeur_manquante="na")


print(ma_table.liste_var_float()==['taille'])
print(ma_table.liste_var_na(freqNA=0.19)==['id', 'date'])
