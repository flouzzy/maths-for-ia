---
uuid: "jalon-75"
title: "Complétude des espaces Lp (Riesz-Fischer)"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/convergence
prev: "[[Jalon 74 (Inégalités fondamentales de l'analyse fonctionnelle).md]]"
next: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
---

# Jalon 75 : Complétude des espaces $L^p$ (Théorème de Riesz-Fischer)

## 1. Genèse et Intuition de la Complétude

L'introduction de l'intégrale de Lebesgue visait principalement à corriger une faiblesse structurelle majeure de l'intégrale de Riemann : le manque de bonnes propriétés de passage à la limite. Si l'on conçoit l'espace des fonctions intégrables muni d'une distance (ou norme), on souhaite que cet espace soit "sans trou". C'est l'analogue pour les espaces de fonctions de la complétude de $\mathbb{R}$ par rapport à $\mathbb{Q}$.

Historiquement, le besoin s'est fait sentir au début du XXe siècle lors du développement de l'analyse fonctionnelle par Frigyes Riesz et Ernst Sigismund Fischer (indépendamment, en 1907). Ils cherchaient à donner un sens à la convergence des séries de Fourier. Dans un espace non complet, une suite de fonctions (les sommes partielles de la série de Fourier, par exemple) peut "converger" au sens où ses termes se rapprochent arbitrairement les uns des autres (suite de Cauchy), mais sans que la "limite" ne soit une fonction de notre espace de départ.

La complétude garantit que toute suite de Cauchy de fonctions converge vers une limite qui est elle-même une fonction bien définie dans l'espace. Le théorème de Riesz-Fischer affirme précisément que les espaces $L^p$, munis de leur norme naturelle, possèdent cette propriété cruciale : ce sont des espaces de Banach.

## 2. Définitions et Théorèmes Fondamentaux

### Le cadre et les normes $L^p$

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Pour $p \in [1, +\infty[$, l'espace $L^p(X, \mu)$ est l'espace vectoriel des classes d'équivalence (pour l'égalité $\mu$-presque partout) de fonctions mesurables $f : X \to \mathbb{R}$ (ou $\mathbb{C}$) telles que :

$$ \|f\|_p = \left( \int_X |f|^p \, d\mu \right)^{\frac{1}{p}} < +\infty $$

Pour $p = +\infty$, $L^\infty(X, \mu)$ est l'espace des classes de fonctions mesurables essentiellement bornées, muni de la norme :

$$ \|f\|_\infty = \inf \{ C \ge 0 \mid \mu(\{x \in X \mid |f(x)| > C\}) = 0 \} $$

### Le Théorème de Riesz-Fischer

> **Théorème de Riesz-Fischer**
> Pour tout $p \in [1, +\infty]$, l'espace vectoriel normé $(L^p(X, \mu), \|\cdot\|_p)$ est complet.
> Autrement dit, c'est un espace de Banach.

**Précision sur la convergence et les suites de Cauchy :**
Une suite $(f_n)_{n \in \mathbb{N}}$ d'éléments de $L^p$ est dite de Cauchy si :
$$ \forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall m, n \ge N, \|f_n - f_m\|_p \le \varepsilon $$

Le théorème affirme que pour toute telle suite de Cauchy, il existe $f \in L^p$ telle que :
$$ \lim_{n \to +\infty} \|f_n - f\|_p = 0 $$

### Extraction d'une sous-suite convergente presque partout

Un corollaire fondamental (parfois inclus dans l'énoncé de Riesz-Fischer) relie la convergence en norme $L^p$ à la convergence ponctuelle.

> **Théorème (Convergence en norme et convergence presque partout)**
> Si une suite $(f_n)_{n \in \mathbb{N}}$ converge vers $f$ dans $L^p$ (pour $1 \le p \le +\infty$), alors il existe une sous-suite $(f_{\varphi(n)})_{n \in \mathbb{N}}$ qui converge vers $f$ $\mu$-presque partout.

**Exemple concret immédiat : L'escargot glissant (ou la bosse fuyante)**
Considérons l'espace mesuré $([0, 1], \mathcal{B}([0, 1]), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Construisons une suite de fonctions indicatrices d'intervalles qui "balayent" $[0,1]$ en se rétrécissant :
Pour $k \ge 1$ et $0 \le j < k$, on définit $n = \frac{k(k-1)}{2} + j$ et $I_n = \left[\frac{j}{k}, \frac{j+1}{k}\right]$.
Posons $f_n = \mathbf{1}_{I_n}$.
- Pour la norme $L^1$, on a $\|f_n\|_1 = \frac{1}{k}$. Puisque $k \to +\infty$ quand $n \to +\infty$, $\|f_n\|_1 \to 0$. Donc $f_n$ converge vers $0$ dans $L^1$.
- Cependant, pour tout $x \in [0, 1]$, la suite $(f_n(x))$ prend la valeur 1 une infinité de fois (chaque fois qu'un "balayage" de niveau $k$ passe sur $x$) et la valeur 0 une infinité de fois. Donc $f_n(x)$ ne converge en aucun point.
- Conformément au théorème, on peut extraire une sous-suite convergente presque partout : il suffit de prendre par exemple la sous-suite $g_k = f_{\frac{k(k-1)}{2}} = \mathbf{1}_{[0, 1/k]}$. Pour $x \in ]0, 1]$, $g_k(x) = 0$ dès que $k > 1/x$, donc $g_k \to 0$ ponctuellement sur $]0, 1]$, soit Lebesgue-presque partout sur $[0,1]$.

