---
uuid: "exo-21-09"
title: "Exercice 9 : Théorème de Dini"
difficulty: 5
---

# Exercice 9 : Théorème de Dini

**Niveau :** $★★★★★$

## Problème

Démontrer le théorème de Dini : si une suite $(f_n)$ de fonctions continues réelles converge simplement sur un compact $K$ vers une fonction continue $f$, et si la suite $(f_n)$ est monotone croissante (resp. décroissante), alors la convergence est uniforme.

## Démonstration et Solution

**Théorème de Dini :** Soit $K$ un espace compact (par exemple un segment fermé borné de $\mathbb{R}$). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions continues de $K$ dans $\mathbb{R}$. Si $(f_n)$ converge simplement sur $K$ vers une fonction continue $f$, et si la suite $(f_n)$ est monotone en tout point (par exemple décroissante : $\forall x \in K, \forall n, f_{n+1}(x) \leq f_n(x)$), alors la convergence est uniforme sur $K$.

**Démonstration formelle (Cas décroissant) :**
Définissons la suite de fonctions auxiliaire $g_n = f_n - f$.
Puisque chaque $f_n$ est continue et $f$ est continue, par combinaison linéaire, chaque $g_n$ est une fonction continue sur le compact $K$.
La suite $(f_n)$ étant décroissante vers $f$, nous avons pour tout $x \in K$ et tout entier $n$, $f_n(x) \geq f_{n+1}(x) \geq f(x)$.
En soustrayant $f(x)$, cela implique $g_n(x) \geq g_{n+1}(x) \geq 0$. La suite $(g_n)$ est donc une suite de fonctions continues, positives et décroissante vers 0.
Démontrer la convergence uniforme de $(f_n)$ vers $f$ équivaut à démontrer la convergence uniforme de $(g_n)$ vers la fonction nulle 0.
Soit un réel arbitraire $\epsilon > 0$.
Pour chaque entier $n \in \mathbb{N}$, définissons l'ensemble de niveau $O_n$ :
$O_n = \{x \in K \mid g_n(x) < \epsilon\}$.
Puisque la fonction $g_n$ est continue, et que l'intervalle $]-\infty, \epsilon[$ est un sous-ensemble ouvert de $\mathbb{R}$, l'image réciproque $O_n = g_n^{-1}(]-\infty, \epsilon[)$ est un ensemble ouvert de $K$.
De plus, comme la suite $(g_n)$ est décroissante, si $g_n(x) < \epsilon$, alors a fortiori $g_{n+1}(x) \leq g_n(x) < \epsilon$. Cela implique rigoureusement l'inclusion ensembliste : $O_n \subset O_{n+1}$. La suite d'ouverts $(O_n)$ est croissante.
Montrons que ces ouverts recouvrent $K$. Pour tout $x \in K$, par la convergence simple de $g_n$ vers 0, on a $\lim_{n \to \infty} g_n(x) = 0$. Donc, par définition de la limite, il existe un rang $N_x$ (qui dépend de $x$) tel que $g_{N_x}(x) < \epsilon$, ce qui signifie que $x \in O_{N_x}$.
Ainsi, l'union infinie $\bigcup_{n \in \mathbb{N}} O_n$ couvre intégralement $K$.
La famille $(O_n)_{n \in \mathbb{N}}$ constitue donc un recouvrement ouvert du compact $K$.
Par la propriété fondamentale de Borel-Lebesgue (définition de la compacité), il est possible d'en extraire un sous-recouvrement fini. Il existe donc un ensemble fini d'indices $\{n_1, n_2, \dots, n_k\}$ tel que $K \subset O_{n_1} \cup O_{n_2} \cup \dots \cup O_{n_k}$.
Posons $N = \max(n_1, n_2, \dots, n_k)$. Puisque la suite d'ouverts est emboîtée de manière croissante ($O_p \subset O_q$ pour $p < q$), l'union finie est égale à son plus grand élément : $O_{n_1} \cup \dots \cup O_{n_k} \subset O_N$.
Nous obtenons alors $K \subset O_N$.
Cela signifie que pour tout $x \in K$, on a $x \in O_N$, c'est-à-dire rigoureusement $0 \leq g_N(x) < \epsilon$.
Enfin, par la décroissance de la suite $(g_n)$, pour tout $n \geq N$ et pour tout $x \in K$, on a $0 \leq g_n(x) \leq g_N(x) < \epsilon$.
En passant au supremum, on obtient que pour tout $n \geq N$, $\sup_{x \in K} g_n(x) \leq \epsilon$.
Ceci est la définition stricte de la limite uniforme de $(g_n)$ vers 0, prouvant le théorème.
