---
title: "Exercice 1 - Jalon 15"
subtitle: "Introduction aux sous-suites et à la convergence"
theme: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
difficulty: "1/5"
author: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
keywords:
  - sous-suite
  - convergence
  - suite bornée
  - non-convergence
  - Bolzano-Weierstrass
---

## Énoncé

Soit la suite $(u_n)_{n \in \mathbb{N}}$ définie pour tout $n \in \mathbb{N}$ par :
$$u_n = \cos\left(\frac{n\pi}{3}\right)$$

1.  Calculer les six premiers termes de la suite : $u_0, u_1, u_2, u_3, u_4, u_5$.
2.  Montrer que la suite $(u_n)$ est bornée.
3.  Considérons la sous-suite $(v_k)_{k \in \mathbb{N}}$ définie par $v_k = u_{6k}$. Déterminer la limite de $(v_k)$ lorsque $k \to \infty$.
4.  Considérons la sous-suite $(w_k)_{k \in \mathbb{N}}$ définie par $w_k = u_{6k+2}$. Déterminer la limite de $(w_k)$ lorsque $k \to \infty$.
5.  La suite $(u_n)$ est-elle convergente ? Justifier votre réponse.

---

## Correction

### Question 1 : Calcul des premiers termes

Nous calculons les termes $u_n$ en substituant $n$ dans l'expression $u_n = \cos\left(\frac{n\pi}{3}\right)$.

*   Pour $n=0$:
    $$u_0 = \cos\left(\frac{0\pi}{3}\right) = \cos(0) = 1$$
*   Pour $n=1$:
    $$u_1 = \cos\left(\frac{1\pi}{3}\right) = \cos\left(\frac{\pi}{3}\right) = \frac{1}{2}$$
*   Pour $n=2$:
    $$u_2 = \cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$$
*   Pour $n=3$:
    $$u_3 = \cos\left(\frac{3\pi}{3}\right) = \cos(\pi) = -1$$
*   Pour $n=4$:
    $$u_4 = \cos\left(\frac{4\pi}{3}\right) = -\frac{1}{2}$$
*   Pour $n=5$:
    $$u_5 = \cos\left(\frac{5\pi}{3}\right) = \frac{1}{2}$$

Les six premiers termes de la suite sont donc $1, \frac{1}{2}, -\frac{1}{2}, -1, -\frac{1}{2}, \frac{1}{2}$.

### Question 2 : La suite $(u_n)$ est-elle bornée ?

La fonction cosinus est une fonction bornée. Pour tout $x \in \mathbb{R}$, nous savons que :
$$-1 \le \cos(x) \le 1$$
Puisque $u_n = \cos\left(\frac{n\pi}{3}\right)$, il s'ensuit que pour tout $n \in \mathbb{N}$ :
$$-1 \le u_n \le 1$$
La suite $(u_n)$ est donc bornée, car tous ses termes sont compris entre $-1$ et $1$.

### Question 3 : Limite de la sous-suite $(v_k)_{k \in \mathbb{N}}$

La sous-suite $(v_k)$ est définie par $v_k = u_{6k}$. Substituons $6k$ à la place de $n$ dans l'expression de $u_n$:
$$v_k = \cos\left(\frac{(6k)\pi}{3}\right) = \cos\left(\frac{6k\pi}{3}\right) = \cos(2k\pi)$$
Nous savons que pour tout entier $k$, $\cos(2k\pi) = 1$.
Ainsi, la sous-suite $(v_k)$ est une suite constante égale à $1$ pour tout $k \in \mathbb{N}$.
Par conséquent, la limite de $(v_k)$ lorsque $k \to \infty$ est :
$$\lim_{k \to \infty} v_k = \lim_{k \to \infty} 1 = 1$$

### Question 4 : Limite de la sous-suite $(w_k)_{k \in \mathbb{N}}$

La sous-suite $(w_k)$ est définie par $w_k = u_{6k+2}$. Substituons $6k+2$ à la place de $n$ dans l'expression de $u_n$:
$$w_k = \cos\left(\frac{(6k+2)\pi}{3}\right)$$
Nous pouvons réécrire l'argument du cosinus :
$$\frac{(6k+2)\pi}{3} = \frac{6k\pi}{3} + \frac{2\pi}{3} = 2k\pi + \frac{2\pi}{3}$$
En utilisant la périodicité de la fonction cosinus (qui est $2\pi$), nous avons $\cos(x + 2k\pi) = \cos(x)$ pour tout entier $k$.
Donc :
$$w_k = \cos\left(2k\pi + \frac{2\pi}{3}\right) = \cos\left(\frac{2\pi}{3}\right)$$
Nous savons que $\cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$.
Ainsi, la sous-suite $(w_k)$ est une suite constante égale à $-\frac{1}{2}$ pour tout $k \in \mathbb{N}$.
Par conséquent, la limite de $(w_k)$ lorsque $k \to \infty$ est :
$$\lim_{k \to \infty} w_k = \lim_{k \to \infty} \left(-\frac{1}{2}\right) = -\frac{1}{2}$$

### Question 5 : La suite $(u_n)$ est-elle convergente ?

Une propriété fondamentale des suites convergentes est que si une suite converge, alors toutes ses sous-suites convergent vers la même limite.
Dans les questions précédentes, nous avons trouvé deux sous-suites de $(u_n)$:
*   La sous-suite $(v_k)$ qui converge vers $1$.
*   La sous-suite $(w_k)$ qui converge vers $-\frac{1}{2}$.

Puisque les limites de ces deux sous-suites sont différentes ($1 \ne -\frac{1}{2}$), la suite $(u_n)$ ne peut pas être convergente. Si elle l'était, toutes ses sous-suites devraient converger vers une unique limite.
Par conséquent, la suite $(u_n)$ est divergente.

---
