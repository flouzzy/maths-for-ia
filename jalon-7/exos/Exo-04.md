---
uuid: "exo-7-4"
title: "Exo 4 - Jalon 7"
---

Mes chers étudiants,

Nous allons aujourd'hui explorer les concepts fondamentaux d'espaces vectoriels, de familles libres, génératrices et de bases à travers un exemple concret, mais suffisamment abstrait pour illustrer la généralité de ces notions. L'exercice que je vous propose porte sur un espace de suites réelles, un cadre qui vous est familier mais que nous allons analyser sous l'angle de l'algèbre linéaire.

---

### Exercice 4 : L'Espace des Suites de Fibonacci Généralisées

Soit $E$ l'ensemble de toutes les suites réelles $(u_n)_{n \in \mathbb{N}}$ qui vérifient la relation de récurrence linéaire suivante pour tout entier naturel $n$:
$$u_{n+2} = u_{n+1} + u_n$$
On munit $E$ des opérations d'addition de suites et de multiplication par un scalaire réel usuelles, c'est-à-dire, pour deux suites $(u_n)$ et $(v_n)$ de $E$ et un scalaire $\lambda \in \mathbb{R}$:
*   L'addition: $(u_n) + (v_n) = (u_n + v_n)_{n \in \mathbb{N}}$
*   La multiplication par un scalaire: $\lambda (u_n) = (\lambda u_n)_{n \in \mathbb{N}}$

