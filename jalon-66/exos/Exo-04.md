---
uuid: "jalon-66-exo-04"
title: "Exercice 4 - Jalon 66"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 4 : Séries et intégrale pour la mesure de comptage

**Énoncé :**
Soit $X = \mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$ (c'est-à-dire $\mu(A) = \text{card}(A)$ si $A$ est fini, et $+\infty$ sinon).
Soit $f : \mathbb{N} \to \mathbb{R}_+$ une fonction positive.
Démontrer rigoureusement en utilisant la définition du supremum que :
$$\int_{\mathbb{N}} f \, d\mu = \sum_{n=0}^{+\infty} f(n)$$

**Corrigé :**
Soit $f : \mathbb{N} \to \mathbb{R}_+$.
Par définition, $\int_{\mathbb{N}} f \, d\mu = \sup \{ \int s \, d\mu \mid s \in \mathcal{E}^+, 0 \le s \le f \}$.

**1. Minoration par la série (ou somme finie)**
Pour tout entier $N \in \mathbb{N}$, définissons la fonction simple $s_N$ :
$$s_N(k) = \begin{cases} f(k) & \text{si } 0 \le k \le N \\ 0 & \text{si } k > N \end{cases}$$
$s_N$ est bien une fonction simple positive car elle prend un nombre fini de valeurs non nulles. Elle peut s'écrire $s_N = \sum_{k=0}^N f(k) \mathbf{1}_{\{k\}}$.
Il est évident que $0 \le s_N \le f$.
Calculons l'intégrale de $s_N$ :
$$\int_{\mathbb{N}} s_N \, d\mu = \sum_{k=0}^N f(k) \mu(\{k\}) = \sum_{k=0}^N f(k) \times 1 = \sum_{k=0}^N f(k)$$
Puisque $s_N$ fait partie de l'ensemble sur lequel on prend le supremum pour définir $\int f d\mu$, on a nécessairement :
$$\int_{\mathbb{N}} f \, d\mu \ge \int_{\mathbb{N}} s_N \, d\mu = \sum_{k=0}^N f(k)$$
Cette inégalité étant vraie pour tout $N$, on peut passer à la limite (le membre de droite est une série à termes positifs, donc la limite existe dans $[0, +\infty]$) :
$$\int_{\mathbb{N}} f \, d\mu \ge \sum_{k=0}^{+\infty} f(k)$$

**2. Majoration de l'intégrale**
Soit $s$ une fonction simple quelconque telle que $0 \le s \le f$.
Puisque $s$ est simple et que $s(n) \le f(n)$ pour tout $n$, et $s$ a un support fini ou prend ses valeurs constantes sur des ensembles infinis. Si $s$ est non nulle sur un ensemble infini, $\int s \, d\mu = +\infty$. Mais comme $s \le f$, $f$ serait minorée par une constante positive sur un ensemble infini, donc la série divergerait vers $+\infty$, respectant l'égalité.
Supposons que $s$ soit nulle en dehors d'un ensemble fini $K \subset \mathbb{N}$.
$$\int_{\mathbb{N}} s \, d\mu = \sum_{k \in K} s(k) \mu(\{k\}) = \sum_{k \in K} s(k)$$
Puisque $s \le f$, $s(k) \le f(k)$ pour tout $k$.
$$\int_{\mathbb{N}} s \, d\mu \le \sum_{k \in K} f(k) \le \sum_{k=0}^{+\infty} f(k)$$
(La dernière inégalité provient de la positivité de $f$).
Ainsi, le nombre $\sum_{k=0}^{+\infty} f(k)$ est un majorant de l'ensemble $\{ \int s \, d\mu \mid s \in \mathcal{E}^+, 0 \le s \le f \}$.
Par définition du supremum (le plus petit des majorants) :
$$\int_{\mathbb{N}} f \, d\mu \le \sum_{k=0}^{+\infty} f(k)$$

**Conclusion :**
Les deux inégalités donnent l'égalité : $\int_{\mathbb{N}} f \, d\mu = \sum_{k=0}^{+\infty} f(k)$.
