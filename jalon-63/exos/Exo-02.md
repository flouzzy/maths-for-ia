---
uuid: "exo-jalon-63-02"
title: "Exercice 2 : La mesure de comptage"
difficulty: "$\bigstar\star\star\star\star$"
---

# La mesure de comptage

## Énoncé

Soit $X$ un ensemble. On définit l'application $c : \mathcal{P}(X) \to [0, +\infty]$ par $c(A) = \text{Card}(A)$ si $A$ est un ensemble fini, et $c(A) = +\infty$ si $A$ est infini. Montrer que $c$ est une mesure sur $(X, \mathcal{P}(X))$.

## Correction Détaillée

1. **Mesure de l'ensemble vide :**
L'ensemble vide est fini et ne contient aucun élément. Son cardinal est nul, donc $c(\emptyset) = 0$.

2. **$\sigma$-additivité :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite de parties disjointes de $X$. Posons $A = \bigcup_{n=0}^{+\infty} A_n$.
- **Cas 1 : Il existe au moins un $k$ tel que $A_k$ soit infini.**
  Alors $A$, qui contient $A_k$, est également infini. Par définition, $c(A) = +\infty$.
  De plus, la série à termes positifs $\sum_{n=0}^{+\infty} c(A_n)$ contient le terme $c(A_k) = +\infty$. Ainsi, la somme vaut $+\infty$. L'égalité tient.
- **Cas 2 : Il existe une infinité d'indices $k$ tels que $A_k$ est non vide (et fini).**
  L'union disjointe d'une infinité d'ensembles non vides est un ensemble infini, donc $c(A) = +\infty$.
  La série $\sum_{n=0}^{+\infty} c(A_n)$ contient une infinité de termes strictement positifs (des entiers $\geq 1$). La série diverge donc vers $+\infty$. L'égalité tient.
- **Cas 3 : Seul un nombre fini d'ensembles $A_n$ sont non vides, et ils sont tous finis.**
  Soit $N$ le plus grand indice tel que $A_N \neq \emptyset$. Alors $A = \bigcup_{n=0}^{N} A_n$.
  L'union finie d'ensembles finis est finie. Le cardinal d'une union finie d'ensembles disjoints est la somme des cardinaux.
  Donc $c(A) = \sum_{n=0}^{N} \text{Card}(A_n) = \sum_{n=0}^{+\infty} c(A_n)$ (puisque les termes pour $n > N$ valent 0).

La $\sigma$-additivité est démontrée dans tous les cas de figure. $\blacksquare$
