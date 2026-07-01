---
uuid: "jalon-14-exo-02"
title: "Exercice 2 : Convergence d'une suite rationnelle par la définition $(\epsilon, N)$"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 2 : Convergence d'une suite rationnelle par la définition $(\epsilon, N)$
## Énoncé
Soit la suite de nombres réels $(u_n)_{n \in \mathbb{N}}$ définie pour tout entier naturel $n$ par l'expression :
$$u_n = \frac{2n+1}{n+3}$$
En utilisant la définition rigoureuse de la limite d'une suite (la définition avec $\epsilon$ et $N$), démontrer que la suite $(u_n)$ converge vers 2.

## Correction Détaillée
Pour démontrer qu'une suite $(u_n)$ converge vers une limite $L$ en utilisant la définition rigoureuse, nous devons montrer que pour tout nombre réel $\epsilon > 0$, il existe un entier naturel $N$ tel que pour tout entier naturel $n \ge N$, l'inégalité $|u_n - L| < \epsilon$ est vérifiée.

Dans cet exercice, la suite est $u_n = \frac{2n+1}{n+3}$ et la limite proposée est $L=2$.

**Étape 1 : Écrire l'inégalité à vérifier.**
Nous devons montrer que pour tout $\epsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $n \ge N$, nous ayons :
$$ \left| \frac{2n+1}{n+3} - 2 \right| < \epsilon $$

**Étape 2 : Simplifier l'expression $|u_n - L|$.**
Commençons par simplifier l'expression à l'intérieur de la valeur absolue :
$$ \frac{2n+1}{n+3} - 2 = \frac{2n+1}{n+3} - \frac{2(n+3)}{n+3} $$
$$ = \frac{2n+1 - (2n+6)}{n+3} $$
$$ = \frac{2n+1 - 2n - 6}{n+3} $$
$$ = \frac{-5}{n+3} $$
Maintenant, appliquons la valeur absolue :
$$ \left| \frac{-5}{n+3} \right| $$
Puisque $n$ est un entier naturel, $n \ge 0$. Par conséquent, $n+3$ est toujours positif ($n+3 \ge 3$).
Ainsi, $\frac{-5}{n+3}$ est toujours un nombre négatif. La valeur absolue d'un nombre négatif est son opposé.
$$ \left| \frac{-5}{n+3} \right| = - \left( \frac{-5}{n+3} \right) = \frac{5}{n+3} $$
L'inégalité à résoudre devient donc :
$$ \frac{5}{n+3} < \epsilon $$

**Étape 3 : Isoler $n$ pour trouver une condition sur $N$.**
Nous cherchons un $N$ tel que pour tout $n \ge N$, l'inégalité $\frac{5}{n+3} < \epsilon$ soit satisfaite.
Puisque $\epsilon > 0$ et $n+3 > 0$, nous pouvons manipuler cette inégalité en toute sécurité (sans changer le sens des inégalités) :
$$ \frac{5}{n+3} < \epsilon $$
Multiplions les deux côtés par $(n+3)$ :
$$ 5 < \epsilon (n+3) $$
Divisons les deux côtés par $\epsilon$ (qui est strictement positif) :
$$ \frac{5}{\epsilon} < n+3 $$
Soustrayons 3 des deux côtés :
$$ \frac{5}{\epsilon} - 3 < n $$
Donc, nous avons besoin que $n$ soit strictement supérieur à $\frac{5}{\epsilon} - 3$.

**Étape 4 : Choisir l'entier $N$.**
Nous devons choisir un entier naturel $N$ tel que si $n \ge N$, alors $n > \frac{5}{\epsilon} - 3$.
Un choix approprié pour $N$ est la partie entière supérieure de $\frac{5}{\epsilon} - 3$, en s'assurant que $N$ est un entier naturel (non-négatif).
$$ N = \max\left(0, \left\lceil \frac{5}{\epsilon} - 3 \right\rceil\right) $$
*   La fonction $\lceil x \rceil$ (plafond ou partie entière supérieure) donne le plus petit entier supérieur ou égal à $x$. Cela garantit que $N$ est un entier.
*   La fonction $\max(0, \cdot)$ garantit que $N$ est un entier naturel (puisque les indices de la suite commencent à $n=0$). Par exemple, si $\epsilon$ est très grand (disons $\epsilon=10$), alors $\frac{5}{10} - 3 = 0.5 - 3 = -2.5$. Dans ce cas, $\lceil -2.5 \rceil = -2$. Le $\max(0, -2)$ donne $0$, ce qui est un $N$ valide. Pour $n \ge 0$, $\frac{5}{n+3} \le \frac{5}{3} \approx 1.67$, ce qui est bien inférieur à $\epsilon=10$.

**Étape 5 : Vérifier que ce choix de $N$ fonctionne.**
Soit $\epsilon > 0$ un nombre réel arbitrairement petit.
Choisissons $N = \max\left(0, \left\lceil \frac{5}{\epsilon} - 3 \right\rceil\right)$.
Considérons tout entier naturel $n$ tel que $n \ge N$.
Par la définition de $N$, nous avons $N \ge \frac{5}{\epsilon} - 3$.
Donc, $n \ge N \implies n \ge \frac{5}{\epsilon} - 3$.
Puisque $n$ est un entier et $\lceil x \rceil$ est le plus petit entier supérieur ou égal à $x$, si $n \ge \lceil x \rceil$, alors $n \ge x$.
Ainsi, $n > \frac{5}{\epsilon} - 3$.
En remontant les étapes de l'inégalité :
$$ n+3 > \frac{5}{\epsilon} $$
Puisque $\epsilon > 0$ et $n+3 > 0$, nous pouvons multiplier par $\epsilon$ et diviser par $n+3$ :
$$ \epsilon > \frac{5}{n+3} $$
Et comme nous avons établi à l'Étape 2 que $\frac{5}{n+3} = \left| \frac{2n+1}{n+3} - 2 \right|$, nous avons bien :
$$ \left| \frac{2n+1}{n+3} - 2 \right| < \epsilon $$

**Étape 6 : Conclusion.**
Nous avons démontré que pour tout $\epsilon > 0$, il existe un entier naturel $N = \max\left(0, \left\lceil \frac{5}{\epsilon} - 3 \right\rceil\right)$ tel que pour tout $n \ge N$, l'inégalité $|u_n - 2| < \epsilon$ est vérifiée.
Par conséquent, selon la définition rigoureuse de la limite, la suite $(u_n)$ converge vers 2.