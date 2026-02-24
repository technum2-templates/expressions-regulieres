# Exercices - Expressions régulières avec Python

Ce répertoire contient les exercices pour apprendre les expressions régulières en Python.

## Comment utiliser ces exercices

### Exercices sur Regex101 (ex01 à ex04)

Ces exercices se font entièrement dans le navigateur, sans Python.

1. Ouvrez [regex101.com](https://regex101.com)
2. Sélectionnez le flavour **Python** dans le panneau gauche
3. Lisez le `README.md` de l'exercice pour comprendre l'objectif
4. Construisez votre pattern dans le champ *Regular Expression*
5. Vérifiez vos critères de réussite un par un
6. Appelez votre enseignant pour un feedback sur votre solution

### Structure d'un exercice Regex101

Chaque exercice contient :

- `README.md` : Énoncé, texte de test, critères de réussite, indices

## Liste des exercices

### Séance 3 - Introduction aux expressions régulières

| Exercice | Niveau | Temps | Concepts |
| --- | --- | --- | --- |
| ex01_telephone | [Facile] | 10 min | `\d`, `{n}`, séparateurs littéraux |
| ex02_codes_produits | [Moyen] | 10 min | `[A-Z]`, `\d`, `{n,m}` |
| ex03_date | [Moyen] | 10 min | `\d{n}`, combinaison de blocs |
| ex04_plaque | [Moyen] | 10 min | `[A-Z]{n}`, combinaison de blocs |

## Conseils

1. **Construisez progressivement** : ajoutez un bloc à la fois et vérifiez à chaque étape
2. **Regex101 est votre ami** : la coloration en temps réel vous dit immédiatement si ça matche
3. **Il y a souvent plusieurs bonnes réponses** : ce qui compte, c'est la lisibilité et la correction
4. **Testez les cas qui ne doivent PAS matcher** autant que ceux qui doivent matcher

## Ressources

- [regex101.com](https://regex101.com) — outil interactif indispensable
- [Documentation re — Python](https://docs.python.org/3/library/re.html)
