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
ma_table_csv.afficher(nb_lignes=54,
                      nb_colonnes=60)
print(ma_table_csv.type_var)
print(ma_table_csv.variables)

#concatenation de listes
print([1,2]+[3])

print(np.isnan(ma_table.donnees[0,2]))

#moyenne avec NA
liste=[5,3,5,10,9,np.nan]
print(statistics.mean(liste))

#boxplot
plt.boxplot([[5,3,10,9],[10,15,30]])
plt.show()
plt.pause
#coeff de corr
print(np.corrcoef([1,2,3],[10,15,30])[1,0])

#nuage de points

plt.scatter([1,2,3],[10,15,30],color="green")
plt.scatter([0.5,2.1,4],[5,15,20])
plt.show()


#variable ou liste générées dans une boucle
#tab=["a","b","c"]
#for i in enumerate(tab):
#    globals()["liste%s"%i]=[]

matrice=[]
matrice.append([])
matrice[0].append(2)
matrice[0].append(3)
matrice.append([])
matrice[1].append(5)
print(matrice)