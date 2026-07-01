---
uuid: "jalon-14-exo-08"
title: "Exercice 8 : Convergence rigoureuse d'une suite de racines polynomiales"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 8 : Convergence rigoureuse d'une suite de racines polynomiales

## Énoncé

Soit, pour tout entier naturel $n \ge 1$, l'équation polynomiale $P_n(x) = x^n + x - 1 = 0$.

1.  Démontrer que pour chaque $n \ge 1$, l'équation $P_n(x) = 0$ admet une unique solution réelle $u_n$ dans l'intervalle $(0, 1)$.
2.  Établir que la suite $(u_n)_{n \ge 1}$ est strictement croissante. En déduire qu'elle est convergente.
3.  Déterminer la limite $L$ de la suite $(u_n)_{n \ge 1}$.
4.  En utilisant la définition rigoureuse de la limite ($\epsilon, N$), démontrer que $\lim_{n \to \infty} u_n = L$.

## Correction Détaillée

### 1. Existence et unicité de $u_n$ dans $(0,1)$

Pour chaque $n \ge 1$, considérons la fonction $P_n(x) = x^n + x - 1$ définie sur $\mathbb{R}$.

**Existence :**
Évaluons $P_n(x)$ aux bornes de l'intervalle $(0,1)$:
*   $P_n(0) = 0^n + 0 - 1 = -1$.
*   $P_n(1) = 1^n + 1 - 1 = 1$.
Puisque $P_n(0) = -1 < 0$ et $P_n(1) = 1 > 0$, et que $P_n(x)$ est une fonction continue sur $[0,1]$ (étant un polynôme), le Théorème des Valeurs Intermédiaires (TVI) garantit l'existence d'au moins une racine $u_n$ dans l'intervalle $(0,1)$.

**Unicité :**
Calculons la dérivée de $P_n(x)$ par rapport à $x$:
$P_n'(x) = \frac{d}{dx}(x^n + x - 1) = nx^{n-1} + 1$.
Pour $x \in (0,1)$, $x^{n-1} > 0$ (sauf si $n=1$ et $x=0$, mais nous sommes sur $(0,1)$).
Donc, $nx^{n-1} > 0$ pour $n \ge 1$ et $x \in (0,1)$.
Par conséquent, $P_n'(x) = nx^{n-1} + 1 > 1$ pour tout $x \in (0,1)$.
Puisque $P_n'(x) > 0$ sur $(0,1)$, la fonction $P_n(x)$ est strictement croissante sur cet intervalle.
Une fonction strictement monotone ne peut couper l'axe des abscisses qu'en un seul point.
Ainsi, l'équation $P_n(x) = 0$ admet une unique solution $u_n$ dans $(0,1)$.

### 2. Monotonie de la suite $(u_n)_{n \ge 1}$

Nous avons $P_n(u_n) = u_n^n + u_n - 1 = 0$, ce qui implique $u_n^n = 1 - u_n$.
Pour étudier la monotonie de la suite $(u_n)$, comparons $u_n$ et $u_{n+1}$.
Nous savons que $u_{n+1}$ est la racine de $P_{n+1}(x) = x^{n+1} + x - 1 = 0$.
Évaluons $P_{n+1}(u_n)$:
$P_{n+1}(u_n) = u_n^{n+1} + u_n - 1$.
En utilisant la relation $u_n^n = 1 - u_n$ (obtenue de $P_n(u_n)=0$), nous pouvons réécrire $u_n^{n+1}$ comme $u_n \cdot u_n^n = u_n(1 - u_n)$.
Donc, $P_{n+1}(u_n) = u_n(1 - u_n) + u_n - 1$.
Développons et simplifions cette expression :
$P_{n+1}(u_n) = u_n - u_n^2 + u_n - 1 = -u_n^2 + 2u_n - 1$.
Nous reconnaissons une forme quadratique : $-(u_n^2 - 2u_n + 1) = -(u_n - 1)^2$.
Puisque $u_n \in (0,1)$, $u_n \neq 1$, donc $(u_n - 1)^2 > 0$.
Par conséquent, $P_{n+1}(u_n) = -(u_n - 1)^2 < 0$.

