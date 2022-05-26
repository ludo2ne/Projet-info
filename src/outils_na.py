import numpy as np
from table.tabledonnees import TableDonnees

ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids","pb_sante","autre"],
                                             ["id1", 20120101, 160, 50,"oui", np.nan],
                                             ["id2", 20060920, 180, 80, np.nan, "nan"],
                                             ["id3", 20010815, 155, np.nan, "non","nan" ]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float","str","str"], valeur_manquante="nan")

print(ma_table)

for i in range(len(ma_table.donnees)):
    print("ligne",i)
    for j in range(len(ma_table.variables)):
        print("colonne",j)
        a= ma_table.donnees[i,j]
        print(a)
        if type(a)==str:
            print(False)
        else:
            print(np.isnan(a))
print("end")

print(np.isnan(3))
print(3==np.nan)
#np.isnan("nan")
print(np.isnan(np.nan))
print("je suis ici","na"==np.nan)

ma_table = TableDonnees(nom="t1",
                            donnees_avec_entete=[["id",  "mat", "date", "taille"],
                                                 ["id1", "A", "20120101", "160"],
                                                 ["id2", "B", "20060920", "180"],
                                                 ["id3", "C", "20060920", "na"],
                                                 ["id4", "D", "20010525", "165"],
                                                 ["id5", "na", "19860525", "175"]],
                            identifiants=["id", "mat"],
                            valeur_manquante="na")
print(ma_table)
print(ma_table.type_var)

a=ma_table.donnees[4,1] # valeur manquante de str
b=ma_table.donnees[2,3] # valeur manquante de float
print(a,type(a),b,type(b)) # nan est de type float
print("ça devrait afficher True True :",a==np.nan,b==np.nan) #bug
print(a=="nan",b=="nan") #bug idem
print(np.isnan(a)) #ça fonctionne
print(np.isnan(b)) #ça fonctionne

a=ma_table.donnees[3,1] # str pas manquant
b=ma_table.donnees[3,3] # float pas manquant
print( a,type(a),b,type(b))
print("ça devrait afficher False False:",a==np.nan,b==np.nan)

print(np.isnan(b))
print(np.isnan(a)) #bug
