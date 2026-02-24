"""
Module telephone - Validation de numéros de téléphone belges.
"""

import re


def est_valide_telephone(numero: str) -> bool:
    """
    Vérifie si une chaîne est un numéro de téléphone belge valide.

    Le format attendu est : 0XXX/XX.XX.XX (ex: 0486/12.34.56)

    Args:
        numero (str): La chaîne à valider

    Returns:
        bool: True si le numéro est valide, False sinon
    """
    # TODO: définissez le pattern regex
    pattern = r""
    return bool(re.match(pattern, numero))
