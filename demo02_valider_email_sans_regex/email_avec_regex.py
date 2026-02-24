import re


def est_email_valide(adresse):
    pattern = r"[\w\.-]+@[\w-]+\.[\w\.]+"
    return bool(re.match(pattern, adresse))
