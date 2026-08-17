---
title: "Exercice 10 - Intégrale de Stieltjes et sauts"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 10 - Introduction à Riemann-Stieltjes

**Énoncé :**
Si on intègre par rapport à une fonction $g(x) = \lfloor x \rfloor$ au lieu de $x$, comment s'écrit la somme de Riemann-Stieltjes $S(f, g, \sigma) = \sum f(c_k)(g(x_k) - g(x_{k-1}))$ pour une fonction $f$ continue sur $[0, 2]$ avec la subdivision $(0, 1-\epsilon, 1+\epsilon, 2)$ ?

**Démonstration pas à pas :**
1. $g(x_k) - g(x_{k-1})$ représente l'accroissement de $g$ sur l'intervalle.
2. Pour $I_1 = [0, 1-\epsilon]$, l'accroissement est $g(1-\epsilon) - g(0) = 0 - 0 = 0$.
3. Pour $I_2 = [1-\epsilon, 1+\epsilon]$, l'accroissement est $g(1+\epsilon) - g(1-\epsilon) = 1 - 0 = 1$.
4. Pour $I_3 = [1+\epsilon, 2]$, si on s'arrête avant 2, l'accroissement est nul. Autour de 2, il y a un autre saut de 1.
5. À la limite $\epsilon \to 0$, les seuls intervalles où l'accroissement n'est pas nul sont ceux contenant les sauts de $g$ (en 1 et 2).
6. Ainsi $\int f dg = f(1) + f(2)$. Ceci anticipe la mesure de Dirac, inatteignable par Riemann classique.
