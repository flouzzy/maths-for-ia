---
title: "Continuité sur des topologies triviale et discrète"
difficulty: $\bigstar\star\star\star\star$
---

# Exercice 01 : Continuité sur des topologies triviale et discrète
**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $X$ un ensemble non vide. On munit $X$ de deux topologies : la topologie discrète $\mathcal{T}_d$ (où tout sous-ensemble est ouvert) et la topologie grossière $\mathcal{T}_g = \{\emptyset, X\}$.
Soit $(Y, \mathcal{T}_Y)$ un espace topologique quelconque et $f : X \to Y$ une application.
1. Montrer que si $X$ est muni de $\mathcal{T}_d$, alors $f$ est nécessairement continue, quelle que soit $\mathcal{T}_Y$.
2. Montrer que si $X$ est muni de $\mathcal{T}_g$, alors $f$ n'est continue que si $f$ est constante ou si la topologie de $Y$ est très faible sur l'image de $f$.

**Correction Détaillée :**
1. Supposons $(X, \mathcal{T}_d)$. Soit $O \in \mathcal{T}_Y$ un ouvert quelconque de $Y$.
L'image réciproque $f^{-1}(O) = \{ x \in X \mid f(x) \in O \}$ est un sous-ensemble de $X$.
Puisque la topologie est discrète, tout sous-ensemble de $X$ appartient à $\mathcal{T}_d$.
Donc $f^{-1}(O) \in \mathcal{T}_d$. L'application $f$ est donc toujours continue.

2. Supposons $(X, \mathcal{T}_g)$. Soit $O \in \mathcal{T}_Y$. Pour que $f$ soit continue, il faut que $f^{-1}(O) \in \mathcal{T}_g$.
Or, $\mathcal{T}_g = \{\emptyset, X\}$. Ainsi, on doit avoir soit $f^{-1}(O) = \emptyset$, soit $f^{-1}(O) = X$.
Cela signifie que pour tout ouvert $O$ de $Y$, soit aucun élément de $X$ n'est envoyé dans $O$, soit tous les éléments de $X$ sont envoyés dans $O$.
Ceci est trivialement respecté si $f$ est une fonction constante (toute l'image est réduite à un seul point, qui appartient ou n'appartient pas à $O$).