1.  Démontrer que $E$ est un $\mathbb{R}$-espace vectoriel.
2.  On considère les deux nombres réels $\phi = \frac{1+\sqrt{5}}{2}$ (le nombre d'or) et $1-\phi = \frac{1-\sqrt{5}}{2}$.
    On définit deux suites $F = (\phi^n)_{n \in \mathbb{N}}$ et $G = ((1-\phi)^n)_{n \in \mathbb{N}}$.
    a.  Vérifier que $F$ et $G$ sont des éléments de $E$.
    b.  Démontrer que la famille $\{F, G\}$ est une famille libre dans $E$.
3.  Démontrer que la famille $\{F, G\}$ est une famille génératrice de $E$.
4.  En déduire une base de $E$ et sa dimension.

---

### Correction de l'Exercice 4

Nous allons aborder chaque question avec la rigueur nécessaire, en détaillant chaque étape.

#### Question 1 : Démontrer que $E$ est un $\mathbb{R}$-espace vectoriel.

Pour démontrer que $E$ est un $\mathbb{R}$-espace vectoriel, nous allons montrer qu'il s'agit d'un sous-espace vectoriel de l'espace vectoriel des suites réelles $\mathbb{R}^{\mathbb{N}}$. L'espace $\mathbb{R}^{\mathbb{N}}$ est l'ensemble de toutes les suites réelles, muni des opérations d'addition de suites et de multiplication par un scalaire réel définies dans l'énoncé. Nous savons que $\mathbb{R}^{\mathbb{N}}$ est un $\mathbb{R}$-espace vectoriel.

Pour qu'un sous-ensemble $E$ d'un espace vectoriel $V$ soit lui-même un espace vectoriel (un sous-espace vectoriel), trois conditions doivent être satisfaites :
1.  $E$ doit être non vide.
2.  $E$ doit être fermé sous l'addition vectorielle.
3.  $E$ doit être fermé sous la multiplication par un scalaire.

Appliquons ces conditions à notre ensemble $E$:

1.  **$E$ est non vide :**
    Considérons la suite nulle, notée $(0)_{n \in \mathbb{N}}$, dont tous les termes sont égaux à 0. C'est-à-dire $u_n = 0$ pour tout $n \in \mathbb{N}$.
    Vérifions si cette suite satisfait la relation de récurrence $u_{n+2} = u_{n+1} + u_n$.
    Pour tout $n \in \mathbb{N}$, nous avons $0 = 0 + 0$.
    Cette égalité est vraie. Par conséquent, la suite nulle appartient à $E$.
    Puisque la suite nulle est un élément de $E$, l'ensemble $E$ n'est pas vide.

2.  **$E$ est fermé sous l'addition vectorielle :**
    Soient $(u_n)_{n \in \mathbb{N}}$ et $(v_n)_{n \in \mathbb{N}}$ deux suites quelconques appartenant à $E$.
    Par définition, cela signifie que pour tout $n \in \mathbb{N}$:
    *   $u_{n+2} = u_{n+1} + u_n$ (car $(u_n) \in E$)
    *   $v_{n+2} = v_{n+1} + v_n$ (car $(v_n) \in E$)
    Considérons la suite somme $(w_n)_{n \in \mathbb{N}} = (u_n)_{n \in \mathbb{N}} + (v_n)_{n \in \mathbb{N}}$. Par définition de l'addition de suites, chaque terme de $(w_n)$ est $w_n = u_n + v_n$.
    Nous devons vérifier si $(w_n)$ satisfait la relation de récurrence. Calculons $w_{n+2}$:
    $w_{n+2} = u_{n+2} + v_{n+2}$
    En utilisant les relations de récurrence pour $(u_n)$ et $(v_n)$, nous substituons:
    $w_{n+2} = (u_{n+1} + u_n) + (v_{n+1} + v_n)$
    Par associativité et commutativité de l'addition des nombres réels, nous pouvons regrouper les termes:
    $w_{n+2} = (u_{n+1} + v_{n+1}) + (u_n + v_n)$
    En reconnaissant les termes de la suite $(w_n)$:
    $w_{n+2} = w_{n+1} + w_n$
    Cette égalité est vraie pour tout $n \in \mathbb{N}$. Par conséquent, la suite $(w_n)$ appartient à $E$.
    L'ensemble $E$ est donc fermé sous l'addition vectorielle.

3.  **$E$ est fermé sous la multiplication par un scalaire :**
    Soit $(u_n)_{n \in \mathbb{N}}$ une suite quelconque appartenant à $E$, et soit $\lambda$ un scalaire réel quelconque ($\lambda \in \mathbb{R}$).
    Par définition, $(u_n) \in E$ signifie que pour tout $n \in \mathbb{N}$, $u_{n+2} = u_{n+1} + u_n$.
    Considérons la suite produit par un scalaire $(x_n)_{n \in \mathbb{N}} = \lambda (u_n)_{n \in \mathbb{N}}$. Par définition de la multiplication par un scalaire, chaque terme de $(x_n)$ est $x_n = \lambda u_n$.
    Nous devons vérifier si $(x_n)$ satisfait la relation de récurrence. Calculons $x_{n+2}$:
    $x_{n+2} = \lambda u_{n+2}$
    En utilisant la relation de récurrence pour $(u_n)$, nous substituons:
    $x_{n+2} = \lambda (u_{n+1} + u_n)$
    Par distributivité de la multiplication sur l'addition dans $\mathbb{R}$:
    $x_{n+2} = \lambda u_{n+1} + \lambda u_n$
    En reconnaissant les termes de la suite $(x_n)$:
    $x_{n+2} = x_{n+1} + x_n$
    Cette égalité est vraie pour tout $n \in \mathbb{N}$. Par conséquent, la suite $(x_n)$ appartient à $E$.
    L'ensemble $E$ est donc fermé sous la multiplication par un scalaire.

Puisque les trois conditions sont satisfaites, nous pouvons conclure que $E$ est un sous-espace vectoriel de $\mathbb{R}^{\mathbb{N}}$. Par conséquent, $E$ est un $\mathbb{R}$-espace vectoriel.

#### Question 2a : Vérifier que $F$ et $G$ sont des éléments de $E$.

Les suites $F = (\phi^n)_{n \in \mathbb{N}}$ et $G = ((1-\phi)^n)_{n \in \mathbb{N}}$ sont définies à partir des nombres $\phi = \frac{1+\sqrt{5}}{2}$ et $1-\phi = \frac{1-\sqrt{5}}{2}$.
Ces deux nombres sont les racines de l'équation caractéristique associée à la relation de récurrence $r^2 - r - 1 = 0$.
Cela signifie que $\phi^2 - \phi - 1 = 0$ et $(1-\phi)^2 - (1-\phi) - 1 = 0$.
Ces équations peuvent être réécrites comme $\phi^2 = \phi + 1$ et $(1-\phi)^2 = (1-\phi) + 1$.

1.  **Vérification pour la suite $F = (\phi^n)_{n \in \mathbb{N}}$ :**
    Pour que $F$ appartienne à $E$, ses termes doivent satisfaire la relation de récurrence $u_{n+2} = u_{n+1} + u_n$.
    Nous devons vérifier si $\phi^{n+2} = \phi^{n+1} + \phi^n$ pour tout $n \in \mathbb{N}$.
    Puisque $\phi = \frac{1+\sqrt{5}}{2}$ est un nombre non nul, nous pouvons diviser l'équation par $\phi^n$ (pour $n \ge 0$).
    L'équation devient $\phi^2 = \phi + 1$.
    Nous savons que $\phi$ est une racine de $r^2 - r - 1 = 0$, donc $\phi^2 - \phi - 1 = 0$, ce qui est équivalent à $\phi^2 = \phi + 1$.
    Cette égalité est vraie. Par conséquent, la suite $F$ appartient à $E$.

2.  **Vérification pour la suite $G = ((1-\phi)^n)_{n \in \mathbb{N}}$ :**
    Pour que $G$ appartienne à $E$, ses termes doivent satisfaire la relation de récurrence $u_{n+2} = u_{n+1} + u_n$.
    Nous devons vérifier si $(1-\phi)^{n+2} = (1-\phi)^{n+1} + (1-\phi)^n$ pour tout $n \in \mathbb{N}$.
    Puisque $1-\phi = \frac{1-\sqrt{5}}{2}$ est un nombre non nul, nous pouvons diviser l'équation par $(1-\phi)^n$ (pour $n \ge 0$).
    L'équation devient $(1-\phi)^2 = (1-\phi) + 1$.
    Nous savons que $1-\phi$ est l'autre racine de $r^2 - r - 1 = 0$, donc $(1-\phi)^2 - (1-\phi) - 1 = 0$, ce qui est équivalent à $(1-\phi)^2 = (1-\phi) + 1$.
    Cette égalité est vraie. Par conséquent, la suite $G$ appartient à $E$.

Nous avons vérifié que $F$ et $G$ sont bien des éléments de l'espace vectoriel $E$.

#### Question 2b : Démontrer que la famille $\{F, G\}$ est une famille libre dans $E$.

Une famille de vecteurs $\{v_1, v_2, \dots, v_k\}$ d'un espace vectoriel est dite libre si la seule combinaison linéaire de ces vecteurs qui est égale au vecteur nul est celle où tous les coefficients scalaires sont nuls.
Dans notre cas, les vecteurs sont les suites $F$ et $G$, et le vecteur nul est la suite nulle $(0)_{n \in \mathbb{N}}$.
Soient $\alpha, \beta \in \mathbb{R}$ des scalaires tels que la combinaison linéaire $\alpha F + \beta G$ est égale à la suite nulle.
Cela signifie que pour tout $n \in \mathbb{N}$, le $n$-ième terme de la suite $\alpha F + \beta G$ est égal à 0.
Donc, pour tout $n \in \mathbb{N}$:
$$\alpha \phi^n + \beta (1-\phi)^n = 0$$
Nous allons utiliser cette égalité pour des valeurs spécifiques de $n$.

1.  **Pour $n=0$ :**
    $\alpha \phi^0 + \beta (1-\phi)^0 = 0$
    Puisque $\phi^0 = 1$ et $(1-\phi)^0 = 1$:
    $\alpha \cdot 1 + \beta \cdot 1 = 0$
    $\alpha + \beta = 0$ (Équation 1)

2.  **Pour $n=1$ :**
    $\alpha \phi^1 + \beta (1-\phi)^1 = 0$
    $\alpha \phi + \beta (1-\phi) = 0$ (Équation 2)

Nous avons maintenant un système de deux équations linéaires avec deux inconnues $\alpha$ et $\beta$:
$$ \begin{cases} \alpha + \beta = 0 \\ \alpha \phi + \beta (1-\phi) = 0 \end{cases} $$
De l'Équation 1, nous pouvons exprimer $\beta$ en fonction de $\alpha$:
$\beta = -\alpha$

Substituons cette expression de $\beta$ dans l'Équation 2:
$\alpha \phi + (-\alpha) (1-\phi) = 0$
$\alpha \phi - \alpha (1-\phi) = 0$
Factorisons $\alpha$:
$\alpha (\phi - (1-\phi)) = 0$
$\alpha (\phi - 1 + \phi) = 0$
$\alpha (2\phi - 1) = 0$

Calculons la valeur de $2\phi - 1$:
$2\phi - 1 = 2 \left(\frac{1+\sqrt{5}}{2}\right) - 1 = (1+\sqrt{5}) - 1 = \sqrt{5}$

L'équation devient donc:
$\alpha \sqrt{5} = 0$
Puisque $\sqrt{5}$ est un nombre réel non nul, nous devons avoir $\alpha = 0$.

Maintenant, substituons $\alpha = 0$ dans l'expression de $\beta$:
$\beta = -\alpha = -0 = 0$

Nous avons trouvé que $\alpha = 0$ et $\beta = 0$ sont les seules solutions possibles pour que la combinaison linéaire $\alpha F + \beta G$ soit la suite nulle.
Par conséquent, la famille $\{F, G\}$ est une famille libre dans $E$.

#### Question 3 : Démontrer que la famille $\{F, G\}$ est une famille génératrice de $E$.

Une famille de vecteurs $\{v_1, v_2, \dots, v_k\}$ est dite génératrice d'un espace vectoriel $E$ si tout vecteur de $E$ peut être exprimé comme une combinaison linéaire de ces vecteurs.
Dans notre cas, nous devons montrer que pour toute suite $U = (u_n)_{n \in \mathbb{N}}$ appartenant à $E$, il existe des scalaires $A, B \in \mathbb{R}$ tels que $U = A F + B G$.
Cela signifie que pour tout $n \in \mathbb{N}$:
$$u_n = A \phi^n + B (1-\phi)^n$$

Une propriété fondamentale des suites définies par une relation de récurrence linéaire d'ordre 2 (comme celle de $E$) est qu'une suite est entièrement déterminée par ses deux premiers termes, $u_0$ et $u_1$. En effet, si $u_0$ et $u_1$ sont connus, alors $u_2 = u_1 + u_0$, $u_3 = u_2 + u_1$, et ainsi de suite, tous les termes suivants sont fixés de manière unique.

Nous allons donc chercher à trouver des scalaires $A$ et $B$ tels que l'égalité $u_n = A \phi^n + B (1-\phi)^n$ soit satisfaite pour $n=0$ et $n=1$. Si nous trouvons de tels $A$ et $B$, alors la suite $A F + B G$ aura les mêmes termes $u_0$ et $u_1$ que la suite $U$. Puisque les deux suites appartiennent à $E$ et sont déterminées de manière unique par leurs deux premiers termes, elles doivent être identiques pour tous les $n$.

1.  **Pour $n=0$ :**
    $u_0 = A \phi^0 + B (1-\phi)^0$
    $u_0 = A \cdot 1 + B \cdot 1$
    $u_0 = A + B$ (Équation 3)

2.  **Pour $n=1$ :**
    $u_1 = A \phi^1 + B (1-\phi)^1$
    $u_1 = A \phi + B (1-\phi)$ (Équation 4)

Nous avons un système de deux équations linéaires avec deux inconnues $A$ et $B$:
$$ \begin{cases} A + B = u_0 \\ A \phi + B (1-\phi) = u_1 \end{cases} $$
De l'Équation 3, nous exprimons $B$ en fonction de $A$ et $u_0$:
$B = u_0 - A$

Substituons cette expression de $B$ dans l'Équation 4:
$A \phi + (u_0 - A)(1-\phi) = u_1$
Développons le terme $(u_0 - A)(1-\phi)$:
$A \phi + u_0(1-\phi) - A(1-\phi) = u_1$
Regroupons les termes contenant $A$:
$A (\phi - (1-\phi)) + u_0(1-\phi) = u_1$
Simplifions le coefficient de $A$:
$\phi - (1-\phi) = \phi - 1 + \phi = 2\phi - 1$
Comme nous l'avons calculé précédemment, $2\phi - 1 = \sqrt{5}$.
Donc l'équation devient:
$A \sqrt{5} + u_0(1-\phi) = u_1$
Isolons $A$:
$A \sqrt{5} = u_1 - u_0(1-\phi)$
$A = \frac{u_1 - u_0(1-\phi)}{\sqrt{5}}$

Maintenant, substituons la valeur de $A$ dans l'expression de $B = u_0 - A$:
$B = u_0 - \frac{u_1 - u_0(1-\phi)}{\sqrt{5}}$
Pour simplifier, mettons au même dénominateur:
$B = \frac{u_0 \sqrt{5} - (u_1 - u_0(1-\phi))}{\sqrt{5}}$
$B = \frac{u_0 \sqrt{5} - u_1 + u_0(1-\phi)}{\sqrt{5}}$
$B = \frac{u_0 (\sqrt{5} + 1 - \phi) - u_1}{\sqrt{5}}$
Rappelons que $\phi = \frac{1+\sqrt{5}}{2}$, donc $\sqrt{5} = 2\phi - 1$.
Substituons $\sqrt{5}$ dans l'expression de $B$:
$B = \frac{u_0 (2\phi - 1 + 1 - \phi) - u_1}{\sqrt{5}}$
$B = \frac{u_0 \phi - u_1}{\sqrt{5}}$

Puisque $\sqrt{5} \neq 0$, nous avons trouvé des valeurs uniques pour $A$ et $B$ pour n'importe quelle paire de termes initiaux $(u_0, u_1)$.
Cela signifie que pour toute suite $U = (u_n)_{n \in \mathbb{N}}$ dans $E$, il existe une unique combinaison linéaire $A F + B G$ qui correspond à $U$.
Par conséquent, la famille $\{F, G\}$ est une famille génératrice de $E$.

#### Question 4 : En déduire une base de $E$ et sa dimension.

Une base d'un espace vectoriel est une famille de vecteurs qui est à la fois libre et génératrice de cet espace.
1.  D'après la Question 2b, nous avons démontré que la famille $\{F, G\}$ est une famille libre dans $E$.
2.  D'après la Question 3, nous avons démontré que la famille $\{F, G\}$ est une famille génératrice de $E$.

Puisque la famille $\{F, G\}$ est à la fois libre et génératrice pour l'espace vectoriel $E$, elle constitue une base de $E$.

La dimension d'un espace vectoriel est le nombre de vecteurs dans n'importe laquelle de ses bases.
La base $\{F, G\}$ contient deux vecteurs distincts ($F$ et $G$).
Par conséquent, la dimension de l'espace vectoriel $E$ est 2.
Nous notons $\dim_{\mathbb{R}}(E) = 2$.

---
Ceci conclut l'exercice. J'espère que cette exploration détaillée vous a permis de solidifier votre compréhension des concepts fondamentaux des espaces vectoriels en dimension finie.
