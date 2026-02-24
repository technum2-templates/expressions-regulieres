# Exercice 4 - Plaque d'immatriculation belge

**Niveau :** [Moyen]
**Temps estimé :** 10 minutes
**Concepts :** Classes `[A-Z]`, `\d`, quantificateurs `{n}`, combinaison de blocs

## Objectif

Construire un pattern regex qui matche une plaque d'immatriculation belge au format
`1-ABC-234`.

## Instructions

1. Ouvrez [regex101.com](https://regex101.com) et sélectionnez le flavour **Python**
2. Collez le texte de test ci-dessous dans la zone *Test String*
3. Construisez votre pattern dans le champ *Regular Expression*
4. Vérifiez que seules les plaques valides sont matchées

## Texte de test

```text
1-ABC-234
1-abc-234
1-AB-234
1-ABCD-234
1-ABC-23
ABC-234
```

## Critères de réussite

- [ ] `1-ABC-234` est matché ✅
- [ ] `1-abc-234` (minuscules) n'est pas matché ✅
- [ ] `1-AB-234` (deux lettres) n'est pas matché ✅
- [ ] `1-ABCD-234` (quatre lettres) n'est pas matché ✅
- [ ] `1-ABC-23` (deux chiffres finaux) n'est pas matché ✅
- [ ] `ABC-234` (pas de chiffre initial) n'est pas matché ✅

## Indices

- Le format est : 1 chiffre, tiret, 3 lettres majuscules, tiret, 3 chiffres
- 3 lettres majuscules : `[A-Z]{3}`
- Combinez les blocs que vous connaissez déjà
