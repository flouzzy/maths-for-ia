---
uuid: "jalon-34"
title: "Topologie élémentaire des espaces vectoriels normés"
year: 1
trimester: 3
tags:
  - math/analyse
  - ia/regularisation
prev: "[[Jalon 33 (Formes quadratiques).md]]"
next: "[[Jalon 35 (Caractérisation séquentielle des ouverts).md]]"
---
# Jalon 34 : Topologie élémentaire des espaces vectoriels normés

## 1. L'Échafaudage Cognitif & Traçabilité Historique

### Genèse et Motivation
La notion de distance est fondamentale en mathématiques. Historiquement, la géométrie euclidienne reposait sur une notion de distance intuitive, issue du théorème de Pythagore, qui mesure la longueur du segment de droite reliant deux points. Cependant, avec le développement de l'analyse fonctionnelle à la fin du XIXe siècle et au début du XXe siècle, sous l'impulsion de mathématiciens comme Maurice Fréchet, Stefan Banach, et David Hilbert, il est apparu nécessaire de mesurer des "distances" non plus seulement entre des points d'un espace de dimension finie, mais entre des fonctions, des suites, ou des objets plus abstraits.

Cette abstraction a conduit à la formalisation du concept de "norme". Une norme généralise la notion de longueur d'un vecteur. L'impasse intellectuelle résidait dans l'incapacité de l'analyse classique à traiter la convergence de suites de fonctions (par exemple, la convergence uniforme de séries de Fourier) de la même manière que la convergence de suites réelles. Il fallait une structure algébrique et topologique unifiée : l'espace vectoriel normé.

La métaphore du chauffeur de taxi à Manhattan est célèbre pour illustrer la flexibilité de la distance. Dans une grille de rues perpendiculaires, la "ligne droite" n'est pas un chemin possible. La distance parcourue par le taxi est la somme des distances horizontales et verticales (la norme $L^1$). Ce simple changement de règle du jeu modifie radicalement la géométrie : la "boule unité", c'est-à-dire l'ensemble des points à distance 1 de l'origine, n'est plus un cercle rond, mais un losange. Comprendre cette flexibilité est crucial pour l'apprentissage automatique, où différentes normes (comme $L^1$ pour la sparsité ou $L^2$ pour l'énergie) régularisent différemment les modèles (Lasso vs Ridge).

## 2. Le Protocole d'Exégèse Conceptuelle

### Définition 1 : Norme sur un Espace Vectoriel

**A. Énoncé Symbolique Strict**
Soit $E$ un $\mathbb{K}$-espace vectoriel, où $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$. Une application $N : E \to \mathbb{R}_+$ est appelée une *norme* sur $E$ si et seulement si elle vérifie les trois axiomes suivants :
1. **Séparation :** $\forall x \in E, \; (N(x) = 0 \iff x = 0_E)$
2. **Homogénéité absolue :** $\forall \lambda \in \mathbb{K}, \forall x \in E, \; N(\lambda x) = |\lambda| N(x)$
3. **Inégalité triangulaire :** $\forall x, y \in E, \; N(x + y) \leq N(x) + N(y)$

On note usuellement $N(x) = \|x\|$. Un espace vectoriel muni d'une norme, noté $(E, \|\cdot\|)$, est appelé un *espace vectoriel normé* (EVN).

**B. Anatomie et Typage Chirurgical**
- $E$ désigne un espace vectoriel abstrait sur le corps des scalaires $\mathbb{K}$.
- $N$ (ou $\|\cdot\|$) est une fonction scalaire qui prend un vecteur et renvoie un réel positif ou nul.
- L'axiome de séparation stipule que le seul vecteur de "longueur" nulle est le vecteur nul $0_E$. Sans cette condition (si l'on a seulement $\impliedby$), on parle de *semi-norme*.
- L'homogénéité implique que si on étire un vecteur par un facteur $\lambda$, sa norme est étirée par le module (ou valeur absolue) $|\lambda|$.
- L'inégalité triangulaire traduit le fait géométrique intuitif que le chemin le plus court entre deux points est la ligne droite.

**C. Exemples de Validation**
- *Trivial :* Sur $E = \mathbb{R}$, la valeur absolue $|x|$ est une norme.
- *Complexe :* Sur l'espace $E = \mathcal{C}([a, b], \mathbb{R})$ des fonctions continues de $[a,b]$ dans $\mathbb{R}$, on définit la norme de la convergence uniforme (ou norme infinie) par $\|f\|_\infty = \sup_{x \in [a, b]} |f(x)|$. La séparation est vérifiée car l'intégrale d'une fonction continue positive d'intégrale nulle implique que la fonction est identiquement nulle.

