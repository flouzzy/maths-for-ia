---
title: "Ouverture d'une application et homéomorphisme"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 06 : Ouverture d'une application et homéomorphisme
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Une application $f : X \to Y$ est dite **ouverte** si pour tout ouvert $O \in \mathcal{T}_X$, l'image $f(O)$ est un ouvert de $\mathcal{T}_Y$.
Montrer qu'une application bijective $f : X \to Y$ est un homéomorphisme si et seulement si elle est continue et ouverte.

**Correction Détaillée :**
1. **Sens ($\implies$) :** Supposons que $f$ est un homéomorphisme.
Alors $f$ est bijective et continue, et $f^{-1} : Y \to X$ est continue.
Soit $O$ un ouvert de $X$. Nous voulons montrer que $f(O)$ est ouvert dans $Y$.
La continuité de $f^{-1}$ implique que pour tout ouvert $U$ de $X$, l'image réciproque de $U$ par l'application $f^{-1}$, notée $(f^{-1})^{-1}(U)$, est ouverte dans $Y$.
Or, $(f^{-1})^{-1}(U) = f(U)$.
En prenant $U = O$, on conclut que $f(O)$ est un ouvert de $Y$. Ainsi $f$ est ouverte.

2. **Sens ($\impliedby$) :** Supposons $f$ bijective, continue et ouverte.
Il faut montrer que $f^{-1}$ est continue.
Par définition de la continuité pour l'application réciproque $g = f^{-1}$, il faut que pour tout ouvert $O$ de $X$, $g^{-1}(O)$ soit un ouvert de $Y$.
Or $g^{-1}(O) = (f^{-1})^{-1}(O) = f(O)$.
Par hypothèse, $f$ est ouverte, donc $f(O)$ est bien un ouvert de $Y$.
Cela démontre la continuité de $f^{-1}$, et donc $f$ est un homéomorphisme.
