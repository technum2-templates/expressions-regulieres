"""
Tests pour le module telephone.

Pour lancer les tests :
    python test_telephone.py
ou
    python -m unittest test_telephone.py
"""

import unittest
from telephone import est_valide_telephone


class TestEstValideTelephone(unittest.TestCase):
    """Tests pour la fonction est_valide_telephone()."""

    def test_numero_valide(self):
        self.assertTrue(est_valide_telephone("0486/12.34.56"))

    # TODO: ajoutez des tests pour les cas suivants :
    #
    # - Un numéro incomplet (ex: "0486/12.34")
    # - Un numéro avec un mauvais séparateur (ex: "0486-12.34.56")
    # - Une chaîne sans rapport (ex: "bonjour")


if __name__ == "__main__":
    unittest.main()
