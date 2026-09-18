---
uuid: "jalon-73"
title: "Espaces Lp et passage au quotient"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 72 (Livrable IA).md]]"
next: "[[Jalon 74 (Inégalités fondamentales de l'analyse fonctionnelle).md]]"
---

# Jalon 73 : Les Espaces $\mathcal{L}^p$ et le Passage à l'Espace Quotient $L^p$

## 1. La Quête d'une Véritable Distance entre Fonctions

Au cœur de l'analyse fonctionnelle se trouve le besoin de mesurer l'écart ou la taille des fonctions, de la même manière que l'on mesure la longueur d'un vecteur dans $\mathbb{R}^n$. Historiquement, l'intégration de Riemann a permis de définir une notion de moyenne et d'énergie pour les fonctions continues. Cependant, sous l'impulsion d'Henri Lebesgue au début du XXe siècle, la théorie de la mesure a ouvert la porte à des espaces de fonctions beaucoup plus vastes : les fonctions mesurables.

Si l'on veut définir une géométrie sur cet immense ensemble de fonctions, il faut pouvoir les regrouper selon certaines propriétés d'intégrabilité (sommabilité absolue, énergie finie). C'est ainsi que naissent les espaces $\mathcal{L}^p$.

Le défi fondamental qui surgit immédiatement est le suivant : dans la théorie de Lebesgue, une fonction qui est nulle partout sauf sur un ensemble de mesure nulle (comme les rationnels $\mathbb{Q}$ dans $\mathbb{R}$) a une intégrale nulle. Géométriquement, si l'intégrale du module (ou du carré) représente une norme, une "longueur" nulle devrait impliquer que la fonction est elle-même rigoureusement le vecteur nul. Or, ce n'est pas le cas ici ! Nous faisons face à des "fonctions fantômes" qui échappent à l'intégrale.

Pour résoudre cette obstruction géométrique et faire de notre espace un véritable espace vectoriel normé (une condition sine qua non pour définir des limites, des projections ou des dérivées de fonctions), les mathématiciens ont dû concevoir une identification abstraite : le passage au quotient. Le principe est d'ignorer les différences de comportement sur les ensembles de mesure nulle. Deux fonctions deviennent indiscernables si elles ne diffèrent que sur un ensemble négligeable. C'est ce saut conceptuel qui donne naissance aux espaces $L^p$, piliers incontournables des mathématiques modernes et de l'apprentissage statistique.

## 2. Définitions et Théorèmes Fondamentaux

Dans toute cette section, nous considérons un espace mesuré $(X, \mathcal{F}, \mu)$ et $\mathbb{K}$ désigne le corps $\mathbb{R}$ ou $\mathbb{C}$.

### Définition des espaces $\mathcal{L}^p$

