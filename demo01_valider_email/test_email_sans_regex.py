# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import unittest
from email_sans_regex import est_email_valide


class TestEstEmailValide(unittest.TestCase):
    def test_email_classique(self):
        self.assertTrue(est_email_valide("jean.dupont@example.com"))

    def test_email_court(self):
        self.assertTrue(est_email_valide("j@x.be"))

    def test_sans_arobase(self):
        self.assertFalse(est_email_valide("invalide"))

    def test_deux_arobase(self):
        self.assertFalse(est_email_valide("deux@@arrobas.com"))

    def test_sans_extension(self):
        self.assertFalse(est_email_valide("manque_extension@example"))

    def test_avec_espace(self):
        # Ce test va échouer : la version sans regex ne détecte pas les espaces.
        # C'est un des bugs que la regex corrige.
        self.assertFalse(est_email_valide("espace inclus@example.com"))

    def test_partie_locale_vide(self):
        self.assertFalse(est_email_valide("@example.com"))

    def test_sous_partie_domaine_vide(self):
        self.assertFalse(est_email_valide("jean@.com"))


if __name__ == "__main__":
    unittest.main()
