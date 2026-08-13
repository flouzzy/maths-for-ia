---
uuid: "jalon-59"
title: "Topologie des espaces de fonctions, convergence compacte et théorème d'Arzelà-Ascoli"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/abstraction
prev: "[[jalon-58/Jalon-58.md]]"
next: "[[jalon-60/Jalon-60.md]]"
---

# Jalon 59 : Topologie des espaces de fonctions, convergence compacte et théorème d'Arzelà-Ascoli

## 1. Genèse et Intuition Géométrique

Historiquement, l'analyse mathématique a commencé par l'étude de points dans des espaces euclidiens comme $\mathbb{R}^n$. Cependant, avec l'émergence du calcul des variations (Euler, Lagrange) et de la résolution d'équations aux dérivées partielles (Cauchy, Dirichlet), une impasse computationnelle et géométrique majeure est apparue : comment mesurer la distance ou la proximité, non plus entre deux points, mais entre deux *fonctions* ?

Lorsque nous cherchons la solution d'une équation différentielle sous la forme d'une limite de fonctions approximatives (comme dans la méthode des itérations de Picard), nous manipulons une suite dont chaque terme est lui-même une courbe entière. La topologie des espaces de fonctions est née de cette nécessité physique : définir rigoureusement ce que signifie pour une courbe "d'approcher" une autre courbe.

Giulio Ascoli (1883) et Cesare Arzelà (1889) ont posé les fondations pour comprendre la compacité dans ces espaces infini-dimensionnels. Le problème fondamental est que, contrairement à $\mathbb{R}^n$, être fermé et borné ne suffit plus pour garantir qu'une suite de fonctions possède une sous-suite convergente. Il faut que ces fonctions ne "gigent" pas trop sauvagement. C'est l'essence même de l'équicontinuité.

## 2. Définitions et Structures Fondamentales

### A. Modes de convergence d'une suite de fonctions

Soit $X$ un ensemble quelconque et $(Y, d)$ un espace métrique. Considérons une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ de $X$ dans $Y$.

> **Définition 1 : Convergence Simple (CVS)**
> La suite $(f_n)_{n \in \mathbb{N}}$ converge **simplement** vers une fonction $f : X \to Y$ si, pour chaque point $x \in X$ fixé :
> $$\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, d(f_n(x), f(x)) < \epsilon$$