Pour $p \in [1, +\infty[$, on s'intéresse aux fonctions dont la puissance $p$-ième du module est intégrable.

> **Définition 1 (L'espace $\mathcal{L}^p$) :**
> Soit $p \in [1, +\infty[$. L'espace $\mathcal{L}^p(X, \mathcal{F}, \mu)$, souvent noté plus simplement $\mathcal{L}^p$, est l'ensemble des fonctions $f : X \to \mathbb{K}$ mesurables telles que :
> $$ \int_X |f|^p \, d\mu < +\infty $$
> On associe à cet espace l'application $N_p : \mathcal{L}^p \to \mathbb{R}^+$ définie par :
> $$ N_p(f) = \left( \int_X |f|^p \, d\mu \right)^{1/p} $$

**Analyse de la définition :**
- $f$ est une fonction mesurable à valeurs scalaires.
- L'intégrale est bien définie, éventuellement égale à $+\infty$, car $|f|^p$ est une fonction mesurable positive.
- Le paramètre $p$ détermine le "poids" que l'on accorde aux grandes valeurs de $f$. Pour $p=1$, c'est la norme absolue moyenne. Pour $p=2$, c'est l'énergie.
- L'exposant $1/p$ à l'extérieur de l'intégrale garantit l'homogénéité : $N_p(\lambda f) = |\lambda| N_p(f)$.

Le cas limite, $p = +\infty$, nécessite une définition spécifique reposant sur la notion de "presque partout" (p.p.).

> **Définition 2 (L'espace $\mathcal{L}^\infty$) :**
> L'espace $\mathcal{L}^\infty(X, \mathcal{F}, \mu)$ est l'ensemble des fonctions $f : X \to \mathbb{K}$ mesurables pour lesquelles il existe une constante réelle $C \ge 0$ telle que :
> $$ |f(x)| \le C \quad \mu\text{-presque partout (p.p.)} $$
> C'est-à-dire que $\mu(\{ x \in X \mid |f(x)| > C \}) = 0$.
> L'application $N_\infty : \mathcal{L}^\infty \to \mathbb{R}^+$ est définie comme le **supremum essentiel** de $|f|$ :
> $$ N_\infty(f) = \inf \left\{ C \ge 0 \mid \mu(\{ x \in X \mid |f(x)| > C \}) = 0 \right\} $$

**Exemples concrets immédiats :**
Plaçons-nous sur $X = ]0, 1]$ avec la mesure de Lebesgue $\lambda$.
Considérons la fonction $f(x) = \frac{1}{\sqrt{x}}$.
Est-ce que $f \in \mathcal{L}^1$ ? Calculons l'intégrale :
$\int_0^1 |f(x)|^1 \, dx = \int_0^1 x^{-1/2} \, dx = \left[ 2x^{1/2} \right]_0^1 = 2 < +\infty$.
Donc $f \in \mathcal{L}^1$ et $N_1(f) = 2$.
Est-ce que $f \in \mathcal{L}^2$ ?
$\int_0^1 |f(x)|^2 \, dx = \int_0^1 \left(\frac{1}{\sqrt{x}}\right)^2 \, dx = \int_0^1 \frac{1}{x} \, dx = \left[ \ln(x) \right]_0^1 = +\infty$.
Donc $f \notin \mathcal{L}^2$.
Une fonction peut être dans $\mathcal{L}^1$ mais pas dans $\mathcal{L}^2$ si elle présente une divergence locale suffisamment forte.

Considérons maintenant $g(x) = 5$ sur $]0, 1] \setminus \mathbb{Q}$ et $g(x) = 100$ sur $]0, 1] \cap \mathbb{Q}$.
Puisque la mesure des rationnels est nulle ($\lambda(]0, 1] \cap \mathbb{Q}) = 0$), $g(x) \le 5$ p.p.
Le supremum absolu de $g$ est $100$. Mais son supremum essentiel est $N_\infty(g) = 5$.

### Le problème de la norme et la relation d'équivalence

Pour que l'espace $\mathcal{L}^p$ devienne un espace vectoriel normé, $N_p$ doit satisfaire les trois axiomes d'une norme :
1. Homogénéité : $N_p(\lambda f) = |\lambda| N_p(f)$ (Vérifié).
2. Inégalité triangulaire : $N_p(f+g) \le N_p(f) + N_p(g)$ (C'est l'inégalité de Minkowski, que nous démontrerons formellement au Jalon 74).
3. Séparation : $N_p(f) = 0 \implies f = 0_{X \to \mathbb{K}}$.

C'est ce troisième point qui échoue sur $\mathcal{L}^p$.

> **Théorème 1 (Caractérisation des fonctions de semi-norme nulle) :**
> Soit $f \in \mathcal{L}^p(X, \mathcal{F}, \mu)$ avec $1 \le p \le +\infty$.
> $$ N_p(f) = 0 \iff f(x) = 0 \quad \mu\text{-presque partout} $$

Cela signifie que $N_p$ est seulement une **semi-norme**. Pour rendre la séparation vraie de manière stricte, nous devons modifier les objets mathématiques que nous manipulons. Au lieu de travailler avec des fonctions individuelles, nous allons travailler avec des **classes** de fonctions.

