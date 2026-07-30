---
title: "Exercice 1 : Intégrales à paramètres basique"
difficulty: "$\star$$\circ$$\circ$$\circ$$\circ$"
---
# Exercice 1 : Intégrales à paramètres basique ($\star$$\circ$$\circ$$\circ$$\circ$)

**Énoncé :**
Soit $F(x) = \int_0^1 t^x dt$.
1. Pour quelles valeurs de $x$ la fonction $F$ est-elle bien définie ?
2. Calculer explicitement $F(x)$.
3. Calculer la dérivée $F'(x)$ de deux manières différentes :
   - En dérivant l'expression explicite trouvée à la question 2.
   - En utilisant le théorème de dérivation sous le signe intégral.

**Démonstration pas-à-pas :**
1. L'intégrale $\int_0^1 t^x dt$ est convergente si et seulement si $x > -1$. En effet, pour $t \in ]0, 1]$, $t^x = e^{x \ln(t)}$. Si $x = -1$, on obtient $\int_0^1 \frac{1}{t} dt$ qui diverge. Si $x > -1$, la primitive $\frac{t^{x+1}}{x+1}$ admet une limite finie en $0$.
2. Pour $x > -1$, $F(x) = \left[ \frac{t^{x+1}}{x+1} \right]_0^1 = \frac{1}{x+1}$.
3. Première méthode : $F'(x) = \frac{d}{dx} \left( \frac{1}{x+1} \right) = -\frac{1}{(x+1)^2}$.
   Deuxième méthode : Soit $f(x, t) = t^x = e^{x \ln(t)}$.
   - Pour $t \in ]0, 1]$, $x \mapsto f(x,t)$ est de classe $\mathcal{C}^1$ et $\frac{\partial f}{\partial x}(x,t) = \ln(t) t^x$.
   - Soit $K = [a, b] \subset ]-1, +\infty[$ avec $a > -1$. Pour tout $x \ge a$, on a $\left| \frac{\partial f}{\partial x}(x,t) \right| = -\ln(t) t^x \le -\ln(t) t^a$.
   - La fonction $\psi(t) = -\ln(t) t^a$ est intégrable sur $]0, 1]$ (croissance comparée en $0$).
   - Donc on peut dériver sous l'intégrale : $F'(x) = \int_0^1 \ln(t) t^x dt$.
   Par intégration par parties ($u = \ln(t)$, $v' = t^x$) :
   $F'(x) = \left[ \ln(t) \frac{t^{x+1}}{x+1} \right]_0^1 - \int_0^1 \frac{1}{t} \frac{t^{x+1}}{x+1} dt = 0 - \frac{1}{x+1} \int_0^1 t^x dt = -\frac{1}{x+1} \left[ \frac{t^{x+1}}{x+1} \right]_0^1 = -\frac{1}{(x+1)^2}$.
   Les deux méthodes coïncident.
