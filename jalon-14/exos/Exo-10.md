---
uuid: "exo-14-10"
title: "Exercice 10 - Suites (Difficulté 5 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 10
Soit la suite définie par $u_0 = 1$ et $u_{n+1} = \frac{1}{1 + u_n}$ pour $n \in \mathbb{N}$.
Montrer que la suite converge et trouver sa limite en utilisant le théorème des accroissements finis et le théorème du point fixe.

## Correction

Étape 1 : Bonne définition et stabilité d'un intervalle
On pose $f(x) = \frac{1}{1+x}$. La suite s'écrit $u_{n+1} = f(u_n)$.
La fonction $f$ est définie sur $[0, +\infty[$ et à valeurs dans $]0, 1] \subset [0, +\infty[$.
Comme $u_0 = 1 \in [0, +\infty[$, par récurrence immédiate, $u_n$ est bien définie pour tout $n$ et $u_n \ge 0$.

Étape 2 : Recherche du point fixe
Si la suite $(u_n)$ converge vers une limite $l$, par continuité de $f$ sur $[0, +\infty[$, cette limite doit vérifier l'équation $f(l) = l$.
$$
\begin{align*}
f(l) &= l \\
\frac{1}{1+l} &= l \\
1 &= l(1+l) \\
l^2 + l - 1 &= 0
\end{align*}
$$
Le discriminant de cette équation du second degré est $\Delta = 1^2 - 4(1)(-1) = 5$.
Les solutions sont $l_1 = \frac{-1 - \sqrt{5}}{2}$ et $l_2 = \frac{-1 + \sqrt{5}}{2}$.
Comme pour tout $n$, $u_n \ge 0$, si la limite existe, elle doit être positive. On écarte $l_1 < 0$.
L'unique candidat pour la limite est le nombre d'or conjugué $l = \frac{-1 + \sqrt{5}}{2}$.
Remarquons que $l \in [0, 1]$.

Étape 3 : Utilisation du théorème des accroissements finis (TAF)
La fonction $f$ est dérivable sur $[0, +\infty[$ et sa dérivée est :
$$ f'(x) = \frac{-1}{(1+x)^2} $$

Pour tout $x \ge 0$, on a $(1+x)^2 \ge 1$, donc :
$$ |f'(x)| = \frac{1}{(1+x)^2} \le 1 $$
Cependant, ceci ne donne pas une contraction stricte.
Réduisons l'intervalle d'étude. On remarque que $u_1 = f(1) = 1/2$.
Donc pour tout $n \ge 1$, $u_n = f(u_{n-1}) \in [1/2, 1]$.
L'intervalle $I = [1/2, 1]$ est stable par $f$. La limite $l$ appartient aussi à cet intervalle.

Évaluons la dérivée sur cet intervalle.
Pour tout $x \in [1/2, 1]$, $1+x \ge \frac{3}{2}$.
Donc $(1+x)^2 \ge \frac{9}{4}$.
Ainsi, $|f'(x)| = \frac{1}{(1+x)^2} \le \frac{4}{9}$.

Posons $k = \frac{4}{9}$. Puisque $k \in ]0, 1[$, $f$ est $k$-lipschitzienne sur $I$.
Par le théorème des accroissements finis, pour tous $x, y \in I$ :
$$ |f(x) - f(y)| \le k|x - y| $$

Étape 4 : Preuve de la convergence
Pour tout entier $n \ge 1$, appliquons cette inégalité à $x = u_n$ et $y = l$. (Sachant que $u_n \in I$ et $l \in I$ et que $f(l) = l$).
$$
\begin{align*}
|f(u_n) - f(l)| &\le k|u_n - l| \\
|u_{n+1} - l| &\le k|u_n - l|
\end{align*}
$$

Par une récurrence immédiate, pour tout $n \ge 1$ :
$$ |u_n - l| \le k^{n-1} |u_1 - l| $$

Comme $k = 4/9 < 1$, on a $\lim_{n \to \infty} k^{n-1} = 0$.
Par le théorème d'encadrement, $0 \le |u_n - l| \le k^{n-1} |u_1 - l|$, ce qui implique que :
$$ \lim_{n \to \infty} |u_n - l| = 0 $$

Donc la suite $(u_n)_{n \in \mathbb{N}}$ converge rigoureusement vers $l = \frac{\sqrt{5} - 1}{2}$.
