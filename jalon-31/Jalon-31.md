---
uuid: "jalon-31"
title: "Introduction à la réduction de Jordan et structure des nilpotents"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/recherche-theorique
prev: "[[Jalon-30.md]]"
next: "[[Jalon-32.md]]"
---

# Jalon 31 : Introduction à la réduction de Jordan et structure des nilpotents

## 1. Genèse et Motivation (L'Échafaudage Cognitif)

L'algèbre linéaire classique, telle qu'introduite par la diagonalisation, propose un idéal séduisant : tout endomorphisme $u$ d'un espace vectoriel $E$ de dimension finie pourrait se réduire à de simples homothéties unidimensionnelles, si seulement l'on trouvait la "bonne" base de vecteurs propres. Dans ce monde parfait, la matrice représentative devient diagonale, et les calculs sur les puissances ou les exponentielles de matrices deviennent triviaux.

Mais cet idéal est fragile. Dès que le polynôme caractéristique possède des racines multiples dont l'ordre de multiplicité algébrique strictement supérieur à la dimension du sous-espace propre associé (multiplicité géométrique), la machine s'enraye. La diagonalisation échoue. L'espace vectoriel n'est plus la somme directe des sous-espaces propres. Que se passe-t-il alors dans les "trous" laissés par ce déficit de vecteurs propres ?

Historiquement, cette question obsédait Camille Jordan au XIXe siècle. Il comprit que l'échec de la diagonalisation n'est pas un chaos informe, mais obéit à une structure hiérarchique profonde. Au lieu de vecteurs totalement indépendants évoluant chacun sur leur propre axe, on découvre des vecteurs "enchaînés" : le premier est transformé par $u - \lambda \mathrm{id}$ en un multiple du second, qui lui-même se transforme dans le troisième, jusqu'à s'écraser sur le vecteur nul. C'est l'essence de la nilpotence. La réduction de Jordan montre que tout endomorphisme (sur un corps algébriquement clos, comme $\mathbb{C}$) peut être vu comme une somme de comportements diagonaux (étirements) et de comportements nilpotents (décalages successifs et annulations en cascade), offrant ainsi une classification structurelle absolue et exhaustive.

## 2. Le Protocole d'Exégèse Conceptuelle

### A. Énoncé Symbolique Strict

**Définition (Opérateur Nilpotent) :**
Soit $E$ un espace vectoriel sur un corps $\mathbb{K}$. Un endomorphisme $u \in \mathcal{L}(E)$ est dit **nilpotent** s'il existe un entier $k \in \mathbb{N}^*$ tel que $u^k = 0_{\mathcal{L}(E)}$. Le plus petit entier naturel non nul vérifiant cette propriété est appelé l'**indice de nilpotence** de $u$.

**Définition (Bloc de Jordan) :**
Pour un scalaire $\lambda \in \mathbb{K}$ et un entier $k \ge 1$, le bloc de Jordan $J_k(\lambda) \in \mathcal{M}_k(\mathbb{K})$ est la matrice définie par :
$$ J_k(\lambda) = \begin{pmatrix}
\lambda & 1 & 0 & \cdots & 0 \\
0 & \lambda & 1 & \ddots & \vdots \\
0 & 0 & \ddots & \ddots & 0 \\
\vdots & \ddots & \ddots & \lambda & 1 \\
0 & \cdots & 0 & 0 & \lambda
\end{pmatrix} = \lambda I_k + N_k $$
où $N_k$ est la matrice nilpotente de taille $k \times k$ ayant des $1$ sur la surdiagonale principale, et $0$ partout ailleurs.

### B. Anatomie et Typage Chirurgical

- $E$ : Un $\mathbb{K}$-espace vectoriel, typiquement de dimension finie $n$.
- $u$ : Endomorphisme de $E$, c'est-à-dire une application linéaire de $E$ dans $E$.
- $u^k = u \circ u \circ \cdots \circ u$ ($k$ fois) : La composition itérée de l'endomorphisme.
- $0_{\mathcal{L}(E)}$ : L'application nulle qui associe le vecteur nul $0_E$ à tout vecteur de $E$.
- $J_k(\lambda)$ : Une matrice carrée d'ordre $k$ dont la diagonale principale est entièrement occupée par la valeur propre $\lambda$, et dont la première surdiagonale est remplie de $1$. Elle représente intrinsèquement la somme d'une homothétie et d'un "shift" (décalage) nilpotent de rang maximum.

### C. Exemples de Validation

**Exemple 1 (Nilpotent trivial) :**
Considérons la matrice $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
On a $A^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
C'est une matrice nilpotente d'indice 2, et elle correspond exactement au bloc de Jordan $J_2(0)$.

