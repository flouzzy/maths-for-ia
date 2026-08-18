---
uuid: "exo-jalon-63-01"
title: "Exercice 1 : La mesure de Dirac"
difficulty: "$\bigstar\star\star\star\star$"
---

# La mesure de Dirac

## Énoncé

Soit $X$ un ensemble non vide et $a \in X$. On définit l'application $\delta_a : \mathcal{P}(X) \to [0, +\infty]$ par $\delta_a(A) = 1$ si $a \in A$ et $0$ sinon. Démontrer de manière exhaustive que $\delta_a$ est une mesure de probabilité sur $(X, \mathcal{P}(X))$.

## Correction Détaillée

1. **Mesure de l'ensemble vide :**
L'ensemble vide $\emptyset$ ne contient aucun élément, donc $a \notin \emptyset$. Par définition de $\delta_a$, on a $\delta_a(\emptyset) = 0$.

2. **$\sigma$-additivité :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles de $\mathcal{P}(X)$ deux à deux disjoints. Notons $A = \bigcup_{n=0}^{+\infty} A_n$.
Nous distinguons deux cas exhaustifs et mutuellement exclusifs :
- **Cas 1 : $a \in A$.** Cela signifie qu'il existe un $k \in \mathbb{N}$ tel que $a \in A_k$. Puisque les $A_n$ sont deux à deux disjoints, ce $k$ est unique. Ainsi, $a \notin A_n$ pour tout $n \neq k$.
  On a alors $\delta_a(A) = 1$.
  De l'autre côté, la somme vaut $\sum_{n=0}^{+\infty} \delta_a(A_n) = \delta_a(A_k) + \sum_{n \neq k} \delta_a(A_n) = 1 + \sum 0 = 1$. L'égalité $\delta_a(A) = \sum_{n=0}^{+\infty} \delta_a(A_n)$ est vérifiée.
- **Cas 2 : $a \notin A$.** Cela implique que pour tout $n \in \mathbb{N}$, $a \notin A_n$.
  On a alors $\delta_a(A) = 0$.
  La somme vaut $\sum_{n=0}^{+\infty} \delta_a(A_n) = \sum_{n=0}^{+\infty} 0 = 0$. L'égalité est également vérifiée.

3. **Masse totale :**
Comme $a \in X$, par définition $\delta_a(X) = 1$.
Ainsi, $\delta_a$ vérifie toutes les propriétés d'une mesure de probabilité. $\blacksquare$
