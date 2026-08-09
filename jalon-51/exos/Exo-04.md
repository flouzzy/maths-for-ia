---
title: "Exo-04 : Distance sur l'espace des suites"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exo-04 : Distance sur l'espace des suites


## 1. Énoncé

Soit $S$ l'ensemble de toutes les suites à valeurs réelles $x = (x_n)_{n \in \mathbb{N}}$.
On définit l'application :
$$d(x, y) = \sum_{n=0}^{+\infty} \frac{1}{2^n} \frac{|x_n - y_n|}{1 + |x_n - y_n|}$$

1. Montrer que la fonction $t \mapsto \frac{t}{1+t}$ est strictement croissante sur $\mathbb{R}_+$ et majorée.
2. Justifier que la série définissant $d$ converge toujours.
3. Montrer que $d$ est une distance sur $S$.

## 2. Correction détaillée

**Question 1 :**
Soit $f(t) = \frac{t}{1+t}$. La fonction est dérivable sur $\mathbb{R}_+$.
$f'(t) = \frac{1 \cdot (1+t) - t \cdot 1}{(1+t)^2} = \frac{1}{(1+t)^2}$.
Puisque $f'(t) > 0$, $f$ est strictement croissante.
De plus, $f(t) = 1 - \frac{1}{1+t}$, donc pour $t \ge 0$, $f(t) < 1$. Elle est majorée par 1.

**Question 2 :**
Pour tout entier $n$, posons $u_n = \frac{1}{2^n} f(|x_n - y_n|)$.
Puisque $f(t) < 1$, on a $0 \le u_n \le \frac{1}{2^n}$.
La série de terme général $1/2^n$ est une série géométrique convergente de raison $1/2$.
Par le théorème de comparaison des séries à termes positifs, la série définissant $d(x,y)$ converge absolument pour toutes suites $x, y$.

**Question 3 :**
Vérifions les axiomes :
- **Séparation :** $d(x, y) = 0 \iff \sum_{n=0}^{+\infty} u_n = 0$. Comme c'est une somme de termes positifs ou nuls, elle est nulle si et seulement si tous les termes sont nuls : $\forall n, |x_n - y_n| = 0$, donc $x = y$.
- **Symétrie :** Évidente car $|x_n - y_n| = |y_n - x_n|$.
- **Inégalité triangulaire :** Utilisons la croissance de $f$.
  On a $|x_n - z_n| \le |x_n - y_n| + |y_n - z_n|$.
  Comme $f$ est croissante, $f(|x_n - z_n|) \le f(|x_n - y_n| + |y_n - z_n|)$.
  Or, on peut montrer que pour tous $a,b \ge 0$, $f(a+b) = \frac{a+b}{1+a+b} = \frac{a}{1+a+b} + \frac{b}{1+a+b} \le \frac{a}{1+a} + \frac{b}{1+b} = f(a) + f(b)$.
  Donc $f(|x_n - z_n|) \le f(|x_n - y_n|) + f(|y_n - z_n|)$.
  En multipliant par $1/2^n$ et en sommant sur $n$, on obtient $d(x, z) \le d(x, y) + d(y, z)$.