**D. Cas Pathologiques et Contre-exemples**
- Sur $\mathbb{R}^2$, l'application $N(x,y) = \sqrt{|x|} + \sqrt{|y|}$ ne vérifie pas l'homogénéité (à cause de la racine carrée sur le paramètre scalaire sorti). Ce n'est donc pas une norme.
- Sur $\mathbb{R}^2$, $N(x,y) = |x|$ est une *semi-norme* mais pas une norme, car le vecteur $(0, 1)$ n'est pas le vecteur nul mais $N(0,1) = 0$.

### Définition 2 : Distance associée à une norme

**A. Énoncé Symbolique Strict**
Soit $(E, \|\cdot\|)$ un espace vectoriel normé. L'application $d : E \times E \to \mathbb{R}_+$ définie par :
$$d(x, y) = \|x - y\|$$
est la distance induite par la norme $\|\cdot\|$.

**B. Anatomie et Typage Chirurgical**
- $x, y \in E$ sont des vecteurs.
- $d(x, y)$ quantifie "l'éloignement" entre l'extrémité du vecteur $x$ et celle de $y$.
- Cette distance vérifie les axiomes métriques : symétrie $d(x,y)=d(y,x)$, séparation $d(x,y)=0 \iff x=y$, et l'inégalité triangulaire métrique $d(x,z) \leq d(x,y) + d(y,z)$.

**C. Exemples de Validation**
- Si $x = (1, 0)$ et $y = (0, 1)$ dans $\mathbb{R}^2$ avec la norme euclidienne usuelle $\|\cdot\|_2$, la distance est $d_2(x,y) = \sqrt{(1-0)^2 + (0-1)^2} = \sqrt{2}$.

**D. Cas Pathologiques et Contre-exemples**
Toutes les distances sur un espace vectoriel ne proviennent pas d'une norme. Par exemple, la distance discrète $d(x,y) = 1$ si $x \neq y$, $0$ si $x=y$, ne provient d'aucune norme car elle ne satisfait pas l'homogénéité ($d(2x, 2y) \neq 2d(x,y)$ en général).

### Définition 3 : Équivalence des normes

**A. Énoncé Symbolique Strict**
Deux normes $N_1$ et $N_2$ sur un espace vectoriel $E$ sont dites *équivalentes*, et on note $N_1 \sim N_2$, s'il existe deux constantes réelles $\alpha > 0$ et $\beta > 0$ telles que :
$$\forall x \in E, \quad \alpha N_1(x) \leq N_2(x) \leq \beta N_1(x)$$

**B. Anatomie et Typage Chirurgical**
- $N_1, N_2$ sont deux normes distinctes sur le même espace $E$.
- Les scalaires $\alpha, \beta \in \mathbb{R}_+^*$ encadrent le rapport de "taille" entre les deux mesures pour n'importe quel vecteur, indépendamment du vecteur choisi.
- L'équivalence est une relation d'équivalence (réflexive, symétrique, transitive).

**C. Exemples de Validation**
- Sur $\mathbb{R}^n$, les normes classiques sont équivalentes. Soit $x = (x_1, \dots, x_n) \in \mathbb{R}^n$.
  - Norme 1 : $\|x\|_1 = \sum_{i=1}^n |x_i|$
  - Norme 2 : $\|x\|_2 = \sqrt{\sum_{i=1}^n |x_i|^2}$
  - Norme infini : $\|x\|_\infty = \max_{1 \le i \le n} |x_i|$
On a l'encadrement : $\|x\|_\infty \leq \|x\|_2 \leq \sqrt{n} \|x\|_\infty$, montrant que $\|\cdot\|_2 \sim \|\cdot\|_\infty$.

