---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]"
next: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## Introduction

Le théorème de convergence monotone, formulé par le mathématicien italien Beppo Levi au début du XXe siècle, est l'un des piliers fondateurs de la théorie de l'intégration de Lebesgue. Il répond à un problème crucial laissé ouvert par l'intégrale de Riemann : sous quelles conditions peut-on intervertir la limite et l'intégrale ?

Dans le cadre de l'intégrale de Riemann, une suite de fonctions intégrables convergeant simplement vers une fonction peut avoir une limite non intégrable, ou pire, l'intégrale de la limite peut différer de la limite des intégrales. Le théorème de Beppo Levi apporte une condition de régularité remarquablement simple : la croissance presque partout de la suite de fonctions positives.

Géométriquement, si l'on considère une suite de fonctions $(f_n)$ dont les graphes montent inexorablement (presque partout) vers le graphe d'une fonction $f$, l'aire sous les courbes $f_n$ s'approchera naturellement de l'aire sous la courbe limite $f$. Ce résultat permet de manipuler les séries de fonctions et les espérances avec une robustesse inégalée, justifiant l'utilisation des méthodes limites en analyse fonctionnelle et en probabilités.

\begin{tikzpicture}[scale=1.5]
\draw[->] (-0.2,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (0,3) node[above] {$y$};
\draw[domain=0:3.5, smooth, variable=\x, blue, thick] plot ({\x}, {2 - 1.5*exp(-\x)});
\node[blue] at (3.5, 2.2) {$f(x)$};
\draw[domain=0:3.5, smooth, variable=\x, cyan, dashed] plot ({\x}, {2 - 1.5*exp(-\x) - 0.3});
\node[cyan] at (3.5, 1.6) {$f_{n+1}(x)$};
\draw[domain=0:3.5, smooth, variable=\x, cyan!50, dotted, thick] plot ({\x}, {2 - 1.5*exp(-\x) - 0.7});
\node[cyan!50] at (3.5, 1.2) {$f_n(x)$};
\draw[domain=0:3.5, smooth, variable=\x, cyan!30, dotted, thick] plot ({\x}, {2 - 1.5*exp(-\x) - 1.2});
\end{tikzpicture}

## Définitions, Théorèmes et Exemples

### Enoncé du théorème de convergence monotone

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.

**Théorème (Beppo Levi) :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
Si la suite est croissante presque partout, c'est-à-dire :
$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-presque partout,}$
Alors la fonction limite $f = \lim_{n \to \infty} f_n$ (qui existe dans $[0, +\infty]$) est mesurable, et on a l'égalité :
$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$

**Dissection des variables :**
- $X$ : l'espace de base (par exemple $\mathbb{R}$).
- $\mathcal{A}$ : la tribu des ensembles mesurables.
- $\mu$ : la mesure positive sur $(X, \mathcal{A})$ (par exemple la mesure de Lebesgue).
- $f_n$ : fonctions à valeurs dans $[0, +\infty]$. La positivité est cruciale pour éviter les formes indéterminées $\infty - \infty$.
- $f$ : la limite ponctuelle.

**Corollaire (Sommation de séries à termes positifs) :**
Si $(u_n)_{n \in \mathbb{N}}$ est une suite de fonctions mesurables positives, alors :
$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$
*Preuve immédiate :* Appliquer Beppo Levi à la suite des sommes partielles $f_N = \sum_{n=0}^N u_n$, qui est croissante car $u_n \ge 0$.

### Exemples concrets et pathologiques

