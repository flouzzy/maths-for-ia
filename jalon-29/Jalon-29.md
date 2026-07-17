---
uuid: "jalon-29"
title: "Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/reduction-endomorphismes
prev: "[[Jalon 28 (Polynômes d'endomorphismes).md]]"
next: "[[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.).md]]"
---
# Jalon 29 : Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité

## 1. Genèse et Motivation (Échafaudage Cognitif)

L'algèbre linéaire a forgé les outils permettant d'appréhender des transformations vectorielles complexes. Cependant, analyser l'action d'un endomorphisme $f$ sur un espace vectoriel $E$ de dimension $n$ en considérant toutes les directions possibles s'avère rapidement inextricable. La motivation historique derrière la théorie de la réduction des endomorphismes (initiée notamment par Augustin-Louis Cauchy et Karl Weierstrass) naît d'une question d'une élégante simplicité : *existe-t-il des directions privilégiées dans l'espace que la transformation $f$ laisse globalement invariantes, c'est-à-dire où elle se comporte comme une simple homothétie ?*

Imaginez déformer un objet élastique : bien que la plupart des points subissent des rotations et des cisaillements complexes, certaines directions fondamentales (les axes principaux de déformation) sont simplement étirées ou contractées. Les vecteurs non nuls portés par ces axes sont appelés **vecteurs propres**, et le facteur d'étirement associé est la **valeur propre**.

L'objectif ultime de cette quête est la **diagonalisation** : trouver une base de l'espace entièrement constituée de ces vecteurs privilégiés. Dans une telle base, la matrice de l'endomorphisme devient diagonale, ce qui rend le calcul de ses puissances ou de son exponentielle (fondamental en dynamique des systèmes ou en IA, via les chaînes de Markov et l'analyse en composantes principales) immédiat.

## 2. Formalisation : Le Protocole d'Exégèse Conceptuelle

### 2.1 Valeurs Propres, Vecteurs Propres et Spectre

**A. Énoncé Symbolique Strict**
Soit $E$ un $\mathbb{K}$-espace vectoriel et $f \in \mathcal{L}(E)$.
Un scalaire $\lambda \in \mathbb{K}$ est une **valeur propre** de $f$ s'il existe un vecteur $x \in E \setminus \{0_E\}$ tel que :
$$f(x) = \lambda x$$
Le vecteur $x$ est alors appelé **vecteur propre** de $f$ associé à la valeur propre $\lambda$.
L'ensemble des valeurs propres de $f$ est appelé le **spectre** de $f$, noté $\text{Sp}(f)$.

**B. Anatomie et Typage Chirurgical**
- $E$ : Un espace vectoriel sur un corps $\mathbb{K}$ (typiquement $\mathbb{R}$ ou $\mathbb{C}$).
- $f$ : Un endomorphisme de $E$, c'est-à-dire une application linéaire de $E$ dans $E$.
- $\lambda \in \mathbb{K}$ : Un scalaire. Il représente le facteur d'homothétie. Remarquons que $\lambda$ peut être nul.
- $x \in E \setminus \{0_E\}$ : Le vecteur propre. La condition $x \neq 0_E$ est **cruciale**. Si l'on acceptait le vecteur nul, l'équation $f(0_E) = \lambda 0_E$ serait vérifiée pour n'importe quel $\lambda \in \mathbb{K}$ (car $f(0_E)=0_E$), ce qui viderait le concept de tout intérêt.

**C. Exemples de Validation**
- *Exemple trivial* : Soit $f = \text{Id}_E$, l'application identité. Pour tout $x \neq 0_E$, $f(x) = x = 1 \cdot x$. Donc $1$ est la seule valeur propre, et tout vecteur non nul est vecteur propre. $\text{Sp}(f) = \{1\}$.
- *Exemple complexe* : Dans $\mathbb{R}[X]$, soit $D : P \mapsto P'$ l'opérateur de dérivation. Si $D(P) = \lambda P$, alors $P' = \lambda P$. Les seules solutions polynomiales sont les polynômes constants si $\lambda = 0$, et aucune solution non nulle si $\lambda \neq 0$. Le spectre est $\text{Sp}(D) = \{0\}$, et les vecteurs propres sont les polynômes constants non nuls.