> **Définition 3 (Relation d'égalité presque partout) :**
> On définit sur l'espace vectoriel des fonctions mesurables la relation binaire $\sim$ par :
> $$ f \sim g \iff f = g \quad \mu\text{-presque partout} $$
> C'est-à-dire : $\mu(\{ x \in X \mid f(x) \neq g(x) \}) = 0$.

> **Proposition 1 :**
> La relation $\sim$ est une relation d'équivalence (réflexive, symétrique, transitive).

**Exemple concret immédiat :**
Soit $f(x) = 0$ partout sur $\mathbb{R}$. Soit $h(x) = 0$ pour $x \neq 0$ et $h(0) = 42$.
Avec la mesure de Lebesgue, le singleton $\{0\}$ est de mesure nulle. Ainsi, $f = h$ presque partout. Ces deux fonctions appartiennent à la même classe d'équivalence pour la relation $\sim$.

### L'Espace Quotient $L^p$

> **Définition 4 (L'espace de Banach $L^p$) :**
> L'espace $L^p(X, \mathcal{F}, \mu)$ est défini comme l'ensemble quotient de $\mathcal{L}^p$ par la relation d'équivalence $\sim$ :
> $$ L^p = \mathcal{L}^p / \sim $$
> Un élément de $L^p$ (que l'on notera souvent abusivement $f$ au lieu de $\dot{f}$ ou $[f]$) est une classe d'équivalence de fonctions qui coïncident presque partout.
> Sur cet espace quotient, l'application $\|f\|_p = N_p(f)$ est une véritable norme.

**Remarque fondamentale :** En mathématiques appliquées et en physique, lorsqu'on parle d'une "fonction $f \in L^p$", on parle formellement d'une classe d'équivalence. Il n'a aucun sens de parler de "la valeur de $f$ au point $x_0$" (i.e. $f(x_0)$), car on peut toujours trouver un représentant de la classe qui vaut n'importe quoi au point $x_0$, cet ensemble singleton étant de mesure nulle (pour la mesure de Lebesgue). On ne peut parler que des intégrales de $f$ sur des ensembles de mesure strictement positive.

## 3. Démonstrations

### Preuve du Théorème 1 : Caractérisation de $N_p(f)=0$

Nous allons démontrer en détail que pour $p \in [1, +\infty[$, $N_p(f) = 0 \iff f = 0$ p.p.

**Sens réciproque ($\impliedby$) :**
Supposons que $f = 0$ $\mu$-p.p.
Soit $E = \{ x \in X \mid f(x) \neq 0 \}$. Par hypothèse, $\mu(E) = 0$.
Posons $g(x) = |f(x)|^p$. La fonction $g$ est positive, et elle est nulle en dehors de $E$.
On peut décomposer l'intégrale sur une partition de l'espace $X = E \cup (X \setminus E)$ :
$$ \int_X g \, d\mu = \int_{E} g \, d\mu + \int_{X \setminus E} g \, d\mu $$
Sur $X \setminus E$, $g = 0$ partout, donc l'intégrale est rigoureusement nulle.
Sur $E$, on sait que l'intégrale d'une fonction mesurable sur un ensemble de mesure nulle est nulle (propriété de base de l'intégrale de Lebesgue). Donc $\int_{E} g \, d\mu = 0$.
Ainsi, $\int_X |f|^p \, d\mu = 0$, et donc $N_p(f) = 0$.

**Sens direct ($\implies$) :**
Supposons que $N_p(f) = 0$, ce qui implique $\int_X |f|^p \, d\mu = 0$.
Définissons les sous-ensembles suivants pour tout entier $n \ge 1$ :
$$ A_n = \left\{ x \in X \;\middle|\; |f(x)|^p \ge \frac{1}{n} \right\} $$
Remarquons que sur $A_n$, la fonction indicatrice $\mathbf{1}_{A_n}$ vérifie :
$$ |f(x)|^p \ge \frac{1}{n} \mathbf{1}_{A_n}(x) $$
Ceci est vrai sur tout $X$, car si $x \notin A_n$, le membre de droite vaut 0, et le membre de gauche est toujours $\ge 0$.
En intégrant cette inégalité positive (par monotonie de l'intégrale de Lebesgue) :
$$ \int_X |f|^p \, d\mu \ge \int_X \frac{1}{n} \mathbf{1}_{A_n} \, d\mu = \frac{1}{n} \mu(A_n) $$
Or, par hypothèse, le membre de gauche est strictement nul. Donc :
$$ 0 \ge \frac{1}{n} \mu(A_n) $$
Puisque la mesure $\mu(A_n)$ est toujours positive ou nulle, on en déduit que $\mu(A_n) = 0$ pour tout $n \ge 1$.
Maintenant, posons $A = \{ x \in X \mid |f(x)| > 0 \} = \{ x \in X \mid |f(x)|^p > 0 \}$.
Un point $x$ appartient à $A$ si et seulement si $|f(x)|^p > 0$, donc s'il existe un entier $n$ suffisamment grand tel que $|f(x)|^p \ge \frac{1}{n}$. Autrement dit, $A$ est la réunion dénombrable des ensembles $A_n$ :
$$ A = \bigcup_{n=1}^\infty A_n $$
Par sous-additivité dénombrable de la mesure $\mu$ :
$$ \mu(A) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0 $$
Ainsi, $\mu(A)=0$. L'ensemble des points où $f$ est non nulle est de mesure nulle. C'est exactement la définition de $f = 0$ p.p.

### Preuve de la structure d'espace vectoriel : $f+g \in \mathcal{L}^p$

Nous devons justifier que la somme de deux fonctions de $\mathcal{L}^p$ reste dans $\mathcal{L}^p$.
Soient $f, g \in \mathcal{L}^p$. La fonction $f+g$ est mesurable.
Pour tout $x \in X$, par inégalité triangulaire dans $\mathbb{K}$ :
$$ |f(x) + g(x)| \le |f(x)| + |g(x)| $$
En élevant à la puissance $p$ (la fonction $t \mapsto t^p$ est strictement croissante sur $\mathbb{R}^+$) :
$$ |f(x) + g(x)|^p \le \left( |f(x)| + |g(x)| \right)^p $$
En utilisant la convexité de la fonction $t \mapsto t^p$ pour $p \ge 1$. Pour deux réels positifs $a,b$ :
$$ \left( \frac{a+b}{2} \right)^p \le \frac{1}{2} a^p + \frac{1}{2} b^p $$
En multipliant par $2^p$, on obtient l'inégalité algébrique :
$$ (a+b)^p \le 2^{p-1} (a^p + b^p) $$
Appliquons cela à $|f(x)|$ et $|g(x)|$ :
$$ |f(x) + g(x)|^p \le 2^{p-1} \left( |f(x)|^p + |g(x)|^p \right) $$
Les fonctions à droite sont intégrables par hypothèse. Par linéarité et croissance de l'intégrale :
$$ \int_X |f+g|^p \, d\mu \le 2^{p-1} \left( \int_X |f|^p \, d\mu + \int_X |g|^p \, d\mu \right) < +\infty $$
Ceci prouve rigoureusement que $f+g \in \mathcal{L}^p$. L'espace $\mathcal{L}^p$ (et par passage au quotient $L^p$) est bien un espace vectoriel.

## 4. Applications en Apprentissage Statistique et IA

Le choix de l'espace géométrique $L^p$ dans lequel on projette et optimise les fonctions est fondamental dans l'architecture des algorithmes prédictifs. La norme utilisée pour quantifier l'écart entre la réalité $Y$ et notre prédiction $f(X)$ définit l'espace topologique de l'apprentissage.

**1. L'Espace $L^2$ (Mean Squared Error, Régression OLS) :**
C'est le royaume des moindres carrés. Minimiser l'erreur quadratique revient à chercher la projection orthogonale (car $L^2$ est le seul espace de Hilbert parmi les $L^p$) de la variable cible sur l'espace des prédicteurs.
$$ \min_f \| Y - f(X) \|_2^2 $$
Le problème de la norme $L^2$ est qu'elle pénalise quadratiquement les erreurs de grande amplitude. Si un point aberrant (outlier) existe, sa contribution à l'erreur va exploser, forçant le modèle $f$ à se déformer massivement pour le compenser, ce qui dégrade la prédiction sur les données majoritaires (phénomène d'instabilité).

**2. L'Espace $L^1$ (Mean Absolute Error, Régression Robuste) :**
L'espace $L^1$ pèse chaque erreur proportionnellement à son amplitude absolue, et non au carré.
$$ \min_f \| Y - f(X) \|_1 $$
Un outlier d'amplitude $D$ ajoutera $D$ à l'erreur, contre $D^2$ en norme $L^2$. Ainsi, un algorithme optimisant la norme $L^1$ est intrinsèquement robuste aux anomalies. Cependant, la norme $L^1$ n'est pas strictement différentiable en $0$ (pas de gradient lisse), ce qui complexifie les algorithmes d'optimisation par descente de gradient.

**3. Le Quotient dans les Graphes et le Clustering :**
La notion d'ignorer un ensemble de mesure nulle se retrouve abstraitement en Data Science lorsqu'on ignore un très faible pourcentage de points déconnectés du graphe principal lors du partitionnement spectral (Spectral Clustering). L'algorithme opère sur des "classes d'équivalence" de partitions qui coïncident "presque partout" vis-à-vis de la distribution de probabilité génératrice.
