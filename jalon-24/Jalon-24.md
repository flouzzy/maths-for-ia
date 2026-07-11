---
uuid: "jalon-24"
title: "Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites"
year: 1
trimester: 2
tags:
  - math/synthese
  - ia/regression-polynomiale
  - math/analyse-fonctionnelle
prev: "[[Jalon-23.md]]"
next: "[[Jalon 25 (Formes bilinéaires).md]]"
---

# Jalon 24 : Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale

## 1. Genèse et Motivation (Échafaudage Cognitif)

L'un des défis fondamentaux des mathématiques appliquées et de l'intelligence artificielle réside dans la capacité à inférer une loi générale à partir d'observations finies et potentiellement bruitées. Historiquement, des mathématiciens comme Carl Friedrich Gauss et Adrien-Marie Legendre ont été confrontés à ce problème lorsqu'ils tentaient de prédire les orbites cométaires (notamment celle de Cérès en 1801) à partir de mesures astronomiques sporadiques.

L'intuition première consiste à faire passer une courbe "simple" au plus près des points d'observation. Les polynômes, grâce à leur structure algébrique épurée et leur dérivabilité infinie, s'imposent comme des candidats naturels pour modéliser cette courbe. Cependant, un paradoxe profond émerge : si l'on augmente le degré du polynôme d'interpolation pour qu'il passe exactement par tous les points de données, la fonction résultante se met à osciller violemment entre ces points, perdant toute capacité prédictive. Ce phénomène, découvert par Carl Runge en 1901, démontre que la recherche naïve de l'erreur nulle sur un ensemble d'apprentissage conduit à une divergence catastrophique sur de nouvelles données.

Ainsi, la régression polynomiale ne se résume pas à un simple ajustement de courbe. Elle nécessite une analyse mathématique rigoureuse de la convergence des suites de fonctions. Il faut arbitrer entre la capacité du modèle à représenter la complexité des données (le biais) et sa sensibilité aux variations de l'échantillon (la variance). Ce jalon établit les fondations théoriques de ce compromis, justifiant le recours aux moindres carrés et à la régularisation pour garantir une convergence uniforme vers la loi génératrice sous-jacente.

## 2. Protocole d'Exégèse Conceptuelle : Régression Polynomiale aux Moindres Carrés

### A. Énoncé Symbolique Strict

Soit $n \in \mathbb{N}^*$ le nombre d'observations et $d \in \mathbb{N}$ tel que $d < n$. Soit un jeu de données $\mathcal{D} = \{(x_i, y_i) \in \mathbb{R}^2 \mid 1 \le i \le n\}$ où les $(x_i)_{1 \le i \le n}$ sont deux à deux distincts.

On cherche un polynôme $P \in \mathbb{R}_d[X]$, de la forme $P(X) = \sum_{k=0}^d a_k X^k$, qui minimise la fonctionnelle de risque empirique quadratique :
$$ \mathcal{L}(a_0, \dots, a_d) = \sum_{i=1}^n \left( \sum_{k=0}^d a_k x_i^k - y_i \right)^2 $$

Sous forme matricielle, en notant $\mathbf{a} = (a_0, \dots, a_d)^\top \in \mathbb{R}^{d+1}$, $\mathbf{y} = (y_1, \dots, y_n)^\top \in \mathbb{R}^n$, et $\mathbf{X} \in \mathcal{M}_{n, d+1}(\mathbb{R})$ la matrice de Vandermonde définie par $X_{i,j} = x_i^{j-1}$ pour $1 \le i \le n$ et $1 \le j \le d+1$, le problème d'optimisation s'écrit :
$$ \hat{\mathbf{a}} = \underset{\mathbf{a} \in \mathbb{R}^{d+1}}{\text{argmin}} \|\mathbf{X}\mathbf{a} - \mathbf{y}\|_2^2 $$

### B. Anatomie et Typage Chirurgical

