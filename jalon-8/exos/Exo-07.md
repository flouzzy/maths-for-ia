---
uuid: "jalon-8-exo-07"
title: "Exercice 7 : Endomorphisme de différences finies sur les polynômes"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 7 : Endomorphisme de différences finies sur les polynômes (Difficulté : ★★★★☆)

## Énoncé
Soit $n \in \mathbb{N}^*$. On considère l'espace vectoriel $E = \mathbb{R}_n[X]$ des polynômes à coefficients réels de degré inférieur ou égal à $n$.
On définit l'application $f : E \to E$ par $f(P)(X) = P(X+1) - P(X)$ pour tout $P \in E$.

1.  Démontrer que $f$ est une application linéaire.
2.  Déterminer le noyau $\ker f$. En déduire $\dim(\ker f)$.
3.  Déterminer l'image $\text{Im } f$. En déduire $\text{rg } f$.
4.  Vérifier que le théorème du rang est satisfait.

## Correction Détaillée

**1. Démontrer que $f$ est une application linéaire.**
Pour démontrer que $f$ est une application linéaire, nous devons vérifier trois propriétés : l'additivité, l'homogénéité et la fermeture de l'espace d'arrivée.

*   **Vérification de l'additivité :**
    Soient $P, Q \in E = \mathbb{R}_n[X]$.
    Pour tout $X \in \mathbb{R}$, nous calculons $f(P+Q)(X)$ :
    $$f(P+Q)(X) = (P+Q)(X+1) - (P+Q)(X)$$
    Par définition de l'addition des polynômes, $(P+Q)(Y) = P(Y) + Q(Y)$ pour tout $Y \in \mathbb{R}$.
    Donc,
    $$f(P+Q)(X) = (P(X+1) + Q(X+1)) - (P(X) + Q(X))$$
    En réarrangeant les termes,
    $$f(P+Q)(X) = (P(X+1) - P(X)) + (Q(X+1) - Q(X))$$
    Par définition de $f$,
    $$f(P+Q)(X) = f(P)(X) + f(Q)(X)$$
    Cette égalité étant vraie pour tout $X \in \mathbb{R}$, nous avons $f(P+Q) = f(P) + f(Q)$.

*   **Vérification de l'homogénéité :**
    Soient $P \in E = \mathbb{R}_n[X]$ et $\lambda \in \mathbb{R}$.
    Pour tout $X \in \mathbb{R}$, nous calculons $f(\lambda P)(X)$ :
    $$f(\lambda P)(X) = (\lambda P)(X+1) - (\lambda P)(X)$$
    Par définition de la multiplication d'un polynôme par un scalaire, $(\lambda P)(Y) = \lambda P(Y)$ pour tout $Y \in \mathbb{R}$.
    Donc,
    $$f(\lambda P)(X) = \lambda P(X+1) - \lambda P(X)$$
    En factorisant $\lambda$,
    $$f(\lambda P)(X) = \lambda (P(X+1) - P(X))$$
    Par définition de $f$,
    $$f(\lambda P)(X) = \lambda f(P)(X)$$
    Cette égalité étant vraie pour tout $X \in \mathbb{R}$, nous avons $f(\lambda P) = \lambda f(P)$.

