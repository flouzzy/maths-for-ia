---
uuid: "jalon-67-exo-08"
title: "Exercice 08 - Espace des séries l^p"
difficulty: "\bigstar\bigstar\bigstar\bigstar\star"
---

# Exercice 08 - Espace des séries l^p

## Énoncé

On considère l'espace $\mathbb{N}$ muni de la mesure de comptage $\mu$. Montrer, à l'aide du TCM, que si une suite complexe double $(a_{i,j})$ vérifie $\sum_i (\sum_j |a_{i,j}|) < \infty$, alors on peut intervertir les sommes infinies.

## Correction Détaillée

1. **Cadre de la mesure :**
La sommation d'une série numérique correspond à l'intégrale par rapport à la mesure de comptage.
Posons $f_n(i) = \sum_{j=0}^n |a_{i,j}|$. La suite de fonctions $(f_n)_{n \in \mathbb{N}}$ (définies sur $\mathbb{N}$) est à valeurs positives.

2. **Croissance :**
Puisque $|a_{i,j}| \ge 0$, on a $f_n(i) \le f_{n+1}(i)$. La suite de fonctions $(f_n)$ est croissante.

3. **Application du TCM :**
Par le TCM, l'intégrale de la limite est la limite des intégrales :
$\int_\mathbb{N} \left( \lim_{n \to \infty} f_n(i) \right) d\mu(i) = \lim_{n \to \infty} \int_\mathbb{N} f_n(i) d\mu(i)$
Ce qui s'écrit formellement :
$\sum_{i=0}^\infty \left( \sum_{j=0}^\infty |a_{i,j}| \right) = \lim_{n \to \infty} \sum_{i=0}^\infty \left( \sum_{j=0}^n |a_{i,j}| \right)$

4. **Conclusion de l'interversion (Fubini-Tonelli discret) :**
La somme finie sur $j$ peut être intervertie avec la somme sur $i$. Le TCM prouve donc rigoureusement que pour des termes positifs (ici la valeur absolue), on peut Sommer dans n'importe quel ordre. La condition de finitude permet ensuite d'étendre cela aux séries de termes non positifs (théorème de Fubini discret).