- $n \in \mathbb{N}^*$ : Le cardinal de l'échantillon d'apprentissage. Il doit être strictement positif.
- $d \in \mathbb{N}$ : L'hyperparamètre contrôlant la complexité de l'espace d'hypothèses $\mathcal{H} = \mathbb{R}_d[X]$. La condition $d < n$ assure que le système est surdéterminé, évitant l'interpolation exacte qui mène au surapprentissage.
- $\mathbf{X} \in \mathcal{M}_{n, d+1}(\mathbb{R})$ : La matrice de conception (Design matrix). Ses colonnes représentent les puissances successives des variables explicatives. Son rang est crucial pour l'unicité de la solution.
- $\mathcal{L} : \mathbb{R}^{d+1} \to \mathbb{R}_+$ : La fonction de perte (Loss function). Elle est de classe $\mathcal{C}^\infty$ et strictement convexe si $\mathbf{X}^\top\mathbf{X}$ est définie positive.
- $\|\cdot\|_2$ : La norme euclidienne standard sur $\mathbb{R}^n$, induite par le produit scalaire canonique $\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u}^\top\mathbf{v}$.

### C. Exemples de Validation

**Exemple 1 (Régression linéaire simple, $d=1$) :**
Soit $\mathcal{D} = \{(1, 2), (2, 3), (3, 5)\}$. $n=3$, $d=1$.
$\mathbf{X} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}$. L'objectif est de trouver la droite d'équation $y = a_0 + a_1 x$ minimisant l'erreur résiduelle, ce qui revient à projeter orthogonalement $\mathbf{y}$ sur l'image de l'application linéaire associée à $\mathbf{X}$.

**Exemple 2 (Ajustement quadratique, $d=2$) :**
Pour des données décrivant une trajectoire balistique $\mathcal{D} = \{(0, 0), (1, 4), (2, 6), (3, 4), (4, 0)\}$. $n=5$, $d=2$.
On cherche $\mathbf{a} = (a_0, a_1, a_2)^\top$ pour $P(X) = a_0 + a_1 X + a_2 X^2$. La matrice $\mathbf{X} \in \mathcal{M}_{5, 3}(\mathbb{R})$ a pour termes $X_{i,j} = x_i^{j-1}$.

### D. Cas Pathologiques et Contre-exemples

- **Dégénérescence par colinéarité :** Si certains $x_i$ ne sont pas distincts, ou si $n \le d$, les colonnes de $\mathbf{X}$ ne sont plus linéairement indépendantes. La matrice $\mathbf{X}^\top\mathbf{X}$ devient singulière (non inversible), et la fonction $\mathcal{L}$ perd sa stricte convexité, admettant une infinité de solutions.
- **Phénomène de Runge (Échec de la convergence uniforme) :** Soit la fonction de Runge $f(x) = \frac{1}{1 + 25x^2}$ sur $[-1, 1]$. Si l'on choisit $n$ points équidistants $x_i = -1 + \frac{2i}{n-1}$ et qu'on cherche le polynôme d'interpolation exact $P_n$ (i.e. $d = n-1$), on constate que $\lim_{n \to \infty} \left\|f - P_n\right\|_\infty = +\infty$. L'erreur explose aux bords de l'intervalle. Cela prouve que minimiser l'erreur d'entraînement à zéro avec un modèle trop complexe ruine la capacité de généralisation.

## 3. Démonstrations à Zéro Ellipse Mathématique

### Théorème (Solution Analytique et Équations Normales)
Si les $(x_i)_{1 \le i \le n}$ sont distincts et $n > d$, alors le problème d'optimisation admet une unique solution globale donnée par :
$$ \hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y} $$

**Démonstration détaillée :**

Soit $\mathcal{L}(\mathbf{a}) = \|\mathbf{X}\mathbf{a} - \mathbf{y}\|_2^2$. Exprimons cette fonction sous forme de produit scalaire :
$$ \mathcal{L}(\mathbf{a}) = (\mathbf{X}\mathbf{a} - \mathbf{y})^\top(\mathbf{X}\mathbf{a} - \mathbf{y}) $$

Par linéarité de la transposition, $(A+B)^\top = A^\top + B^\top$ et $(AB)^\top = B^\top A^\top$ :
$$ \mathcal{L}(\mathbf{a}) = (\mathbf{a}^\top\mathbf{X}^\top - \mathbf{y}^\top)(\mathbf{X}\mathbf{a} - \mathbf{y}) $$

