---
title: "Exercice 4 : Étude d'un ensemble ouvert (Topologie)"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 4 : Étude d'un ensemble ouvert (Topologie)

## Énoncé

Soit $U = \{(x, y) \in \mathbb{R}^2 \mid x^2 + 4y^2 < 4\}$.
Démontrer rigoureusement que $U$ est un ouvert de $\mathbb{R}^2$.

## Solution détaillée

1. **Rappel théorique** :
   Un sous-ensemble $U \subset \mathbb{R}^n$ est ouvert si, pour tout point $a \in U$, il existe un rayon $r > 0$ tel que la boule ouverte $B(a, r)$ est entièrement incluse dans $U$.
   Il existe aussi une approche via les fonctions continues : l'image réciproque d'un ouvert par une fonction continue est un ouvert.

2. **Démonstration par la continuité (Méthode la plus élégante)** :
   Considérons la fonction $f : \mathbb{R}^2 \to \mathbb{R}$ définie par :
   $$ f(x, y) = x^2 + 4y^2 $$

   - **Continuité de $f$** : La fonction $f$ est une fonction polynomiale en $x$ et en $y$. Elle est donc continue sur l'ensemble de son domaine de définition, $\mathbb{R}^2$.

   - **Formulation topologique** : L'ensemble $U$ peut être réécrit comme :
     $$ U = \{(x, y) \in \mathbb{R}^2 \mid f(x, y) < 4\} $$
     Ce qui équivaut à dire que $U$ est l'image réciproque de l'intervalle $]-\infty, 4[$ par la fonction $f$ :
     $$ U = f^{-1}(]-\infty, 4[) $$

   - **Conclusion** : L'intervalle $I = ]-\infty, 4[$ est un ensemble ouvert de $\mathbb{R}$. Comme $f$ est une fonction continue de $\mathbb{R}^2$ vers $\mathbb{R}$, un théorème fondamental de la topologie stipule que l'image réciproque de tout ouvert par une fonction continue est un ouvert.
   Par conséquent, $U = f^{-1}(I)$ est un ensemble ouvert de $\mathbb{R}^2$.
