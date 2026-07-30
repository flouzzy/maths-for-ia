---
title: "Exercice 4 : Calcul de l'intégrale de Gauss"
difficulty: "$\star$$\star$$\star$$\circ$$\circ$"
---
# Exercice 4 : Calcul de l'intégrale de Gauss ($\star$$\star$$\star$$\circ$$\circ$)

**Énoncé :**
Soit $F(x) = \left( \int_0^x e^{-t^2} dt \right)^2$ et $G(x) = \int_0^1 \frac{e^{-x^2(1+t^2)}}{1+t^2} dt$.
1. Calculer $F'(x)$ et $G'(x)$.
2. En déduire que $F(x) + G(x) = \frac{\pi}{4}$.
3. Calculer la limite de $G(x)$ quand $x \to +\infty$.
4. En déduire la valeur de $\int_0^{+\infty} e^{-t^2} dt$.

**Démonstration pas-à-pas :**
1. $F'(x) = 2 e^{-x^2} \int_0^x e^{-t^2} dt$.
   Pour $G$, le théorème de dérivation sous le signe intégral s'applique sur l'intervalle compact $[0,1]$ :
   $G'(x) = \int_0^1 \frac{\partial}{\partial x} \left( \frac{e^{-x^2(1+t^2)}}{1+t^2} \right) dt = \int_0^1 \frac{-2x(1+t^2)e^{-x^2(1+t^2)}}{1+t^2} dt = -2xe^{-x^2} \int_0^1 e^{-x^2 t^2} dt$.
   Par le changement de variable $u = xt$ ($du = x dt$), l'intégrale devient $\int_0^x e^{-u^2} du$.
   Ainsi, $G'(x) = -2 e^{-x^2} \int_0^x e^{-u^2} du$.
2. On remarque que $F'(x) + G'(x) = 0$ pour tout $x$. Donc $F(x) + G(x) = C$.
   Pour $x=0$, $F(0) = 0$ et $G(0) = \int_0^1 \frac{1}{1+t^2} dt = [\arctan(t)]_0^1 = \frac{\pi}{4}$. Donc $C = \frac{\pi}{4}$.
3. Pour tout $t \in [0,1]$, $e^{-x^2(1+t^2)} \le e^{-x^2}$.
   Donc $0 \le G(x) \le e^{-x^2} \int_0^1 \frac{1}{1+t^2} dt = e^{-x^2} \frac{\pi}{4}$.
   Par encadrement, $\lim_{x \to +\infty} G(x) = 0$.
4. En passant à la limite quand $x \to +\infty$ dans la relation $F(x) + G(x) = \frac{\pi}{4}$, on obtient :
   $\lim_{x \to +\infty} F(x) + 0 = \frac{\pi}{4}$, soit $\left( \int_0^{+\infty} e^{-t^2} dt \right)^2 = \frac{\pi}{4}$.
   Puisque l'intégrande est positive, $\int_0^{+\infty} e^{-t^2} dt = \frac{\sqrt{\pi}}{2}$.
