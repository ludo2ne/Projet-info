# -----------------------------------------------------------------------------------------------
# Test sur les arrays
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

var_tri = 'date'
index_var_tri = ma_table.index_variable(var_tri)  # récupérer l'index de date
echelon_init = 'region'
index_echelon_init = ma_table.index_variable(
    echelon_init)  # récupérer l'index de région
echelon_final = 'national'

autres_variables = [var_tri, echelon_final]
for var in ma_table.variables:
    if var not in [var_tri, echelon_init]:
        autres_variables.append(var)
print(autres_variables)
# print(ma_table)
# for k in range(len(ma_table.donnees[0])):
#    if ma_table.type_var[k] == 'float':
#        result = np.cumsum(ma_table.donnees[:, k])[
#            len(ma_table.donnees[:, k])-1]
#        print(result)

# définition d'une fonction de cumul


# def cumul(table, var_tri, echelon_init, echelon_final):
#    result = [var_tri, echelon_final]
#
#     for k in range(len(table.donnees[0])):
#
#         if table.type_var[k] == 'float' and table.variables[k] not in [var_tri, echelon_init]:
#
#             result.append(np.cumsum(table.donnees[:, k])[
#
#                 len(table.donnees[:, k])-1])
#
#     return result
#

#

#
# print(cumul(ma_table, "date", "region", "national"))
