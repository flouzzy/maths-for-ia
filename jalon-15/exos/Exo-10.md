---
title: "Exercice 10 - Jalon 15"
subtitle: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
author: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
difficulty: "★★★★★"
keywords:
  - "sous-suites"
  - "valeurs d'adhérence"
  - "Bolzano-Weierstrass"
  - "compacité"
  - "espaces métriques"
  - "suites bornées"
  - "théorème de Kronecker"
  - "adhérence d'un ensemble"
  - "fermé"
```

# Exercice 10 - Jalon 15

## Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass

Soit $(x_n)_{n \in \mathbb{N}}$ une suite dans $\mathbb{R}^d$, où $d \ge 1$. On munit $\mathbb{R}^d$ de sa norme euclidienne usuelle $\| \cdot \|$.
On rappelle qu'une valeur d'adhérence de la suite $(x_n)$ est un point $L \in \mathbb{R}^d$ tel qu'il existe une sous-suite $(x_{\varphi(k)})_{k \in \mathbb{N}}$ qui converge vers $L$.
On note $V$ l'ensemble de toutes les valeurs d'adhérence de la suite $(x_n)$.

1.  Démontrer que l'ensemble $V$ est un ensemble fermé de $\mathbb{R}^d$.

2.  Démontrer que si la suite $(x_n)$ est bornée, alors $V$ est un ensemble non vide et compact.

3.  Pour tout $n \in \mathbb{N}$, on définit l'ensemble $S_n = \{x_k \mid k \ge n\}$. Démontrer que $V = \bigcap_{n \in \mathbb{N}} \overline{S_n}$, où $\overline{S_n}$ désigne l'adhérence de $S_n$.

4.  Considérons la suite $(x_n)_{n \in \mathbb{N}}$ dans $\mathbb{R}^2$ définie par $x_n = (\cos(n\theta), \sin(n\theta))$ pour un certain $\theta \in \mathbb{R}$.
    a.  Déterminer l'ensemble $V$ des valeurs d'adhérence de la suite $(x_n)$ lorsque $\theta = 2\pi p/q$ pour des entiers $p \in \mathbb{Z}$ et $q \in \mathbb{N}^*$.
    b.  Déterminer l'ensemble $V$ des valeurs d'adhérence de la suite $(x_n)$ lorsque $\theta / (2\pi)$ est un nombre irrationnel.

---

# Correction de l'Exercice 10

## Question 1 : Démontrer que l'ensemble $V$ est un ensemble fermé de $\mathbb{R}^d$.

Pour démontrer que $V$ est fermé, nous allons montrer que toute suite convergente de points de $V$ a sa limite dans $V$.
Soit $(L_j)_{j \in \mathbb{N}}$ une suite de points de $V$ qui converge vers un point $L \in \mathbb{R}^d$. Nous devons montrer que $L \in V$.

Puisque chaque $L_j \in V$, par définition, pour chaque $j \in \mathbb{N}$, il existe une sous-suite $(x_{\varphi_j(k)})_{k \in \mathbb{N}}$ de $(x_n)$ qui converge vers $L_j$.
Nous allons construire une sous-suite de $(x_n)$ qui converge vers $L$.

Pour chaque $j \in \mathbb{N}$, comme $L_j = \lim_{k \to \infty} x_{\varphi_j(k)}$, il existe un indice $k_j$ tel que pour tout $k \ge k_j$, $\|x_{\varphi_j(k)} - L_j\| < \frac{1}{j+1}$.
De plus, comme $L = \lim_{j \to \infty} L_j$, pour tout $\varepsilon > 0$, il existe un indice $J \in \mathbb{N}$ tel que pour tout $j \ge J$, $\|L_j - L\| < \varepsilon/2$.

Nous construisons la sous-suite $(x_{\psi(m)})_{m \in \mathbb{N}}$ de la manière suivante :
Pour $m=0$: Puisque $L_0 \in V$, il existe une sous-suite $(x_{\varphi_0(k)})$ convergeant vers $L_0$. Nous pouvons choisir un indice $n_0 = \varphi_0(k_0)$ tel que $\|x_{n_0} - L_0\| < 1$. Nous posons $\psi(0) = n_0$.
Pour $m=1$: Puisque $L_1 \in V$, il existe une sous-suite $(x_{\varphi_1(k)})$ convergeant vers $L_1$. Nous pouvons choisir un indice $n_1 = \varphi_1(k_1)$ tel que $n_1 > \psi(0)$ et $\|x_{n_1} - L_1\| < 1/2$. Nous posons $\psi(1) = n_1$.
En général, supposons que $\psi(m-1)$ a été choisi. Puisque $L_m \in V$, il existe une sous-suite $(x_{\varphi_m(k)})$ convergeant vers $L_m$. Nous pouvons choisir un indice $n_m = \varphi_m(k_m)$ tel que $n_m > \psi(m-1)$ et $\|x_{n_m} - L_m\| < \frac{1}{m+1}$. Nous posons $\psi(m) = n_m$.
Cette construction est toujours possible car chaque sous-suite $(x_{\varphi_m(k)})$ a une infinité de termes, ce qui nous permet de choisir un indice $\varphi_m(k_m)$ arbitrairement grand. La suite d'indices $(\psi(m))_{m \in \mathbb{N}}$ est strictement croissante par construction.

Maintenant, nous allons montrer que la sous-suite $(x_{\psi(m)})_{m \in \mathbb{N}}$ converge vers $L$.
Pour tout $m \in \mathbb{N}$, nous avons :
$\|x_{\psi(m)} - L\| = \|x_{\psi(m)} - L_m + L_m - L\|$
Par l'inégalité triangulaire, nous obtenons :
$\|x_{\psi(m)} - L\| \le \|x_{\psi(m)} - L_m\| + \|L_m - L\|$

Par construction, nous avons $\|x_{\psi(m)} - L_m\| < \frac{1}{m+1}$.
De plus, comme la suite $(L_j)$ converge vers $L$, pour tout $\varepsilon > 0$, il existe un entier $J \in \mathbb{N}$ tel que pour tout $m \ge J$, $\|L_m - L\| < \varepsilon/2$.
Choisissons $M_0 \in \mathbb{N}$ tel que pour tout $m \ge M_0$, $\frac{1}{m+1} < \varepsilon/2$.
Alors, pour tout $m \ge \max(J, M_0)$, nous avons :
$\|x_{\psi(m)} - L\| < \frac{1}{m+1} + \|L_m - L\| < \varepsilon/2 + \varepsilon/2 = \varepsilon$.

Ceci prouve que la sous-suite $(x_{\psi(m)})_{m \in \mathbb{N}}$ converge vers $L$.
Par conséquent, $L$ est une valeur d'adhérence de $(x_n)$, ce qui signifie $L \in V$.
L'ensemble $V$ est donc fermé.

## Question 2 : Démontrer que si la suite $(x_n)$ est bornée, alors $V$ est un ensemble non vide et compact.

**$V$ est non vide :**
Puisque la suite $(x_n)$ est bornée, il existe une constante $M > 0$ telle que pour tout $n \in \mathbb{N}$, $\|x_n\| \le M$.
Le théorème de Bolzano-Weierstrass dans $\mathbb{R}^d$ stipule que toute suite bornée dans $\mathbb{R}^d$ admet au moins une sous-suite convergente.
Soit $(x_{\varphi(k)})_{k \in \mathbb{N}}$ une telle sous-suite convergente. Sa limite $L = \lim_{k \to \infty} x_{\varphi(k)}$ est, par définition, une valeur d'adhérence de $(x_n)$.
Donc, $L \in V$, ce qui prouve que $V$ est non vide.

**$V$ est compact :**
Dans $\mathbb{R}^d$, un ensemble est compact si et seulement s'il est fermé et borné (théorème de Heine-Borel).
Nous avons déjà démontré à la question 1 que $V$ est un ensemble fermé. Il nous reste à montrer que $V$ est borné.

Puisque la suite $(x_n)$ est bornée, il existe une constante $M > 0$ telle que pour tout $n \in \mathbb{N}$, $\|x_n\| \le M$.
Soit $L \in V$. Par définition, il existe une sous-suite $(x_{\varphi(k)})_{k \in \mathbb{N}}$ qui converge vers $L$.
Puisque tous les termes de la suite $(x_n)$ sont bornés par $M$, tous les termes de la sous-suite $(x_{\varphi(k)})$ sont également bornés par $M$, c'est-à-dire $\|x_{\varphi(k)}\| \le M$ pour tout $k \in \mathbb{N}$.
Par une propriété fondamentale des limites, si une suite $(y_k)$ converge vers $L$ et que $\|y_k\| \le M$ pour tout $k$, alors $\|L\| \le M$.
Pour le prouver, supposons par l'absurde que $\|L\| > M$. Posons $\varepsilon = (\|L\| - M)/2$. Alors $\varepsilon > 0$.
Puisque $(x_{\varphi(k)})$ converge vers $L$, il existe un $K \in \mathbb{N}$ tel que pour tout $k \ge K$, $\|x_{\varphi(k)} - L\| < \varepsilon$.
En utilisant l'inégalité triangulaire inverse, nous avons $|\|L\| - \|x_{\varphi(k)}\|| \le \|L - x_{\varphi(k)}\| < \varepsilon$.
Donc, $\|L\| - \|x_{\varphi(k)}\| < \varepsilon$, ce qui implique $\|x_{\varphi(k)}\| > \|L\| - \varepsilon$.
En substituant la valeur de $\varepsilon$: $\|x_{\varphi(k)}\| > \|L\| - (\|L\| - M)/2 = (\|L\| + M)/2$.
Puisque $\|L\| > M$, on a $(\|L\| + M)/2 > (M+M)/2 = M$.
Ainsi, pour $k \ge K$, nous aurions $\|x_{\varphi(k)}\| > M$, ce qui contredit l'hypothèse que $\|x_n\| \le M$ pour tout $n$.
Par conséquent, notre supposition était fausse, et nous devons avoir $\|L\| \le M$.

Puisque cette propriété est vraie pour tout $L \in V$, cela signifie que $V$ est contenu dans la boule fermée $B(0, M)$, et donc $V$ est borné.
Puisque $V$ est fermé et borné, il est compact d'après le théorème de Heine-Borel.

## Question 3 : Démontrer que $V = \bigcap_{n \in \mathbb{N}} \overline{S_n}$.

Rappelons que $S_n = \{x_k \mid k \ge n\}$.

**Partie 1 : Montrons que $V \subseteq \bigcap_{n \in \mathbb{N}} \overline{S_n}$.**
Soit $L \in V$. Par définition, il existe une sous-suite $(x_{\varphi(k)})_{k \in \mathbb{N}}$ qui converge vers $L$.
Nous devons montrer que $L \in \overline{S_n}$ pour tout $n \in \mathbb{N}$.
Fixons un entier $n \in \mathbb{N}$. Puisque $\varphi(k) \to \infty$ lorsque $k \to \infty$, il existe un entier $K_n$ tel que pour tout $k \ge K_n$, $\varphi(k) \ge n$.
Cela signifie que pour tout $k \ge K_n$, le terme $x_{\varphi(k)}$ appartient à l'ensemble $S_n = \{x_j \mid j \ge n\}$.
La suite $(x_{\varphi(k)})_{k \ge K_n}$ est une suite de points de $S_n$ qui converge vers $L$.
Par définition de l'adhérence, un point $L$ appartient à l'adhérence d'un ensemble $A$ si et seulement s'il existe une suite de points de $A$ qui converge vers $L$.
Puisque $L$ est la limite d'une suite de points de $S_n$, $L \in \overline{S_n}$.
Cette conclusion est valable pour tout $n \in \mathbb{N}$.
Par conséquent, $L \in \bigcap_{n \in \mathbb{N}} \overline{S_n}$.
Ceci prouve que $V \subseteq \bigcap_{n \in \mathbb{N}} \overline{S_n}$.

**Partie 2 : Montrons que $\bigcap_{n \in \mathbb{N}} \overline{S_n} \subseteq V$.**
Soit $L \in \bigcap_{n \in \mathbb{N}} \overline{S_n}$. Cela signifie que pour tout $n \in \mathbb{N}$, $L \in \overline{S_n}$.
Nous allons construire une sous-suite $(x_{\psi(m)})_{m \in \mathbb{N}}$ qui converge vers $L$.

Pour $m=0$: Puisque $L \in \overline{S_0}$, par définition de l'adhérence, il existe un point $y_0 \in S_0$ tel que $\|y_0 - L\| < 1$. Puisque $y_0 \in S_0$, $y_0 = x_k$ pour un certain $k \ge 0$. Nous posons $\psi(0) = k$.
Pour $m=1$: Puisque $L \in \overline{S_{\psi(0)+1}}$, il existe un point $y_1 \in S_{\psi(0)+1}$ tel que $\|y_1 - L\| < 1/2$. Puisque $y_1 \in S_{\psi(0)+1}$, $y_1 = x_k$ pour un certain $k \ge \psi(0)+1$. Nous posons $\psi(1) = k$. Par construction, $\psi(1) > \psi(0)$.
En général, supposons que $\psi(m-1)$ a été choisi. Puisque $L \in \overline{S_{\psi(m-1)+1}}$, il existe un point $y_m \in S_{\psi(m-1)+1}$ tel que $\|y_m - L\| < \frac{1}{m+1}$. Puisque $y_m \in S_{\psi(m-1)+1}$, $y_m = x_k$ pour un certain $k \ge \psi(m-1)+1$. Nous posons $\psi(m) = k$.
Par construction, la suite d'indices $(\psi(m))_{m \in \mathbb{N}}$ est strictement croissante, donc $(x_{\psi(m)})$ est bien une sous-suite de $(x_n)$.
De plus, par construction, nous avons $\|x_{\psi(m)} - L\| < \frac{1}{m+1}$.
Comme $\lim_{m \to \infty} \frac{1}{m+1} = 0$, il s'ensuit que $\lim_{m \to \infty} x_{\psi(m)} = L$.
Donc, $L$ est une valeur d'adhérence de la suite $(x_n)$, ce qui signifie $L \in V$.
Ceci prouve que $\bigcap_{n \in \mathbb{N}} \overline{S_n} \subseteq V$.

En combinant les deux parties, nous avons démontré que $V = \bigcap_{n \in \mathbb{N}} \overline{S_n}$.

## Question 4 : Suite $x_n = (\cos(n\theta), \sin(n\theta))$ dans $\mathbb{R}^2$.

La suite $(x_n)$ est une suite de points sur le cercle unité $C = \{(x,y) \in \mathbb{R}^2 \mid x^2+y^2=1\}$.
Le cercle unité est un ensemble fermé et borné dans $\mathbb{R}^2$, donc il est compact d'après le théorème de Heine-Borel.
Puisque tous les termes de la suite $(x_n)$ sont sur le cercle unité, la suite est bornée.
D'après la question 2, l'ensemble $V$ des valeurs d'adhérence est non vide et compact. De plus, $V \subseteq C$.

### a. Cas où $\theta = 2\pi p/q$ pour $p \in \mathbb{Z}$ et $q \in \mathbb{N}^*$.

Dans ce cas, $\theta$ est un multiple rationnel de $2\pi$.
Les termes de la suite sont $x_n = (\cos(n \cdot 2\pi p/q), \sin(n \cdot 2\pi p/q))$.
Considérons le terme $x_{n+q}$:
$x_{n+q} = (\cos((n+q) \cdot 2\pi p/q), \sin((n+q) \cdot 2\pi p/q))$
$x_{n+q} = (\cos(n \cdot 2\pi p/q + q \cdot 2\pi p/q), \sin(n \cdot 2\pi p/q + q \cdot 2\pi p/q))$
$x_{n+q} = (\cos(n \cdot 2\pi p/q + 2\pi p), \sin(n \cdot 2\pi p/q + 2\pi p))$
Puisque les fonctions cosinus et sinus sont $2\pi$-périodiques, et $2\pi p$ est un multiple entier de $2\pi$:
$x_{n+q} = (\cos(n \cdot 2\pi p/q), \sin(n \cdot 2\pi p/q)) = x_n$.
La suite $(x_n)$ est donc périodique de période $q$.
Par conséquent, la suite ne prend qu'un nombre fini de valeurs distinctes. Ces valeurs sont $\{x_0, x_1, \dots, x_{q-1}\}$.
L'ensemble des valeurs d'adhérence $V$ d'une suite qui ne prend qu'un nombre fini de valeurs est précisément l'ensemble de ces valeurs elles-mêmes.
Pour le démontrer :
1.  **Si $L \in V$ :** Il existe une sous-suite $(x_{\varphi(k)})$ qui converge vers $L$. Puisque la suite $(x_n)$ ne prend qu'un nombre fini de valeurs, la sous-suite $(x_{\varphi(k)})$ doit prendre au moins une de ces valeurs une infinité de fois. Soit $x_j$ cette valeur. Alors la sous-suite $(x_{\varphi(k)})$ contient une sous-sous-suite constante égale à $x_j$. Cette sous-sous-suite converge vers $x_j$. Par unicité de la limite, $L = x_j$. Donc $L$ est l'une des valeurs prises par la suite.
2.  **Si $x_j$ est une valeur prise par la suite :** Puisque la suite est périodique de période $q$, la valeur $x_j$ apparaît une infinité de fois dans la suite (par exemple, $x_j, x_{j+q}, x_{j+2q}, \dots$). Cette sous-suite constante $(x_{j+kq})_{k \in \mathbb{N}}$ converge vers $x_j$. Donc $x_j$ est une valeur d'adhérence.

Ainsi, l'ensemble des valeurs d'adhérence est $V = \{x_0, x_1, \dots, x_{q-1}\}$.
Ces points sont $x_k = (\cos(k \cdot 2\pi p/q), \sin(k \cdot 2\pi p/q))$ pour $k \in \{0, 1, \dots, q-1\}$.
Il est à noter que si $p$ et $q$ ne sont pas premiers entre eux, le nombre de points distincts peut être inférieur à $q$. Plus précisément, le nombre de points distincts est $q/\text{pgcd}(p,q)$.

### b. Cas où $\theta / (2\pi)$ est un nombre irrationnel.

Dans ce cas, nous allons montrer que l'ensemble des valeurs d'adhérence $V$ est le cercle unité tout entier, $C = \{(x,y) \in \mathbb{R}^2 \mid x^2+y^2=1\}$.
Pour cela, nous allons utiliser un résultat fondamental de la théorie des nombres : le théorème de Kronecker (ou un cas particulier de celui-ci).
Le théorème de Kronecker affirme que si $\alpha$ est un nombre irrationnel, alors l'ensemble $\{n\alpha - \lfloor n\alpha \rfloor \mid n \in \mathbb{N}\}$ est dense dans $[0, 1]$.
En d'autres termes, l'ensemble des parties fractionnaires de $n\alpha$ est dense dans $[0, 1]$.
Si nous posons $\alpha = \theta/(2\pi)$, alors $\alpha$ est irrationnel par hypothèse.
L'ensemble $\{n\theta/(2\pi) \pmod 1 \mid n \in \mathbb{N}\}$ est dense dans $[0, 1]$.
Ceci est équivalent à dire que l'ensemble $\{n\theta \pmod{2\pi} \mid n \in \mathbb{N}\}$ est dense dans $[0, 2\pi]$.

**Preuve de la densité de $\{n\theta \pmod{2\pi}\}$ dans $[0, 2\pi]$ (esquisse, car c'est un résultat classique) :**
Soit $y_n = n\theta \pmod{2\pi}$.
1.  **Les points $y_n$ sont distincts :** Si $y_n = y_m$ pour $n \ne m$, alors $n\theta - m\theta = k \cdot 2\pi$ pour un certain entier $k$. Cela implique $(n-m)\theta = k \cdot 2\pi$, et donc $\theta/(2\pi) = k/(n-m)$, ce qui est un nombre rationnel. Ceci contredit l'hypothèse que $\theta/(2\pi)$ est irrationnel. Donc tous les $y_n$ sont distincts.
2.  **Densité :** Puisqu'il y a une infinité de points distincts $y_n$ dans l'intervalle borné $[0, 2\pi]$, il doit y avoir des points arbitrairement proches les uns des autres.
    Pour tout $N \in \mathbb{N}^*$, considérons les $N+1$ points $y_0, y_1, \dots, y_N$ dans $[0, 2\pi)$. Divisons l'intervalle $[0, 2\pi)$ en $N$ sous-intervalles de longueur $2\pi/N$. Par le principe des tiroirs de Dirichlet, il doit y avoir au moins deux points $y_j, y_k$ (avec $0 \le j < k \le N$) qui tombent dans le même sous-intervalle.
    Donc, $|y_k - y_j| < 2\pi/N$. Soit $\delta = |y_k - y_j|$. Alors $\delta = |(k-j)\theta - l \cdot 2\pi|$ pour un certain entier $l$.
    Ainsi, $\delta$ est de la forme $m\theta \pmod{2\pi}$ pour $m=k-j \ne 0$.
    Les multiples de $\delta$, c'est-à-dire $\{p\delta \pmod{2\pi} \mid p \in \mathbb{N}\}$, sont également de la forme $p(k-j)\theta \pmod{2\pi}$, donc ils sont des points de la suite $\{n\theta \pmod{2\pi}\}$.
    Puisque $\delta$ peut être rendu arbitrairement petit en choisissant $N$ suffisamment grand, l'ensemble $\{p\delta \pmod{2\pi}\}$ est dense dans $[0, 2\pi]$.
    Par conséquent, l'ensemble $\{n\theta \pmod{2\pi} \mid n \in \mathbb{N}\}$ est dense dans $[0, 2\pi]$.

Maintenant, revenons à la suite $x_n = (\cos(n\theta), \sin(n\theta))$.
L'ensemble des points $x_n$ est l'image de l'ensemble $\{n\theta \pmod{2\pi} \mid n \in \mathbb{N}\}$ par l'application $f: t \mapsto (\cos t, \sin t)$.
L'application $f: [0, 2\pi] \to C$ est continue et surjective.
Puisque l'ensemble $\{n\theta \pmod{2\pi} \mid n \in \mathbb{N}\}$ est dense dans $[0, 2\pi]$, et que $f$ est une application continue, l'image de cet ensemble, c'est-à-dire $\{x_n \mid n \in \mathbb{N}\}$, est dense dans l'image de $[0, 2\pi]$ par $f$.
L'image de $[0, 2\pi]$ par $f$ est le cercle unité $C$.
Donc, l'ensemble $A = \{x_n \mid n \in \mathbb{N}\}$ est dense dans le cercle unité $C$.

L'ensemble des valeurs d'adhérence $V$ d'une suite est égal à l'adhérence de l'ensemble des valeurs prises par la suite, c'est-à-dire $V = \overline{A}$.
Puisque $A$ est dense dans $C$, son adhérence est $C$.
Donc, $V = C$.

En résumé, lorsque $\theta / (2\pi)$ est un nombre irrationnel, l'ensemble des valeurs d'adhérence de la suite $x_n = (\cos(n\theta), \sin(n\theta))$ est le cercle unité tout entier.
