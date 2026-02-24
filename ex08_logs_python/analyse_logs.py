"""
Module analyse_logs - Extraction d'informations depuis des fichiers de logs.

Format d'une ligne de log valide :
    YYYY-MM-DD HH:MM:SS NIVEAU  Message...

Exemple :
    2024-03-15 08:17:45 ERROR Échec de l'écriture en base : timeout après 30s
"""

import re


def extraire_timestamp(ligne: str) -> str | None:
    """
    Extrait le timestamp d'une ligne de log.

    Args:
        ligne (str): Une ligne de log

    Returns:
        str | None: Le timestamp au format "YYYY-MM-DD HH:MM:SS", ou None si absent
    """
    # TODO: écrivez le pattern et l'extraction
    pass


def extraire_niveau(ligne: str) -> str | None:
    """
    Extrait le niveau de log d'une ligne de log.

    Les niveaux possibles sont : DEBUG, INFO, WARNING, ERROR, CRITICAL

    Args:
        ligne (str): Une ligne de log

    Returns:
        str | None: Le niveau de log (ex: "ERROR"), ou None si absent
    """
    # TODO: écrivez le pattern et l'extraction
    pass


def analyser_fichier(chemin: str) -> list[dict]:
    """
    Lit un fichier de logs et retourne la liste des lignes valides analysées.

    Chaque ligne valide est représentée par un dictionnaire :
        {"timestamp": "YYYY-MM-DD HH:MM:SS", "niveau": "ERROR", "message": "..."}

    Les lignes sans timestamp valide sont ignorées.

    Args:
        chemin (str): Chemin vers le fichier de logs

    Returns:
        list[dict]: La liste des entrées de log analysées
    """
    resultats = []
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.rstrip()
            timestamp = extraire_timestamp(ligne)
            niveau = extraire_niveau(ligne)
            if timestamp and niveau:
                message = ligne[len(timestamp) + len(niveau) + 2:].strip()
                resultats.append({
                    "timestamp": timestamp,
                    "niveau": niveau,
                    "message": message,
                })
    return resultats
