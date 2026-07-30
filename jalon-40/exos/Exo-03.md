---
title: "Exercice 3 : Intégrale de Dirichlet"
difficulty: "$\star$$\star$$\circ$$\circ$$\circ$"
---
# Exercice 3 : Intégrale de Dirichlet ($\star$$\star$$\circ$$\circ$$\circ$)

**Énoncé :**
On s'intéresse à l'intégrale de Dirichlet $I = \int_0^{+\infty} \frac{\sin(t)}{t} dt$.
Pour cela, on introduit la fonction paramétrée $F(x) = \int_0^{+\infty} e^{-xt} \frac{\sin(t)}{t} dt$ pour $x > 0$.
1. Montrer que $F$ est dérivable sur $]0, +\infty[$ et calculer $F'(x)$.
2. En déduire une expression de $F(x)$ sans intégrale.
3. On admet que $F$ est continue en $0$. En déduire la valeur de $I$.

**Démonstration pas-à-pas :**
1. Soit $f(x,t) = e^{-xt} \frac{\sin(t)}{t}$. Pour $x>0$, $\frac{\partial f}{\partial x}(x,t) = -e^{-xt} \sin(t)$.
   Pour $x \ge a > 0$, on a $\left| \frac{\partial f}{\partial x}(x,t) \right| \le e^{-at}$, qui est intégrable sur $]0, +\infty[$.
   Le théorème de Leibniz s'applique : $F'(x) = \int_0^{+\infty} -e^{-xt} \sin(t) dt$.
   Le calcul de cette intégrale classique (par deux IPP successives ou passage en complexe avec $Im(\int e^{(-x+i)t}dt)$) donne :
   $F'(x) = - \frac{1}{x^2+1}$.
2. Par primitivation, $F(x) = -\arctan(x) + C$.
   Or, par majoration simple, $|F(x)| \le \int_0^{+\infty} e^{-xt} dt = \frac{1}{x}$.
   Donc $\lim_{x \to +\infty} F(x) = 0$. On a donc $-\frac{\pi}{2} + C = 0 \implies C = \frac{\pi}{2}$.
   Ainsi, $F(x) = \frac{\pi}{2} - \arctan(x)$.
3. Si $F$ est continue en $0$, alors $\lim_{x \to 0^+} F(x) = F(0) = \int_0^{+\infty} \frac{\sin(t)}{t} dt$.
   D'autre part, $\lim_{x \to 0^+} (\frac{\pi}{2} - \arctan(x)) = \frac{\pi}{2}$.
   On en conclut que $I = \frac{\pi}{2}$.