Développons par distributivité :
$$ \mathcal{L}(\mathbf{a}) = \mathbf{a}^\top\mathbf{X}^\top\mathbf{X}\mathbf{a} - \mathbf{a}^\top\mathbf{X}^\top\mathbf{y} - \mathbf{y}^\top\mathbf{X}\mathbf{a} + \mathbf{y}^\top\mathbf{y} $$

Notons que la quantité $\mathbf{a}^\top\mathbf{X}^\top\mathbf{y}$ est le produit d'une matrice $(1 \times (d+1))$, $((d+1) \times n)$, et $(n \times 1)$. Le résultat est donc un scalaire (matrice $1 \times 1$). Pour tout scalaire $\lambda$, $\lambda^\top = \lambda$.
Ainsi, $(\mathbf{a}^\top\mathbf{X}^\top\mathbf{y})^\top = \mathbf{y}^\top(\mathbf{X}^\top)^\top(\mathbf{a}^\top)^\top = \mathbf{y}^\top\mathbf{X}\mathbf{a}$.
On peut donc regrouper les termes linéaires :
$$ \mathcal{L}(\mathbf{a}) = \mathbf{a}^\top(\mathbf{X}^\top\mathbf{X})\mathbf{a} - 2\mathbf{a}^\top\mathbf{X}^\top\mathbf{y} + \mathbf{y}^\top\mathbf{y} $$

Calculons à présent le gradient de $\mathcal{L}$ par rapport au vecteur $\mathbf{a}$.
Rappelons les propriétés différentielles matricielles :
1. $\nabla_\mathbf{x} (\mathbf{c}^\top\mathbf{x}) = \nabla_\mathbf{x} (\mathbf{x}^\top\mathbf{c}) = \mathbf{c}$
2. $\nabla_\mathbf{x} (\mathbf{x}^\top \mathbf{M} \mathbf{x}) = (\mathbf{M} + \mathbf{M}^\top)\mathbf{x}$

Posons $\mathbf{M} = \mathbf{X}^\top\mathbf{X}$. La matrice $\mathbf{M}$ est symétrique car $\mathbf{M}^\top = (\mathbf{X}^\top\mathbf{X})^\top = \mathbf{X}^\top(\mathbf{X}^\top)^\top = \mathbf{X}^\top\mathbf{X} = \mathbf{M}$.
Donc $\nabla_\mathbf{a} (\mathbf{a}^\top\mathbf{X}^\top\mathbf{X}\mathbf{a}) = 2\mathbf{X}^\top\mathbf{X}\mathbf{a}$.

Posons $\mathbf{c} = \mathbf{X}^\top\mathbf{y}$. Alors $\nabla_\mathbf{a} (-2\mathbf{a}^\top\mathbf{c}) = -2\mathbf{c} = -2\mathbf{X}^\top\mathbf{y}$.
Le terme constant $\mathbf{y}^\top\mathbf{y}$ a pour gradient le vecteur nul.

En additionnant ces résultats, on obtient le gradient de la fonction de perte :
$$ \nabla_\mathbf{a} \mathcal{L}(\mathbf{a}) = 2\mathbf{X}^\top\mathbf{X}\mathbf{a} - 2\mathbf{X}^\top\mathbf{y} $$

Pour trouver les points critiques, on résout $\nabla_\mathbf{a} \mathcal{L}(\mathbf{a}) = \mathbf{0}_{d+1}$ :
$$ 2\mathbf{X}^\top\mathbf{X}\mathbf{a} - 2\mathbf{X}^\top\mathbf{y} = \mathbf{0}_{d+1} $$
En divisant chaque membre par 2, on obtient les équations normales :
$$ (\mathbf{X}^\top\mathbf{X})\mathbf{a} = \mathbf{X}^\top\mathbf{y} $$

