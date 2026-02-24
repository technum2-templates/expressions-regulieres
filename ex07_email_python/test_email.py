"""
Tests pour le module email.

Pour lancer les tests :
    python test_email.py
ou
    python -m unittest test_email.py
"""

import unittest
from email import nettoyer_donnees


class TestNettoyerDonnees(unittest.TestCase):
    """Tests pour la fonction nettoyer_donnees()."""

    def test_liste_avec_un_email_valide(self):
        self.assertEqual(
            nettoyer_donnees(["jean@example.com", "bonjour"]),
            ["jean@example.com"],
        )

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Une liste sans aucun email valide
    # - Une liste vide
    # - Plusieurs emails mélangés à des chaînes invalides


if __name__ == "__main__":
    unittest.main()