*   **Vérification que l'image est bien dans $E$ :**
    Soit $P \in E = \mathbb{R}_n[X]$. Cela signifie que le degré de $P$, noté $\deg(P)$, est inférieur ou égal à $n$.
    Si $P$ est un polynôme constant, c'est-à-dire $\deg(P) = 0$, alors $P(X) = c$ pour une constante $c \in \mathbb{R}$.
    Dans ce cas, $f(P)(X) = P(X+1) - P(X) = c - c = 0$. Le polynôme nul est bien dans $E$.
    Si $P$ n'est pas un polynôme constant, soit $k = \deg(P)$ avec $1 \le k \le n$.
    Nous pouvons écrire $P(X) = a_k X^k + a_{k-1} X^{k-1} + \dots + a_1 X + a_0$, où $a_k \neq 0$.
    Alors $P(X+1) = a_k (X+1)^k + a_{k-1} (X+1)^{k-1} + \dots + a_1 (X+1) + a_0$.
    En développant $(X+1)^k$ à l'aide de la formule du binôme de Newton :
    $(X+1)^k = X^k + k X^{k-1} + \binom{k}{2} X^{k-2} + \dots + 1$.
    Donc,
    $$P(X+1) = a_k (X^k + k X^{k-1} + \dots) + a_{k-1} (X^{k-1} + \dots) + \dots$$
    Calculons $f(P)(X) = P(X+1) - P(X)$ :
    $$f(P)(X) = (a_k (X^k + k X^{k-1} + \dots) + a_{k-1} (X^{k-1} + \dots) + \dots) - (a_k X^k + a_{k-1} X^{k-1} + \dots)$$
    $$f(P)(X) = (a_k X^k + a_k k X^{k-1} + \dots) - a_k X^k + (a_{k-1} X^{k-1} + \dots) - a_{k-1} X^{k-1} + \dots$$
    Les termes de plus haut degré $a_k X^k$ s'annulent. Le terme de plus haut degré restant est $a_k k X^{k-1}$.
    Puisque $a_k \neq 0$ et $k \ge 1$, $a_k k \neq 0$.
    Donc $\deg(f(P)) = k-1$.
    Comme $k \le n$, nous avons $k-1 \le n-1$.
    Par conséquent, $\deg(f(P)) \le n-1$, ce qui implique $\deg(f(P)) \le n$.
    Ainsi, $f(P) \in \mathbb{R}_n[X] = E$.
    L'application $f$ est donc bien une application linéaire de $E$ dans $E$.

**2. Déterminer le noyau $\ker f$. En déduire $\dim(\ker f)$.**
Par définition, le noyau de $f$ est l'ensemble des polynômes $P \in E$ tels que $f(P) = 0_E$.
$$P \in \ker f \iff f(P)(X) = 0_E \iff P(X+1) - P(X) = 0_E$$
Ceci signifie que pour tout $X \in \mathbb{R}$, $P(X+1) = P(X)$.

Considérons un polynôme $P(X)$ vérifiant $P(X+1) = P(X)$ pour tout $X \in \mathbb{R}$.
De cette égalité, nous pouvons déduire que $P(0) = P(1) = P(2) = \dots = P(k)$ pour tout entier $k \in \mathbb{N}$.
Considérons le polynôme $Q(X) = P(X) - P(0)$.
Nous avons $Q(0) = P(0) - P(0) = 0$.
Nous avons $Q(1) = P(1) - P(0) = P(0) - P(0) = 0$.
De manière générale, pour tout entier $k \in \mathbb{N}$, $Q(k) = P(k) - P(0) = P(0) - P(0) = 0$.
Le polynôme $Q(X)$ possède donc une infinité de racines distinctes ($0, 1, 2, \dots$).
Le seul polynôme qui possède une infinité de racines est le polynôme nul.
Par conséquent, $Q(X) = 0_E$.
Ceci implique $P(X) - P(0) = 0_E$, et donc $P(X) = P(0)$.
Ainsi, tout polynôme $P$ appartenant à $\ker f$ doit être un polynôme constant.

Réciproquement, si $P(X) = c$ (où $c \in \mathbb{R}$) est un polynôme constant, alors :
$f(P)(X) = P(X+1) - P(X) = c - c = 0$.
Donc, les polynômes constants appartiennent bien à $\ker f$.

En conclusion, $\ker f$ est l'ensemble des polynômes constants de $E$.
$\ker f = \{ P \in \mathbb{R}_n[X] \mid P \text{ est constant} \} = \mathbb{R}_0[X]$.
L'espace vectoriel $\mathbb{R}_0[X]$ est engendré par le polynôme $1$ (qui est non nul).
Sa dimension est donc $\dim(\ker f) = 1$.

**3. Déterminer l'image $\text{Im } f$. En déduire $\text{rg } f$.**
L'espace vectoriel $E = \mathbb{R}_n[X]$ est l'espace des polynômes de degré au plus $n$. Une base canonique de $E$ est $(1, X, X^2, \dots, X^n)$.
La dimension de $E$ est $\dim E = n+1$.

D'après le théorème du rang, pour toute application linéaire $f : E \to F$ où $E$ est de dimension finie, nous avons :
$$\dim E = \dim(\ker f) + \text{rg}(f)$$
En substituant les valeurs connues :
$$(n+1) = 1 + \text{rg}(f)$$
Nous en déduisons que :
$$\text{rg}(f) = n$$
Par définition, $\text{rg}(f) = \dim(\text{Im } f)$. Donc $\dim(\text{Im } f) = n$.