**Exemple 2 (Dérivation sur les polynômes) :**
Considérons l'espace vectoriel $\mathbb{R}_n[X]$ des polynômes de degré inférieur ou égal à $n$. L'opérateur de dérivation $D : P \mapsto P'$ est un endomorphisme de $\mathbb{R}_n[X]$. Comme la dérivation diminue le degré d'un polynôme non nul d'exactement 1, pour tout polynôme $P \in \mathbb{R}_n[X]$, on a $D^{n+1}(P) = 0$. Ainsi, $D^{n+1} = 0$, et l'opérateur de dérivation est nilpotent d'indice $n+1$. Dans la base canonique $(1, X, X^2/2!, \ldots, X^n/n!)$, la matrice de $D$ est exactement $J_{n+1}(0)$.

### D. Cas Pathologiques et Contre-exemples

- **Dimension infinie :** La nilpotence est globale (il existe un $k$ fixe pour tous les vecteurs). Si l'on a un opérateur $u$ tel que pour chaque vecteur $x$, il existe $k_x$ avec $u^{k_x}(x) = 0$, mais que $\sup \{k_x\} = +\infty$, alors $u$ n'est pas nilpotent.
- **Corps de base non algébriquement clos :** Si le polynôme caractéristique ne se scinde pas (par exemple $X^2+1$ sur $\mathbb{R}$), il est impossible d'obtenir une forme de Jordan classique. La théorie de Jordan suppose que toutes les racines du polynôme caractéristique appartiennent au corps de base.

## 3. Zéro Ellipse : Théorème Fondamental des Nilpotents

**Théorème :** Un endomorphisme $u \in \mathcal{L}(E)$ de dimension finie $n \ge 1$ est nilpotent si et seulement si son polynôme caractéristique est $\chi_u(X) = X^n$.

**Démonstration :**

**Sens $\impliedby$ :**
Supposons que $\chi_u(X) = X^n$.
Par le théorème de Cayley-Hamilton, tout endomorphisme annule son polynôme caractéristique.
Ainsi, $\chi_u(u) = u^n = 0_{\mathcal{L}(E)}$.
L'endomorphisme $u$ est donc nilpotent, d'indice inférieur ou égal à $n$.

**Sens $\implies$ :**
Supposons que $u$ est nilpotent. Soit $k \in \mathbb{N}^*$ l'indice de nilpotence de $u$, donc $u^k = 0_{\mathcal{L}(E)}$.
Soit $\lambda \in \mathbb{K}$ une valeur propre de $u$ dans un corps de décomposition de $\chi_u$, et $x \in E \setminus \{0_E\}$ un vecteur propre associé.
On a $u(x) = \lambda x$.
Par une récurrence immédiate, pour tout entier $m \ge 1$, $u^m(x) = \lambda^m x$.
En particulier, pour $m = k$, nous obtenons :
$u^k(x) = \lambda^k x$.
Or, $u^k = 0_{\mathcal{L}(E)}$, donc $u^k(x) = 0_E$.
Nous avons donc $\lambda^k x = 0_E$.
Comme $x \neq 0_E$ (par définition d'un vecteur propre), il vient $\lambda^k = 0$.
Le corps $\mathbb{K}$ étant intègre, la seule solution est $\lambda = 0$.
L'unique valeur propre possible pour $u$ est $0$.
Le polynôme caractéristique $\chi_u(X)$, de degré $n$ et de coefficient dominant $(-1)^n$ (ou $1$ selon les conventions), dont les racines sont exactement les valeurs propres, n'admet que $0$ pour racine.
Ainsi, dans le corps de décomposition, $\chi_u(X) = X^n$. Comme les coefficients de $\chi_u$ sont intrinsèquement dans $\mathbb{K}$, cette factorisation vaut sur $\mathbb{K}$.

## 4. Introduction à la Réduction de Jordan

**Théorème (Réduction de Jordan) :**
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$. Soit $u \in \mathcal{L}(E)$ un endomorphisme dont le polynôme caractéristique est scindé sur $\mathbb{K}$.
Alors, il existe une base de $E$ dans laquelle la matrice de $u$ est bloc-diagonale, constituée exclusivement de blocs de Jordan $J_k(\lambda)$, où les $\lambda$ sont les valeurs propres de $u$.
Cette représentation est unique, à l'ordre des blocs près.

*La preuve détaillée, reposant sur le lemme des noyaux, les sous-espaces caractéristiques et la réduction des endomorphismes nilpotents, sera explorée dans les jalons ultérieurs. Ce résultat constitue le pinacle de la théorie de la réduction.*
