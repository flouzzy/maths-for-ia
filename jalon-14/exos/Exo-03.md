---
uuid: "jalon-14-exo-03"
title: "Application de la définition de la limite pour une suite rationnelle"
tags: ["math/analyse", "suites", "limites", "epsilon-N", "exercice"]
---
# Exercice 3 : Application de la définition de la limite pour une suite rationnelle
## Énoncé
Soit la suite réelle $(u_n)_{n \in \mathbb{N}}$ définie pour tout entier naturel $n$ par la relation $u_n = \frac{3n+2}{n+1}$.

Démontrer, en utilisant la définition rigoureuse de la limite d'une suite (la définition avec $\epsilon$ et $N$), que la suite $(u_n)$ converge vers 3.

## Correction Détaillée
Pour démontrer que la suite $(u_n)$ converge vers 3 en utilisant la définition rigoureuse de la limite, nous devons montrer que pour tout réel $\epsilon > 0$, il existe un entier naturel $N$ tel que pour tout entier naturel $n \ge N$, l'inégalité $|u_n - 3| < \epsilon$ est vérifiée.

1.  **Fixons un $\epsilon$ arbitraire :**
    Soit $\epsilon$ un nombre réel strictement positif ($\epsilon > 0$). Notre objectif est de trouver un entier $N$ (qui dépendra de $\epsilon$) tel que la condition de convergence soit satisfaite.

2.  **Calcul de la différence $|u_n - 3|$ :**
    Nous commençons par exprimer la valeur absolue de la différence entre $u_n$ et la limite supposée 3 :
    $$|u_n - 3| = \left|\frac{3n+2}{n+1} - 3\right|$$
    Pour simplifier cette expression, nous mettons les termes sous un dénominateur commun :
    $$|u_n - 3| = \left|\frac{3n+2}{n+1} - \frac{3(n+1)}{n+1}\right|$$
    $$|u_n - 3| = \left|\frac{(3n+2) - (3n+3)}{n+1}\right|$$
    $$|u_n - 3| = \left|\frac{3n+2-3n-3}{n+1}\right|$$
    $$|u_n - 3| = \left|\frac{-1}{n+1}\right|$$
    Puisque $n$ est un entier naturel, $n \ge 0$. Par conséquent, $n+1$ est toujours strictement positif ($n+1 \ge 1$). La valeur absolue de $\frac{-1}{n+1}$ est donc $\frac{1}{n+1}$ :
    $$|u_n - 3| = \frac{1}{n+1}$$

3.  **Établissement de l'inégalité :**
    Nous voulons que cette différence soit inférieure à $\epsilon$ :
    $$\frac{1}{n+1} < \epsilon$$

4.  **Résolution de l'inégalité pour $n$ :**
    Puisque $\epsilon > 0$ et $n+1 > 0$, nous pouvons prendre l'inverse des deux côtés de l'inégalité, ce qui inverse le sens de l'inégalité :
    $$n+1 > \frac{1}{\epsilon}$$
    Maintenant, isolons $n$ :
    $$n > \frac{1}{\epsilon} - 1$$

5.  **Choix de l'entier $N$ :**
    Nous devons trouver un entier $N$ tel que pour tout $n \ge N$, la condition $n > \frac{1}{\epsilon} - 1$ soit satisfaite.
    Un choix approprié pour $N$ est le plus petit entier supérieur ou égal à $\frac{1}{\epsilon} - 1$. Nous pouvons utiliser la fonction partie entière supérieure (plafond) ou simplement prendre un entier légèrement plus grand.
    Choisissons $N$ comme l'entier naturel défini par :
    $$N = \max\left(0, \left\lfloor \frac{1}{\epsilon} - 1 \right\rfloor + 1\right)$$
    *Justification du choix de $N$ :*
    Si $\frac{1}{\epsilon} - 1$ est négatif ou nul (ce qui arrive si $\epsilon \ge 1$), alors $\left\lfloor \frac{1}{\epsilon} - 1 \right\rfloor + 1$ pourrait être 0 ou 1. Dans ce cas, $N=0$ est suffisant car $n \ge 0$ implique $n > \frac{1}{\epsilon} - 1$ (par exemple, si $\epsilon=2$, $1/\epsilon - 1 = -0.5$, $n > -0.5$ est vrai pour tout $n \ge 0$).
    Si $\frac{1}{\epsilon} - 1$ est positif, alors $N = \left\lfloor \frac{1}{\epsilon} - 1 \right\rfloor + 1$ est un entier strictement supérieur à $\frac{1}{\epsilon} - 1$.
    Ainsi, pour tout $n \ge N$, nous avons $n \ge N > \frac{1}{\epsilon} - 1$.

6.  **Conclusion :**
    Nous avons montré que pour tout $\epsilon > 0$, il existe un entier naturel $N = \max\left(0, \left\lfloor \frac{1}{\epsilon} - 1 \right\rfloor + 1\right)$ tel que pour tout $n \ge N$, l'inégalité $n > \frac{1}{\epsilon} - 1$ est vérifiée.
    Cette inégalité implique successivement :
    $$n+1 > \frac{1}{\epsilon}$$
    $$\frac{1}{n+1} < \epsilon$$
    $$|u_n - 3| < \epsilon$$
    Par conséquent, selon la définition rigoureuse de la limite, la suite $(u_n)$ converge vers 3.
    $$\lim_{n \to \infty} \frac{3n+2}{n+1} = 3$$