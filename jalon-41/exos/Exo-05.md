---
title: "Exercice 5 : Superposition des solutions"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : Superposition des solutions

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Résoudre sur $\mathbb{R}$ l'équation $y' + 2y = \cos(t) + e^{-2t}$.

**Correction détaillée :**
1. **Équation homogène :**
   $y' + 2y = 0 \implies y_H(t) = C e^{-2t}, C \in \mathbb{R}$.
2. **Principe de superposition :**
   L'équation étant linéaire, on peut chercher une solution particulière $y_{P1}$ pour $y' + 2y = \cos(t)$ et $y_{P2}$ pour $y' + 2y = e^{-2t}$. La somme $y_{P1} + y_{P2}$ sera solution de l'équation complète.
3. **Recherche de $y_{P1}$ (second membre trigonométrique) :**
   On passe en complexes : on cherche une solution de $z' + 2z = e^{it}$.
   On cherche $z(t) = A e^{it}$ avec $A \in \mathbb{C}$.
   $z' + 2z = iA e^{it} + 2A e^{it} = A(2+i) e^{it}$.
   Pour avoir $e^{it}$, on prend $A = \frac{1}{2+i} = \frac{2-i}{(2+i)(2-i)} = \frac{2-i}{5}$.
   La solution complexe est $z(t) = \frac{2-i}{5} (\cos(t) + i\sin(t))$.
   On prend la partie réelle : $y_{P1}(t) = \Re(z(t)) = \frac{2}{5}\cos(t) + \frac{1}{5}\sin(t)$.
4. **Recherche de $y_{P2}$ (second membre exponentiel avec résonance) :**
   Pour $y' + 2y = e^{-2t}$, le second membre est de la forme de la solution homogène.
   Par variation de la constante : on pose $y_{P2}(t) = C(t) e^{-2t}$.
   On a $C'(t) e^{-2t} = e^{-2t} \implies C'(t) = 1 \implies C(t) = t$.
   Donc $y_{P2}(t) = t e^{-2t}$.
5. **Solution générale :**
   $y(t) = y_H(t) + y_{P1}(t) + y_{P2}(t) = C e^{-2t} + \frac{2}{5}\cos(t) + \frac{1}{5}\sin(t) + t e^{-2t}, C \in \mathbb{R}$.