## 3. Démonstrations

### Preuve du Théorème de Riesz-Fischer pour $1 \le p < +\infty$

La preuve repose sur un critère classique de complétude : un espace vectoriel normé est complet si et seulement si toute série absolument convergente est convergente.

Soit $(u_n)_{n \in \mathbb{N}}$ une suite d'éléments de $L^p(X, \mu)$ telle que la série $\sum u_n$ est absolument convergente, c'est-à-dire :
$$ M = \sum_{n=0}^{+\infty} \|u_n\|_p < +\infty $$

**Étape 1 : Construction d'une fonction limite majorante**
Pour chaque entier $N$, posons :
$$ S_N = \sum_{n=0}^N |u_n| $$
Les fonctions $S_N$ sont mesurables et positives. Par l'inégalité de Minkowski, on a :
$$ \|S_N\|_p = \left\| \sum_{n=0}^N |u_n| \right\|_p \le \sum_{n=0}^N \|u_n\|_p \le M $$
La suite de fonctions $(S_N)_{N \in \mathbb{N}}$ est croissante (car $|u_{N+1}| \ge 0$). On peut donc définir la limite ponctuelle (pouvant prendre la valeur $+\infty$) :
$$ S(x) = \lim_{N \to +\infty} S_N(x) = \sum_{n=0}^{+\infty} |u_n(x)| $$
D'après le théorème de convergence monotone (Beppo-Levi), appliqué à la suite $(S_N^p)_{N \in \mathbb{N}}$ qui croît vers $S^p$ :
$$ \int_X S^p \, d\mu = \lim_{N \to +\infty} \int_X S_N^p \, d\mu = \lim_{N \to +\infty} \|S_N\|_p^p \le M^p < +\infty $$
Ainsi, $S \in L^p$. Une conséquence immédiate est que la fonction $S$ est finie $\mu$-presque partout. En d'autres termes, pour $\mu$-presque tout $x \in X$, la série numérique $\sum |u_n(x)|$ converge.

**Étape 2 : Définition de la fonction limite de la série**
Puisque la série numérique converge absolument pour presque tout $x$, elle converge simplement pour presque tout $x$. On peut donc définir $\mu$-presque partout :
$$ f(x) = \sum_{n=0}^{+\infty} u_n(x) $$
On pose $f(x) = 0$ sur l'ensemble de mesure nulle où la série diverge. La fonction $f$ est mesurable comme limite presque partout de fonctions mesurables.
De plus, $|f(x)| \le S(x)$ presque partout. Puisque $S \in L^p$, on en déduit que $f \in L^p$.

