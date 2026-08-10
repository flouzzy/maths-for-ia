---
title: "Continuité et passage aux limites pour les suites"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 03 : Continuité et passage aux limites pour les suites
**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f : X \to Y$ une application continue entre deux espaces topologiques.
Soit $(x_n)_{n \ge 0}$ une suite d'éléments de $X$ qui converge vers une limite $l \in X$.
Démontrer rigoureusement que la suite image $(f(x_n))_{n \ge 0}$ converge vers $f(l)$ dans $Y$.

**Correction Détaillée :**
Rappelons la définition de la convergence dans un espace topologique : $(x_n) \to l$ ssi pour tout voisinage $U$ de $l$, il existe un entier $N$ tel que $\forall n \ge N, x_n \in U$.
1. Soit $V$ un voisinage de $f(l)$ dans $Y$.
2. Puisque $f$ est continue en $l$ (par hypothèse de continuité globale), l'image réciproque $f^{-1}(V)$ est un voisinage de $l$ dans $X$.
3. Comme la suite $(x_n)$ converge vers $l$, il existe un rang $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $x_n \in f^{-1}(V)$.
4. Par définition de l'image réciproque, la condition $x_n \in f^{-1}(V)$ équivaut à $f(x_n) \in V$.
5. Ainsi, pour tout voisinage $V$ de $f(l)$, à partir du rang $N$, $f(x_n)$ est dans $V$. Cela signifie exactement que la suite $(f(x_n))$ converge vers $f(l)$.
