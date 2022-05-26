'''
Module tabledonnees
Auteurs : Deneuville Ludovic, Trotta Jean-Philippe et Villacampa Laurene
Date    : 05/05/2022
Licence : Domaine public
Version : 1.0
'''
import unittest
from tabledonnees import TableDonnees


class TableDonneesTest(unittest.TestCase):

    ma_table = TableDonnees(nom="t1",
                            donnees_avec_entete=[["id",  "mat", "date", "taille"],
                                                 ["id1", "A", "20120101", "160"],
                                                 ["id2", "B", "20060920", "180"],
                                                 ["id3", "C", "20060920", "na"],
                                                 ["id4", "D", "20010525", "165"],
                                                 ["id5", "na", "19860525", "175"]],
                            identifiants=["id", "mat"],
                            valeur_manquante="na")

    def test_creation_table(self):
        self.ma_table.afficher()
        print(self.ma_table)

        # resultat de determiner_formats
        self.assertEqual(list(self.ma_table.determiner_formats()), [
                         'str', 'str', 'date', 'float'])

        # application des formats
        self.assertEqual(list(self.ma_table.type_var), [
                         'str', 'str', 'date', 'float'])
        self.assertIsInstance(self.ma_table.donnees[0][3], float)

        # nombre de lignes
        self.assertTrue(len(self.ma_table.donnees) == 5)
        # nombre de variables
        self.assertTrue(len(self.ma_table.variables) == 4)
        # nombre de valeur manque d'une variable
        self.assertTrue(self.ma_table.compte_na("taille") == 1)
        self.assertTrue(self.ma_table.compte_na("mat") == 1)


if __name__ == '__main__':
    unittest.main()
