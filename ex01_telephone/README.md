# Exercice 1 - Numéro de téléphone belge

**Niveau :** [Facile]
**Temps estimé :** 10 minutes
**Concepts :** Caractères littéraux, `\d`, quantificateurs `{n}`, séparateurs

## Objectif

Construire un pattern regex qui matche un numéro de téléphone belge au format `0486/12.34.56`.

## Instructions

1. Ouvrez [regex101.com](https://regex101.com) et sélectionnez le flavour **Python**
2. Collez le texte de test ci-dessous dans la zone *Test String*
3. Construisez votre pattern dans le champ *Regular Expression*
4. Vérifiez que seuls les numéros valides sont matchés

## Texte de test

```text
0486/12.34.56
0032/12.34.56
bonjour
123
0486/12.34
0486-12.34.56
```

## Critères de réussite

- [ ] `0486/12.34.56` est matché ✅
- [ ] `0032/12.34.56` est matché ✅
- [ ] `bonjour` n'est pas matché ✅
- [ ] `123` n'est pas matché ✅
- [ ] `0486/12.34` (incomplet) n'est pas matché ✅
- [ ] `0486-12.34.56` (mauvais séparateur) n'est pas matché ✅

## Indices

- Le numéro commence par 4 chiffres : `\d{4}`
- Suivi du séparateur `/` (caractère littéral)
- Puis 2 chiffres, un point `.` littéral (attention : `.` est un métacaractère, comment
  l'échapper ?), 2 chiffres, un point, 2 chiffres
