# Exercice 2 - Codes produits

**Niveau :** [Moyen]
**Temps estimé :** 10 minutes
**Concepts :** Classes de caractères `[A-Z]`, `\d`, quantificateurs `{n}`

## Objectif

Construire un pattern regex qui matche des codes produits au format `PROD-A123` ou
`PROD-B4567`.

## Instructions

1. Ouvrez [regex101.com](https://regex101.com) et sélectionnez le flavour **Python**
2. Collez le texte de test ci-dessous dans la zone *Test String*
3. Construisez votre pattern dans le champ *Regular Expression*
4. Vérifiez que seuls les codes valides sont matchés

## Texte de test

```text
PROD-A123
PROD-B4567
prod-A123
PROD-1234
PROD-AB12
PROD-
bonjour
```

## Critères de réussite

- [ ] `PROD-A123` est matché ✅
- [ ] `PROD-B4567` est matché ✅
- [ ] `prod-A123` (minuscules) n'est pas matché ✅
- [ ] `PROD-1234` (pas de lettre) n'est pas matché ✅
- [ ] `PROD-AB12` (deux lettres) n'est pas matché ✅
- [ ] `PROD-` (incomplet) n'est pas matché ✅

## Indices

- Le préfixe `PROD-` est un littéral
- Une seule lettre majuscule : `[A-Z]`
- Suivi de chiffres : combien ? Regardez les exemples — le nombre de chiffres varie
  entre 3 et 4. Quel quantificateur utiliser ?
