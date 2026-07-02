---
title: "Exercice 4 - Jalon 15"
subtitle: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
author: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
difficulty: "★★"
keywords:
  - sous-suite
  - valeur d'adhérence
  - Bolzano-Weierstrass
  - suite bornée
  - limite supérieure
  - limite inférieure
---

## Énoncé

Soit la suite $(u_n)_{n \in \mathbb{N}^*}$ définie pour tout $n \in \mathbb{N}^*$ par :
$$u_n = \left(1 + \frac{(-1)^n}{n}\right) \sin\left(\frac{n\pi}{2}\right)$$

1.  Démontrer que la suite $(u_n)$ admet au moins une sous-suite convergente.
2.  Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$.
3.  En déduire la limite supérieure ($\limsup u_n$) et la limite inférieure ($\liminf u_n$) de la suite $(u_n)$.

---

## Correction

### Question 1 : Démontrer que la suite $(u_n)$ admet au moins une sous-suite convergente.

Pour démontrer qu'une suite réelle admet au moins une sous-suite convergente, nous pouvons invoquer le théorème de Bolzano-Weierstrass. Ce théorème stipule que toute suite réelle bornée admet au moins une sous-suite convergente. Il est donc nécessaire et suffisant de prouver que la suite $(u_n)$ est bornée.

Pour tout $n \in \mathbb{N}^*$, nous calculons la valeur absolue de $u_n$ :
$$|u_n| = \left|\left(1 + \frac{(-1)^n}{n}\right) \sin\left(\frac{n\pi}{2}\right)\right|$$
En utilisant la propriété de multiplicativité de la valeur absolue, $|ab| = |a||b|$ :
$$|u_n| = \left|1 + \frac{(-1)^n}{n}\right| \left|\sin\left(\frac{n\pi}{2}\right)\right|$$
Nous savons que pour tout $x \in \mathbb{R}$, $|\sin(x)| \le 1$. En particulier, pour tout $n \in \mathbb{N}^*$, $\left|\sin\left(\frac{n\pi}{2}\right)\right| \le 1$.

Concentrons-nous sur le terme $\left|1 + \frac{(-1)^n}{n}\right|$ :
Pour tout $n \in \mathbb{N}^*$, nous avons $\left|\frac{(-1)^n}{n}\right| = \frac{1}{n}$.
Par l'inégalité triangulaire inverse, $| |a| - |b| | \le |a+b| \le |a| + |b|$.
Ici, $a=1$ et $b=\frac{(-1)^n}{n}$. Donc, $\left|1 + \frac{(-1)^n}{n}\right| \le |1| + \left|\frac{(-1)^n}{n}\right| = 1 + \frac{1}{n}$.

Puisque $n \in \mathbb{N}^*$, le plus petit entier $n$ est $1$.
Pour $n=1$, $1 + \frac{1}{n} = 1 + \frac{1}{1} = 2$.
Pour $n \ge 1$, la fonction $f(x) = 1/x$ est décroissante. Donc, $1/n \le 1/1 = 1$.
Par conséquent, $1 + \frac{1}{n} \le 1 + 1 = 2$ pour tout $n \in \mathbb{N}^*$.

En combinant ces inégalités, nous obtenons :
$$|u_n| \le \left(1 + \frac{1}{n}\right) \cdot 1 \le 2$$
Ainsi, pour tout $n \in \mathbb{N}^*$, $|u_n| \le 2$. Cela signifie que la suite $(u_n)$ est bornée (elle est majorée par $2$ et minorée par $-2$).

Puisque la suite $(u_n)$ est une suite réelle bornée, le théorème de Bolzano-Weierstrass s'applique et garantit qu'elle admet au moins une sous-suite convergente.

### Question 2 : Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$.

Pour déterminer l'ensemble des valeurs d'adhérence, nous allons analyser le comportement de la suite $(u_n)$ en fonction des valeurs que prend $\sin(n\pi/2)$. Les valeurs de $\sin(n\pi/2)$ dépendent de la parité de $n$ et de $n \pmod 4$.

