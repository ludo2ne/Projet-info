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


class Export(Transformation):
    '''Export de la table

    Cette classe ne contient qu'une seule méthode statique qui exporte une table de données au format csv
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

        donnees_exportees = np.concatenate(([table.variables], table.donnees))
        current_date_and_time = datetime.datetime.now().strftime("%Y.%m.%d %Hh%M")
        nom_fichier_exporte = os.getcwd() + "/donnees/exports/" + table.nom + \
            "_" + current_date_and_time + ".csv"

        if format == "csv":
            np.savetxt(nom_fichier_exporte, donnees_exportees,
                       delimiter=";", fmt="%s")
        else:
            warnings.warn("Seul le format csv est autorisé pour l'export")
