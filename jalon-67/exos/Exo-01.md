---
title: "Exercice 1 : Application directe du théorème"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Application directe du théorème

**Difficulté :** $\bigstar\star\star\star\star$

## Problème

Soit $f_n(x) = \left(1 - \frac{x}{n}\right)^n \mathbf{1}_{[0,n]}(x)$. Calculer $\lim_{n \to \infty} \int_0^n f_n(x) dx$.

## Démonstration et Résolution

### Étape 1 : Mesurabilité et positivité
Pour tout entier $n \ge 1$, la fonction $f_n(x) = \left(1 - \frac{x}{n}\right)^n \mathbf{1}_{[0,n]}(x)$ est le produit d'un polynôme et de l'indicatrice d'un segment. Elle est continue sur $[0,n]$ et mesurable au sens de Borel. De plus, pour $x \in [0,n]$, $\frac{x}{n} \le 1$, donc $1 - \frac{x}{n} \ge 0$. Par suite, $f_n(x) \ge 0$ pour tout $x \in \mathbb{R}$.

### Étape 2 : Convergence ponctuelle
Fixons un réel $x \ge 0$. Il existe un rang $N$ tel que pour tout $n \ge N$, on a $n > x$, ce qui implique que $\mathbf{1}_{[0,n]}(x) = 1$.
Pour $n \ge N$, nous avons $f_n(x) = \left(1 - \frac{x}{n}\right)^n$.
Prenons le logarithme naturel :
$\ln(f_n(x)) = n \ln\left(1 - \frac{x}{n}\right)$
En effectuant un développement limité de $\ln(1 - u)$ en $0$ pour $u = \frac{x}{n} \to 0$ :
$\ln\left(1 - \frac{x}{n}\right) = -\frac{x}{n} + o\left(\frac{1}{n}\right)$
Donc, $n \ln\left(1 - \frac{x}{n}\right) = n \left(-\frac{x}{n} + o\left(\frac{1}{n}\right)\right) = -x + o(1)$.
Par passage à la limite, $\lim_{n \to \infty} \ln(f_n(x)) = -x$.
Par continuité de la fonction exponentielle, on conclut que :
$\lim_{n \to \infty} f_n(x) = e^{-x}$.

### Étape 3 : Croissance de la suite de fonctions
Il faut démontrer que pour tout $x \in \mathbb{R}$ et tout $n \ge 1$, $f_n(x) \le f_{n+1}(x)$.
Si $x \notin [0, n+1]$, $f_n(x) = f_{n+1}(x) = 0$.
Si $x \in (n, n+1]$, $f_n(x) = 0$ et $f_{n+1}(x) \ge 0$, l'inégalité est vérifiée.
Si $x \in [0, n]$, on étudie la fonction $t \mapsto \left(1 - \frac{x}{t}\right)^t$ pour $t \ge x$.
Posons $g(t) = t \ln\left(1 - \frac{x}{t}\right) = t \ln\left(\frac{t-x}{t}\right)$.
Dérivons $g$ par rapport à $t$ :
$g'(t) = \ln\left(1 - \frac{x}{t}\right) + t \cdot \frac{t}{t-x} \cdot \frac{x}{t^2} = \ln\left(1 - \frac{x}{t}\right) + \frac{x}{t-x}$.
Or, pour tout $u \in (0,1)$, on sait que $\ln(1-u) \ge -\frac{u}{1-u}$ (ce qui se démontre en étudiant la fonction $u \mapsto \ln(1-u) + \frac{u}{1-u}$). En posant $u = \frac{x}{t}$, on obtient exactement $g'(t) \ge 0$.
La fonction $t \mapsto f_t(x)$ est donc croissante. En particulier, $f_n(x) \le f_{n+1}(x)$.

### Étape 4 : Application du théorème de Beppo Levi
La suite $(f_n)_{n \in \mathbb{N}}$ est mesurable, positive et croissante. Elle converge ponctuellement vers $f(x) = e^{-x} \mathbf{1}_{[0,+\infty)}(x)$.
D'après le théorème de convergence monotone de Beppo Levi, nous pouvons intervertir la limite et l'intégrale :
$\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n dx = \int_0^{+\infty} \lim_{n \to \infty} f_n(x) dx = \int_0^{+\infty} e^{-x} dx$
Calculons cette intégrale de base :
$\int_0^{+\infty} e^{-x} dx = \lim_{M \to +\infty} \left[-e^{-x}\right]_0^M = \lim_{M \to +\infty} (-e^{-M} + 1) = 1$.
La limite cherchée vaut $1$.
