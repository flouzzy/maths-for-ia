# Exercice 5 : Égalité presque partout de fonctions continues

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $X = \mathbb{R}$ muni de la mesure de Lebesgue $\lambda$.
Soient $f$ et $g$ deux fonctions **continues** de $\mathbb{R}$ dans $\mathbb{R}$.
Supposons que $f = g$ presque partout.
Démontrer que $f(x) = g(x)$ pour tout $x \in \mathbb{R}$ (égalité partout).

---

## Correction détaillée

Soit $h = f - g$. La fonction $h$ est continue sur $\mathbb{R}$ car différence de fonctions continues.
L'hypothèse indique que $h = 0$ presque partout. Soit $N = \{x \in \mathbb{R} \mid h(x) \neq 0\}$. On a $\lambda(N) = 0$.
Procédons par l'absurde. Supposons qu'il existe $x_0 \in \mathbb{R}$ tel que $h(x_0) \neq 0$. Sans perte de généralité, supposons $h(x_0) = c > 0$.
Par définition de la continuité de $h$ en $x_0$, pour $\epsilon = c/2 > 0$, il existe un $\delta > 0$ tel que pour tout $x \in ]x_0 - \delta, x_0 + \delta[$, on a :
$$ |h(x) - h(x_0)| < \epsilon \implies h(x) > c - \epsilon = c/2 > 0 $$
Ainsi, pour tout $x \in ]x_0 - \delta, x_0 + \delta[$, la fonction $h$ est strictement non nulle.
Soit $I = ]x_0 - \delta, x_0 + \delta[$. On a $I \subset N$.
Par monotonie de la mesure de Lebesgue :
$$ \lambda(N) \ge \lambda(I) = (x_0 + \delta) - (x_0 - \delta) = 2\delta > 0 $$
Ceci contredit l'hypothèse $\lambda(N) = 0$.
L'hypothèse de départ est donc fausse. On en conclut qu'il n'existe aucun $x_0$ tel que $h(x_0) \neq 0$.
Donc $h(x) = 0$ pour tout $x \in \mathbb{R}$, c'est-à-dire $f(x) = g(x)$ partout.

**Remarque :** Ce résultat est crucial. Dans une classe d'équivalence de $L^p$, s'il existe un représentant continu, alors il est **unique**. C'est le "meilleur" représentant.
