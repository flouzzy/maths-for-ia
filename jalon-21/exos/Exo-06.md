---
uuid: "exo-21-06"
title: "Exercice 6 : Théorème d'interversion limite-intégrale (Contre-exemple)"
difficulty: 3
---

# Exercice 6 : Théorème d'interversion limite-intégrale (Contre-exemple)

**Niveau :** $★★★☆☆$

## Problème

Considérer $f_n(x) = n^2 x (1-x^2)^n$ sur $[0,1]$. Étudier la convergence simple. Comparer l'intégrale de la limite et la limite de l'intégrale.

## Démonstration et Solution

**Étape 1 : Étude de la convergence simple**
Soit $f_n(x) = n^2 x (1-x^2)^n$ sur $[0,1]$.
Si $x = 0$, $f_n(0) = n^2 \times 0 \times 1^n = 0$. La limite est 0.
Si $x = 1$, $f_n(1) = n^2 \times 1 \times 0^n = 0$. La limite est 0.
Si $x \in ]0, 1[$, alors $1-x^2 \in ]0, 1[$. Posons $q = 1-x^2$, avec $0 < q < 1$.
L'expression devient $f_n(x) = x \times n^2 q^n$.
Puisque $0 < q < 1$, nous avons une forme indéterminée du type "+$\infty \times 0$". Par le théorème de croissance comparée entre les fonctions puissances et les exponentielles (ou en écrivant $q^n = e^{n \ln q}$ avec $\ln q < 0$), l'exponentielle l'emporte. Rigoureusement, $\lim_{n \to \infty} n^k q^n = 0$ pour tout $k > 0$ et $q \in ]0,1[$.
Ainsi, $\lim_{n \to \infty} f_n(x) = x \times 0 = 0$.
La suite converge simplement vers la fonction nulle $f(x)=0$ sur $[0,1]$.

**Étape 2 : Intégrale de la limite**
La fonction limite étant nulle partout, son intégrale sur le segment est nulle :
$\int_0^1 f(x) dx = \int_0^1 0 dx = 0$.

**Étape 3 : Limite de l'intégrale**
Calculons l'intégrale de $f_n(x)$ sur $[0,1]$ pour un $n$ fixé :
$I_n = \int_0^1 n^2 x (1-x^2)^n dx$
Effectuons le changement de variable $u = 1-x^2$.
Alors $du = -2x dx$, ce qui donne $x dx = -\frac{1}{2} du$.
Les bornes deviennent : pour $x=0$, $u=1$ ; pour $x=1$, $u=0$.
$I_n = \int_1^0 n^2 (u)^n \left(-\frac{1}{2}\right) du = \frac{n^2}{2} \int_0^1 u^n du = \frac{n^2}{2} \left[ \frac{u^{n+1}}{n+1} \right]_0^1 = \frac{n^2}{2(n+1)}$
Calculons la limite de $I_n$ lorsque $n$ tend vers l'infini :
$\lim_{n \to \infty} I_n = \lim_{n \to \infty} \frac{n^2}{2n+2} = \lim_{n \to \infty} \frac{n^2}{2n(1 + 1/n)} = \lim_{n \to \infty} \frac{n}{2(1+1/n)} = +\infty$.

**Conclusion :**
Nous observons que la limite des intégrales est $+\infty$, tandis que l'intégrale de la limite est $0$. Les deux quantités sont distinctes ($\lim \int f_n \neq \int \lim f_n$). Ceci prouve formellement, par l'absurde via le théorème d'interversion, que la convergence de $(f_n)$ vers $f$ n'est pas uniforme sur $[0,1]$.
