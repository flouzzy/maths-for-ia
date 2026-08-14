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

# Jalon 59 : Topologie des espaces de fonctions et Arzelà-Ascoli

## 1. Origines et Nécessité Géométrique

Historiquement, l'analyse mathématique s'est d'abord concentrée sur l'étude des points et de leurs voisinages au sein d'espaces de dimension finie, typiquement $\mathbb{R}^n$. Cependant, avec l'émergence du calcul des variations (Euler, Lagrange) et de la résolution d'équations aux dérivées partielles (Fourier, Cauchy), il est devenu impératif de ne plus considérer les fonctions comme de simples transformations, mais comme les *points* eux-mêmes d'un espace vectoriel de dimension infinie.

L'impasse fondamentale rencontrée à la fin du XIXe siècle par Weierstrass, Dini et Arzelà fut la suivante : dans $\mathbb{R}^n$, le théorème de Bolzano-Weierstrass garantit que toute suite bornée admet une sous-suite convergente (compacité séquentielle). Mais dans un espace de fonctions, par exemple l'espace $\mathcal{C}([a, b])$ des fonctions continues sur le segment $[a, b]$, cette propriété est radicalement fausse. La compacité y est un phénomène rare et subtil.

Si nous regardons une séquence de fonctions $(f_n)_{n\in\mathbb{N}}$, la convergence "point par point" (chaque $f_n(x)$ converge vers $f(x)$ pour un $x$ donné) ne garantit pas que la limite $f$ conserve les propriétés topologiques (comme la continuité) des $f_n$. La courbe limite peut se déchirer. Pour éviter cela, il a fallu introduire une topologie plus rigide : la topologie de la convergence uniforme, gouvernée par la norme du supremum.

Le théorème d'Arzelà-Ascoli (établi par Cesare Arzelà et Giulio Ascoli) répond exactement à cette question : sous quelles conditions un ensemble de fonctions est-il "assez compact" pour que toute suite de fonctions de cet ensemble possède une sous-suite convergeant *uniformément* ? Ce résultat est la clé de voûte permettant de prouver l'existence de solutions à de nombreuses équations différentielles (via le théorème de Peano) en garantissant que les approximations successives ne s'éparpillent pas dans le vide de la dimension infinie.

## 2. Définitions, Topologies et Convergence

### A. La Convergence Simple (Ponctuelle)

Soit $X$ un ensemble et $(Y, d)$ un espace métrique. Soit $(f_n)_{n\in\mathbb{N}}$ une suite d'applications de $X$ dans $Y$.

**Définition 1 :** On dit que la suite de fonctions $f_n$ converge **simplement** sur $X$ vers une fonction $f: X \to Y$ si, pour tout $x \in X$, la suite $(f_n(x))_{n\in\mathbb{N}}$ converge vers $f(x)$ dans l'espace $(Y, d)$.
Formellement :
$$ \forall x \in X, \quad \forall \epsilon > 0, \quad \exists N \in \mathbb{N}, \quad \forall n \ge N, \quad d(f_n(x), f(x)) < \epsilon $$

