# -----------------------------------------------------------------------------------------------
# Test des classes estimateurs:
# -----------------------------------------------------------------------------------------------

from table.tabledonnees import TableDonnees
from estimateur.moyenne import Moyenne
from estimateur.ecarttype import EcartType

# Table de test
ma_table = TableDonnees(nom="t1",
                        donnees_avec_entete=[["id", "dnais", "taille", "poids"],
                                             ["id1", 20120101, 160, 50],
                                             ["id2", 20060920, 180, 80],
                                             ["id3", 20010815, 155, 45]],
                        identifiants=["id"],
                        type_var=["str", "date", "float", "float"])


# Calcul de la moyenne de "poids"
# détermination de l'index de la variable
print(ma_table.index_variable("taille"))  # index : 2

# application de la méthode 1var
Moyenne.estim1var(ma_table, 2)  # OK

# application de la méthode appliquer()
table_moyenne = Moyenne().appliquer(table=ma_table)
table_moyenne.afficher()

# Calcul de l'écart-type de "taille"
# détermination de l'index de la variable
print(ma_table.index_variable("poids"))  # index : 3

# application de l'index de la variable
EcartType.estim1var(ma_table, 3)

# application de la méthode appliquer ()
table_ecarttype = EcartType().appliquer(ma_table)
table_ecarttype.afficher()
