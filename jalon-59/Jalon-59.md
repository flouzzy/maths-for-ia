---
uuid: "jalon-59"
title: "Topologie des espaces de fonctions et Arzelà-Ascoli"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 58 (Théorème de Baire).md]]"
next: "[[Jalon 60 (Livrable IA).md]]"
---
# Topologie des espaces de fonctions et Arzelà-Ascoli

## Introduction et genèse du concept

Dans l'étude des espaces fonctionnels, la notion de limite d'une suite de fonctions est fondamentale pour l'approximation et la résolution d'équations différentielles ou intégrales. Historiquement, l'analyse des propriétés de ces suites a mis en évidence que la simple convergence en chaque point (convergence simple) ne suffit pas pour préserver des propriétés analytiques cruciales telles que la continuité, la dérivabilité ou l'intégrabilité limite.

L'exigence d'une convergence globale et simultanée sur tout le domaine a conduit à la formalisation de la convergence uniforme par Weierstrass. Cependant, pour extraire des sous-suites convergentes (ce qui est l'essence de la compacité), une condition supplémentaire est nécessaire : c'est l'équicontinuité. Le théorème d'Arzelà-Ascoli généralise le théorème de Bolzano-Weierstrass (valable en dimension finie) aux espaces de fonctions de dimension infinie, en identifiant précisément les parties relativement compactes.

\begin{tikzpicture}[scale=1.5]
    \draw[->] (-0.5, 0) -- (4, 0) node[right] {$x$};
    \draw[->] (0, -0.5) -- (0, 3) node[above] {$y$};
    \draw[thick, blue] (0, 1) .. controls (1, 2) and (2, 0.5) .. (3, 2.5) node[right] {$f(x)$};
    \draw[dashed, red] (0, 1.2) .. controls (1, 2.2) and (2, 0.7) .. (3, 2.7) node[above right] {$f(x) + \epsilon$};
    \draw[dashed, red] (0, 0.8) .. controls (1, 1.8) and (2, 0.3) .. (3, 2.3) node[below right] {$f(x) - \epsilon$};

    \draw[thick, green!60!black] (0, 0.9) .. controls (1, 2.1) and (1.5, 0.6) .. (3, 2.4) node[right] {$f_n(x)$};

    \node[anchor=north west, text width=6cm] at (4, 2) {Le "tube" de rayon $\epsilon$ illustre la convergence uniforme : à partir d'un certain rang, toute la courbe de $f_n$ reste confinée dans ce tube autour de la limite $f$.};
\end{tikzpicture}

## Définitions, Théorèmes et Exemples Concrets

### Convergence Simple et Convergence Uniforme

Soit $(f_n)_{n \in \mathbb{N}}$ une suite d'applications d'un ensemble $X$ dans un espace métrique $(Y, d)$.

**Définition (Convergence Simple) :**
La suite $(f_n)$ converge simplement vers une fonction $f : X \to Y$ si :
$$ \forall x \in X, \quad \lim_{n \to \infty} d(f_n(x), f(x)) = 0 $$

**Définition (Convergence Uniforme) :**
La suite $(f_n)$ converge uniformément vers une fonction $f : X \to Y$ si :
$$ \lim_{n \to \infty} \left( \sup_{x \in X} d(f_n(x), f(x)) \right) = 0 $$
Autrement dit, $\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in X, d(f_n(x), f(x)) \le \epsilon$.

**Exemples concrets et pathologiques :**
1. **Exemple 1 :** Soit $f_n(x) = \frac{x}{n}$ sur $X = [0, 1]$. Pour tout $x$, $\lim \frac{x}{n} = 0$. De plus, $\sup_{x \in [0,1]} \left| \frac{x}{n} - 0 \right| = \frac{1}{n} \to 0$. La convergence est uniforme vers $f(x)=0$.
2. **Exemple 2 :** Soit $f_n(x) = x^n$ sur $X = [0, 1]$. La limite simple est $f(x) = 0$ pour $x \in [0, 1[$ et $f(1) = 1$. La fonction limite n'est pas continue. Comme les $f_n$ sont continues, la convergence ne peut pas être uniforme (théorème de transfert de continuité). D'ailleurs, $\sup_{x \in [0,1]} |x^n - f(x)| = 1 \not\to 0$.
3. **Exemple 3 (Bosse glissante) :** Soit $f_n(x) = n x e^{-n x^2}$ sur $X = [0, \infty[$. La limite simple est $f(x) = 0$. L'aire sous la courbe $\int_0^\infty f_n(x)dx = \frac{1}{2}$, alors que $\int_0^\infty f(x)dx = 0$. La convergence n'est pas uniforme. En effet, $f_n(1/\sqrt{n}) = \sqrt{n} e^{-1} \to \infty$.
4. **Exemple 4 :** Soit $f_n(x) = \sin(nx)/n$ sur $\mathbb{R}$. La limite simple est $0$. $\sup |\sin(nx)/n| \le 1/n \to 0$. La convergence est uniforme. Notons que $f_n'(x) = \cos(nx)$ ne converge pas en tout point (ex: $x=\pi$). La CVU ne garantit pas la CV de la dérivée.
5. **Exemple 5 :** $f_n(x) = \sum_{k=1}^n \frac{\sin(kx)}{k^2}$. Par le test de Weierstrass, comme $|\frac{\sin(kx)}{k^2}| \le \frac{1}{k^2}$ qui est le terme général d'une série convergente, la suite des sommes partielles converge uniformément sur $\mathbb{R}$.

### Équicontinuité

Soit $X$ et $Y$ deux espaces métriques (de distances $d_X$ et $d_Y$).

**Définition (Équicontinuité) :**
Une famille $\mathcal{F}$ d'applications de $X$ dans $Y$ est dite *équicontinue* au point $a \in X$ si :
$$ \forall \epsilon > 0, \exists \delta > 0, \forall f \in \mathcal{F}, \forall x \in X, \quad d_X(x, a) \le \delta \implies d_Y(f(x), f(a)) \le \epsilon $$
La famille est uniformément équicontinue sur $X$ si le $\delta$ dépend uniquement de $\epsilon$ et non de $a$. L'équicontinuité garantit que les variations des fonctions sont contrôlées de la même manière pour *toute* la famille, empêchant des oscillations arbitrairement rapides.

**Exemples de familles équicontinues :**
6. **Exemple 6 :** Toute famille finie de fonctions continues est uniformément équicontinue sur un compact.
7. **Exemple 7 :** La famille $\mathcal{F} = \{f : [0,1] \to \mathbb{R} \mid f \text{ est } 1\text{-lipschitzienne}\}$ est uniformément équicontinue. En effet, $|f(x)-f(y)| \le |x-y|$. Il suffit de prendre $\delta = \epsilon$.
8. **Exemple 8 (Famille non équicontinue) :** $\mathcal{F} = \{f_n(x) = \sin(nx) \mid n \in \mathbb{N}\}$. En $0$, pour $x_n = \pi/(2n)$, on a $|x_n - 0| \to 0$, mais $|f_n(x_n) - f_n(0)| = 1$. Aucun $\delta$ universel ne fonctionne.
9. **Exemple 9 :** Soit $\mathcal{F}$ l'ensemble des primitives $F(x) = \int_0^x f(t)dt$ pour $f$ continue avec $|f(t)| \le M$. La famille est équicontinue car $M$-lipschitzienne (Théorème des accroissements finis).
10. **Exemple 10 :** La famille $\{x \mapsto x^n \mid n \in \mathbb{N}\}$ n'est pas équicontinue en $1$ sur $[0,1]$, ce qui explique la discontinuité de la limite.

### Le Théorème d'Arzelà-Ascoli

Le théorème caractérise les parties relativement compactes de l'espace des fonctions continues munies de la norme de la convergence uniforme.

**Théorème (Arzelà-Ascoli) :**
Soit $K$ un espace métrique compact et $(E, d_E)$ un espace métrique. Munissons $\mathcal{C}(K, E)$ de la distance uniforme $d_\infty(f, g) = \sup_{x \in K} d_E(f(x), g(x))$.
Une partie $\mathcal{F} \subset \mathcal{C}(K, E)$ est relativement compacte si et seulement si :
1. $\mathcal{F}$ est équicontinue sur $K$.
2. Pour tout $x \in K$, l'ensemble ponctuel $\mathcal{F}(x) = \{f(x) \mid f \in \mathcal{F}\}$ est relativement compact dans $E$.

Si $E = \mathbb{R}$ ou $\mathbb{C}$, la condition 2 équivaut à la bornitude ponctuelle de la famille (théorème de Bolzano-Weierstrass).

## Démonstrations

### Démonstration de la préservation de la continuité par convergence uniforme

**Théorème :** Si $(f_n)$ est une suite de fonctions continues sur $X$ qui converge uniformément vers $f$, alors $f$ est continue sur $X$.

**Preuve pas-à-pas :**
Fixons $a \in X$ et montrons que $f$ est continue en $a$. Soit $\epsilon > 0$.
Nous utilisons l'inégalité triangulaire (méthode dite des "trois $\epsilon$") :
$$ d_Y(f(x), f(a)) \le d_Y(f(x), f_N(x)) + d_Y(f_N(x), f_N(a)) + d_Y(f_N(a), f(a)) $$
1. Puisque $f_n \xrightarrow{\text{CVU}} f$, il existe un rang $N$ tel que pour tout $x \in X$, $d_Y(f_N(x), f(x)) \le \frac{\epsilon}{3}$.
2. Ce rang $N$ étant fixé, la fonction $f_N$ est continue en $a$. Par conséquent, il existe $\delta > 0$ tel que pour tout $x \in X$ avec $d_X(x, a) \le \delta$, on ait $d_Y(f_N(x), f_N(a)) \le \frac{\epsilon}{3}$.
3. Supposons que $d_X(x, a) \le \delta$. Alors :
$$ d_Y(f(x), f(a)) \le \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon $$
La fonction $f$ est donc continue en $a$. Le point $a$ étant quelconque, $f$ est continue sur $X$. $\blacksquare$

### Démonstration de la nécessité de l'équicontinuité (Arzelà-Ascoli direct)

Supposons que $\mathcal{F}$ est précompacte (donc totalement bornée) dans $\mathcal{C}(K, E)$. Montrons que $\mathcal{F}$ est équicontinue.
Soit $\epsilon > 0$. Comme $\mathcal{F}$ est totalement bornée, il existe un nombre fini de fonctions $g_1, \dots, g_p \in \mathcal{F}$ telles que des boules de rayon $\epsilon/3$ centrées en ces $g_i$ recouvrent $\mathcal{F}$.
Les $g_i$ sont en nombre fini et sont continues sur le compact $K$, donc elles sont uniformément continues. Il existe donc $\delta > 0$ tel que pour tout $x, y \in K$ avec $d_K(x,y) \le \delta$, et pour tout $i \in \{1,\dots,p\}$, on a $d_E(g_i(x), g_i(y)) \le \epsilon/3$.
Maintenant, prenons $f \in \mathcal{F}$ quelconque. Il existe $g_k$ telle que $d_\infty(f, g_k) \le \epsilon/3$.
Pour tout $x, y \in K$ avec $d_K(x, y) \le \delta$, évaluons :
$$ d_E(f(x), f(y)) \le d_E(f(x), g_k(x)) + d_E(g_k(x), g_k(y)) + d_E(g_k(y), f(y)) $$
$$ d_E(f(x), f(y)) \le \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon $$
Comme ce $\delta$ ne dépend ni de $f$, ni de $x$, ni de $y$, la famille $\mathcal{F}$ est uniformément équicontinue. $\blacksquare$

## Applications en Physique, Logique et Intelligence Artificielle

En apprentissage statistique et en Deep Learning, les modèles cherchés (par exemple un réseau de neurones) appartiennent à un espace de fonctions. L'étude de la convergence de l'algorithme d'apprentissage repose sur la compacité de l'espace de recherche.

1. **Régularisation et Lipschitz-continuité :** Les réseaux antagonistes génératifs (GANs), particulièrement les Wasserstein GANs, requièrent que le "discriminateur" soit 1-Lipschitzien. L'ensemble des fonctions 1-Lipschitziennes bornées sur un domaine compact est un ensemble compact pour la norme uniforme (conséquence directe d'Arzelà-Ascoli). Cela garantit la stabilité de l'entraînement et limite les fortes variations du gradient (gradient penalty).
2. **Bornes de généralisation Rademacher :** La théorie de l'apprentissage PAC (Probably Approximately Correct) évalue la capacité d'une classe de fonctions $\mathcal{H}$ à généraliser sur des données invisibles. La compacité de $\mathcal{H}$ (prouvable via Arzelà-Ascoli) est indispensable pour calculer l'entropie métrique et borner l'erreur de généralisation via des arguments d'uniforme continuité.
3. **Optimisation Fonctionnelle et Réseaux Infinis (NTK) :** Pour les réseaux de neurones de largeur tendant vers l'infini, la dynamique d'apprentissage par descente de gradient peut être modélisée en espace continu. L'équicontinuité des trajectoires fonctionnelles assure, via Arzelà-Ascoli, qu'il existe une limite déterministe au processus, souvent liée à un Noyau Tangent Neural (NTK).