Nous avons $P_{n+1}(u_n) < 0$ et nous savons que $P_{n+1}(u_{n+1}) = 0$.
Puisque $P_{n+1}(x)$ est strictement croissante sur $(0,1)$ (d'après la partie 1, car $P_{n+1}'(x) = (n+1)x^n + 1 > 0$), l'inégalité $P_{n+1}(u_n) < P_{n+1}(u_{n+1})$ implique $u_n < u_{n+1}$.
La suite $(u_n)_{n \ge 1}$ est donc strictement croissante.

De plus, nous avons montré en partie 1 que $u_n \in (0,1)$ pour tout $n$. La suite $(u_n)$ est donc majorée par 1.
Toute suite réelle croissante et majorée est convergente.
Par conséquent, la suite $(u_n)_{n \ge 1}$ converge vers une limite $L$.

### 3. Détermination de la limite $L$

Puisque $u_n \in (0,1)$ pour tout $n$, et que la suite est croissante, sa limite $L$ doit satisfaire $u_1 \le L \le 1$.
(Pour $n=1$, $P_1(x) = x+x-1 = 2x-1=0 \implies u_1 = 1/2$. Donc $1/2 \le L \le 1$.)

Nous avons la relation $u_n^n = 1 - u_n$.
Passons à la limite lorsque $n \to \infty$ :
$\lim_{n \to \infty} u_n^n = \lim_{n \to \infty} (1 - u_n)$.
Le membre de droite converge vers $1 - L$.

Analysons le membre de gauche, $\lim_{n \to \infty} u_n^n$.
*   **Cas 1 : Si $L < 1$.**
    Si $L < 1$, alors pour $n$ suffisamment grand, $u_n$ est proche de $L$ et donc $u_n < 1$.
    Dans ce cas, $\lim_{n \to \infty} u_n^n = 0$.
    L'équation à la limite devient $0 = 1 - L$, ce qui implique $L = 1$.
    Ceci contredit notre hypothèse $L < 1$. Donc le cas $L < 1$ est impossible.

*   **Cas 2 : Si $L = 1$.**
    Si $L = 1$, alors le membre de droite $1 - L = 1 - 1 = 0$.
    Le membre de gauche $\lim_{n \to \infty} u_n^n = \lim_{n \to \infty} 1^n = 1$.
    Ceci conduit à $1 = 0$, ce qui est une contradiction.

Il y a une erreur dans le raisonnement du Cas 2. Si $L=1$, alors $u_n \to 1$.
Le terme $u_n^n$ ne tend pas nécessairement vers 1. Par exemple, $(1-1/n)^n \to 1/e$.
Reprenons l'analyse de $\lim_{n \to \infty} u_n^n$ lorsque $L=1$.
Si $L=1$, alors $u_n \to 1$.
L'équation $u_n^n = 1-u_n$ devient, à la limite, $\lim_{n \to \infty} u_n^n = 1 - 1 = 0$.
Pour que $\lim_{n \to \infty} u_n^n = 0$ alors que $u_n \to 1$, il faut que $u_n$ s'approche de 1 "suffisamment lentement".
Ceci n'est pas une contradiction. En fait, c'est ce que nous allons prouver.

Le raisonnement correct pour la limite est le suivant :
Nous savons que $L \in [1/2, 1]$.
De $u_n^n = 1 - u_n$, si $L < 1$, alors $u_n \to L < 1$.
Pour tout $x \in [0,1)$, $\lim_{n \to \infty} x^n = 0$.
Donc, si $L < 1$, alors $\lim_{n \to \infty} u_n^n = 0$.
L'équation à la limite devient $0 = 1 - L$, ce qui implique $L = 1$.
Ceci contredit l'hypothèse $L < 1$.
Par conséquent, la seule possibilité est que $L = 1$.