**Exemple concret immédiat :**
Considérons la suite $f_n : [0, 1] \to \mathbb{R}$ définie par $f_n(x) = x^n$.
Fixons $x \in [0, 1[$. Alors $\lim_{n \to \infty} x^n = 0$.
Fixons $x = 1$. Alors $\lim_{n \to \infty} 1^n = 1$.
La limite simple est donc la fonction discontinue $f$ telle que $f(x) = 0$ sur $[0, 1[$ et $f(1) = 1$. La topologie de la convergence simple est trop faible pour préserver les propriétés topologiques comme la continuité.

> **Définition 2 : Convergence Uniforme (CVU)**
> La suite $(f_n)_{n \in \mathbb{N}}$ converge **uniformément** vers $f : X \to Y$ si :
> $$\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in X, d(f_n(x), f(x)) < \epsilon$$
> Autrement dit, $\lim_{n \to \infty} \left( \sup_{x \in X} d(f_n(x), f(x)) \right) = 0$.

**Exemple concret immédiat :**
Considérons $g_n(x) = \frac{\sin(nx)}{n}$ sur $\mathbb{R}$.
On a $\sup_{x \in \mathbb{R}} \left| \frac{\sin(nx)}{n} - 0 \right| = \frac{1}{n}$.
Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, la suite $(g_n)$ converge uniformément vers la fonction nulle sur $\mathbb{R}$. Toute la courbe est enfermée dans un "tube" horizontal de largeur $2/n$ centré sur l'axe des abscisses.

### B. Équicontinuité

> **Définition 3 : Famille Équicontinue**
> Soit $(X, d_X)$ un espace métrique. Une famille $\mathcal{F}$ de fonctions de $X$ dans $Y$ est dite **équicontinue** en un point $x_0 \in X$ si :
> $$\forall \epsilon > 0, \exists \delta > 0, \forall f \in \mathcal{F}, \forall x \in X, d_X(x, x_0) < \delta \implies d_Y(f(x), f(x_0)) < \epsilon$$

Le point crucial ici est l'ordre des quantificateurs : le $\delta$ dépend de $\epsilon$ et de $x_0$, mais est **indépendant** du choix de la fonction $f$ dans la famille $\mathcal{F}$. Toutes les fonctions de la famille ont un module de continuité commun.

**Exemple concret immédiat :**
La famille $\mathcal{F} = \{f \in \mathcal{C}^1([0, 1], \mathbb{R}) \mid \forall x, |f'(x)| \le 5\}$ est uniformément équicontinue. En effet, par l'inégalité des accroissements finis, chaque fonction est $5$-lipschitzienne : $|f(x) - f(y)| \le 5|x - y|$. Pour un $\epsilon > 0$ donné, il suffit de choisir $\delta = \epsilon / 5$. Ce $\delta$ fonctionne pour toutes les infinités de fonctions dans $\mathcal{F}$.

## 3. Théorèmes Fondamentaux et Démonstrations

### A. Théorème de conservation de la continuité

> **Théorème :**
> Si une suite de fonctions continues $(f_n)$ converge uniformément vers une fonction $f$ sur $X$, alors la limite $f$ est continue sur $X$.

**Exemple concret immédiat :**
Soit $f_n(x) = \sum_{k=1}^n \frac{\sin(k^2 x)}{k^2}$. Chaque $f_n$ est une fonction continue (somme finie de fonctions trigonométriques continues).
Puisque $\left|\frac{\sin(k^2 x)}{k^2}\right| \le \frac{1}{k^2}$ et que la série $\sum \frac{1}{k^2}$ converge (série de Riemann avec $\alpha = 2 > 1$), la suite $(f_n)$ converge uniformément (par le critère de Weierstrass pour la convergence normale) sur $\mathbb{R}$ vers la fonction limite $f(x) = \sum_{k=1}^{\infty} \frac{\sin(k^2 x)}{k^2}$. D'après le théorème de conservation de la continuité, nous pouvons affirmer rigoureusement, sans le moindre calcul de limite explicite, que cette fonction limite $f(x)$ est partout continue sur $\mathbb{R}$.

**Démonstration pas à pas :**
Soit $a \in X$. Montrons que $f$ est continue en $a$. Soit $\epsilon > 0$.
Nous allons utiliser une technique classique de majoration par l'inégalité triangulaire (souvent appelée "technique des $3 \epsilon$").
Écrivons :
$$ d_Y(f(x), f(a)) \le d_Y(f(x), f_n(x)) + d_Y(f_n(x), f_n(a)) + d_Y(f_n(a), f(a)) $$
Par définition de la convergence uniforme, il existe un entier $N \in \mathbb{N}$ tel que pour tout $n \ge N$ et pour tout $t \in X$, $d_Y(f_n(t), f(t)) < \frac{\epsilon}{3}$.
Fixons l'indice $n = N$. La fonction $f_N$ est continue en $a$. Par conséquent, il existe $\delta > 0$ tel que pour tout $x \in X$ vérifiant $d_X(x, a) < \delta$, on ait :
$$ d_Y(f_N(x), f_N(a)) < \frac{\epsilon}{3} $$
En sommant ces termes pour $n = N$ et pour $d_X(x, a) < \delta$ :
$$ d_Y(f(x), f(a)) < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon $$
La fonction $f$ est donc continue en $a$. Puisque cela est vrai pour tout $a \in X$, $f$ est continue sur $X$.

### B. Le Théorème d'Arzelà-Ascoli

> **Théorème (Arzelà-Ascoli) :**
> Soit $K$ un espace métrique compact et $E$ un espace de Banach. On munit l'espace $\mathcal{C}(K, E)$ de la norme de la convergence uniforme $\|\cdot\|_\infty$.
> Une partie $\mathcal{F} \subset \mathcal{C}(K, E)$ est relativement compacte (c'est-à-dire que de toute suite de $\mathcal{F}$, on peut extraire une sous-suite uniformément convergente) si et seulement si les deux conditions suivantes sont vérifiées :
> 1. $\mathcal{F}$ est **équicontinue**.
> 2. Pour tout $x \in K$, l'ensemble $\{ f(x) \mid f \in \mathcal{F} \}$ est relativement compact dans $E$.

**Exemple concret immédiat :**
Si $K = [0, 1]$ et $E = \mathbb{R}$, considérons la famille $\mathcal{F} = \{ f_n(x) = \sin(nx) \mid n \in \mathbb{N} \}$.
Évaluée en $x=0$, $f_n(0) = 0$, donc ponctuellement bornée.
Cependant, la dérivée est $f_n'(x) = n \cos(nx)$, qui n'est pas uniformément bornée. La famille n'est **pas** équicontinue.
En effet, on ne peut extraire aucune sous-suite uniformément convergente de $\sin(nx)$, ce qui illustre la nécessité de l'équicontinuité.
Si nous prenons plutôt $\mathcal{G} = \{ g(x) = c \sin(x) \mid c \in [-1, 1] \}$, on a $|g'(x)| = |c \cos(x)| \le 1$. La famille est 1-lipschitzienne (donc équicontinue) et $\{g(x)\}$ est inclus dans $[-1, 1]$ pour tout $x$. D'après le théorème, de toute suite de $\mathcal{G}$, on peut extraire une sous-suite qui converge uniformément, ce qui est évident car la suite des paramètres $c_n \in [-1, 1]$ admettra une sous-suite convergente $c_{\phi(n)} \to c^*$, et $c_{\phi(n)} \sin(x)$ convergera uniformément vers $c^* \sin(x)$.

**Démonstration rigoureuse de la condition suffisante :**
La preuve repose sur l'argument diagonal de Cantor. Soit $(f_n)_{n\in\mathbb{N}}$ une suite d'éléments de $\mathcal{F}$.

1. **Extraction diagonale sur un ensemble dense :**
Puisque $K$ est compact, il est séparable, donc il contient une partie dénombrable dense $D = \{x_1, x_2, \dots\}$.
Évaluons la suite en $x_1$. La suite $(f_n(x_1))$ prend ses valeurs dans l'ensemble $\{f(x_1) \mid f \in \mathcal{F}\}$, qui est relativement compact dans $E$.
D'après le théorème de Bolzano-Weierstrass, il existe une extractrice $\phi_1 : \mathbb{N} \to \mathbb{N}$ telle que la sous-suite $(f_{\phi_1(n)}(x_1))$ converge dans $E$.
Considérons ensuite le point $x_2$. La suite $(f_{\phi_1(n)}(x_2))$ prend ses valeurs dans l'ensemble relativement compact $\{f(x_2) \mid f \in \mathcal{F}\}$. Il existe donc une nouvelle extractrice $\phi_2$ telle que $(f_{\phi_1(\phi_2(n))}(x_2))$ converge, et notons que cette extraction préserve la convergence en $x_1$.
En procédant par récurrence, on construit une suite d'extractrices $(\phi_k)_{k\in\mathbb{N}}$ telle que pour chaque $k$, la suite $n \mapsto f_{\phi_1 \circ \dots \circ \phi_k(n)}$ converge aux points $x_1, \dots, x_k$.
On définit alors l'extraction diagonale $\psi(n) = \phi_1 \circ \dots \circ \phi_n(n)$.
La suite diagonale $g_n = f_{\psi(n)}$ est une sous-suite, et pour tout $x_i \in D$, la suite $(g_n(x_i))_{n \ge i}$ est extraite d'une suite convergente, donc elle converge. La suite $(g_n)$ converge ponctuellement sur tout l'ensemble $D$.

2. **Extension à la convergence uniforme par équicontinuité :**
Soit $\epsilon > 0$.
L'hypothèse d'équicontinuité pour $\mathcal{F}$ stipule qu'il existe $\delta > 0$ tel que :
$$\forall f \in \mathcal{F}, \forall x, y \in K, \quad d_K(x, y) < \delta \implies \|f(x) - f(y)\|_E < \frac{\epsilon}{3}$$
Puisque $D$ est dense dans $K$, les boules ouvertes $B(x_i, \delta)$ pour $x_i \in D$ recouvrent $K$.
Comme $K$ est compact, on peut extraire un sous-recouvrement fini. Il existe donc un entier $p$ tel que $K \subset \bigcup_{i=1}^p B(x_i, \delta)$.
La suite $(g_n)$ converge ponctuellement sur $D$, donc en particulier aux points $x_1, \dots, x_p$.
Puisqu'il y a un nombre fini de points, il existe un rang $N$ tel que pour tous $m, n \ge N$, et pour tout $i \in \{1, \dots, p\}$ :
$$\|g_n(x_i) - g_m(x_i)\|_E < \frac{\epsilon}{3}$$
Soit maintenant $x \in K$ un point quelconque. Il existe un point $x_i$ parmi les $p$ points choisis tel que $d_K(x, x_i) < \delta$.
Par l'inégalité triangulaire, pour $m, n \ge N$ :
$$\|g_n(x) - g_m(x)\|_E \le \|g_n(x) - g_n(x_i)\|_E + \|g_n(x_i) - g_m(x_i)\|_E + \|g_m(x_i) - g_m(x)\|_E$$
Puisque $g_n$ et $g_m$ appartiennent à $\mathcal{F}$, l'équicontinuité implique que $\|g_n(x) - g_n(x_i)\|_E < \frac{\epsilon}{3}$ et $\|g_m(x) - g_m(x_i)\|_E < \frac{\epsilon}{3}$.
Le terme central est strictement inférieur à $\frac{\epsilon}{3}$ d'après le choix de $N$.
Ainsi :
$$\|g_n(x) - g_m(x)\|_E < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon$$
Cette majoration est vraie pour tout $x \in K$, de manière indépendante de $x$.
On a donc montré que :
$$\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall m, n \ge N, \sup_{x \in K} \|g_n(x) - g_m(x)\|_E < \epsilon$$
La suite $(g_n)$ est donc une suite de Cauchy pour la norme uniforme sur l'espace de Banach $E$. Puisque $E$ est complet, $\mathcal{C}(K, E)$ muni de la norme infinie est un espace de Banach. Par conséquent, la suite $(g_n)$ converge uniformément sur $K$. Cela conclut la preuve que $\mathcal{F}$ est relativement compacte.

## 4. Applications en Intelligence Artificielle et Théorie de l'Apprentissage

Le théorème d'Arzelà-Ascoli n'est pas qu'une abstraction topologique ; c'est le moteur mathématique garantissant que l'apprentissage automatique est possible.

Dans le paradigme PAC (Probably Approximately Correct) de l'apprentissage statistique, on cherche une fonction cible dans un espace d'hypothèses $\mathcal{H}$. Si cet espace est trop vaste (trop "souple"), le modèle sur-apprendra (overfitting) et l'erreur de généralisation explosera.

**Exemple d'Application : Contrainte Lipschitzienne dans les WGANs (Wasserstein GANs)**
Dans l'architecture WGAN, le réseau critique (ou discriminateur) cherche à estimer la distance de Wasserstein entre la distribution réelle des données et la distribution générée. Pour que cette estimation soit mathématiquement valide et stable, le discriminateur *doit* appartenir à l'espace des fonctions $1$-lipschitziennes.
Grâce à Arzelà-Ascoli, nous savons que l'ensemble des fonctions $1$-lipschitziennes bornées sur un domaine compact forme un espace relativement compact. Cette compacité fondamentale dans l'espace fonctionnel est ce qui assure que l'algorithme d'optimisation (Descente de Gradient) ne divergera pas vers une fonction pathologique, mais convergera bien vers un discriminateur optimal. La topologie régit ainsi directement la géométrie de la fonction de perte dans les architectures profondes.
