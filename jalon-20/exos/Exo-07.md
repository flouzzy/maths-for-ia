---
uuid: "jalon-20-exo-07"
title: "Exercice 07 : ★★★★☆"
---
# Exercice 07

## Énoncé
Soit $f$ une fonction de classe $C^2$ sur $[a,b]$. On suppose que $f(a)=f(b)=0$ et qu'il existe $M > 0$ tel que pour tout $x \in [a,b]$, $|f''(x)| \le M$. Montrer que pour tout $x \in [a,b]$, $|f(x)| \le \frac{M}{2} (x-a)(b-x)$.

## Correction
1. Soit $x \in ]a,b[$. Appliquons la formule de Taylor-Lagrange entre $x$ et $a$ à l'ordre 1 :
   $f(a) = f(x) + f'(x)(a-x) + \frac{f''(c_1)}{2}(a-x)^2$ avec $c_1 \in ]a,x[$.
   Comme $f(a)=0$, on a $f(x) = f'(x)(x-a) - \frac{f''(c_1)}{2}(x-a)^2$.
2. Appliquons la formule de Taylor-Lagrange entre $x$ et $b$ à l'ordre 1 :
   $f(b) = f(x) + f'(x)(b-x) + \frac{f''(c_2)}{2}(b-x)^2$ avec $c_2 \in ]x,b[$.
   Comme $f(b)=0$, on a $f(x) = -f'(x)(b-x) - \frac{f''(c_2)}{2}(b-x)^2$.
3. Éliminons $f'(x)$. Multiplions la première équation par $(b-x)$ et la seconde par $(x-a)$ et sommons :
   $(b-x)f(x) + (x-a)f(x) = - \frac{f''(c_1)}{2}(x-a)^2(b-x) - \frac{f''(c_2)}{2}(b-x)^2(x-a)$.
   $(b-a)f(x) = - \frac{(x-a)(b-x)}{2} [ f''(c_1)(x-a) + f''(c_2)(b-x) ]$.
4. Passons à la valeur absolue et utilisons $|f''(c)| \le M$ :
   $(b-a)|f(x)| \le \frac{(x-a)(b-x)}{2} [ M(x-a) + M(b-x) ]$.
   $(b-a)|f(x)| \le \frac{(x-a)(b-x)}{2} M (b-a)$.
5. En divisant par $(b-a) > 0$ :
   $|f(x)| \le \frac{M}{2} (x-a)(b-x)$. $\blacksquare$