# -----------------------------------------------------------------------------------------------
# Test de la classe agrégation spatiale
# -----------------------------------------------------------------------------------------------

import numpy as np
from table.tabledonnees import TableDonnees
from estimateur.moyenne import Moyenne
from estimateur.ecarttype import EcartType
#from transformation.agregationspatialeLau import AgregationSpatialeLau

# Table de test
ma_table = TableDonnees(nom="table_test",
                        donnees_avec_entete=[["region", "date", "consommation", "meteo"],
                                             ["R1", 20120101, 100, 50],
                                             ["R2", 20060920, 180, 80],
                                             ["R3", 20120101, 160, 50],
                                             ["R2", 20120101, 160, 50],
                                             ["R1", 20010815, 200, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])

# je veux :
# sur fichier électricité
# pour chaque date (set(date)), les conso totales

var_tri = 'date'
echelon_init = 'region'
echelon_final = 'national'  # on va remplacer à la fin echelon_init par echelon_final

index_var_tri = ma_table.index_variable(var_tri)  # récupérer l'index de date

ma_table.donnees = ma_table.donnees[ma_table.donnees[:,
                                                     index_var_tri].argsort()]
print(ma_table.donnees)

liste_finale = []
k = 0
donnees_extraites = list(ma_table.donnees[k])
print(len(ma_table.donnees))
var_tri_current = donnees_extraites[index_var_tri]
print(var_tri_current)

# while k < len(ma_table.donnees) - 1:
#    k += 1
#    if ma_table.donnees[k, index_var_tri] == var_tri_current:
#        donnees_extraites.append(list(ma_table.donnees[k]))
#        if k + 1 == len(ma_table.donnees):
#            liste_finale.append(donnees_extraites)
#            break
#    else:
#        liste_finale.append(donnees_extraites)
#        donnees_extraites = [ma_table.donnees[k]]
#        var_tri_current = donnees_extraites[0][index_var_tri]


# fonction pour faire le cumul sur les variables num d'une table
# def cumul(var_tri, table):
#    '''
#    var_tri : une valeur
#    table : une liste de liste
#    '''
#    result = [var_tri]
#    table = np.asarray(table)
#    nrow = len(table)
#    ncol = len(table[0])
#    for j in range(ncol):
#        S = 0
#        for i in range(nrow):
#            S += table[i,j]
#        result.append(S)
#    return result


tmp_liste = []
var_tri_prev = donnees_extraites[index_var_tri]
while k < len(ma_table.donnees):
    donnees_extraites = list(ma_table.donnees[k])
    var_tri_current = donnees_extraites[index_var_tri]
    if var_tri_current == var_tri_prev:
        tmp_liste.append(donnees_extraites)
    else:
        # TODO function : somme ou moyenne
        #result = cumul(var_tri_prev, tmp_liste)
        liste_finale.append(tmp_liste)
        var_tri_prev = donnees_extraites[index_var_tri]
        tmp_liste = []
        tmp_liste.append(donnees_extraites)
    k += 1

#result = cumul(tmp_liste)
# liste_finale.append(result)

liste_finale.append(tmp_liste)

print('la liste finale est :')
print(liste_finale)

# ==> dans liste finale on récupère les tableaux/listes sur lesquels faire l'agrégation
# pour le moment on ne fait que des additions (cumul)


# Version np.array
#liste_finale = []
#k = 0
#donnees_extraites = ma_table.donnees[k]
#var_tri_current = donnees_extraites[index_var_tri]
#
# while k < len(ma_table.donnees) - 1:
#    k += 1
#    if ma_table.donnees[k, index_var_tri] == var_tri_current:
#        donnees_extraites = np.concatenate(
#            (donnees_extraites, ma_table.donnees[k]))
#        print(donnees_extraites)
#        if k + 1 == len(ma_table.donnees):
#            liste_finale.append(donnees_extraites)
#            break
#    else:
#        liste_finale.append(donnees_extraites)
#        donnees_extraites = ma_table.donnees[k]
#        var_tri_current = donnees_extraites[index_var_tri]
#
#print('la liste finale est :')
# print(np.asarray(liste_finale))


#index_echelon_init = ma_table.index_variable(echelon_init)
# print(index_echelon_init)
# on récupère les autres variables de type float
# autres_variables = np.delete(
#    ma_table.variables, [index_echelon_init, index_var_tri])
# for variable in autres_variables:
#    index = ma_table.index_variable(variable)
#    if ma_table.type_var[index] != 'float':
#        autres_variables = np.delete(autres_variables, variable)
# On a récupéré les autres variables numériques : on va pouvoir s'en servir pour initialiser les array
# print(autres_variables)

# Définition des variables de la table de sortie :
#variables_tabledef = [echelon_final, var_tri]
# print(autres_variables)
# pour récupérer les valeurs uniques de var_tri (dates uniques):
#valeurs = set(ma_table.donnees[:, index_var_tri])
# print(valeurs)
##
##print(ma_table.donnees[:, index_echelon_init])
##
# TODO if 'consommation' in variable :cumul else : moyenne
##
#donnees_finales = np.array([])
# for valeur in valeurs:  # pour chaque date
#    #donnees_extraites = np.empty((1, 2 + len(autres_variables)))
#    donnees_extraites = np.asanyarray([[]])  # comment initialiser ce bordel???
#    n = len(valeurs)
#    for k in range(len(ma_table.donnees)):  # pour chaque ligne
#        if ma_table.donnees[k, index_var_tri] == valeur:
#            #donnees_extraites.append(list(ma_table.donnees[k, :]))
#            donnees_extraites = np.vstack([
#                donnees_extraites, ma_table.donnees[k, :]])
#    print(donnees_extraites)
#    # for k in range(len(donnees_extraites)):
#
#
# for variable in autres_variables: #pour chaque autre variable de type numérique
#       if ma_table.type_var(variable) == 'float':
#           index = ma_table.index_variable(variable) #index de colonne de la variable sur laquelle on fait l'agrégation
#           variables_tabledef.append(variable) #ajoute la variable à la liste de la table de retour
#           S= 0        #somme initialisée à 0 (ici on cumule)
#           for k in range(len(ma_table.donnees[:,index_echelon_init])): #pour chaque valeur de région
#               if ma_table.donnees[k, index_var_tri] == :
#                   S += ma_table.donnees[ ,index]

# mylist = ['nowplaying', 'PBS', 'PBS',
#          'nowplaying', 'job', 'debate', 'thenandnow']
#myset = set(mylist)
# print(myset)
