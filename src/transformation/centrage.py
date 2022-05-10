'''
Module centrage
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import warnings
import doctest
from transformation.transformation import Transformation
from estimateur.moyenne import Moyenne


class Centrage(Transformation):
    '''Centrage d'une ou plusieurs variables
    '''

    def __init__(self, liste_colonnes):
        '''Constructeur de l'objet

        Attributes
        ----------
        liste_colonnes : list[str]
            liste des noms des colonnes auquelles appliquer la transformation
        '''
        self.liste_colonnes = liste_colonnes

    def appliquer_variable(self, table, numero_colonne):
        '''Appliquer le centrage à une variable de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        numero_colonne : int
            numéro de la colonne sur laquelle appliquer

        Examples
        --------

        '''

        print("------------------------------------------------------")
        print("Centrage de la variable " + table.variables[numero_colonne])

        # Calcul de la moyenne
        moyenne = Moyenne.appliquer(table, numero_colonne)

        # Centrage de toutes les valeurs
        for i in range(0, len(table.donnees)):
            if table.donnees[i][numero_colonne] != "mq":
                old_value = float(table.donnees[i][numero_colonne])
                new_value = str(old_value - moyenne)
                table.donnees[i][numero_colonne] = new_value

        return table

    def appliquer(self, table):
        '''Appliquer la transformation à plusieurs variables de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''
        for col in self.liste_colonnes:
            try:
                num_col = table.variables.tolist().index(col)
            except:
                warnings.warn("Variable " + col +
                              " non trouvée dans la table " + table.nom)
            else:
                self.appliquer_variable(table, num_col)

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Je suis un centrage"
