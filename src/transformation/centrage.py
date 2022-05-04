'''
Module transformation
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import doctest
from estimateur.moyenne import Moyenne


class Centrage:
    '''Centrage d'une variable

    Cette classe ne contient qu'une seule méthode statique
    Il n'y a pas de constructeur car il n'est pas nécessaire d'instancier une objet de cette classe
    '''

    @staticmethod
    def appliquer(table, numero_colonne):
        '''Appliquer le centrage à une colonne de la table

        Cette méthode est statique, elle peut être utilisée sans 

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            index de la colonne à centrer
            TODO éventuellement remplacer par une liste

        Examples
        --------

        '''

        print("------------------------------------------------------")
        print("Centrage de la variable " + table.donnees[0][numero_colonne])

        # Calcul de la moyenne
        moyenne = Moyenne.appliquer(table, numero_colonne)

        # Centrage de toutes les valeurs
        for i in range(1, len(table.donnees)):
            if table.donnees[i][numero_colonne] != "mq":
                old_value = float(table.donnees[i][numero_colonne])
                new_value = str(old_value - moyenne)
                table.donnees[i][numero_colonne] = new_value

        return table

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Je suis un centrage"
