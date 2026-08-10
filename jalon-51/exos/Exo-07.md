# Exercice 7 : Générer une distance bornée
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé formel
Montrer que si $d$ est une distance sur $X$, alors $d'(x,y) = \frac{d(x,y)}{1+d(x,y)}$ définit une autre distance sur $X$ qui est majorée par 1. Sont-elles topologiquement équivalentes ?

## Résolution pas à pas
**Étape 1 : Étude de la fonction de modification**

Posons $f(t) = \frac{t}{1+t}$. Sa dérivée est $f'(t) = \frac{1}{(1+t)^2} > 0$. La fonction est donc strictement croissante sur $\mathbb{R}_+$. De plus, $f(t) < 1$.

**Étape 2 : Axiomes de la distance**

Séparation et symétrie découlent directement de celles de $d$. L'inégalité triangulaire nécessite la monotonie. Soit $d(x,z) \le d(x,y) + d(y,z)$. Puisque $f$ croît, $f(d(x,z)) \le f(d(x,y) + d(y,z))$.
Or, on montre algébriquement que $\frac{a+b}{1+a+b} = \frac{a}{1+a+b} + \frac{b}{1+a+b} \le \frac{a}{1+a} + \frac{b}{1+b}$.
Donc $d'(x,z) \le d'(x,y) + d'(y,z)$. $d'$ est bien une distance.

**Étape 3 : Équivalence topologique**

Les distances sont topologiquement équivalentes car l'application $x \mapsto \frac{x}{1+x}$ est un homéomorphisme de $\mathbb{R}_+$ sur $[0, 1[$. Elles induisent les mêmes voisinages (si l'une tend vers 0, l'autre aussi). Cependant, elles ne sont *pas* uniformément équivalentes si $X$ est non borné. $\blacksquare$