Il reste à prouver que la matrice carrée d'ordre $d+1$, $\mathbf{M} = \mathbf{X}^\top\mathbf{X}$, est inversible.
Pour tout vecteur $\mathbf{u} \in \mathbb{R}^{d+1}$, on a :
$$ \mathbf{u}^\top\mathbf{M}\mathbf{u} = \mathbf{u}^\top\mathbf{X}^\top\mathbf{X}\mathbf{u} = (\mathbf{X}\mathbf{u})^\top(\mathbf{X}\mathbf{u}) = \|\mathbf{X}\mathbf{u}\|_2^2 \ge 0 $$
La matrice $\mathbf{M}$ est donc semi-définie positive.
Supposons qu'il existe $\mathbf{u}$ tel que $\mathbf{u}^\top\mathbf{M}\mathbf{u} = 0$. Alors $\|\mathbf{X}\mathbf{u}\|_2^2 = 0$, ce qui implique $\mathbf{X}\mathbf{u} = \mathbf{0}_n$.
Le vecteur $\mathbf{X}\mathbf{u}$ correspond à l'évaluation du polynôme $Q(X) = \sum_{k=0}^d u_k X^k$ sur les $n$ points $x_i$.
Donc, pour tout $1 \le i \le n$, $Q(x_i) = 0$.
Le polynôme $Q$ est de degré au plus $d$. Or, il possède $n$ racines distinctes (les $x_i$).
Comme $n > d$, le théorème de d'Alembert-Gauss stipule que le seul polynôme de degré inférieur ou égal à $d$ possédant strictement plus de $d$ racines est le polynôme nul.
Ainsi, $Q = 0$, ce qui implique que tous ses coefficients sont nuls : $\mathbf{u} = \mathbf{0}_{d+1}$.
Par conséquent, $\mathbf{M}$ est définie positive, et donc inversible.

On peut alors multiplier à gauche par $(\mathbf{X}^\top\mathbf{X})^{-1}$ :
$$ \hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y} $$
Puisque $\mathbf{M}$ est définie positive, la matrice Hessienne $\nabla^2 \mathcal{L}(\mathbf{a}) = 2\mathbf{X}^\top\mathbf{X}$ est définie positive en tout point, garantissant que $\mathcal{L}$ est strictement convexe et que le point critique $\hat{\mathbf{a}}$ est l'unique minimum global. $\blacksquare$

## 4. Application en Intelligence Artificielle : La Régularisation de Tikhonov (Ridge)

En pratique, dans des régimes en grande dimension (où $d \approx n$ ou $d > n$), la matrice $\mathbf{X}^\top\mathbf{X}$ devient mal conditionnée ou singulière. Le modèle est alors sujet à une variance extrême (surapprentissage).
Pour pallier cela, on introduit une pénalité sur la norme des coefficients, modifiant l'espace d'hypothèses et forçant la régularité.

**Le Pont Théorique :**
On modifie la fonctionnelle de perte en ajoutant un terme de régularisation $L_2$ pondéré par un hyperparamètre $\lambda > 0$ :
$$ \mathcal{L}_{Ridge}(\mathbf{a}) = \|\mathbf{X}\mathbf{a} - \mathbf{y}\|_2^2 + \lambda \|\mathbf{a}\|_2^2 $$

Le gradient devient :
$$ \nabla_\mathbf{a} \mathcal{L}_{Ridge}(\mathbf{a}) = 2\mathbf{X}^\top\mathbf{X}\mathbf{a} - 2\mathbf{X}^\top\mathbf{y} + 2\lambda\mathbf{a} = 2(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}_{d+1})\mathbf{a} - 2\mathbf{X}^\top\mathbf{y} $$

L'équation normale régularisée est donc :
$$ (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}_{d+1})\mathbf{a} = \mathbf{X}^\top\mathbf{y} $$

Même si $\mathbf{X}^\top\mathbf{X}$ n'est pas inversible (seulement semi-définie positive), pour tout $\lambda > 0$, la matrice $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}_{d+1})$ est définie positive, car ses valeurs propres sont translatées de $+\lambda$. L'inversibilité est mathématiquement garantie, offrant une solution stable :
$$ \hat{\mathbf{a}}_{Ridge} = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}_{d+1})^{-1}\mathbf{X}^\top\mathbf{y} $$
Ceci est le fondement algébrique de la robustesse des modèles prédictifs modernes face au bruit stochastique.

## 5. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 9 (Calcul matriciel)]], [[Jalon 21 (Suites de fonctions)]], [[Jalon 22 (Séries de fonctions)]]
- **Concepts Futurs dépendants :** [[Jalon 25 (Formes bilinéaires)]], [[Jalon 133 (Modèle PAC)]], [[Jalon 144 (Le phénomène de double descente)]]
