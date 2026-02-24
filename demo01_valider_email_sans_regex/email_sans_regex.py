def est_email_valide(adresse):
    # Vérifier qu'il y a exactement un @
    if adresse.count("@") != 1:
        return False

    partie_locale, domaine = adresse.split("@")

    # Vérifier que la partie locale n'est pas vide
    if len(partie_locale) == 0:
        return False

    # Vérifier que le domaine contient au moins un point
    if "." not in domaine:
        return False

    # Séparer le domaine en sous-parties
    sous_parties = domaine.split(".")

    # Vérifier qu'aucune sous-partie n'est vide
    for partie in sous_parties:
        if len(partie) == 0:
            return False

    # Vérifier que l'extension fait au moins 2 caractères
    if len(sous_parties[-1]) < 2:
        return False

    return True
