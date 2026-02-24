# Exercice 7 - Nettoyage de données (Python)

**Niveau :** [Difficile]
**Temps estimé :** 30 minutes
**Concepts :** `re.match()`, filtrage de liste, pattern email

## Objectif

Implémenter la fonction `nettoyer_donnees()` qui filtre une liste de chaînes et retourne
uniquement celles qui ressemblent à une adresse email simple (format `xxx@xxx.xxx`).

## Instructions

1. Ouvrez `email.py`
2. Définissez le pattern regex dans la variable `pattern`
3. Lancez les tests : `python test_email.py`
4. Tous les tests passent ? Ajoutez vos propres tests pour les cas limites (voir TODO dans
   le fichier de test)

## Critères de réussite

- [ ] `["jean@example.com", "bonjour"]` retourne `["jean@example.com"]`
- [ ] Une liste sans email retourne `[]`
- [ ] Une liste vide retourne `[]`
- [ ] Plusieurs emails mélangés à des invalides : seuls les emails sont retournés
- [ ] Tous les tests passent ✅

## Contraintes du pattern

Un email valide pour cet exercice :

- une partie locale : lettres, chiffres, `.`, `-`, `_`
- un `@`
- un domaine : lettres, chiffres, `-`
- un `.`
- une extension d'au moins 2 caractères

## Indice

Contrairement aux exercices 5 et 6, vous n'avez pas construit ce pattern sur Regex101.
Construisez-le bloc par bloc, comme vous l'avez fait pendant la démo.
La structure de la fonction (boucle sur la liste) est déjà en place — concentrez-vous
sur le pattern.
