# Exercice 8 : Prolongement sur $c_0$ et $l^\infty$
$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $c_0$ l'espace des suites réelles tendant vers 0, muni de la norme infinie.
Montrer qu'il existe $L \in (l^\infty)^*$ tel que $L(x) = \lim_{n \to \infty} x_n$ si la limite existe, et de norme 1, mais que $L$ s'annule sur tout $c_0$.

## Correction Détaillée
1. Soit $c$ le sous-espace de $l^\infty$ des suites convergentes.
2. Sur $c$, $f(x) = \lim x_n$ est linéaire, et $|f(x)| \le \|x\|_\infty$, donc $\|f\| = 1$.
3. Par Hahn-Banach, on prolonge $f$ en $L$ sur $l^\infty$ avec $\|L\| = \|f\| = 1$.
4. Pour tout $x \in c_0$, $x$ converge vers 0, donc $x \in c$. Par construction, $L(x) = f(x) = \lim x_n = 0$.
5. Donc $L$ s'annule sur $c_0$.
6. Cet exemple prouve que le dual de $l^\infty$ est strictement plus grand que $l^1$ (car les éléments de $l^1$ s'identifient au dual de $c_0$). $\blacksquare$
