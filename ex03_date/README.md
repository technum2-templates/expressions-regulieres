# Exercice 3 - Date

**Niveau :** [Moyen]
**Temps estimé :** 10 minutes
**Concepts :** `\d{n}`, séparateurs littéraux, combinaison de blocs

## Objectif

Construire un pattern regex qui matche une date au format `DD/MM/YYYY`.

## Instructions

1. Ouvrez [regex101.com](https://regex101.com) et sélectionnez le flavour **Python**
2. Collez le texte de test ci-dessous dans la zone *Test String*
3. Construisez votre pattern dans le champ *Regular Expression*
4. Vérifiez que seules les dates valides sont matchées

## Texte de test

```text
25/12/2025
01/01/2000
1/1/2025
25-12-2025
25/12/25
bonjour
```

## Critères de réussite

- [ ] `25/12/2025` est matché ✅
- [ ] `01/01/2000` est matché ✅
- [ ] `1/1/2025` (un seul chiffre) n'est pas matché ✅
- [ ] `25-12-2025` (mauvais séparateur) n'est pas matché ✅
- [ ] `25/12/25` (année sur 2 chiffres) n'est pas matché ✅

## Indices

- Jour : 2 chiffres → `\d{2}`
- Séparateur `/` : caractère littéral (pas besoin de l'échapper en Python)
- Mois : 2 chiffres
- Année : 4 chiffres
