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

### Exercices Python avec unittest (ex05 à ex07)

Ces exercices se font dans votre éditeur de code.

1. Naviguez dans le dossier de l'exercice : `cd ex05_telephone_python`
2. Lisez le `README.md` pour comprendre l'objectif
3. Ouvrez le fichier de test et complétez les tests
4. Lancez les tests : `python test_telephone.py`
5. Appelez votre enseignant pour un feedback sur votre solution

### Structure des exercices

- Exercices Regex101 : `README.md` uniquement (énoncé, texte de test, critères, indices)
- Exercices Python : `README.md` + `module.py` (code fourni) + `test_module.py` (à compléter)

## Liste des exercices

### Séance 3 - Introduction aux expressions régulières

| Exercice | Outil | Niveau | Temps | Concepts |
| --- | --- | --- | --- | --- |
| ex01_telephone | Regex101 | [Facile] | 10 min | `\d`, `{n}`, séparateurs littéraux |
| ex02_codes_produits | Regex101 | [Moyen] | 10 min | `[A-Z]`, `\d`, `{n,m}` |
| ex03_date | Regex101 | [Moyen] | 10 min | `\d{n}`, combinaison de blocs |
| ex04_plaque | Regex101 | [Moyen] | 10 min | `[A-Z]{n}`, combinaison de blocs |
| ex05_telephone_python | Python | [Facile] | 10 min | `re.match()`, pattern à écrire |
| ex06_codes_produits_python | Python | [Moyen] | 15 min | `re.findall()`, pattern à écrire |
| ex07_email_python | Python | [Difficile] | 30 min | Pattern email, filtrage de liste |
| ex08_logs_python | Python | [Difficile] | 30 min | Extraction depuis données réelles |

## Conseils

### Sur Regex101

1. **Construisez progressivement** : ajoutez un bloc à la fois et vérifiez à chaque étape
2. **Il y a souvent plusieurs bonnes réponses** : ce qui compte, c'est la lisibilité et la correction
3. **Testez les cas qui ne doivent PAS matcher** autant que ceux qui doivent matcher

### Sur les exercices Python

1. **Réutilisez vos patterns** de Regex101 — ils fonctionnent tels quels en Python
2. **Lancez souvent** : vérifiez vos tests régulièrement
3. **Lisez les erreurs** : les messages d'erreur sont vos amis

## Ressources

- [regex101.com](https://regex101.com) — outil interactif indispensable
- [Documentation re — Python](https://docs.python.org/3/library/re.html)