Le terme $\sin(n\pi/2)$ prend les valeurs suivantes :
*   Si $n$ est un entier pair, $n=2k$ pour $k \in \mathbb{N}^*$: $\sin(k\pi) = 0$.
*   Si $n$ est un entier impair, $n=2k+1$ pour $k \in \mathbb{N}$: $\sin((2k+1)\pi/2) = \sin(k\pi + \pi/2) = (-1)^k$.

Nous allons considérer trois cas distincts pour les indices $n$, qui partitionnent $\mathbb{N}^*$.

**Cas 1 : $n$ est un entier pair.**
Soit $n=2k$ pour $k \in \mathbb{N}^*$.
Alors l'expression de $u_n$ devient :
$$u_{2k} = \left(1 + \frac{(-1)^{2k}}{2k}\right) \sin\left(\frac{2k\pi}{2}\right) = \left(1 + \frac{1}{2k}\right) \sin(k\pi)$$
Puisque $\sin(k\pi) = 0$ pour tout $k \in \mathbb{N}^*$, nous avons :
$$u_{2k} = \left(1 + \frac{1}{2k}\right) \cdot 0 = 0$$
La sous-suite $(u_{2k})_{k \in \mathbb{N}^*}$ est la suite constante $(0, 0, 0, \dots)$. Cette sous-suite converge trivialement vers $0$.
Par conséquent, $0$ est une valeur d'adhérence de la suite $(u_n)$.

**Cas 2 : $n$ est un entier impair de la forme $4m+1$.**
Soit $n=4m+1$ pour $m \in \mathbb{N}$.
Dans ce cas, $n$ est impair, donc $(-1)^n = (-1)^{4m+1} = -1$.
Pour le terme $\sin(n\pi/2)$, nous avons $n=2(2m)+1$, ce qui correspond à $k=2m$ (un entier pair) dans l'expression $\sin(k\pi + \pi/2) = (-1)^k$.
Ainsi, $\sin\left(\frac{(4m+1)\pi}{2}\right) = \sin\left(2m\pi + \frac{\pi}{2}\right) = \sin\left(\frac{\pi}{2}\right) = 1$.
La sous-suite $(u_{4m+1})_{m \in \mathbb{N}}$ est donnée par :
$$u_{4m+1} = \left(1 + \frac{(-1)^{4m+1}}{4m+1}\right) \sin\left(\frac{(4m+1)\pi}{2}\right) = \left(1 - \frac{1}{4m+1}\right) \cdot 1 = 1 - \frac{1}{4m+1}$$
Lorsque $m \to \infty$, le terme $\frac{1}{4m+1}$ tend vers $0$.
Donc, la limite de cette sous-suite est :
$$\lim_{m \to \infty} u_{4m+1} = \lim_{m \to \infty} \left(1 - \frac{1}{4m+1}\right) = 1 - 0 = 1$$
Par conséquent, $1$ est une valeur d'adhérence de la suite $(u_n)$.

**Cas 3 : $n$ est un entier impair de la forme $4m+3$.**
Soit $n=4m+3$ pour $m \in \mathbb{N}$.
Dans ce cas, $n$ est impair, donc $(-1)^n = (-1)^{4m+3} = -1$.
Pour le terme $\sin(n\pi/2)$, nous avons $n=2(2m+1)+1$, ce qui correspond à $k=2m+1$ (un entier impair) dans l'expression $\sin(k\pi + \pi/2) = (-1)^k$.
Ainsi, $\sin\left(\frac{(4m+3)\pi}{2}\right) = \sin\left(2m\pi + \frac{3\pi}{2}\right) = \sin\left(\frac{3\pi}{2}\right) = -1$.
La sous-suite $(u_{4m+3})_{m \in \mathbb{N}}$ est donnée par :
$$u_{4m+3} = \left(1 + \frac{(-1)^{4m+3}}{4m+3}\right) \sin\left(\frac{(4m+3)\pi}{2}\right) = \left(1 - \frac{1}{4m+3}\right) \cdot (-1) = -\left(1 - \frac{1}{4m+3}\right)$$
Lorsque $m \to \infty$, le terme $\frac{1}{4m+3}$ tend vers $0$.
Donc, la limite de cette sous-suite est :
$$\lim_{m \to \infty} u_{4m+3} = \lim_{m \to \infty} -\left(1 - \frac{1}{4m+3}\right) = -(1 - 0) = -1$$
Par conséquent, $-1$ est une valeur d'adhérence de la suite $(u_n)$.

