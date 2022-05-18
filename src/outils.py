
from table.tabledonnees import TableDonnees
from table.donneescsv import DonneesCsv
import os
import numpy as np

ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids"],
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
print(liste_test)
print(np.delete(liste_test,1,None)) #supprime le 2ème élément (d'indice 1) de la liste
print(np.delete(ma_table.donnees,3,1)) #supprime la 4ème (d'incice 3) colonne (axe 1)
print(np.delete(ma_table.donnees,[1,3],1)) #supprime les 2ème et 4ème colonnes
print(np.delete(ma_table.donnees,1,0)) #supprime la 2ème ligne (axe 0)
#liste_test.pop([3,0]) ne fonctionne pas ainsi

ma_table_csv = DonneesCsv(nom="table_csv",
                          chemin_complet=os.getcwd() + "/donnees/test/synop.201301.csv.gz",
                          identifiants=['numer_sta', 'date'],
                          valeur_manquante="mq")
ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)


ma_table_csv.donnees = np.delete(ma_table_csv.donnees, 7, 0) #supprime la 8ème ligne
ma_table_csv.afficher(nb_lignes=10,
                      nb_colonnes=12)

#concatenation de listes
print([1,2]+[3])

print(np.isnan(ma_table.donnees[0,2]))
