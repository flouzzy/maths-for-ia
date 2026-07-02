---
title: "Exercice 5 - Jalon 15"
theme: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
difficulty: "★★★"
author: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
keywords:
  - "sous-suite"
  - "valeur d'adhérence"
  - "Bolzano-Weierstrass"
  - "suite bornée"
  - "ensemble des valeurs d'adhérence"
  - "limite supérieure"
  - "limite inférieure"
  - "suite périodique"
---

## Énoncé

Soit la suite $(u_n)_{n \in \mathbb{N}}$ définie pour tout $n \in \mathbb{N}$ par :
$$u_n = \sin\left(\frac{n\pi}{3}\right) + \cos\left(\frac{n\pi}{2}\right)$$

1.  Montrer que la suite $(u_n)_{n \in \mathbb{N}}$ est bornée.
2.  Déterminer l'ensemble $A$ des valeurs d'adhérence de la suite $(u_n)_{n \in \mathbb{N}}$.
3.  Déterminer $\limsup_{n \to \infty} u_n$ et $\liminf_{n \to \infty} u_n$.
4.  La suite $(u_n)_{n \in \mathbb{N}}$ converge-t-elle ? Justifier votre réponse.

---

## Correction

### Question 1 : Montrer que la suite $(u_n)_{n \in \mathbb{N}}$ est bornée.

Pour tout $x \in \mathbb{R}$, nous savons que les fonctions sinus et cosinus sont bornées. Plus précisément, pour tout $x \in \mathbb{R}$, nous avons :
$$|\sin(x)| \le 1 \quad \text{et} \quad |\cos(x)| \le 1$$
En appliquant cette propriété à $u_n$, nous obtenons :
$$|u_n| = \left|\sin\left(\frac{n\pi}{3}\right) + \cos\left(\frac{n\pi}{2}\right)\right|$$
Par l'inégalité triangulaire, nous avons :
$$|u_n| \le \left|\sin\left(\frac{n\pi}{3}\right)\right| + \left|\cos\left(\frac{n\pi}{2}\right)\right|$$
En utilisant les bornes des fonctions sinus et cosinus :
$$|u_n| \le 1 + 1$$
$$|u_n| \le 2$$
Ainsi, pour tout $n \in \mathbb{N}$, la suite $(u_n)_{n \in \mathbb{N}}$ est bornée par 2 (elle est minorée par $-2$ et majorée par $2$).

### Question 2 : Déterminer l'ensemble $A$ des valeurs d'adhérence de la suite $(u_n)_{n \in \mathbb{N}}$.

Puisque la suite $(u_n)_{n \in \mathbb{N}}$ est bornée, le théorème de Bolzano-Weierstrass garantit l'existence d'au moins une valeur d'adhérence.

Observons la périodicité des termes de la suite.
La suite $\left(\sin\left(\frac{n\pi}{3}\right)\right)_{n \in \mathbb{N}}$ est périodique de période $T_1$. La plus petite période $T_1$ est telle que $\frac{(n+T_1)\pi}{3} = \frac{n\pi}{3} + 2k\pi$ pour un entier $k$. Cela implique $\frac{T_1\pi}{3} = 2k\pi$, donc $T_1 = 6k$. La plus petite période positive est $T_1 = 6$ (pour $k=1$).
La suite $\left(\cos\left(\frac{n\pi}{2}\right)\right)_{n \in \mathbb{N}}$ est périodique de période $T_2$. La plus petite période $T_2$ est telle que $\frac{(n+T_2)\pi}{2} = \frac{n\pi}{2} + 2k\pi$ pour un entier $k$. Cela implique $\frac{T_2\pi}{2} = 2k\pi$, donc $T_2 = 4k$. La plus petite période positive est $T_2 = 4$ (pour $k=1$).

La suite $(u_n)_{n \in \mathbb{N}}$ est la somme de deux suites périodiques. Sa période $T$ est le plus petit commun multiple des périodes $T_1$ et $T_2$.
$T = \text{lcm}(T_1, T_2) = \text{lcm}(6, 4) = 12$.
Donc, $u_{n+12} = u_n$ pour tout $n \in \mathbb{N}$.

Une suite périodique ne prend qu'un nombre fini de valeurs. L'ensemble des valeurs d'adhérence d'une suite périodique est précisément l'ensemble de toutes les valeurs qu'elle prend. Nous devons donc calculer $u_n$ pour $n = 0, 1, \dots, 11$.