**Étape 3 : Preuve de la convergence en norme $L^p$**
Il reste à montrer que la suite des sommes partielles $f_N = \sum_{n=0}^N u_n$ converge vers $f$ dans $L^p$.
Pour presque tout $x \in X$, $f_N(x) \to f(x)$ par définition. Donc $|f_N(x) - f(x)|^p \to 0$ presque partout.
De plus, on a la majoration :
$$ |f_N(x) - f(x)|^p = \left| \sum_{n=N+1}^{+\infty} u_n(x) \right|^p \le \left( \sum_{n=N+1}^{+\infty} |u_n(x)| \right)^p \le S(x)^p $$
Puisque $S^p$ est une fonction $\mu$-intégrable (indépendante de $N$) qui majore $|f_N - f|^p$, nous pouvons appliquer le théorème de convergence dominée de Lebesgue :
$$ \lim_{N \to +\infty} \int_X |f_N - f|^p \, d\mu = \int_X \lim_{N \to +\infty} |f_N - f|^p \, d\mu = 0 $$
Autrement dit, $\lim_{N \to +\infty} \|f_N - f\|_p = 0$. La série $\sum u_n$ converge donc vers $f$ dans $L^p$.
Ceci prouve que l'espace $L^p$ est complet. $\blacksquare$

### Preuve pour $p = +\infty$

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $L^\infty(X, \mu)$.
Par définition, pour tout $k \ge 1$, il existe $N_k$ tel que pour tous $n, m \ge N_k$, $\|f_n - f_m\|_\infty \le 1/k$.
Soit $A_{n,m,k} = \{x \in X \mid |f_n(x) - f_m(x)| > 1/k\}$. Par définition de la norme essentielle supremum, $\mu(A_{n,m,k}) = 0$.
Posons $A = \bigcup_{k \ge 1} \bigcup_{n, m \ge N_k} A_{n,m,k}$. Comme union dénombrable d'ensembles de mesure nulle, $A$ est de mesure nulle, soit $\mu(A) = 0$.
Pour tout $x \notin A$, et pour tout $k \ge 1$, on a $|f_n(x) - f_m(x)| \le 1/k$ dès que $n, m \ge N_k$. Ainsi, pour tout $x \notin A$, la suite numérique $(f_n(x))_{n \in \mathbb{N}}$ est de Cauchy dans $\mathbb{R}$ (ou $\mathbb{C}$), qui est complet.
On définit $f(x) = \lim_{n \to +\infty} f_n(x)$ pour $x \notin A$, et $f(x) = 0$ sur $A$.
Il est facile de vérifier que $f \in L^\infty$ et que $\|f_n - f\|_\infty \to 0$. $\blacksquare$

## 4. Applications en Physique, Logique & Intelligence Artificielle

### Fondements Mathématiques du Deep Learning

La complétude des espaces $L^p$ (et particulièrement de l'espace de Hilbert $L^2$) est une propriété silencieuse mais absolument fondamentale pour garantir le comportement asymptotique des algorithmes d'apprentissage automatique.

1. **Minimisation du Risque et Théorème de Représentation**
Dans l'apprentissage supervisé, on cherche une fonction de décision $f$ minimisant un risque empirique ou espéré. L'espace des fonctions admissibles est souvent un espace $L^2(P)$ ou un sous-espace dense (comme un RKHS). Si l'espace n'était pas complet, une suite de modèles dont l'erreur d'entraînement diminue (et forme une suite de Cauchy) pourrait "converger" vers un "trou" : c'est-à-dire un état limite inatteignable par aucune fonction mesurable. La complétude assure que le minimiseur limite existe bel et bien mathématiquement.

2. **Équations aux Dérivées Partielles et Espaces de Sobolev**
De nombreuses méthodes d'IA générative modernes, comme les *Diffusion Models* (Score-Based Generative Modeling), s'appuient sur des processus stochastiques décrits par des EDP de Fokker-Planck. La théorie de l'existence et de l'unicité des solutions faibles de ces EDP repose sur les espaces de Sobolev, qui sont construits par complétion des espaces de fonctions régulières pour des normes de type $L^p$ (impliquant la fonction et ses dérivées faibles). La complétude de $L^p$ (Riesz-Fischer) est le pilier fondateur qui permet de construire ces espaces de Sobolev et de prouver que les flots génératifs sont bien définis.

3. **Théorie Ergodique et MDP**
Dans l'apprentissage par renforcement, l'opérateur de Bellman agit sur un espace de fonctions de valeur (souvent $L^\infty$ ou $L^p$ selon la pondération). Le théorème du point fixe de Banach, qui garantit que l'itération de la valeur converge vers la fonction de valeur optimale $V^*$, requiert de manière non négociable que l'espace sous-jacent soit complet. Sans le théorème de Riesz-Fischer, il n'y aurait aucune garantie théorique que l'algorithme Q-Learning converge vers une solution valide dans des espaces d'états continus.
