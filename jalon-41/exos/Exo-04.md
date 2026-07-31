---
title: "Exercice 4 : Problème de Cauchy"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 4 : Problème de Cauchy

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Déterminer l'unique solution du problème de Cauchy suivant sur $]0, +\infty[$ :
$$\begin{cases} t y'(t) + y(t) = \ln(t) \\ y(1) = 2 \end{cases}$$

**Correction détaillée :**
1. **Mise sous forme normale :**
   Sur $I = ]0, +\infty[$, $t \neq 0$, on divise par $t$ pour obtenir une équation de la forme $y' + a(t)y = b(t)$ :
   $$y'(t) + \frac{1}{t} y(t) = \frac{\ln(t)}{t}$$
2. **Équation homogène :**
   Ici $a(t) = \frac{1}{t}$. Une primitive est $A(t) = \ln(t)$ (car $t>0$).
   $y_H(t) = C e^{-\ln(t)} = C \frac{1}{t}$.
3. **Variation de la constante :**
   On cherche $y_P(t) = C(t) \frac{1}{t}$.
   On a $y_P'(t) = C'(t)\frac{1}{t} - C(t)\frac{1}{t^2}$.
   Injection dans l'équation normale :
   $$\left( C'(t)\frac{1}{t} - C(t)\frac{1}{t^2} \right) + \frac{1}{t} \left( C(t)\frac{1}{t} \right) = \frac{\ln(t)}{t}$$
   $$C'(t)\frac{1}{t} = \frac{\ln(t)}{t} \implies C'(t) = \ln(t)$$
4. **Intégration par parties :**
   Une primitive de $\ln(t)$ est obtenue par parties : $\int 1 \cdot \ln(t) dt = t \ln(t) - \int t \cdot \frac{1}{t} dt = t\ln(t) - t$.
   Prenons $C(t) = t\ln(t) - t$.
5. **Solution générale :**
   $y_P(t) = \frac{t\ln(t) - t}{t} = \ln(t) - 1$.
   La solution générale de l'équation est $y(t) = \frac{C}{t} + \ln(t) - 1$.
6. **Condition initiale :**
   On veut $y(1) = 2$.
   $y(1) = \frac{C}{1} + \ln(1) - 1 = C - 1$.
   On a donc $C - 1 = 2 \implies C = 3$.
   L'unique solution est $y(t) = \frac{3}{t} + \ln(t) - 1$.
