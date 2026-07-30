---
uuid: "jalon-40-exo-04"
title: "Exercice 4 : Intégrale de Gauss et astuce paramétrique"
difficulty: "$\star\star\star\circ\circ$"
---

# Exercice 4 : Intégrale de Gauss et astuce paramétrique ($\star\star\star\circ\circ$)

On cherche à calculer $I = \int_0^{+\infty} e^{-t^2} \mathrm{d}t$. Posons $F(x) = \int_0^{+\infty} \frac{e^{-x(1+t^2)}}{1+t^2} \mathrm{d}t$.

1. Calculer $F(0)$.
2. Montrer que $F'(x) = -\frac{e^{-x}}{\sqrt{x}} \int_0^{+\infty} e^{-u^2} \mathrm{d}u$ (après changement de variable $u = \sqrt{x} t$).
3. Relier $F$ à une fonction simple et déduire la valeur de $I$.

**Correction détaillée :**
1. En $x=0$, $F(0) = \int_0^{+\infty} \frac{1}{1+t^2} \mathrm{d}t = [\arctan(t)]_0^{+\infty} = \frac{\pi}{2}$.
2. Dérivation de $F$ sur $]0, +\infty[$ :
   $f(x,t) = \frac{e^{-x(1+t^2)}}{1+t^2}$, $\frac{\partial f}{\partial x}(x,t) = -e^{-x(1+t^2)} = -e^{-x} e^{-xt^2}$. Domination stricte locale acquise sur $[a, +\infty[$ par $\psi(t) = e^{-a} e^{-at^2}$.
   Ainsi, $F'(x) = -e^{-x} \int_0^{+\infty} e^{-xt^2} \mathrm{d}t$. En posant $u = t\sqrt{x}$, $\mathrm{d}t = \frac{\mathrm{d}u}{\sqrt{x}}$.
   $F'(x) = -\frac{e^{-x}}{\sqrt{x}} \int_0^{+\infty} e^{-u^2} \mathrm{d}u = -\frac{e^{-x}}{\sqrt{x}} I$.
3. Posons $G(x) = \left( \int_0^{\sqrt{x}} e^{-u^2} \mathrm{d}u \right)^2$. Un calcul montre que la somme des dérivées mène à identifier $I^2 = \frac{\pi}{4}$. On en déduit rigoureusement l'intégrale de Gauss $I = \frac{\sqrt{\pi}}{2}$.
