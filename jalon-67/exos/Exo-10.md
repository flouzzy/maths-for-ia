# Exercice 10 : Démonstration par l'absurde de la stricte monotonie
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Donner un contre-exemple explicite où $\lim \int f_n = \int \lim f_n$ mais où la suite $(f_n)$ n'est NI croissante NI dominée.

## Correction Détaillée

Considérons sur l'intervalle $[0, 1]$ muni de la mesure de Lebesgue, la suite de fonctions $f_n$ définie par :
$f_n(x) = n \mathbf{1}_{]0, 1/n[}(x) - n \mathbf{1}_{]1/n, 2/n[}(x)$ pour $n \geq 2$.
- Limite simple : Pour tout $x > 0$, il existe $N$ tel que $2/N < x$. Pour $n \geq N$, $f_n(x) = 0$. Donc $f_n(x) \to 0$ p.p., et $f(x) = 0$. Son intégrale est $\int_0^1 f(x) dx = 0$.
- Intégrale des $f_n$ :
$\int_0^1 f_n(x) dx = \int_0^{1/n} n dx - \int_{1/n}^{2/n} n dx = n(1/n) - n(1/n) = 1 - 1 = 0$.
La limite des intégrales est donc $0$.
L'égalité $\lim \int f_n = \int \lim f_n = 0$ est bien vérifiée.
- La suite n'est pas croissante, car $f_n(x)$ prend des valeurs négatives de plus en plus "profondes", par exemple $f_2(3/4) = 0$ mais en prenant un $x$ adéquat la variation alterne.
- La suite n'est pas dominée car les pics positifs et négatifs ont pour hauteur $|f_n(x)| = n \to \infty$. Il n'y a pas de fonction intégrable majorante indépendante de $n$.
Cela montre que les hypothèses du TCM (ou TCD) sont des conditions *suffisantes* mais pas *nécessaires* pour l'interversion de la limite et de l'intégrale.
