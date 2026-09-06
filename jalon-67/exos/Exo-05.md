---
uuid: "exo-67-05"
title: "Exercice 05 : Interversion pour une série double"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 05 : Interversion pour une série double ($\bigstar\bigstar\bigstar\star\star$)

## Énoncé

Soit $(a_{i,j})$ une suite double telle que $a_{i,j} \ge 0$ pour tous $i, j \in \mathbb{N}$. Démontrer que $\sum_{i=0}^\infty \sum_{j=0}^\infty a_{i,j} = \sum_{j=0}^\infty \sum_{i=0}^\infty a_{i,j}$ en utilisant la mesure de comptage.

## Corrigé Rigoureux

1. **Cadre de la mesure :** On se place sur l'espace mesurable $(\mathbb{N}, \mathcal{P}(\mathbb{N}))$ muni de la mesure de comptage $\mu$. L'intégrale d'une fonction positive $f$ sur $\mathbb{N}$ est $\int_{\mathbb{N}} f d\mu = \sum_{j=0}^\infty f(j)$.
2. **Suite croissante :** Pour un point $j \in \mathbb{N}$, définissons $f_n(j) = \sum_{i=0}^n a_{i,j}$. Puisque $a_{i,j} \ge 0$, on a $f_{n+1}(j) = f_n(j) + a_{n+1,j} \ge f_n(j)$. La suite de fonctions $(f_n)$ est donc croissante.
3. **Beppo Levi :** Le théorème nous donne $\lim_n \int f_n d\mu = \int \lim_n f_n d\mu$.
L'intégrale de $f_n$ est $\int f_n d\mu = \sum_{j=0}^\infty \sum_{i=0}^n a_{i,j}$. Sa limite est $\sum_{j=0}^\infty \sum_{i=0}^\infty a_{i,j}$ (en inversant l'ordre des limites si la première est finie, mais ici tout est positif).
De l'autre côté, la limite ponctuelle de $f_n(j)$ est $f(j) = \sum_{i=0}^\infty a_{i,j}$. Son intégrale est $\int f d\mu = \sum_{j=0}^\infty \left( \sum_{i=0}^\infty a_{i,j} \right)$.
Ceci prouve l'égalité stricte des sommations dans n'importe quel ordre pour des termes positifs.
