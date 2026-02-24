"""
Tests pour le module analyse_logs.

Pour lancer les tests :
    python test_analyse_logs.py
ou
    python -m unittest test_analyse_logs.py
"""

import unittest
from analyse_logs import extraire_timestamp, extraire_niveau, analyser_fichier


class TestExtraireTimestamp(unittest.TestCase):
    """Tests pour la fonction extraire_timestamp()."""

    def test_ligne_valide(self):
        ligne = "2024-03-15 08:17:45 ERROR Échec de l'écriture en base"
        self.assertEqual(extraire_timestamp(ligne), "2024-03-15 08:17:45")

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Une ligne sans timestamp (ex: "[corrupted line without timestamp]")
    # - Une ligne avec une date incomplète (ex: "2024-03-15 08:17 ERROR ...")


class TestExtraireNiveau(unittest.TestCase):
    """Tests pour la fonction extraire_niveau()."""

    def test_niveau_error(self):
        ligne = "2024-03-15 08:17:45 ERROR Échec de l'écriture en base"
        self.assertEqual(extraire_niveau(ligne), "ERROR")

    def test_niveau_warning(self):
        ligne = "2024-03-15 08:14:22 WARNING Temps de réponse élevé"
        self.assertEqual(extraire_niveau(ligne), "WARNING")

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Niveau INFO
    # - Niveau CRITICAL
    # - Une ligne sans niveau valide


class TestAnalyserFichier(unittest.TestCase):
    """Tests pour la fonction analyser_fichier()."""

    def test_fichier_simple_nombre_entrees(self):
        resultats = analyser_fichier("app_simple.log")
        self.assertEqual(len(resultats), 7)

    def test_fichier_simple_premiere_entree(self):
        resultats = analyser_fichier("app_simple.log")
        self.assertEqual(resultats[0]["timestamp"], "2024-03-15 08:12:03")
        self.assertEqual(resultats[0]["niveau"], "INFO")

    def test_fichier_mixed_ignore_lignes_invalides(self):
        resultats = analyser_fichier("app_mixed.log")
        # app_mixed.log contient 9 lignes dont 2 invalides --> 7 entrées valides
        self.assertEqual(len(resultats), 7)

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Vérifier le timestamp de la dernière entrée de app_simple.log
    # - Vérifier que app_mixed.log contient bien une entrée CRITICAL
    # - Vérifier le message d'une entrée spécifique


if __name__ == "__main__":
    unittest.main()
