---
title: "Exercice 2 : Variation de la constante : exponentielle"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 2 : Variation de la constante : exponentielle

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Résoudre sur $\mathbb{R}$ l'équation différentielle suivante :
$$y'(t) + y(t) = e^{2t}$$

**Correction détaillée :**
1. **Équation homogène associée :**
   L'équation est $(H) : y'(t) + y(t) = 0$. Ici $a(t) = 1$. Une primitive est $A(t) = t$.
   Les solutions homogènes sont de la forme $y_H(t) = C e^{-t}$, avec $C \in \mathbb{R}$.
2. **Recherche d'une solution particulière par variation de la constante :**
   On cherche une solution sous la forme $y_P(t) = C(t) e^{-t}$.
   La dérivée est $y_P'(t) = C'(t)e^{-t} - C(t)e^{-t}$.
   On injecte dans l'équation complète :
   $$\left(C'(t)e^{-t} - C(t)e^{-t}\right) + C(t)e^{-t} = e^{2t}$$
   $$C'(t)e^{-t} = e^{2t} \implies C'(t) = e^{2t} e^t = e^{3t}$$
3. **Intégration de C'(t) :**
   Une primitive de $C'(t) = e^{3t}$ est $C(t) = \frac{1}{3} e^{3t}$.
4. **Solution particulière :**
   On en déduit $y_P(t) = \left( \frac{1}{3} e^{3t} \right) e^{-t} = \frac{1}{3} e^{2t}$.
5. **Solution générale :**
   La solution générale est la somme de la solution homogène et de la solution particulière :
   $$y(t) = y_H(t) + y_P(t) = C e^{-t} + \frac{1}{3} e^{2t}, \quad C \in \mathbb{R}$$
