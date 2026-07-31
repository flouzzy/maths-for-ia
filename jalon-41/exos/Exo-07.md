---
title: "Exercice 7 : Changement de variable explicite"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Changement de variable explicite

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Résoudre sur $\mathbb{R}^*_+$ l'équation :
$$t^2 y'' + 3t y' + y = 0$$
en posant le changement de variable $t = e^x$.
*(Note : bien qu'étant d'ordre 2, cette équation d'Euler se ramène à l'ordre 1 ou 2 à coefficients constants).*

**Correction détaillée :**
1. **Changement de variable :**
   On pose $x = \ln(t)$ (soit $t = e^x$) et $z(x) = y(e^x) = y(t)$.
   On exprime les dérivées de $y$ en fonction de celles de $z$.
   Par la règle de la chaîne, $z'(x) = y'(e^x) \cdot e^x = t \cdot y'(t)$.
   Donc $y'(t) = \frac{1}{t} z'(\ln(t))$.
   En dérivant encore par rapport à $t$ :
   $y''(t) = -\frac{1}{t^2} z'(\ln(t)) + \frac{1}{t} \cdot z''(\ln(t)) \cdot \frac{1}{t} = \frac{1}{t^2} (z''(x) - z'(x))$.
2. **Injection dans l'équation :**
   $t^2 \left( \frac{1}{t^2} (z'' - z') \right) + 3t \left( \frac{1}{t} z' \right) + z = 0$
   $z'' - z' + 3z' + z = 0$
   $z'' + 2z' + z = 0$
3. **Résolution de l'équation en z :**
   C'est une équation linéaire d'ordre 2 à coefficients constants.
   Polynôme caractéristique : $r^2 + 2r + 1 = 0 \iff (r+1)^2 = 0$. Racine double $r = -1$.
   La solution générale pour $z$ est $z(x) = (Ax + B)e^{-x}$, avec $A, B \in \mathbb{R}$.
4. **Retour à y :**
   $y(t) = z(\ln(t)) = (A\ln(t) + B)e^{-\ln(t)} = \frac{A\ln(t) + B}{t}$.
   Ainsi, $y(t) = \frac{A\ln(t) + B}{t}$.