### 4. Démonstration rigoureuse de la limite par $\epsilon, N$

Nous voulons démontrer que $\lim_{n \to \infty} u_n = 1$ en utilisant la définition $\epsilon, N$.
Cela signifie que pour tout $\epsilon > 0$, il existe un entier $N$ tel que pour tout $n \ge N$, nous ayons $|u_n - 1| < \epsilon$.

Puisque nous savons que $u_n \in (0,1)$ pour tout $n$, l'inégalité $|u_n - 1| < \epsilon$ est équivalente à $1 - u_n < \epsilon$.
Ceci est à son tour équivalent à $u_n > 1 - \epsilon$.

Soit $\epsilon > 0$ donné.
Nous pouvons supposer sans perte de généralité que $\epsilon \in (0,1)$, car si $\epsilon \ge 1$, alors $1-u_n < 1 \le \epsilon$ est toujours vraie puisque $u_n \in (0,1)$.
Nous cherchons donc à trouver $N$ tel que pour tout $n \ge N$, $u_n > 1 - \epsilon$.

Rappelons que $u_n$ est la racine unique de $P_n(x) = x^n + x - 1 = 0$.
Puisque $P_n(x)$ est strictement croissante sur $(0,1)$ (démontré en partie 1), l'inégalité $u_n > 1 - \epsilon$ est équivalente à $P_n(u_n) > P_n(1 - \epsilon)$.
Comme $P_n(u_n) = 0$, nous devons montrer que $0 > P_n(1 - \epsilon)$, c'est-à-dire $P_n(1 - \epsilon) < 0$.

Calculons $P_n(1 - \epsilon)$:
$P_n(1 - \epsilon) = (1 - \epsilon)^n + (1 - \epsilon) - 1 = (1 - \epsilon)^n - \epsilon$.

Nous devons donc montrer que pour $n$ suffisamment grand, $(1 - \epsilon)^n - \epsilon < 0$, ce qui est équivalent à $(1 - \epsilon)^n < \epsilon$.

Puisque nous avons supposé $\epsilon \in (0,1)$, nous avons $0 < 1 - \epsilon < 1$.
Nous savons que pour tout $a \in (0,1)$, la suite géométrique $(a^n)_{n \ge 1}$ converge vers 0.
Donc, $\lim_{n \to \infty} (1 - \epsilon)^n = 0$.

Par la définition de la limite d'une suite, pour tout $\delta' > 0$, il existe un entier $N$ tel que pour tout $n \ge N$, nous ayons $|(1 - \epsilon)^n - 0| < \delta'$.
Choisissons $\delta' = \epsilon$.
Alors, il existe un entier $N$ (qui dépend de $\epsilon$) tel que pour tout $n \ge N$, $(1 - \epsilon)^n < \epsilon$.

Pour ce $N$ et pour tout $n \ge N$:
1.  Nous avons $(1 - \epsilon)^n < \epsilon$.
2.  Ceci implique $P_n(1 - \epsilon) = (1 - \epsilon)^n - \epsilon < 0$.
3.  Puisque $P_n(u_n) = 0$ et $P_n(x)$ est strictement croissante, l'inégalité $P_n(1 - \epsilon) < P_n(u_n)$ implique $1 - \epsilon < u_n$.
4.  Combiné avec $u_n < 1$ (démontré en partie 1), nous obtenons $1 - \epsilon < u_n < 1$.
5.  Ceci signifie $0 < 1 - u_n < \epsilon$, ce qui est équivalent à $|u_n - 1| < \epsilon$.

Nous avons donc trouvé, pour tout $\epsilon > 0$, un $N$ tel que pour tout $n \ge N$, $|u_n - 1| < \epsilon$.
Ceci démontre rigoureusement, par la définition $\epsilon, N$, que $\lim_{n \to \infty} u_n = 1$.