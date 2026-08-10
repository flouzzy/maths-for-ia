---
uuid: "jalon-53-exo-9"
title: "Espace quotient et séparation"
---

## Exercice 9 : Espace quotient et séparation \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


**Énoncé :**
Soit $X = \mathbb{R}$ et la relation d'équivalence $x \sim y \iff x - y \in \mathbb{Q}$. On munit l'espace quotient $X / \sim$ de la topologie quotient. Montrer que $X / \sim$ est un espace topologique grossier (indiscret), et en déduire qu'il n'est pas Hausdorff.

**Correction Détaillée :**
Soit $\pi : \mathbb{R} \to \mathbb{R}/\mathbb{Q}$ la projection canonique. Par définition, $U \subset \mathbb{R}/\mathbb{Q}$ est ouvert si et seulement si $\pi^{-1}(U)$ est ouvert dans $\mathbb{R}$.
Supposons qu'il existe un ouvert non vide $U$ dans $X / \sim$ tel que $U \neq X / \sim$.
Alors $\pi^{-1}(U)$ est un ouvert non vide de $\mathbb{R}$ tel que $\pi^{-1}(U) \neq \mathbb{R}$.
Puisque $U$ est non vide, il existe $\bar{x} \in U$, donc $\pi^{-1}(\{\bar{x}\}) \subset \pi^{-1}(U)$.
Or, $\pi^{-1}(\{\bar{x}\}) = x + \mathbb{Q}$, qui est dense dans $\mathbb{R}$.
Un ouvert $\pi^{-1}(U)$ contenant une partie dense est nécessairement dense. Et un ouvert n'est égal à $\mathbb{R}$ que s'il est vide ou plein ? Non. L'ouvert $\pi^{-1}(U)$ a la propriété supplémentaire d'être saturé pour la relation, c'est-à-dire que si $y \in \pi^{-1}(U)$, alors $y + \mathbb{Q} \subset \pi^{-1}(U)$.
Comme $\pi^{-1}(U)$ contient au moins un point $x$, il contient $x + \mathbb{Q}$. Comme $\pi^{-1}(U)$ est ouvert, il contient un intervalle $]a, b[$. La réunion des translatés rationnels de cet intervalle est $\mathbb{R}$ tout entier : $\bigcup_{q \in \mathbb{Q}} (]a, b[ + q) = \mathbb{R}$.
Donc $\pi^{-1}(U) = \mathbb{R}$, d'où $U = X / \sim$.
Les seuls ouverts sont $\emptyset$ et $X / \sim$. L'espace est grossier.
Puisqu'il a plus d'un point et que les seuls ouverts sont triviaux, il est impossible de séparer deux points. Il n'est pas Hausdorff.
