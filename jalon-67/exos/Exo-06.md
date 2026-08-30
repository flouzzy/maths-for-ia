---
title: "Exercice 6 : Série de fonctions rationnelles"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 6 : Série de fonctions rationnelles

## Énoncé

On définit l'intégrale $J = \int_0^\infty \sum_{n=1}^\infty \frac{x}{(1+x^2)^n} dx$.
1. Justifier rigoureusement l'interversion de la somme et de l'intégrale.
2. Calculer la valeur exacte de l'intégrale de la somme en sommant sous le signe intégrale d'abord.
3. Calculer l'intégrale de chaque terme et sommer, pour vérifier le résultat.

## Correction

1. **Interversion :**
Posons $u_n(x) = \frac{x}{(1+x^2)^n}$. Sur $]0, +\infty[$, pour tout $n \ge 1$, $u_n(x) > 0$. De plus, $u_n$ est continue, donc mesurable par rapport aux boréliens.
Le corollaire du TCM (Théorème de sommation terme à terme de Lebesgue) permet d'intervertir l'intégrale d'une somme infinie de fonctions mesurables **positives** et la série des intégrales. L'interversion est donc inconditionnellement valide.

2. **Calcul en sommant d'abord :**
Fixons $x > 0$. La somme est une série géométrique de raison $q = \frac{1}{1+x^2}$.
Puisque $x>0$, $1+x^2 > 1$, donc $0 < q < 1$. La série géométrique converge.
Le premier terme (pour $n=1$) est $u_1 = \frac{x}{1+x^2}$.
La somme de la série géométrique $S(x) = \sum_{n=1}^\infty u_n(x) = u_1 \frac{1}{1-q} = \frac{x}{1+x^2} \frac{1}{1 - \frac{1}{1+x^2}}$.
Simplifions le dénominateur : $1 - \frac{1}{1+x^2} = \frac{x^2}{1+x^2}$.
Donc $S(x) = \frac{x}{1+x^2} \times \frac{1+x^2}{x^2} = \frac{1}{x}$.
On calcule alors l'intégrale de $S(x)$ :
$$ J = \int_0^\infty S(x) dx = \int_0^\infty \frac{1}{x} dx $$
Cette intégrale diverge en 0 (en $\ln|0|$) et en $+\infty$ (en $\ln|\infty|$).
Donc $J = +\infty$.

3. **Vérification par la somme des intégrales :**
Calculons $I_n = \int_0^\infty \frac{x}{(1+x^2)^n} dx$.
Posons le changement de variable $u = 1+x^2$, $du = 2xdx$, soit $xdx = du/2$.
Les bornes deviennent 1 et $+\infty$.
$I_n = \int_1^\infty \frac{1}{2 u^n} du$.
Si $n=1$, $I_1 = \frac{1}{2} [\ln u]_1^\infty = +\infty$.
La série $\sum I_n$ contient un terme infini. Donc la somme de la série est bien $+\infty$.
Le résultat de Beppo Levi est donc scrupuleusement exact : $+\infty = +\infty$.
