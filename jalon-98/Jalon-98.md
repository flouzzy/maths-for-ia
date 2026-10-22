---
uuid: "jalon-98"
title: "Théorème de Hahn-Banach (forme analytique)"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 97 (Espaces de Banach et Opérateurs Linéaires).md]]"
next: "[[Jalon 99 (Théorème de Hahn-Banach).md]]"
---

# Jalon 98 : Théorème de Hahn-Banach (forme analytique)

## Présentation du concept clé

- Imaginez que vous soyez un cartographe. Vous avez dessiné une carte très précise d'un petit quartier (un sous-espace $M$). Vous avez une règle qui vous donne l'altitude exacte dans ce quartier.
    - Maintenant, on vous demande de compléter la carte pour tout le pays (l'espace $E$).
    - On vous impose une contrainte : votre nouvelle carte ne doit jamais dépasser l'altitude d'une montagne protectrice qui recouvre tout le pays (une fonction sous-linéaire $p$).
    - Le **Théorème de Hahn-Banach** dit que c'est **toujours possible**. Vous pouvez toujours étendre votre règle locale à tout l'espace sans jamais tricher avec les mesures originales et sans jamais percer le "toit" imposé par la montagne.
- En dimension infinie, les espaces sont si vastes qu'on pourrait craindre qu'il n'y ait pas assez de "scanners" (formes linéaires) pour tout voir. Hahn-Banach garantit qu'il y a "suffisamment" de formes linéaires pour distinguer tous les points et pour supporter toutes les contraintes d'optimisation.
- Une droite (forme linéaire) qui effleure une surface courbe (fonction convexe) sans jamais entrer dedans.

## Formalisation

Soit $E$ un espace vectoriel sur $\mathbb{R}$.

### A. Fonctionnelle Sous-linéaire

> **Définition 1 :** Une application $p : E \to \mathbb{R}$ est dite **sous-linéaire** si :
> 1. $\forall x, y \in E, \quad p(x+y) \le p(x) + p(y)$ (Sous-additivité).
> 2. $\forall \lambda \ge 0, \forall x \in E, \quad p(\lambda x) = \lambda p(x)$ (Homogénéité positive).
> *Note :* Toute norme est une fonctionnelle sous-linéaire.

### B. Le Théorème de Hahn-Banach (Analytique)

> **Théorème :**
> Soit $M$ un sous-espace vectoriel de $E$. Soit $f : M \to \mathbb{R}$ une forme linéaire telle que :
> $$\forall x \in M, \quad f(x) \le p(x)$$
> Alors il existe une forme linéaire $F : E \to \mathbb{R}$ telle que :
> 1. $F|_M = f$ (C'est un prolongement).
> 2. $\forall x \in E, \quad F(x) \le p(x)$.



**Exemple Concret 1 : Le demi-espace en dimension 2.**
Considérons $E = \mathbb{R}^2$. Soit $M = \{(x, 0) \mid x \in \mathbb{R}\}$ l'axe des abscisses.
On définit $f : M \to \mathbb{R}$ par $f(x, 0) = x$. $f$ est une forme linéaire sur $M$.
Soit $p : E \to \mathbb{R}$ définie par $p(x, y) = \sqrt{x^2 + y^2}$, la norme euclidienne.
Vérifions que $f \le p$ sur $M$:
$f(x, 0) = x \le |x| = \sqrt{x^2 + 0^2} = p(x, 0)$.
Le théorème de Hahn-Banach nous assure qu'il existe un prolongement $F : \mathbb{R}^2 \to \mathbb{R}$ tel que $F(x, 0) = x$ et $F(x, y) \le \sqrt{x^2 + y^2}$.
Si $F$ est linéaire sur $\mathbb{R}^2$, elle s'écrit $F(x, y) = ax + by$.
Comme $F(x, 0) = x$, on a $a = 1$. Donc $F(x, y) = x + by$.
Pour que $F(x, y) \le \sqrt{x^2 + y^2}$, on prend le carré de $(x+by)^2 \le x^2 + y^2$, d'où $x^2 + 2bxy + b^2y^2 \le x^2 + y^2$.
Cela implique $2bxy + (b^2-1)y^2 \le 0$ pour tout $x,y$. En choisissant $b=0$, cette inégalité (et $x \le \sqrt{x^2+y^2}$) est satisfaite.
Le prolongement naturel est $F(x, y) = x$.

**Exemple Concret 2 : L'espace des suites bornées $\ell^\infty$.**
Soit $E = \ell^\infty$ l'espace des suites réelles bornées $x = (x_n)_{n \in \mathbb{N}}$ muni de la norme $\|x\|_\infty = \sup_{n} |x_n|$.
Soit $M$ le sous-espace des suites convergentes. On définit $f : M \to \mathbb{R}$ par $f(x) = \lim_{n \to \infty} x_n$.
C'est une forme linéaire sur $M$, et pour toute suite convergente $x$, $f(x) \le \|x\|_\infty$.
Par Hahn-Banach, $f$ se prolonge en une forme linéaire continue $F$ sur $E$ telle que $\|F\| \le 1$.
$F$ attribue ainsi une "limite généralisée" (ou limite de Banach) à *toute* suite bornée, même divergente (comme $(-1)^n$).

**Exemple Concret 3 : Fonctionnelle sous-linéaire sur $\mathbb{R}^2$.**
Soit $E = \mathbb{R}^2$. On pose $p(x, y) = \max(|x|, |y|) = \|(x,y)\|_\infty$.
$p$ est sous-linéaire car c'est une norme.
Soit $M = \mathbb{R}(1, 1) = \{(t, t) \mid t \in \mathbb{R}\}$.
Soit $f : M \to \mathbb{R}$ définie par $f(t, t) = t$.
On a $f(t, t) = t \le |t| = \max(|t|, |t|) = p(t, t)$. L'hypothèse de Hahn-Banach est vérifiée.
On cherche $F(x, y) = ax + by$ telle que $a+b = 1$ et $ax+by \le \max(|x|, |y|)$.
Si $a=1, b=0$, on a $F(x, y) = x \le \max(|x|, |y|)$.
Si $a=1/2, b=1/2$, on a $F(x, y) = \frac{x+y}{2} \le \frac{|x|+|y|}{2} \le \max(|x|, |y|)$.
Il y a donc une infinité de prolongements possibles.

**Exemple Concret 4 : Forme linéaire sur $\mathbb{R}[X]$.**
Soit $E = \mathbb{R}[X]$. On définit $p(P) = \int_0^1 |P(t)| dt = \|P\|_1$.
Soit $M = \mathbb{R}_{1}[X]$ (polynômes de degré $\le 1$).
$f(aX+b) = a/2 + b$. $f(P) = \int_0^1 P(t) dt$.
Pour tout $P \in M$, $f(P) \le \int_0^1 |P(t)| dt = p(P)$.
$f$ s'étend à $F$ sur $\mathbb{R}[X]$. Ici l'extension la plus naturelle (et unique pour la continuité $L^1$) est simplement $F(P) = \int_0^1 P(t) dt$ pour tout polynôme.

**Exemple Concret 5 : Séparation dans le plan.**
On a un convexe fermé $C = \{(x, y) \mid x^2 + y^2 \le 1\}$ et un point $x_0 = (2, 0)$.
On peut séparer $x_0$ de $C$ par un hyperplan (une droite affine).
Ici, la droite d'équation $x = 1.5$ sépare strictement $C$ de $x_0$.
La forme linéaire sous-jacente est $f(x, y) = x$. Pour tout $(x, y) \in C$, $f(x,y) \le 1$. Et $f(2, 0) = 2 > 1$.


\begin{center}
\begin{tikzpicture}
  % Draw axes
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,4) node[above] {$p(x)$};

  % Draw convex function p(x)
  \draw[thick, blue, domain=-2.5:2.5, samples=100] plot (\x, {0.5*\x*\x + 0.5}) node[right] {$p(x)$};

  % Draw subspace M (e.g., origin) and function f(x)
  \draw[thick, red] (-2.5, -1.25) -- (2.5, 1.25) node[right] {$f(x)$};

  % Indicate M and extension
  \filldraw[black] (0,0) circle (2pt) node[anchor=north west] {Origine $M$};
  \draw[dashed, green!60!black] (-2, -2) -- (2, 2) node[right] {$F(x)$ prolongement};
  \node[green!60!black] at (1, 1.5) {$F(x) \le p(x)$};

\end{tikzpicture}
\end{center}

## Démonstrations

### Démonstration : Le prolongement d'un pas (Dimension +1)

Soit $x_0 \in E \setminus M$. On veut étendre $f$ à $M \oplus \mathbb{R}x_0$. On cherche donc une valeur $c = F(x_0)$.
Pour tout $x \in M$ and $\lambda \in \mathbb{R}$, on veut $F(x + \lambda x_0) \le p(x + \lambda x_0)$.

1. **Conditions sur c :**
   - Pour $\lambda > 0$ : $f(x) + \lambda c \le p(x + \lambda x_0) \implies c \le \frac{1}{\lambda} [ p(x + \lambda x_0) - f(x) ] = p(\frac{x}{\lambda} + x_0) - f(\frac{x}{\lambda})$.
   - Pour $\lambda = -1$ : $f(y) - c \le p(y - x_0) \implies c \ge f(y) - p(y - x_0)$.
2. **Existence de c :** On a besoin de montrer que $\sup_{y \in M} [f(y) - p(y-x_0)] \le \inf_{x \in M} [p(x+x_0) - f(x)]$.
3. **Preuve de l'inégalité :** Pour tous $x, y \in M$ :
   $f(x) + f(y) = f(x+y) \le p(x+y) = p(x+x_0 + y-x_0) \le p(x+x_0) + p(y-x_0)$.
   D'où $f(y) - p(y-x_0) \le p(x+x_0) - f(x)$.
   Le membre de gauche est toujours inférieur à celui de droite. On peut donc choisir un $c$ entre les deux.
4. **Conclusion :** On peut prolonger de proche en proche. Pour le cas de dimension infinie quelconque, on utilise l'**Axiome du Choix** (sous la forme du Lemme de Zorn) pour montrer qu'il existe un prolongement maximal qui couvre tout $E$.

## Exercices d'Application

### Exercice 1 : Existence de formes linéaires
**Énoncé :** Soit $E$ un espace vectoriel normé et $x \neq 0$. Montrer qu'il existe $L \in E^*$ telle que $\|L\|=1$ and $L(x) = \|x\|$.
**Correction Détaillée :**
1. On pose $M = \mathbb{R}x$ (la droite engendrée par $x$).
2. On définit $f(\lambda x) = \lambda \|x\|$ sur $M$.
3. $f$ est linéaire et vérifie $f(y) \le \|y\|$ pour tout $y \in M$.
4. Par Hahn-Banach (avec $p = \| \cdot \|$), il existe un prolongement $L$ à $E$ tel que $L(y) \le \|y\|$.
5. Cela implique $\|L\| \le 1$. Comme $L(x/\|x\|) = 1$, alors $\|L\|=1$.

### Exercice 2 : Niveau Avancé (Dualité et Distance)
**Énoncé :** Soit $M$ un sous-espace de $E$ and $x \in E$. Montrer que $dist(x, M) = \sup \{ L(x) \mid L \in M^\perp, \|L\| \le 1 \}$.
**Correction Détaillée :**
C'est une application directe de Hahn-Banach. On construit une forme linéaire qui vaut 0 sur $M$ et qui mesure l'écart de $x$ par rapport à $M$. C'est le fondement de la **Dualité de Fenchel** en optimisation.

## Application en Intelligence Artificielle

- **Le Pont Théorique :** Hahn-Banach garantit que les problèmes d'**Optimisation Convexe** sous contraintes ont des solutions duales (les multiplicateurs de Lagrange).
- **Example Concret :**
    - **Support Vector Machines (SVM) :** Pour trouver l'hyperplan séparateur optimal, on résout un problème dual. Hahn-Banach assure que cet hyperplan existe toujours si les données sont linéairement séparables.
    - **Théorie de la Robustesse :** Pour prouver qu'un réseau de neurones est robuste, on essaie de trouver une forme linéaire qui "borne" ses sorties. Hahn-Banach est utilisé pour prouver l'existence de telles bornes dans des espaces de fonctions complexes.
    - **Apprentissage de Mesures (GANS) :** La distance de Wasserstein peut s'écrire sous une forme duale (Kantorovich-Rubinstein) grâce à une variante de Hahn-Banach. C'est ce qui permet de transformer une intégrale difficile sur des joints de probabilités en une optimisation sur des fonctions lipschitziennes.

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 97 (Espaces de Banach et Opérateurs Linéaires).md]], [[Jalon 11 (Formes linéaires).md]]
- **Concepts Futurs dépendants :** [[Jalon 99 (Théorème de Hahn-Banach).md]], [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]]
