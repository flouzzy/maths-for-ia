---
uuid: "jalon-61"
title: "Insuffisances de l'intégrale de Riemann"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 60 (Livrable IA T5).md]]"
next: "[[Jalon 62 (Algèbres).md]]"
---

# Insuffisances de l'intégrale de Riemann

## Genèse et obstacles géométriques

L'intégrale de Riemann, formellement construite par des sommes de Darboux et des approximations par des fonctions en escalier, fut une avancée majeure pour rigoureusement définir l'aire sous la courbe d'une fonction continue ou continue par morceaux. Son approche géométrique consiste à découper le domaine d'intégration, c'est-à-dire l'axe des abscisses, en petits intervalles, et à encadrer la fonction par des rectangles inscrits et circonscrits.

Cependant, cette démarche atteint rapidement ses limites lorsqu'on l'applique à des objets mathématiques présentant une topologie plus complexe ou des discontinuités denses. La physique moderne (notamment la mécanique quantique et la théorie cinétique des gaz) ainsi que la théorie des probabilités nécessitent d'intégrer des fonctions extrêmement irrégulières, où l'oscillation est si intense que les sommes de Darboux inférieures et supérieures ne convergent pas vers la même limite. L'incapacité de l'intégrale de Riemann à passer à la limite sous le signe intégral de manière inconditionnelle (sans requérir la convergence uniforme) a motivé la recherche d'une nouvelle théorie de la mesure, capable de traiter l'axe des ordonnées (les valeurs prises par la fonction) plutôt que de fragmenter aveuglément l'axe des abscisses.

## Construction formelle et impasses de l'intégrale de Riemann

### Rappel de l'intégrabilité au sens de Riemann

Soit $f : [a, b] \to \mathbb{R}$ une fonction bornée. On considère une subdivision $\sigma = (x_0, x_1, \dots, x_n)$ du segment $[a, b]$, telle que $a = x_0 < x_1 < \dots < x_n = b$.

On définit les sommes de Darboux inférieure $s(f, \sigma)$ et supérieure $S(f, \sigma)$ par :

$$s(f, \sigma) = \sum_{k=1}^n \left( \inf_{t \in [x_{k-1}, x_k]} f(t) \right) (x_k - x_{k-1})$$
$$S(f, \sigma) = \sum_{k=1}^n \left( \sup_{t \in [x_{k-1}, x_k]} f(t) \right) (x_k - x_{k-1})$$

Une fonction $f$ est dite Riemann-intégrable sur $[a, b]$ si, et seulement si, le supremum des sommes inférieures est égal à l'infimum des sommes supérieures sur l'ensemble de toutes les subdivisions possibles :

$$\sup_{\sigma} s(f, \sigma) = \inf_{\sigma} S(f, \sigma) = \int_a^b f(x) dx$$

### L'exemple critique : la fonction de Dirichlet

L'exemple le plus célèbre d'une fonction bornée non Riemann-intégrable est la fonction indicatrice des rationnels, introduite par Peter Gustav Lejeune Dirichlet en 1829.

Considérons $f : [0, 1] \to \mathbb{R}$ définie par :
$$f(x) = \begin{cases} 1 & \text{si } x \in \mathbb{Q} \\ 0 & \text{si } x \in \mathbb{R} \setminus \mathbb{Q} \end{cases}$$

**Démonstration de non-intégrabilité :**

Soit $\sigma = (x_0, x_1, \dots, x_n)$ une subdivision quelconque de $[0, 1]$. Pour tout sous-intervalle $[x_{k-1}, x_k]$ de longueur $\Delta x_k = x_k - x_{k-1} > 0$, cet intervalle contient à la fois des nombres rationnels (par densité de $\mathbb{Q}$ dans $\mathbb{R}$) et des nombres irrationnels (par densité de $\mathbb{R} \setminus \mathbb{Q}$ dans $\mathbb{R}$).

Par conséquent, sur chaque sous-intervalle :
$$\inf_{t \in [x_{k-1}, x_k]} f(t) = 0 \quad \text{et} \quad \sup_{t \in [x_{k-1}, x_k]} f(t) = 1$$

Il s'ensuit que pour toute subdivision $\sigma$ :
$$s(f, \sigma) = \sum_{k=1}^n 0 \cdot \Delta x_k = 0$$
$$S(f, \sigma) = \sum_{k=1}^n 1 \cdot \Delta x_k = \sum_{k=1}^n (x_k - x_{k-1}) = 1$$

Puisque $\sup s(f, \sigma) = 0 \neq 1 = \inf S(f, \sigma)$, la fonction de Dirichlet n'est pas Riemann-intégrable sur $[0, 1]$. L'aire sous cette courbe échappe à l'approche de Riemann, bien qu'intuitivement, les rationnels étant "beaucoup moins nombreux" (dénombrables) que les irrationnels, l'aire devrait être nulle.

### Incomplétude de l'espace des fonctions Riemann-intégrables

L'espace vectoriel des fonctions Riemann-intégrables sur $[a, b]$, noté $\mathcal{R}([a, b])$, peut être muni de la norme $L^1$ définie par :
$$\|f\|_1 = \int_a^b |f(x)| dx$$

L'un des défauts majeurs de la théorie de Riemann est que l'espace vectoriel normé $(\mathcal{R}([a, b]), \|\cdot\|_1)$ n'est pas un espace de Banach (il n'est pas complet).

**Contre-exemple d'une suite de Cauchy ne convergeant dans $\mathcal{R}([a, b])$ :**

Énumérons les rationnels de l'intervalle $[0, 1]$ sous forme d'une suite $(q_n)_{n \in \mathbb{N}}$. Définissons une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ telles que :
$$f_n(x) = \begin{cases} 1 & \text{si } x \in \{q_0, q_1, \dots, q_n\} \\ 0 & \text{sinon} \end{cases}$$

Chaque fonction $f_n$ est Riemann-intégrable, car elle ne possède qu'un nombre fini de points de discontinuité. Son intégrale de Riemann est nulle : $\int_0^1 f_n(x) dx = 0$.

Cependant, la limite simple de la suite $(f_n)_{n \in \mathbb{N}}$ lorsque $n \to \infty$ est exactement la fonction de Dirichlet $f$. Comme démontré précédemment, $f$ n'est pas Riemann-intégrable. La complétude est pourtant essentielle en analyse fonctionnelle pour résoudre des équations différentielles ou intégrales, car elle assure que les limites d'approximations successives existent au sein du même espace.

## Conséquences pour l'intelligence artificielle

L'incomplétude et le manque de robustesse des théorèmes de convergence (interversion limite et intégrale) de la théorie de Riemann sont des obstacles majeurs en théorie des probabilités. En apprentissage automatique et en statistique mathématique, nous étudions des espaces de variables aléatoires (notamment les espaces $L^p$) qui doivent être complets.

Par exemple, le calcul de l'espérance mathématique d'une variable aléatoire à densité se formule originellement avec une intégrale. Lorsque nous entraînons un modèle génératif ou minimisons une divergence de Kullback-Leibler, nous prenons des limites d'intégrales de fonctions de densité, et nous exigeons des théorèmes solides (Convergence Monotone, Convergence Dominée) qui ne sont valides que dans le cadre plus étendu et structurellement complet de l'intégration de Lebesgue.
