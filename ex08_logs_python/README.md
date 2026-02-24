# Exercice 8 - Analyse de fichiers de logs (Python)

**Niveau :** [Difficile]
**Temps estimé :** 30 minutes
**Concepts :** `re.match()`, `re.search()`, extraction depuis un texte réel

## Objectif

Implémenter deux fonctions d'extraction pour analyser des fichiers de logs :

- `extraire_timestamp(ligne)` --> extrait la date et l'heure
- `extraire_niveau(ligne)` --> extrait le niveau de log (`INFO`, `WARNING`, `ERROR`...)

Le squelette dans `analyse_logs.py` lit les fichiers et orchestre l'analyse — vous n'avez
qu'à écrire les deux fonctions d'extraction.

## Format d'une ligne de log valide

```text
2024-03-15 08:17:45 ERROR Échec de l'écriture en base : timeout après 30s
└─────────────────┘ └───┘ └─────────────────────────────────────────────┘
     timestamp      niveau                 message
```

## Instructions

1. Ouvrez `analyse_logs.py`
2. Implémentez `extraire_timestamp()` — elle doit retourner le timestamp ou `None`
3. Implémentez `extraire_niveau()` — elle doit retourner le niveau ou `None`
4. Lancez les tests : `python test_analyse_logs.py`
5. Tous les tests passent ? Ajoutez vos propres tests (voir TODO dans le fichier de test)

## Critères de réussite

- [ ] `extraire_timestamp("2024-03-15 08:17:45 ERROR ...")` retourne `"2024-03-15 08:17:45"`
- [ ] `extraire_timestamp("[corrupted line]")` retourne `None`
- [ ] `extraire_niveau("2024-03-15 08:17:45 ERROR ...")` retourne `"ERROR"`
- [ ] `extraire_niveau("2024-03-15 08:14:22 WARNING ...")` retourne `"WARNING"`
- [ ] `analyser_fichier("app_simple.log")` retourne 7 entrées
- [ ] `analyser_fichier("app_mixed.log")` ignore les 2 lignes invalides --> 7 entrées
- [ ] Tous les tests passent ✅

## Indices

- Le timestamp suit toujours le format `YYYY-MM-DD HH:MM:SS` — quels métacaractères
  et quantificateurs permettent de le capturer ?
- Le niveau est un mot en majuscules parmi : `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
- Pensez à utiliser `re.match()` si le pattern est toujours en début de ligne,
  `re.search()` si vous préférez chercher dans toute la ligne
- Si un match est trouvé, `.group()` retourne la chaîne matchée
