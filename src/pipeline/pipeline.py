'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
from transformation.export import Export


class Pipeline:
    '''Classe représentant un pipeline

    Attributes
    ----------
    nom : str
        Nom du pipeline
    liste_transformations : list[Transformation]
        liste des transformations qui seront appliquées
    estimateur_final : EstimateurFinal
        estimateur final à appliquer
    '''

    def __init__(self, nom, liste_transformations, estimateur=None, exporter_table=False):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            Nom du pipeline
        liste_transformations : list[Transformation]
            liste des transformations qui seront appliquées
        estimateur_final : EstimateurFinal
            estimateur final à appliquer
            None par défaut
        exporter_table : bool
            Si True le fichier est exporté dans donnees/export
            False par défaut
        '''
        self.nom = nom
        self.liste_transformations = liste_transformations
        self.estimateur = estimateur
        self.exporter_table = exporter_table

    def lancer(self, table):
        '''Lancement du pipeline

        La liste des transformations est appliquée dans l'ordre à la table en paramètre

        Parameters
        ----------
        table : tableDonnees
            table de données à transformer

        Returns
        -------
        table
            table de données mise à jour
        '''
        print("------------------------------------------------------")
        print("Lancement du pipeline " + self.nom)

        # Pour chaque transformation de la liste
        for i in range(len(self.liste_transformations)):
            self.liste_transformations[i].appliquer(table)

        if self.exporter_table:
            Export.appliquer(table)
