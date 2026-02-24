# Exercice 6 - Extraction de codes produits (Python)

**Niveau :** [Moyen]
**Temps estimé :** 15 minutes
**Concepts :** `re.findall()`, écriture d'un pattern en Python

## Objectif

Implémenter la fonction `extraire_codes()` qui extrait tous les codes produits (format `PROD-A123` ou `PROD-B4567`) présents dans un texte.

## Instructions

1. Ouvrez `codes_produits.py`
2. Définissez le pattern regex dans la variable `pattern`
3. Lancez les tests : `python test_codes_produits.py`
4. Tous les tests passent ? Ajoutez vos propres tests pour les cas limites (voir TODO dans le fichier de test)

## Critères de réussite

- [ ] `"Commandez PROD-A123 maintenant."` retourne `["PROD-A123"]`
- [ ] Un texte avec plusieurs codes retourne tous les codes dans l'ordre
- [ ] Un texte sans code retourne `[]`
- [ ] Un code en minuscules (`"prod-a123"`) n'est pas extrait
- [ ] Tous les tests passent ✅

## Indice

Vous avez construit ce pattern dans l'exercice 2 sur Regex101 — réutilisez-le.
Notez que `re.findall()` retourne directement une liste de chaînes.
