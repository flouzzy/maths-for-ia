---
title: "Exercice 1 : Équation linéaire homogène simple"
difficulty: "$\star\star\star\star\star$"
---

# Exercice 1 : Équation linéaire homogène simple

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Résoudre sur $\mathbb{R}$ l'équation différentielle suivante :
$$y'(t) + 3y(t) = 0$$

**Correction détaillée :**
1. **Identification de l'équation :**
   Il s'agit d'une équation différentielle linéaire du premier ordre sans second membre (homogène) de la forme $y'(t) + a(t)y(t) = 0$, avec $a(t) = 3$.
2. **Calcul de la primitive :**
   La fonction $a : t \mapsto 3$ est continue sur $\mathbb{R}$. Une primitive est $A(t) = 3t$.
3. **Application du théorème :**
   L'ensemble des solutions de l'équation homogène est donné par $\mathcal{S}_H = \{ t \mapsto C e^{-A(t)} \mid C \in \mathbb{R} \}$.
   Donc, les solutions sont les fonctions de la forme $y(t) = C e^{-3t}$ avec $C \in \mathbb{R}$.
