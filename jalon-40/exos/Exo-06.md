---
title: "Exercice 6 : Intégrale de Frullani"
difficulty: "$\star$$\star$$\star$$\star$$\circ$"
---
# Exercice 6 : Intégrale de Frullani ($\star$$\star$$\star$$\star$$\circ$)

**Énoncé :**
Soit $f : \mathbb{R}^+ \to \mathbb{R}$ une fonction continue admettant une limite finie $L$ en $+\infty$.
Pour $a > 0$ et $b > 0$, montrer que :
$\int_0^{+\infty} \frac{f(ax) - f(bx)}{x} dx = (f(0) - L) \ln\left(\frac{b}{a}\right)$.

**Démonstration pas-à-pas :**
1. Fixons un $\epsilon > 0$ et un $X > 0$. Par changement de variable linéaire :
   $\int_{\epsilon}^X \frac{f(ax)}{x} dx = \int_{a\epsilon}^{aX} \frac{f(u)}{u} du$ et $\int_{\epsilon}^X \frac{f(bx)}{x} dx = \int_{b\epsilon}^{bX} \frac{f(u)}{u} du$.
2. Soustrayons ces deux intégrales :
   $\int_{\epsilon}^X \frac{f(ax) - f(bx)}{x} dx = \int_{a\epsilon}^{aX} \frac{f(u)}{u} du - \int_{b\epsilon}^{bX} \frac{f(u)}{u} du$.
   Par la relation de Chasles, cela donne :
   $\int_{a\epsilon}^{b\epsilon} \frac{f(u)}{u} du - \int_{aX}^{bX} \frac{f(u)}{u} du$.
3. Étude du premier terme quand $\epsilon \to 0^+$ :
   Par continuité de $f$ en $0$, $f(u) \approx f(0)$ sur l'intervalle d'intégration.
   $\int_{a\epsilon}^{b\epsilon} \frac{f(u)}{u} du = f(0) \int_{a\epsilon}^{b\epsilon} \frac{1}{u} du + \int_{a\epsilon}^{b\epsilon} \frac{f(u) - f(0)}{u} du$.
   Or $\int_{a\epsilon}^{b\epsilon} \frac{1}{u} du = \ln(b\epsilon) - \ln(a\epsilon) = \ln(b/a)$.
   De plus, pour $\epsilon$ petit, le reste tend vers $0$.
4. Étude du second terme quand $X \to +\infty$ :
   On sait que $f(u) \to L$. De façon analogue :
   $\int_{aX}^{bX} \frac{f(u)}{u} du = L \ln(b/a) + o(1)$.
5. Conclusion :
   En passant simultanément à la limite $\epsilon \to 0^+$ et $X \to +\infty$, on trouve le résultat demandé.