**D. Cas Pathologiques et Contre-exemples**
En dimension infinie, deux normes ne sont pas nécessairement équivalentes. Sur $E = \mathcal{C}([0,1], \mathbb{R})$, la norme $\|f\|_1 = \int_0^1 |f(t)|dt$ n'est pas équivalente à la norme $\|f\|_\infty = \sup_{t \in [0,1]} |f(t)|$. Il n'existe pas de constante $\beta$ telle que $\|f\|_\infty \leq \beta \|f\|_1$ pour toute fonction $f$ (on peut construire une fonction pic d'aire très faible mais de maximum arbitrairement grand).

## 3. Zéro Ellipse dans les Démonstrations

### Théorème : En dimension finie, toutes les normes sont équivalentes.

**Démonstration :**
Soit $E$ un espace vectoriel sur $\mathbb{R}$ de dimension finie $n \ge 1$.
Montrons que toute norme $N$ sur $E$ est équivalente à une norme de référence arbitrairement choisie. Fixons une base de $E$, notée $\mathcal{B} = (e_1, e_2, \dots, e_n)$.
Pour tout vecteur $x \in E$, on peut décomposer de manière unique $x$ dans cette base : $x = \sum_{i=1}^n x_i e_i$, où $(x_1, \dots, x_n) \in \mathbb{R}^n$.
Définissons une norme de référence $N_\infty$ par $N_\infty(x) = \max_{1 \le i \le n} |x_i|$.

Montrons qu'il existe $\alpha > 0$ et $\beta > 0$ tels que $\forall x \in E, \; \alpha N_\infty(x) \leq N(x) \leq \beta N_\infty(x)$.

**Étape 1 : Majoration (trouver $\beta$)**
Soit $x \in E$. D'après l'inégalité triangulaire de la norme $N$ et son homogénéité absolue :
$$N(x) = N\left(\sum_{i=1}^n x_i e_i\right) \leq \sum_{i=1}^n N(x_i e_i) = \sum_{i=1}^n |x_i| N(e_i)$$
Or, par définition de $N_\infty$, $\forall i, \; |x_i| \leq N_\infty(x)$.
Donc, $N(x) \leq \sum_{i=1}^n N_\infty(x) N(e_i) = \left( \sum_{i=1}^n N(e_i) \right) N_\infty(x)$.
Posons $\beta = \sum_{i=1}^n N(e_i)$.
Puisque les vecteurs de base ne sont pas nuls et que $N$ sépare, chaque $N(e_i) > 0$, donc $\beta > 0$.
Ainsi, nous avons établi la majoration $N(x) \leq \beta N_\infty(x)$ pour tout $x \in E$.

**Étape 2 : Continuité de $N$ par rapport à $N_\infty$**
La majoration précédente implique que l'application $N : (E, N_\infty) \to \mathbb{R}$ est lipschitzienne (et donc uniformément continue).
En effet, pour tous $x, y \in E$, la seconde inégalité triangulaire donne $|N(x) - N(y)| \leq N(x - y)$.
Or $N(x - y) \leq \beta N_\infty(x - y)$, d'où $|N(x) - N(y)| \leq \beta N_\infty(x - y)$.

**Étape 3 : Minoration par compacité (trouver $\alpha$)**
Considérons la sphère unité pour la norme de référence $N_\infty$, notée $S = \{ x \in E \mid N_\infty(x) = 1 \}$.
L'ensemble $S$ est borné (par définition) et fermé (car c'est l'image réciproque du singleton fermé $\{1\}$ par l'application continue $N_\infty$).
Dans un espace de dimension finie, d'après le théorème de Borel-Lebesgue, la sphère unité fermée et bornée $S$ est un sous-ensemble compact.
L'application norme $N$, étant continue sur le compact $S$, atteint ses bornes. En particulier, elle atteint son minimum.
Il existe donc $x_0 \in S$ tel que pour tout $x \in S$, $N(x) \ge N(x_0)$.
Posons $\alpha = N(x_0)$.
Puisque $x_0 \in S$, on a $N_\infty(x_0) = 1$, donc $x_0 \neq 0_E$.
Puisque $N$ est une norme, par séparation, $N(x_0) > 0$. Donc $\alpha > 0$.

Soit maintenant un vecteur non nul $x \in E$.
Considérons le vecteur normalisé $y = \frac{x}{N_\infty(x)}$.
Calculons sa norme de référence : $N_\infty(y) = N_\infty\left(\frac{x}{N_\infty(x)}\right) = \frac{1}{N_\infty(x)} N_\infty(x) = 1$.
Donc $y \in S$.
Par définition du minimum $\alpha$ sur $S$, on a $N(y) \ge \alpha$.
Soit $N\left(\frac{x}{N_\infty(x)}\right) \ge \alpha$.
Par homogénéité, $\frac{1}{N_\infty(x)} N(x) \ge \alpha$.
Ce qui donne $N(x) \ge \alpha N_\infty(x)$.
Cette inégalité est trivialement vraie pour $x = 0_E$ (elle donne $0 \ge 0$).
Donc, nous avons trouvé $\alpha > 0$ tel que pour tout $x \in E$, $\alpha N_\infty(x) \leq N(x)$.

**Conclusion :**
Nous avons exhibé $\alpha, \beta > 0$ tels que $\alpha N_\infty \le N \le \beta N_\infty$. Toute norme est équivalente à la norme $N_\infty$, donc par transitivité, toutes les normes en dimension finie sont équivalentes entre elles.
$\blacksquare$