**D. Cas Pathologiques et Contre-exemples**
Une matrice ou un endomorphisme peut n'avoir **aucune** valeur propre (spectre vide) si le corps de base n'est pas algébriquement clos. Par exemple, la matrice de rotation d'angle $\pi/2$ dans $\mathbb{R}^2$ : $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. Son équation $R x = \lambda x$ n'a aucune solution non nulle dans $\mathbb{R}^2$. Ainsi, $\text{Sp}_{\mathbb{R}}(R) = \emptyset$. Cependant, si l'on se place dans $\mathbb{C}$, $\text{Sp}_{\mathbb{C}}(R) = \{i, -i\}$. Le choix du corps $\mathbb{K}$ est donc déterminant.

### 2.2 Sous-espaces Propres

**A. Énoncé Symbolique Strict**
Soit $\lambda \in \text{Sp}(f)$. Le **sous-espace propre** associé à $\lambda$, noté $E_\lambda(f)$, est défini par :
$$E_\lambda(f) = \ker(f - \lambda \text{Id}_E) = \{x \in E \mid f(x) = \lambda x\}$$

**B. Anatomie et Typage Chirurgical**
- $E_\lambda(f)$ : C'est l'ensemble constitué de tous les vecteurs propres associés à $\lambda$, **auquel on rajoute le vecteur nul** $0_E$.
- $f - \lambda \text{Id}_E$ : Un endomorphisme de $E$. Le fait que $\lambda$ soit une valeur propre équivaut exactement à dire que cet endomorphisme n'est pas injectif (son noyau n'est pas réduit à $\{0_E\}$).

**C. Propriétés Fondamentales (Théorème)**
1. $E_\lambda(f)$ est un sous-espace vectoriel de $E$.
2. $\dim(E_\lambda(f)) \geq 1$ (car $\lambda$ est valeur propre, donc $\exists x \neq 0, x \in E_\lambda(f)$).

### 2.3 Le Polynôme Caractéristique

**A. Énoncé Symbolique Strict**
Pour $E$ de dimension finie $n$, soit $A$ la matrice de $f$ dans une base donnée. Le **polynôme caractéristique** de $f$, noté $\chi_f(X)$, est défini par :
$$\chi_f(X) = \det(X I_n - A)$$

**B. Anatomie et Typage Chirurgical**
- $X$ : Une indéterminée. $\chi_f(X)$ est un polynôme de degré $n$ à coefficients dans $\mathbb{K}$.
- $I_n$ : La matrice identité d'ordre $n$.
- $\det$ : Le déterminant. Comme le déterminant de deux matrices semblables est identique, $\chi_f(X)$ ne dépend pas du choix de la base.
- Racines : Les racines de $\chi_f$ dans $\mathbb{K}$ sont **exactement** les valeurs propres de $f$.

**C. Multiplicité Algébrique et Géométrique**
Soit $\lambda_0$ une racine de $\chi_f$.
- **Multiplicité algébrique $m(\lambda_0)$** : C'est l'ordre de multiplicité de la racine $\lambda_0$ dans le polynôme $\chi_f(X)$.
- **Multiplicité géométrique** : C'est la dimension du sous-espace propre associé, $\dim(E_{\lambda_0}(f))$.
- **Théorème fondamental** : $1 \leq \dim(E_{\lambda_0}(f)) \leq m(\lambda_0)$.

### 2.4 Critères de Diagonalisabilité

**A. Énoncé Symbolique Strict**
Un endomorphisme $f \in \mathcal{L}(E)$ est **diagonalisable** s'il existe une base de $E$ formée de vecteurs propres de $f$.

**B. Théorème Principal (Conditions nécessaires et suffisantes)**
Un endomorphisme $f$ de dimension finie est diagonalisable si et seulement si :
1. Son polynôme caractéristique $\chi_f(X)$ est **scindé** sur $\mathbb{K}$ (c'est-à-dire qu'il se factorise complètement en produit de polynômes de degré 1).
2. Pour chaque valeur propre $\lambda$, la dimension de son sous-espace propre est égale à sa multiplicité algébrique : $\dim(E_\lambda(f)) = m(\lambda)$.

## 3. Zéro Ellipse : Preuve de l'Indépendance des Sous-espaces Propres

**Théorème :** Des vecteurs propres associés à des valeurs propres deux à deux distinctes forment une famille libre.

