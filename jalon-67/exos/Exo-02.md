---
title: "Exercice 2"
---
## Exercice 2 : Série de fonctions et interversion $\bigstar\bigstar$

**Énoncé :**
Montrer que $\int_0^1 \frac{-\ln(x)}{1-x} dx = \sum_{n=1}^{\infty} \frac{1}{n^2}$.

**Correction Détaillée :**
1. Soit $x \in ]0, 1[$. On connaît le développement en série entière : $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$.
2. On peut donc écrire l'intégrande comme $f(x) = -\ln(x) \sum_{n=0}^{\infty} x^n = \sum_{n=0}^{\infty} (-\ln(x) x^n)$.
3. Posons $u_n(x) = -x^n \ln(x)$. Sur $]0, 1[$, on a $-\ln(x) > 0$ et $x^n > 0$, donc $u_n(x) \ge 0$.
4. La suite $(u_n)$ est une suite de fonctions mesurables et positives. Le corollaire du théorème de convergence monotone nous autorise à intervertir l'intégrale et la somme :
   $$\int_0^1 \sum_{n=0}^\infty u_n(x) dx = \sum_{n=0}^\infty \int_0^1 u_n(x) dx$$
5. Calculons $\int_0^1 -x^n \ln(x) dx$. Faisons une intégration par parties :
   On pose $u = -\ln(x) \Rightarrow u' = -1/x$
   $v' = x^n \Rightarrow v = \frac{x^{n+1}}{n+1}$
   $$\int_\epsilon^1 -x^n \ln(x) dx = \left[-\ln(x) \frac{x^{n+1}}{n+1}\right]_\epsilon^1 - \int_\epsilon^1 \frac{x^n}{n+1} dx$$
   Le terme de bord en $1$ vaut $0$. En $\epsilon$, $\epsilon^{n+1} \ln(\epsilon) \to 0$ quand $\epsilon \to 0$.
   Donc $\int_0^1 -x^n \ln(x) dx = \left[ -\frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$.
6. Ainsi, l'intégrale totale est $\sum_{n=0}^\infty \frac{1}{(n+1)^2} = \sum_{n=1}^\infty \frac{1}{n^2}$.