*   $n=0: u_0 = \sin(0) + \cos(0) = 0 + 1 = 1$.
*   $n=1: u_1 = \sin(\pi/3) + \cos(\pi/2) = \frac{\sqrt{3}}{2} + 0 = \frac{\sqrt{3}}{2}$.
*   $n=2: u_2 = \sin(2\pi/3) + \cos(\pi) = \frac{\sqrt{3}}{2} - 1$.
*   $n=3: u_3 = \sin(\pi) + \cos(3\pi/2) = 0 + 0 = 0$.
*   $n=4: u_4 = \sin(4\pi/3) + \cos(2\pi) = -\frac{\sqrt{3}}{2} + 1$.
*   $n=5: u_5 = \sin(5\pi/3) + \cos(5\pi/2) = -\frac{\sqrt{3}}{2} + 0 = -\frac{\sqrt{3}}{2}$.
*   $n=6: u_6 = \sin(2\pi) + \cos(3\pi) = 0 - 1 = -1$.
*   $n=7: u_7 = \sin(7\pi/3) + \cos(7\pi/2) = \sin(\pi/3) + \cos(3\pi/2) = \frac{\sqrt{3}}{2} + 0 = \frac{\sqrt{3}}{2}$. (Identique à $u_1$)
*   $n=8: u_8 = \sin(8\pi/3) + \cos(4\pi) = \sin(2\pi/3) + \cos(0) = \frac{\sqrt{3}}{2} + 1$.
*   $n=9: u_9 = \sin(3\pi) + \cos(9\pi/2) = \sin(\pi) + \cos(\pi/2) = 0 + 0 = 0$. (Identique à $u_3$)
*   $n=10: u_{10} = \sin(10\pi/3) + \cos(5\pi) = \sin(4\pi/3) + \cos(\pi) = -\frac{\sqrt{3}}{2} - 1$.
*   $n=11: u_{11} = \sin(11\pi/3) + \cos(11\pi/2) = \sin(5\pi/3) + \cos(3\pi/2) = -\frac{\sqrt{3}}{2} + 0 = -\frac{\sqrt{3}}{2}$. (Identique à $u_5$)

L'ensemble des valeurs prises par la suite est donc :
$$S = \left\{1, \frac{\sqrt{3}}{2}, \frac{\sqrt{3}}{2}-1, 0, -\frac{\sqrt{3}}{2}+1, -\frac{\sqrt{3}}{2}, -1, \frac{\sqrt{3}}{2}+1, -\frac{\sqrt{3}}{2}-1\right\}$$
En ordonnant ces valeurs de manière croissante pour plus de clarté :
*   $-\frac{\sqrt{3}}{2}-1 \approx -1.866$
*   $-1$
*   $-\frac{\sqrt{3}}{2} \approx -0.866$
*   $\frac{\sqrt{3}}{2}-1 \approx -0.134$
*   $0$
*   $-\frac{\sqrt{3}}{2}+1 \approx 0.134$
*   $\frac{\sqrt{3}}{2} \approx 0.866$
*   $1$
*   $\frac{\sqrt{3}}{2}+1 \approx 1.866$

Toutes ces valeurs sont distinctes. L'ensemble $A$ des valeurs d'adhérence de la suite $(u_n)_{n \in \mathbb{N}}$ est donc :
$$A = \left\{-\frac{\sqrt{3}}{2}-1, -1, -\frac{\sqrt{3}}{2}, \frac{\sqrt{3}}{2}-1, 0, -\frac{\sqrt{3}}{2}+1, \frac{\sqrt{3}}{2}, 1, \frac{\sqrt{3}}{2}+1\right\}$$

### Question 3 : Déterminer $\limsup_{n \to \infty} u_n$ et $\liminf_{n \to \infty} u_n$.

Pour une suite bornée, la limite supérieure est la plus grande des valeurs d'adhérence, et la limite inférieure est la plus petite des valeurs d'adhérence.
D'après la question précédente, l'ensemble $A$ des valeurs d'adhérence est :
$$A = \left\{-\frac{\sqrt{3}}{2}-1, -1, -\frac{\sqrt{3}}{2}, \frac{\sqrt{3}}{2}-1, 0, -\frac{\sqrt{3}}{2}+1, \frac{\sqrt{3}}{2}, 1, \frac{\sqrt{3}}{2}+1\right\}$$
La plus grande valeur dans cet ensemble est $\frac{\sqrt{3}}{2}+1$.
La plus petite valeur dans cet ensemble est $-\frac{\sqrt{3}}{2}-1$.

Donc :
$$\limsup_{n \to \infty} u_n = \max A = \frac{\sqrt{3}}{2}+1$$
$$\liminf_{n \to \infty} u_n = \min A = -\frac{\sqrt{3}}{2}-1$$

### Question 4 : La suite $(u_n)_{n \in \mathbb{N}}$ converge-t-elle ? Justifier votre réponse.

Une suite réelle $(u_n)_{n \in \mathbb{N}}$ converge si et seulement si son ensemble de valeurs d'adhérence $A$ contient un unique élément.
Dans notre cas, l'ensemble $A$ contient 9 éléments distincts. Par conséquent, la suite ne converge pas.

Une autre condition équivalente pour la convergence d'une suite bornée est que sa limite supérieure soit égale à sa limite inférieure.
Nous avons trouvé :
$$\limsup_{n \to \infty} u_n = \frac{\sqrt{3}}{2}+1$$
$$\liminf_{n \to \infty} u_n = -\frac{\sqrt{3}}{2}-1$$
Puisque $\frac{\sqrt{3}}{2}+1 \ne -\frac{\sqrt{3}}{2}-1$ (en effet, $\frac{\sqrt{3}}{2}+1 \approx 1.866$ et $-\frac{\sqrt{3}}{2}-1 \approx -1.866$), la suite $(u_n)_{n \in \mathbb{N}}$ ne converge pas.

---