**Démonstration (par récurrence sur la taille de la famille) :**
Soit $f \in \mathcal{L}(E)$.
Montrons par récurrence sur $k \in \mathbb{N}^*$ la proposition $\mathcal{P}(k)$ : "Toute famille $(x_1, \dots, x_k)$ de vecteurs propres de $f$ associés à des valeurs propres $(\lambda_1, \dots, \lambda_k)$ deux à deux distinctes est libre."

**Initialisation ($k=1$) :**
Soit $x_1$ un vecteur propre associé à $\lambda_1$. Par définition d'un vecteur propre, $x_1 \neq 0_E$.
Toute famille constituée d'un seul vecteur non nul est libre.
Donc $\mathcal{P}(1)$ est vraie.

**Hérédité :**
Soit $k \geq 1$. Supposons $\mathcal{P}(k)$ vraie.
Soit $(x_1, \dots, x_{k+1})$ une famille de vecteurs propres associés à des valeurs propres $(\lambda_1, \dots, \lambda_{k+1})$ deux à deux distinctes.
Montrons que cette famille est libre.
Soient $\alpha_1, \dots, \alpha_{k+1} \in \mathbb{K}$ tels que :
$(1) \quad \sum_{i=1}^{k+1} \alpha_i x_i = 0_E$

Appliquons l'endomorphisme $f$ à l'équation $(1)$ :
$f\left(\sum_{i=1}^{k+1} \alpha_i x_i\right) = f(0_E)$
Par linéarité de $f$ :
$\sum_{i=1}^{k+1} \alpha_i f(x_i) = 0_E$
Comme $x_i$ est vecteur propre pour $\lambda_i$, on a $f(x_i) = \lambda_i x_i$. Ainsi :
$(2) \quad \sum_{i=1}^{k+1} \alpha_i \lambda_i x_i = 0_E$

Multiplions maintenant l'équation $(1)$ par $\lambda_{k+1}$ :
$(3) \quad \sum_{i=1}^{k+1} \alpha_i \lambda_{k+1} x_i = 0_E$

Soustrayons l'équation $(3)$ à l'équation $(2)$ :
$\sum_{i=1}^{k+1} \alpha_i \lambda_i x_i - \sum_{i=1}^{k+1} \alpha_i \lambda_{k+1} x_i = 0_E$
En factorisant par $\alpha_i x_i$, on obtient :
$\sum_{i=1}^{k+1} \alpha_i (\lambda_i - \lambda_{k+1}) x_i = 0_E$

Séparons le terme pour $i=k+1$ :
$\sum_{i=1}^{k} \alpha_i (\lambda_i - \lambda_{k+1}) x_i + \alpha_{k+1}(\lambda_{k+1} - \lambda_{k+1})x_{k+1} = 0_E$
Ce qui donne :
$\sum_{i=1}^{k} \alpha_i (\lambda_i - \lambda_{k+1}) x_i = 0_E$

Or, par hypothèse de récurrence $\mathcal{P}(k)$, la famille $(x_1, \dots, x_k)$ est libre.
Par conséquent, tous les coefficients de cette combinaison linéaire sont nuls :
$\forall i \in \{1, \dots, k\}, \quad \alpha_i (\lambda_i - \lambda_{k+1}) = 0$

Comme les valeurs propres sont deux à deux distinctes, $\forall i \in \{1, \dots, k\}, \lambda_i \neq \lambda_{k+1}$, ce qui implique $\lambda_i - \lambda_{k+1} \neq 0$.
Dans le corps $\mathbb{K}$ (sans diviseur de zéro), on en déduit immédiatement que :
$\forall i \in \{1, \dots, k\}, \quad \alpha_i = 0$

On remplace ces valeurs nulles dans l'équation initiale $(1)$ :
$\sum_{i=1}^{k} 0 \cdot x_i + \alpha_{k+1} x_{k+1} = 0_E$
Soit $\alpha_{k+1} x_{k+1} = 0_E$.
Comme $x_{k+1}$ est un vecteur propre, il est non nul ($x_{k+1} \neq 0_E$).
On en conclut que $\alpha_{k+1} = 0$.

Puisque $\alpha_1 = \dots = \alpha_k = \alpha_{k+1} = 0$, la famille $(x_1, \dots, x_{k+1})$ est libre.
La proposition $\mathcal{P}(k+1)$ est vraie.

**Conclusion :** Par le principe de récurrence, pour tout $k \geq 1$, toute famille de $k$ vecteurs propres associés à des valeurs propres distinctes est libre.
