---
title: "Exercice 5 : Produit de Cauchy de deux séries semi-convergentes"
difficulty: ★★★☆☆
---
# Exercice 5 : Produit de Cauchy de deux séries semi-convergentes

## Énoncé
Soit $a_n = b_n = \frac{(-1)^n}{\sqrt{n+1}}$. Montrer que le produit de Cauchy des séries $\sum a_n$ et $\sum b_n$ (qui sont semi-convergentes) est une série divergente.

## Correction
1. **Convergence des séries initiales :** $\sum \frac{(-1)^n}{\sqrt{n+1}}$ est une série alternée dont le terme général tend vers 0 en décroissant en valeur absolue. Par le critère de Leibniz, elle converge. Elle ne converge pas absolument car $\sum \frac{1}{\sqrt{n+1}}$ diverge (série de Riemann avec $\alpha=1/2 \le 1$).
2. **Calcul du terme général du produit de Cauchy :**
   $c_n = \sum_{k=0}^n a_k b_{n-k} = \sum_{k=0}^n \frac{(-1)^k}{\sqrt{k+1}} \frac{(-1)^{n-k}}{\sqrt{n-k+1}} = (-1)^n \sum_{k=0}^n \frac{1}{\sqrt{(k+1)(n-k+1)}}$.
3. **Minoration de $c_n$ :**
   La fonction $f(x) = (x+1)(n-x+1)$ sur l'intervalle $[0, n]$ atteint son maximum en son milieu $x = n/2$.
   On a donc pour tout $k \in \{0, \dots, n\}$ : $(k+1)(n-k+1) \le (\frac{n}{2} + 1)(\frac{n}{2} + 1) = \frac{(n+2)^2}{4}$.
   Ainsi, $\frac{1}{\sqrt{(k+1)(n-k+1)}} \ge \frac{2}{n+2}$.
   On en déduit que $|c_n| = \sum_{k=0}^n \frac{1}{\sqrt{(k+1)(n-k+1)}} \ge \sum_{k=0}^n \frac{2}{n+2} = \frac{2(n+1)}{n+2}$.
4. **Conclusion :**
   $\lim_{n\to\infty} |c_n| \ge \lim_{n\to\infty} \frac{2n+2}{n+2} = 2 \neq 0$.
   Le terme général $c_n$ ne tend pas vers 0, la série produit $\sum c_n$ diverge grossièrement. Cela montre que le théorème de Mertens nécessite absolument la convergence absolue d'au moins l'une des deux séries.
