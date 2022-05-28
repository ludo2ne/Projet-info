'''
Module pipeline
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''


class Pipeline:
    '''Classe implémentant un pipeline, liste d'opérations à réaliser.

    Attributes
    ----------
    nom : str
        Nom du pipeline
    liste_operations : list[Transformation, Estimateur, LienVar]
        liste des opérations qui seront appliquées
    '''

    def __init__(self, nom, liste_operations):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            Nom du pipeline
        liste_operations : list[Transformation, Estimateur, LienVar]
            liste des operations qui seront appliquées
        '''
        self.nom = nom
        self.liste_operations = liste_operations

    def lancer(self, table):
        '''Lancement du pipeline

        La liste des opérations est appliquée (dans l'ordre) à la table en paramètre

        Parameters
        ----------
        table : tableDonnees
            table de données à transformer
        '''

        print("------------------------------------------------------")
        print("Lancement du pipeline " + self.nom)

        # Pour chaque operation de la liste
        for i in range(len(self.liste_operations)):
            self.liste_operations[i].appliquer(table)