**Synthèse des valeurs d'adhérence :**
Nous avons identifié trois valeurs d'adhérence : $0$, $1$, et $-1$.
L'ensemble des indices $\mathbb{N}^*$ peut être partitionné en trois sous-ensembles disjoints et dont l'union est $\mathbb{N}^*$:
1.  Les entiers pairs : $\{2, 4, 6, \dots\}$
2.  Les entiers de la forme $4m+1$ : $\{1, 5, 9, \dots\}$
3.  Les entiers de la forme $4m+3$ : $\{3, 7, 11, \dots\}$

Soit $L$ une valeur d'adhérence de la suite $(u_n)$. Par définition, il existe une sous-suite $(u_{\phi(j)})_{j \in \mathbb{N}}$ qui converge vers $L$.
Puisque l'ensemble des indices $\mathbb{N}^*$ est la réunion des trois types d'indices ci-dessus, la suite d'indices $(\phi(j))$ doit contenir une infinité d'éléments d'au moins un de ces trois types.
*   Si $(\phi(j))$ contient une infinité d'indices pairs, alors la sous-suite $(u_{\phi(j)})$ doit avoir une sous-sous-suite qui est une sous-suite de $(u_{2k})$. Cette sous-sous-suite converge vers $0$, et par unicité de la limite, $L$ doit être $0$.
*   Si $(\phi(j))$ contient une infinité d'indices de la forme $4m+1$, alors la sous-suite $(u_{\phi(j)})$ doit avoir une sous-sous-suite qui est une sous-suite de $(u_{4m+1})$. Cette sous-sous-suite converge vers $1$, et par unicité de la limite, $L$ doit être $1$.
*   Si $(\phi(j))$ contient une infinité d'indices de la forme $4m+3$, alors la sous-suite $(u_{\phi(j)})$ doit avoir une sous-sous-suite qui est une sous-suite de $(u_{4m+3})$. Cette sous-sous-suite converge vers $-1$, et par unicité de la limite, $L$ doit être $-1$.

Par conséquent, toute valeur d'adhérence de la suite $(u_n)$ doit nécessairement appartenir à l'ensemble $\{-1, 0, 1\}$.
L'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$ est donc $A = \{-1, 0, 1\}$.

### Question 3 : En déduire la limite supérieure ($\limsup u_n$) et la limite inférieure ($\liminf u_n$) de la suite $(u_n)$.

Pour une suite réelle bornée $(u_n)$, la limite supérieure ($\limsup u_n$) est définie comme le plus grand élément de l'ensemble de ses valeurs d'adhérence. De même, la limite inférieure ($\liminf u_n$) est définie comme le plus petit élément de l'ensemble de ses valeurs d'adhérence.

D'après la question précédente, l'ensemble des valeurs d'adhérence de la suite $(u_n)$ est $A = \{-1, 0, 1\}$.

La limite supérieure de la suite $(u_n)$ est le maximum de cet ensemble :
$$\limsup_{n \to \infty} u_n = \max(A) = \max(\{-1, 0, 1\}) = 1$$

La limite inférieure de la suite $(u_n)$ est le minimum de cet ensemble :
$$\liminf_{n \to \infty} u_n = \min(A) = \min(\{-1, 0, 1\}) = -1$$

---