**Exemple 1 : Fonctions étagées croissantes**
Considérons $X = [0, 1]$ muni de la mesure de Lebesgue.
Soit $f_n(x) = (1 - x^n)$. Sur $[0, 1]$, on a $x^{n+1} \le x^n$, donc $1 - x^{n+1} \ge 1 - x^n$.
La suite $(f_n)$ est croissante. Sa limite ponctuelle est $f(x) = 1$ pour $x \in [0, 1[$, et $f(1) = 0$.
L'intégrale de $f_n$ est $\int_0^1 (1-x^n)dx = 1 - \frac{1}{n+1} = \frac{n}{n+1}$.
La limite des intégrales est $\lim_{n \to \infty} \frac{n}{n+1} = 1$.
L'intégrale de la limite $f$ (qui vaut $1$ presque partout) est $\int_0^1 1 dx = 1$. L'égalité est vérifiée.

**Exemple 2 : Suite croissante vers l'infini**
Soit $f_n(x) = n \cdot \mathbf{1}_{[0, 1/n]}(x)$.
Attention ! Cette suite *n'est pas* croissante pour tout $x$. Par exemple, en $x = 0.5$, $f_1(0.5) = 1$, mais $f_2(0.5) = 0$. Beppo Levi ne s'applique pas.
En fait, $\int f_n = 1$ pour tout $n$, mais $f(x) = \lim f_n(x) = 0$ pour tout $x > 0$. L'intégrale de la limite est $0 \neq 1$. L'hypothèse de croissance est indispensable.

**Exemple 3 : Convergence monotone avec limites infinies**
Soit $f_n(x) = x^n$ sur $X = [1, +\infty[$. La suite est croissante.
La limite $f(x)$ vaut $+\infty$ pour $x > 1$ et $1$ pour $x=1$. L'intégrale de $f$ est $+\infty$.
L'intégrale de $f_n$ est $\int_1^\infty x^n dx = +\infty$ pour $n \ge 0$. On a bien l'égalité $+\infty = +\infty$.

**Exemple 4 : Série harmonique via le corollaire**
Intégrons $f(x) = \sum_{n=1}^\infty x^n$ sur $]0, 1[$.
Par le corollaire, $\int_0^1 \sum x^n dx = \sum \int_0^1 x^n dx = \sum \frac{1}{n+1} = +\infty$.
Mais on sait aussi que $\sum_{n=1}^\infty x^n = \frac{x}{1-x}$. Et $\int_0^1 \frac{x}{1-x} dx = +\infty$. Les calculs coïncident rigoureusement.

**Exemple 5 : Mesure de comptage**
Soit $X = \mathbb{N}$, $\mathcal{A} = \mathcal{P}(\mathbb{N})$, $\mu$ la mesure de comptage.
Intégrer par rapport à $\mu$, c'est sommer.
Le corollaire donne l'interversion classique des sommes doubles pour des termes positifs :
$\sum_{i \in \mathbb{N}} \sum_{j \in \mathbb{N}} a_{i,j} = \sum_{j \in \mathbb{N}} \sum_{i \in \mathbb{N}} a_{i,j}$ pour $a_{i,j} \ge 0$.

## Demonstrations

**Preuve pas à pas du théorème de Beppo Levi**

**Étape 1 : Inégalité immédiate ($\ge$)**
Puisque $f_n$ est croissante, $\forall n, f_n \le f_{n+1} \le f$.
Par monotonie de l'intégrale, on a pour tout $n$ :
$\int_X f_n d\mu \le \int_X f d\mu$
La suite $(\int f_n d\mu)$ est croissante dans $[0, +\infty]$. Elle admet une limite. En passant à la limite :
$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$

**Étape 2 : L'inégalité réciproque ($\le$) via les fonctions étagées**
Pour prouver $\int_X f d\mu \le \lim \int_X f_n d\mu$, nous utiliserons la définition de l'intégrale de Lebesgue pour les fonctions mesurables positives : le supremum des intégrales des fonctions étagées positives minorant $f$.

Soit $\phi$ une fonction étagée mesurable telle que $0 \le \phi \le f$.
Soit un réel $\alpha \in ]0, 1[$.
Considérons les ensembles mesurables $A_n = \{x \in X \mid f_n(x) \ge \alpha \phi(x)\}$.

**Étape 3 : Propriétés de la suite d'ensembles $(A_n)$**
- **Croissance :** Puisque $f_n(x) \le f_{n+1}(x)$, si $f_n(x) \ge \alpha \phi(x)$, alors $f_{n+1}(x) \ge \alpha \phi(x)$. Donc $A_n \subset A_{n+1}$.
- **Recouvrement :** Si $f(x) = 0$, alors $\phi(x) = 0$, donc $f_n(x) \ge \alpha \phi(x) = 0$ pour tout $n$, $x \in A_n$.
  Si $f(x) > 0$, alors $\alpha \phi(x) < \phi(x) \le f(x)$ car $\alpha < 1$. Puisque $\lim f_n(x) = f(x)$, il existe un rang $N$ tel que pour tout $n \ge N$, $f_n(x) > \alpha \phi(x)$. Donc $x \in A_N$.
  Ainsi, la réunion croissante $\bigcup_{n=1}^\infty A_n$ est l'espace entier $X$.

**Étape 4 : Passage à la limite**
On sait que sur $X$, $f_n \ge f_n \mathbf{1}_{A_n}$. Sur $A_n$, $f_n \ge \alpha \phi$.
Donc $f_n \ge \alpha \phi \mathbf{1}_{A_n}$ sur $X$.
En intégrant :
$\int_X f_n d\mu \ge \int_X \alpha \phi \mathbf{1}_{A_n} d\mu = \alpha \int_{A_n} \phi d\mu$
Puisque $\phi$ est étagée, elle s'écrit $\phi = \sum_{i=1}^k c_i \mathbf{1}_{E_i}$.
$\int_{A_n} \phi d\mu = \sum_{i=1}^k c_i \mu(E_i \cap A_n)$
Comme $(A_n)$ croît vers $X$, $(E_i \cap A_n)$ croît vers $E_i \cap X = E_i$.
Par continuité croissante de la mesure $\mu$, $\lim_{n \to \infty} \mu(E_i \cap A_n) = \mu(E_i)$.
Donc $\lim_{n \to \infty} \int_{A_n} \phi d\mu = \sum_{i=1}^k c_i \mu(E_i) = \int_X \phi d\mu$.
En prenant la limite quand $n \to \infty$ dans l'inégalité intégrale :
$\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \int_X \phi d\mu$

**Étape 5 : Conclusion**
L'inégalité précédente est vraie pour tout $\alpha \in ]0, 1[$. En faisant tendre $\alpha \to 1$, on obtient :
$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X \phi d\mu$
Cette inégalité est vraie pour toute fonction étagée $\phi \le f$.
Par définition de $\int_X f d\mu$ comme supremum sur ces fonctions étagées :
$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X f d\mu$

Les inégalités des étapes 1 et 5 concluent la démonstration. $\blacksquare$

## Applications en Physique, Logique, & AI

En apprentissage automatique (Machine Learning), le théorème de convergence monotone garantit la robustesse des méthodes d'optimisation stochastique lorsque l'on manipule des sommes infinies d'espérances ou de fonctions de perte strictement positives.

Considérons un modèle d'apprentissage probabiliste où l'erreur (Loss) est définie par une série d'espérances sur différents sous-échantillons croissants. Si la fonction de coût à chaque étape est positive et croît au fur et à mesure que l'on ajoute des contraintes au modèle, Beppo Levi certifie que le coût espéré de la limite du processus est exactement la limite des coûts espérés successifs.

De même, dans les architectures génératives basées sur des équations différentielles stochastiques (Diffusion Models), on approxime une intégrale temporelle (sur le processus inverse de diffusion) par des discrétisations fines. Le théorème garantit que si la discrétisation approche de manière croissante la vraie fonction d'erreur sur les trajectoires, l'espérance de l'erreur calculée converge bien vers la vraie perte continue. Il n'y a pas de 'saut' de la valeur de l'intégrale à l'infini, validant ainsi la théorie de la convergence asymptotique de ces modèles massifs.
