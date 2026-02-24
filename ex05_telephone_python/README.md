# Exercice 5 - Validation de numéro de téléphone (Python)

**Niveau :** [Facile]
**Temps estimé :** 10 minutes
**Concepts :** `re.match()`, écriture d'un pattern en Python

## Objectif

Implémenter la fonction `est_valide_telephone()` qui vérifie si une chaîne est un numéro
de téléphone belge valide (format `0486/12.34.56`).

## Instructions

1. Ouvrez `telephone.py`
2. Définissez le pattern regex dans la variable `pattern`
3. Lancez les tests : `python test_telephone.py`
4. Tous les tests passent ? Ajoutez vos propres tests pour les cas limites (voir TODO dans
   le fichier de test)

## Critères de réussite

- [ ] `"0486/12.34.56"` retourne `True`
- [ ] `"0032/12.34.56"` retourne `True`
- [ ] `"0486/12.34"` (incomplet) retourne `False`
- [ ] `"0486-12.34.56"` (mauvais séparateur) retourne `False`
- [ ] `"bonjour"` retourne `False`
- [ ] Tous les tests passent ✅

## Indice

Vous avez construit ce pattern dans l'exercice 1 sur Regex101 — réutilisez-le.
