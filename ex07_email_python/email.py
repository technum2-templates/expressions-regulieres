"""
Module email - Filtrage d'adresses email dans une liste de chaînes.
"""

import re


def nettoyer_donnees(lignes: list) -> list:
    """
    Filtre une liste de chaînes et retourne uniquement celles qui
    ressemblent à une adresse email simple (format xxx@xxx.xxx).

    Args:
        lignes (list): La liste de chaînes à filtrer

    Returns:
        list: La liste des chaînes qui sont des adresses email valides
    """
    # TODO: définissez le pattern regex et filtrez la liste
    pattern = r""
    return [ligne for ligne in lignes if re.match(pattern, ligne)]
