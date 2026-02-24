"""
Tests pour le module codes_produits.

Pour lancer les tests :
    python test_codes_produits.py
ou
    python -m unittest test_codes_produits.py
"""

import unittest
from codes_produits import extraire_codes


class TestExtraireCodes(unittest.TestCase):
    """Tests pour la fonction extraire_codes()."""

    def test_texte_avec_un_code(self):
        self.assertListEqual(extraire_codes("Commandez PROD-A123 maintenant."), ["PROD-A123"])

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Un texte avec plusieurs codes
    # - Un texte sans aucun code
    # - Un code en minuscules (ex: "prod-a123") --> ne doit pas être extrait


if __name__ == "__main__":
    unittest.main()
