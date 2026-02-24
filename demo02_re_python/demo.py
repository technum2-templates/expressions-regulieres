"""
Démonstration : utiliser le module re en Python.

Cette démo reprend les patterns construits sur Regex101 et les applique en Python.
Elle couvre re.match(), re.search() et re.findall().
"""

import re

# ============================================================
# RAPPEL : les patterns sont exactement les mêmes que sur Regex101.
# La différence, c'est qu'on les utilise à l'intérieur de fonctions Python.
# ============================================================

TELEPHONE = r"0\d{3}/\d{2}\.\d{2}\.\d{2}"
CODE_PRODUIT = r"PROD-[A-Z]\d{3,4}"

# ============================================================
# re.match() — valider un format
#
# re.match() cherche le pattern UNIQUEMENT au début de la chaîne.
# Il retourne un objet Match si ça matche, None sinon.
# On le convertit en bool avec bool().
# ============================================================

print("=== re.match() — validation ===")

numeros = [
    "0486/12.34.56",  # valide
    "0032/12.34.56",  # valide
    "0486/12.34",  # incomplet
    "bonjour",  # pas un numéro
]

for numero in numeros:
    est_valide = bool(re.match(TELEPHONE, numero))
    print(f"  {numero!r:25} --> {est_valide}")

# ============================================================
# re.search() — trouver la première occurrence dans un texte
#
# re.search() parcourt TOUTE la chaîne et retourne le premier match.
# Utile quand le pattern peut se trouver n'importe où dans le texte.
# ============================================================

print("\n=== re.search() — première occurrence ===")

textes = [
    "Appelez-moi au 0486/12.34.56 ce soir.",
    "Pas de numéro ici.",
    "0032/98.76.54 ou 0486/11.22.33",  # deux numéros : seul le premier est retourné
]

for texte in textes:
    match = re.search(TELEPHONE, texte)
    if match:
        print(f"  Trouvé : {match.group()!r}")
    else:
        print(f"  Rien trouvé dans : {texte!r}")

# ============================================================
# re.findall() — trouver TOUTES les occurrences
#
# re.findall() retourne une liste de toutes les chaînes matchées.
# Retourne une liste vide si rien n'est trouvé.
# ============================================================

print("\n=== re.findall() — toutes les occurrences ===")

catalogue = """
Références disponibles : PROD-A123, PROD-B4567, article-X, PROD-C99.
Rupture de stock : PROD-D456.
"""

codes = re.findall(CODE_PRODUIT, catalogue)
print(f"  Codes trouvés : {codes}")

# ============================================================
# Différence clé : re.match() vs re.search()
#
# re.match() --> ancré au DÉBUT. Équivalent à ^pattern.
# re.search() --> cherche PARTOUT dans la chaîne.
# ============================================================

print("\n=== match() vs search() ===")

texte = "Commandez le PROD-A123 maintenant."

print(f"  re.match()  : {re.match(CODE_PRODUIT, texte)}")  # None : ne commence pas par PROD-
print(f"  re.search() : {re.search(CODE_PRODUIT, texte)}")  # Match : trouvé dans le texte
