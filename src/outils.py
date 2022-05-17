
from table.tabledonnees import TableDonnees
import numpy as np

ma_table = TableDonnees(nom="t1",
                        donnees=[["id", "dnais", "taille", "poids"],
                                 ["id1", 20120101, 160, 50],
                                 ["id2", 20060920, 180, 80],
                                 ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"]) #il y a encore confusion entre donnees et donnees_avec_entete TODO


# Numero colonne
print(ma_table.index_variable("taille"))
print(np.where(ma_table.variables == "taille")[0][0])

# colonne -> liste
print(ma_table.donnees[:,2])

#liste d'éléments extrait d'une ligne à partir d'une liste de clés
print(ma_table.donnees[1,[3,2]])
#ou
l=[3,2]
print(ma_table.donnees[1,l])

# sous liste
print(ma_table.variables[1:3])

print(ma_table.donnees[1])

#suppression par liste
liste_test = ma_table.donnees[:,2]
#liste_test.pop([3,0]) ne fonctionne pas ainsi

#concatenation de listes
print([1,2]+[3])