Nous avons montré à la question 1 que pour tout $P \in E$, $\deg(f(P)) \le n-1$.
Cela signifie que l'image de $f$, $\text{Im } f$, est un sous-espace vectoriel de $\mathbb{R}_{n-1}[X]$.
L'espace $\mathbb{R}_{n-1}[X]$ est l'espace des polynômes de degré au plus $n-1$. Sa dimension est $\dim(\mathbb{R}_{n-1}[X]) = (n-1)+1 = n$.
Puisque $\text{Im } f$ est un sous-espace vectoriel de $\mathbb{R}_{n-1}[X]$ et que $\dim(\text{Im } f) = n = \dim(\mathbb{R}_{n-1}[X])$, il s'ensuit que $\text{Im } f$ est égal à $\mathbb{R}_{n-1}[X]$.
$$\text{Im } f = \mathbb{R}_{n-1}[X]$$

Pour une démonstration plus constructive de l'image, nous pouvons considérer l'image des éléments de la base canonique de $E$: $\mathcal{B} = (1, X, X^2, \dots, X^n)$.
$f(1) = 1 - 1 = 0$.
$f(X) = (X+1) - X = 1$.
$f(X^2) = (X+1)^2 - X^2 = (X^2+2X+1) - X^2 = 2X+1$.
$f(X^3) = (X+1)^3 - X^3 = (X^3+3X^2+3X+1) - X^3 = 3X^2+3X+1$.
De manière générale, pour $k \in \{1, \dots, n\}$ :
$$f(X^k) = (X+1)^k - X^k = \sum_{j=0}^k \binom{k}{j} X^j - X^k$$
$$f(X^k) = \left(X^k + k X^{k-1} + \binom{k}{2} X^{k-2} + \dots + 1\right) - X^k$$
$$f(X^k) = k X^{k-1} + \binom{k}{2} X^{k-2} + \dots + 1$$
Le polynôme $f(X^k)$ est de degré $k-1$ et son coefficient dominant est $k$.

Considérons la famille de polynômes $\mathcal{F} = (f(X), f(X^2), \dots, f(X^n))$.
Cette famille contient $n$ polynômes.
Les degrés de ces polynômes sont respectivement :
$\deg(f(X)) = 0$
$\deg(f(X^2)) = 1$
$\deg(f(X^3)) = 2$
$\dots$
$\deg(f(X^n)) = n-1$
Puisque $\mathcal{F}$ est une famille de $n$ polynômes non nuls ayant des degrés distincts (de $0$ à $n-1$), cette famille est une famille libre dans $\mathbb{R}_{n-1}[X]$.
De plus, $\mathbb{R}_{n-1}[X]$ est un espace vectoriel de dimension $n$.
Une famille libre de $n$ vecteurs dans un espace de dimension $n$ est une base de cet espace.
Donc, $\mathcal{F}$ est une base de $\mathbb{R}_{n-1}[X]$.
Puisque tous les éléments de $\mathcal{F}$ sont des images par $f$ (donc appartiennent à $\text{Im } f$), et que $\mathcal{F}$ engendre $\mathbb{R}_{n-1}[X]$, il s'ensuit que $\text{Im } f = \mathbb{R}_{n-1}[X]$.
La dimension de l'image est donc $\text{rg } f = \dim(\mathbb{R}_{n-1}[X]) = n$.

**4. Vérifier que le théorème du rang est satisfait.**
Nous avons déterminé les dimensions suivantes :
*   Dimension de l'espace de départ $E = \mathbb{R}_n[X]$ : $\dim E = n+1$.
*   Dimension du noyau $\ker f$ : $\dim(\ker f) = 1$.
*   Dimension de l'image $\text{Im } f$ (le rang de $f$) : $\text{rg } f = n$.

Le théorème du rang stipule que $\dim E = \dim(\ker f) + \text{rg } f$.
Substituons les valeurs trouvées dans cette égalité :
$$(n+1) = 1 + n$$
Cette égalité est manifestement vraie pour tout $n \in \mathbb{N}^*$.
Le théorème du rang est donc satisfait pour l'application linéaire $f$.