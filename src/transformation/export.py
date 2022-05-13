'''
Module centrage
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''

import os
import warnings
import numpy as np
import datetime
from transformation.transformation import Transformation
from estimateur.moyenne import Moyenne


class Export(Transformation):
    '''Export de la table

    cette classe ne contient qu'une seule méthode statique qui exporte une table de données
    '''

    @staticmethod
    def appliquer(table, format='csv'):
        '''Export de la table

        Parameters
        ----------
        table : TableDonnees
            table de données
        '''

        print("------------------------------------------------------")
        print("Export de la table " + table.nom)

        current_date_and_time = datetime.datetime.now().strftime("%Y.%m.%d %Hh%M")

        donnees_exportees = np.concatenate(([table.variables], table.donnees))
        # for i in range(len(table.donnees)):
        #    donnees_exportees = np.concatenate(
        #        donnees_exportees, table.donnees[i])

        if format == 'csv':
            np.savetxt(os.getcwd() + "/donnees/exports/" +
                       table.nom + "_" + current_date_and_time + ".csv", np.array(donnees_exportees), delimiter=";", fmt="%s")
        else:
            warnings.warn("Seul le format csv est autorisé pour l'export")

    def __str__(self):
        '''Conversion de l'objet en chaîne de caractères
        '''
        return "Je suis un centrage"