**Exemple Calculatoire Immédiat :**
Considérons $X = [0, 1]$, $Y = \mathbb{R}$ (avec la distance usuelle $d(x, y) = |x - y|$) et $f_n(x) = x^n$.
- Pour $x \in [0, 1[$, $\lim_{n \to \infty} x^n = 0$.
- Pour $x = 1$, $\lim_{n \to \infty} 1^n = 1$.
Ainsi, $(f_n)$ converge simplement vers la fonction limite $f$ définie par $f(x) = 0$ si $x \in [0, 1[$ et $f(1) = 1$.
*Remarque cruciale :* Bien que toutes les $f_n$ soient continues, la limite $f$ présente une discontinuité brutale en $x=1$. La convergence simple ne préserve pas la continuité.

### B. La Convergence Uniforme

**Définition 2 :** On dit que la suite $(f_n)_{n\in\mathbb{N}}$ converge **uniformément** sur $X$ vers $f$ si l'entier $N$ dépend de $\epsilon$ mais *pas* de $x$.
Formellement :
$$ \forall \epsilon > 0, \quad \exists N \in \mathbb{N}, \quad \forall n \ge N, \quad \forall x \in X, \quad d(f_n(x), f(x)) < \epsilon $$
De manière équivalente, en posant $\|f_n - f\|_\infty = \sup_{x \in X} d(f_n(x), f(x))$, la convergence uniforme équivaut à $\lim_{n \to \infty} \|f_n - f\|_\infty = 0$.

**Exemple Calculatoire Immédiat :**
Soit $f_n(x) = \frac{\sin(nx)}{n}$ sur $X = \mathbb{R}$.
La limite simple est $f(x) = 0$.
Étudions la convergence uniforme :
$$ \|f_n - f\|_\infty = \sup_{x \in \mathbb{R}} \left| \frac{\sin(nx)}{n} - 0 \right| \le \frac{1}{n} $$
Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, la convergence est uniforme sur tout $\mathbb{R}$.

### C. L'Équicontinuité

L'équicontinuité est la notion centrale d'Arzelà-Ascoli. Elle traduit le fait qu'une famille entière de fonctions partage un même module de continuité.

**Définition 3 :** Soient $(X, d_X)$ et $(Y, d_Y)$ deux espaces métriques. Une famille $\mathcal{F}$ d'applications de $X$ dans $Y$ est dite **équicontinue** en $a \in X$ si :
$$ \forall \epsilon > 0, \quad \exists \delta > 0, \quad \forall f \in \mathcal{F}, \quad \forall x \in X, \quad d_X(x, a) < \delta \implies d_Y(f(x), f(a)) < \epsilon $$
La famille est uniformément équicontinue sur $X$ si le $\delta$ est indépendant à la fois de $f$ et du point d'évaluation.

**Exemple Calculatoire Immédiat :**
Soit $\mathcal{F} = \{ f : [0, 1] \to \mathbb{R} \mid f \text{ est } K\text{-lipschitzienne} \}$, où $K > 0$ est fixé.
Prenons $f \in \mathcal{F}$, nous avons $|f(x) - f(y)| \le K|x - y|$.
Pour $\epsilon > 0$, il suffit de choisir $\delta = \frac{\epsilon}{K}$. Ce $\delta$ fonctionne pour *toutes* les fonctions de la famille $\mathcal{F}$ simultanément. Ainsi, toute famille de fonctions uniformément Lipschitzienne de même constante est équicontinue.

**Cas limite :** La famille $f_n(x) = \sin(nx)$ sur $[0, 2\pi]$. En $x=0$, $|f_n(x) - f_n(0)| = |\sin(nx)|$. La pente à l'origine est $n$, qui tend vers l'infini. Il est impossible de trouver un $\delta$ commun pour tous les $n$. Cette famille n'est *pas* équicontinue.

## 3. Théorèmes Fondamentaux et Démonstrations

### Théorème 1 : Conservation de la Continuité (Théorème des Limites Uniformes)

**Énoncé :** Soit $(X, d_X)$ un espace métrique et $(Y, d_Y)$ un espace métrique complet. Soit $(f_n)_{n\in\mathbb{N}}$ une suite de fonctions continues de $X$ dans $Y$. Si $(f_n)$ converge uniformément sur $X$ vers une fonction $f$, alors $f$ est continue sur $X$.

**Démonstration Complète :**
Soit $a \in X$. Fixons $\epsilon > 0$.
L'objectif est de trouver un $\delta > 0$ tel que pour tout $x \in X$, $d_X(x, a) < \delta \implies d_Y(f(x), f(a)) < \epsilon$.
Nous utilisons l'inégalité triangulaire (technique dite des "trois $\epsilon$").
$$ d_Y(f(x), f(a)) \le d_Y(f(x), f_N(x)) + d_Y(f_N(x), f_N(a)) + d_Y(f_N(a), f(a)) $$
1. Puisque $(f_n)$ converge uniformément vers $f$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $t \in X$, $d_Y(f_N(t), f(t)) < \frac{\epsilon}{3}$. Ceci gère le premier et le dernier terme.
2. La fonction $f_N$ étant continue en $a$, il existe $\delta > 0$ tel que pour tout $x \in X$, $d_X(x, a) < \delta \implies d_Y(f_N(x), f_N(a)) < \frac{\epsilon}{3}$.
3. En combinant ces éléments pour $d_X(x, a) < \delta$ :
$$ d_Y(f(x), f(a)) < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon $$
La fonction $f$ est donc continue en $a$. Puisque ceci est vrai pour tout $a \in X$, $f$ est continue sur $X$. $\blacksquare$

### Théorème 2 : Théorème d'Arzelà-Ascoli

**Énoncé :** Soit $K$ un espace topologique compact et $(Y, d)$ un espace métrique complet. Soit $\mathcal{F} \subset \mathcal{C}(K, Y)$.
L'ensemble $\mathcal{F}$ est relativement compact (toute suite admet une sous-suite uniformément convergente) si et seulement si les deux conditions suivantes sont satisfaites :
1. $\mathcal{F}$ est **équicontinue** sur $K$.
2. $\mathcal{F}$ est **ponctuellement relativement compacte** : pour tout $x \in K$, l'ensemble $\{f(x) \mid f \in \mathcal{F}\}$ est relativement compact dans $Y$.

*(Si $Y = \mathbb{R}^n$, la condition 2 équivaut simplement à dire que pour tout $x$, $\sup_{f\in\mathcal{F}} \|f(x)\| < \infty$).*

**Esquisse de la Démonstration (Sens direct) :**
Bien que la démonstration complète par procédé diagonal de Cantor soit longue, en voici l'articulation mathématique stricte :
1. $K$ est compact, donc séparable : il admet une partie dénombrable dense $D = \{x_1, x_2, \ldots\}$.
2. Soit $(f_n)$ une suite dans $\mathcal{F}$. La suite des valeurs $(f_n(x_1))$ est bornée dans $\mathbb{R}^n$ (par l'hypothèse 2), donc par Bolzano-Weierstrass, elle admet une sous-suite convergente $f_{\phi_1(n)}(x_1)$.
3. On extrait une sous-suite de cette sous-suite pour faire converger l'évaluation en $x_2$, puis en $x_3$, etc. On utilise l'extraction diagonale $g_n = f_{\phi_n(n)}$. La suite $(g_n)$ converge simplement sur $D$.
4. L'équicontinuité (hypothèse 1) permet ensuite "d'étendre" cette convergence simple sur la partie dense $D$ en une convergence uniforme sur tout le compact $K$, l'écart entre $x \in K$ et son approximation dans $D$ étant contrôlé uniformément via l'équicontinuité. $\blacksquare$

## 4. Applications en Théorie de l'Apprentissage (IA) et Physique

**Réseaux de neurones et Théorie de l'Approximation (Neural Tangent Kernel) :**
En intelligence artificielle, lors de l'étude théorique des réseaux de neurones profonds (Deep Learning) dans le régime de la largeur infinie (NTK - Neural Tangent Kernel), on démontre que la trajectoire des poids de la descente de gradient converge vers un équilibre. Le théorème d'Arzelà-Ascoli intervient pour assurer que la famille des trajectoires temporelles des sorties du réseau est relativement compacte. Cela permet d'extraire une limite temporelle continue, garantissant que l'entraînement du réseau est bien posé et ne diverge pas chaotiquement.

**Régularisation de Lipschitz et WGAN :**
Les réseaux génératifs antagonistes basés sur la distance de Wasserstein (WGAN) nécessitent que le discriminateur appartienne à une classe de fonctions 1-lipschitziennes. Comme nous l'avons calculé dans l'exemple, les fonctions $K$-lipschitziennes bornées sur un compact forment une famille équicontinue et bornée ponctuellement. Par Arzelà-Ascoli, ce sous-espace de fonctions est compact. En optimisation, cela assure l'existence d'un maximum global pour le problème dual de Kantorovitch : la fonction de perte du discriminateur ne peut pas tendre vers des infinis dégénérés.

**Calcul des Variations (Principe de moindre action) :**
En physique théorique, pour trouver la trajectoire minimisant l'action (par exemple, la courbure d'une surface de savon, ou la géodésique en relativité générale), on considère une suite de fonctions minimisantes. L'énergie bornée de ces fonctions implique souvent une borne sur leurs dérivées (par l'inégalité de Poincaré), ce qui garantit leur équicontinuité. Arzelà-Ascoli permet d'extraire la limite de cette suite, qui sera la trajectoire physique réelle adoptée par le système.
