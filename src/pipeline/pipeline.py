'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
from transformation.export import Export


class Pipeline:
    '''Classe implémentant un pipeline, liste d'opérations à réaliser. 

    Attributes
    ----------
    nom : str
        Nom du pipeline
    liste_operations : list[Transformation, Estimateur, LienVar]
        liste des opérations qui seront appliquées
    '''
    # DONE    proposition : remplacer l'attribut liste_transformation par liste_operation (où la dernière? opération est un estimateur ou lienvar)
    # OK      si estimateur et lienvar ne modifie pas la table initiale, inutile qu'ils soient en dernier d'ailleurs
    # DONE    supprimer l'attibut estimateur en conséquent, idemem pour les paramètres de init
    # DONE    supprimer aussi le paramètre exporter_table
    # question : et si on veut exporter la table du return de estimateur (pas celle sur laquelle le pipeline est appliqué), que faire ?
    # TODO cf UML : méthodes ajouter_oper et supprimer_oper ? (pas sûre que ce soit nécessaire ? -> manipulation de listes ?)

    def __init__(self, nom, liste_transformations):
        '''Constructeur de l'objet

        Parameters
        ----------
        nom : str
            Nom du pipeline
        liste_transformations : list[Transformation]
            liste des transformations qui seront appliquées
        exporter_table : bool
            Si True le fichier est exporté dans donnees/export
            False par défaut
        '''
        self.nom = nom
        self.liste_transformations = liste_transformations

    def lancer(self, table):
        '''Lancement du pipeline

        La liste des opérations est appliquée dans l'ordre à la table en paramètre

        Parameters
        ----------
        table : tableDonnees
            table de données à transformer

        Returns 
        -------
        table
            table de données mise à jour
        '''
        # TODO Question : y a-t-il vraiment un "Returns" ?

        print("------------------------------------------------------")
        print("Lancement du pipeline " + self.nom)

        # Pour chaque transformation de la liste
        for i in range(len(self.liste_transformations)):
            self.liste_transformations[i].appliquer(table)
