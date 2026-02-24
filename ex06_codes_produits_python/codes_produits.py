"""
Module codes_produits - Extraction de codes produits dans un texte.
"""

import re


def extraire_codes(texte: str) -> list:
    """
    Extrait tous les codes produits du type PROD-A123 ou PROD-B4567
    présents dans un texte.

    Args:
        texte (str): Le texte à analyser

    Returns:
        list: La liste des codes produits trouvés (liste vide si aucun)
    """
    # TODO: définissez le pattern regex
    pattern = r""
    return re.findall(pattern, texte)
