---
uuid: "jalon-70"
title: "Espaces mesurés produits"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/probabilites
prev: "[[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]"
next: "[[Jalon 71 (Théorèmes de Fubini-Tonelli).md]]"
---

# Espaces mesurés produits

## Introduction

La théorie de la mesure, bâtie pour quantifier les volumes et les longueurs des ensembles de manière rigoureuse, s'est d'abord concentrée sur des espaces simples comme la droite réelle ou des espaces abstraits uniques. Cependant, la physique et les mathématiques nécessitent constamment de travailler en plusieurs dimensions : analyser conjointement la position et la vitesse d'une particule dans l'espace des phases, modéliser la probabilité de survenue de deux événements aléatoires simultanés, ou simplement calculer l'aire d'une surface bidimensionnelle.

C'est ici qu'intervient la notion d'espace produit. Si l'on dispose d'une mesure pour les longueurs (en une dimension), comment construire rigoureusement une mesure pour les surfaces (en deux dimensions) ? L'idée fondamentale, qui remonte aux travaux de Lebesgue, Radon et Fréchet, est de définir la mesure des rectangles (produits d'ensembles mesurables de chaque espace) comme le produit des mesures de leurs côtés. La tribu produit est alors la tribu engendrée par ces rectangles, et la mesure produit est l'extension naturelle (et unique sous certaines conditions) de cette mesure des rectangles à l'ensemble de la tribu produit. Ce processus de construction de la mesure produit est le pilier central qui permettra ensuite d'énoncer les théorèmes d'intégration multiple de Fubini et Tonelli.

## Définitions, Théorèmes et Exemples

### Tribu Produit

Soient $(X_1, \mathcal{F}_1)$ et $(X_2, \mathcal{F}_2)$ deux espaces mesurables.

**Définition (Rectangle mesurable) :**
Un sous-ensemble de $X_1 \times X_2$ est appelé rectangle mesurable s'il est de la forme $A_1 \times A_2$ avec $A_1 \in \mathcal{F}_1$ et $A_2 \in \mathcal{F}_2$.

**Définition (Tribu produit) :**
La tribu produit, notée $\mathcal{F}_1 \otimes \mathcal{F}_2$, est la tribu sur $X_1 \times X_2$ engendrée par la classe de tous les rectangles mesurables. Formellement :
$$ \mathcal{F}_1 \otimes \mathcal{F}_2 = \sigma(\{A_1 \times A_2 \mid A_1 \in \mathcal{F}_1, A_2 \in \mathcal{F}_2\}) $$

**Exemple concret immédiat :**
Considérons l'espace de la droite réelle $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ où $\mathcal{B}(\mathbb{R})$ est la tribu borélienne. La tribu produit $\mathcal{B}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$ sur $\mathbb{R}^2$ est exactement la tribu borélienne de $\mathbb{R}^2$, notée $\mathcal{B}(\mathbb{R}^2)$. Ainsi, le disque unité fermé $D = \{(x,y) \in \mathbb{R}^2 \mid x^2 + y^2 \leq 1\}$ appartient à $\mathcal{B}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$, bien qu'il ne soit pas lui-même un rectangle mesurable. Il s'obtient par des opérations d'union et d'intersection dénombrables à partir de rectangles.

### Sections de parties et de fonctions

**Définition (Section d'un ensemble) :**
Pour tout ensemble $E \subset X_1 \times X_2$ et tout $x_1 \in X_1$, on définit la section en $x_1$ de $E$ par :
$$ E_{x_1} = \{x_2 \in X_2 \mid (x_1, x_2) \in E\} \subset X_2 $$
De même, pour tout $x_2 \in X_2$, la section en $x_2$ est $E^{x_2} = \{x_1 \in X_1 \mid (x_1, x_2) \in E\} \subset X_1$.

**Théorème (Mesurabilité des sections) :**
Si $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$, alors pour tout $x_1 \in X_1$, $E_{x_1} \in \mathcal{F}_2$ et pour tout $x_2 \in X_2$, $E^{x_2} \in \mathcal{F}_1$.

**Exemples concrets immédiats :**
1. Soit le triangle $T = \{(x,y) \in \mathbb{R}^2 \mid 0 \leq x \leq 1, 0 \leq y \leq x\}$ qui est un borélien de $\mathbb{R}^2$. Si l'on fixe $x = 0.5$, la section est $T_{0.5} = \{y \in \mathbb{R} \mid 0 \leq y \leq 0.5\} = [0, 0.5]$, qui est bien un borélien de $\mathbb{R}$. Si l'on fixe $x = 2$, $T_2 = \emptyset$, un borélien.
2. Section d'un cercle unité $C = \{(x,y) \in \mathbb{R}^2 \mid x^2+y^2 \leq 1\}$. Pour $x = 0.5$, $C_{0.5} = \{y \in \mathbb{R} \mid y^2 \leq 0.75\} = [-\frac{\sqrt{3}}{2}, \frac{\sqrt{3}}{2}]$, qui est mesurable.
3. Section du rectangle $R = [0,2] \times [1,4]$. Pour $y = 2$, $R^2 = [0,2]$. Pour $y = 5$, $R^5 = \emptyset$.
4. Section de la diagonale $\Delta = \{(x,x) \mid x \in [0,1]\}$. Pour $x=0.2$, $\Delta_{0.2} = \{0.2\}$, mesurable car un singleton est borélien.
5. Section d'une union $E = ([0,1] \times [0,1]) \cup ([2,3] \times [2,3])$. Pour $x=0.5$, $E_{0.5} = [0,1]$. Pour $x=2.5$, $E_{2.5} = [2,3]$.

### Construction de la Mesure Produit

Soient $(X_1, \mathcal{F}_1, \mu_1)$ et $(X_2, \mathcal{F}_2, \mu_2)$ deux espaces mesurés.

**Théorème de la Mesure Produit :**
Si les espaces $(X_1, \mathcal{F}_1, \mu_1)$ et $(X_2, \mathcal{F}_2, \mu_2)$ sont $\sigma$-finis, il existe une unique mesure $\pi$ sur l'espace mesurable $(X_1 \times X_2, \mathcal{F}_1 \otimes \mathcal{F}_2)$ telle que, pour tout rectangle mesurable $A_1 \times A_2$ :
$$ \pi(A_1 \times A_2) = \mu_1(A_1)\mu_2(A_2) $$
Cette mesure unique $\pi$ est appelée la mesure produit, et est notée $\mu_1 \otimes \mu_2$.

De plus, pour tout ensemble $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$, les fonctions définies par $x_1 \mapsto \mu_2(E_{x_1})$ et $x_2 \mapsto \mu_1(E^{x_2})$ sont mesurables, et on a :
$$ (\mu_1 \otimes \mu_2)(E) = \int_{X_1} \mu_2(E_{x_1}) \, d\mu_1(x_1) = \int_{X_2} \mu_1(E^{x_2}) \, d\mu_2(x_2) $$

**Exemples concrets de mesures produits :**
1. **L'aire euclidienne:** Considérons la mesure de Lebesgue $\lambda$ sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. La mesure produit $\lambda \otimes \lambda$ sur $\mathbb{R}^2$ correspond à l'aire classique. Calculons l'aire du rectangle $R = [0, 2] \times [1, 4]$.
$$ (\lambda \otimes \lambda)(R) = \lambda([0, 2]) \cdot \lambda([1, 4]) = (2 - 0) \cdot (4 - 1) = 2 \cdot 3 = 6 $$
2. **Mesure d'un triangle:** Pour le triangle $T = \{(x,y) \in [0,1]^2 \mid y \leq x\}$, la section à $x$ fixé est $T_x = [0, x]$. La mesure $\lambda(T_x) = x$. L'aire totale est $\int_0^1 \lambda(T_x) \, dx = \int_0^1 x \, dx = \frac{1}{2}$.
3. **Produit de Gaussiennes:** Soit $\gamma_1$ la loi normale standard sur $\mathbb{R}$. La mesure $\gamma_2 = \gamma_1 \otimes \gamma_1$ sur $\mathbb{R}^2$ a pour densité $\frac{1}{2\pi} e^{-(x^2+y^2)/2}$. La mesure du carré $[-1,1]^2$ est $(\gamma_1([-1,1]))^2$.
4. **Mesure discrète et continue:** Sur $\mathbb{R} \times \{0,1\}$, soit $\lambda$ sur $\mathbb{R}$ et $\delta$ la mesure de comptage sur $\{0,1\}$. La mesure produit $\pi = \lambda \otimes \delta$ pour $E = [0,1] \times \{0\}$ vaut $\pi(E) = \lambda([0,1]) \cdot \delta(\{0\}) = 1 \cdot 1 = 1$.
5. **Mesure de comptage 2D:** Si $X_1 = \mathbb{Z}$ et $X_2 = \mathbb{Z}$ avec les mesures de comptage $\mu_1$ et $\mu_2$, la mesure produit est la mesure de comptage sur $\mathbb{Z}^2$. Le nombre de points dans $\{1,2\} \times \{3,4\}$ est $2 \times 2 = 4$.

**Contre-exemple (pathologie sans $\sigma$-finitude) :**
Soit $X_1 = X_2 = [0,1]$ équipés de la tribu borélienne. Prenons $\mu_1 = \lambda$ (mesure de Lebesgue, finie) et $\mu_2$ la mesure de comptage (non $\sigma$-finie, car $[0,1]$ n'est pas réunion dénombrable d'ensembles finis). Considérons la diagonale $\Delta = \{(x,y) \in [0,1]^2 \mid x=y\}$.
Si l'on calcule l'intégrale selon les sections $x$ : $\Delta_x = \{x\}$, de mesure de comptage $\mu_2(\Delta_x) = 1$. L'intégrale donne $\int_0^1 1 \, dx = 1$.
Si l'on calcule l'intégrale selon les sections $y$ : $\Delta^y = \{y\}$, de mesure de Lebesgue $\mu_1(\Delta^y) = 0$. L'intégrale donne $\int_0^1 0 \, d\mu_2(y) = 0$.
L'unicité de la mesure produit et l'égalité des intégrales échouent de façon spectaculaire car l'hypothèse de $\sigma$-finitude sur $\mu_2$ fait défaut.

## Démonstrations

### Démonstration de l'unicité de la mesure produit par le théorème $\pi$-$\lambda$ de Dynkin

L'unicité de la mesure produit sur $\mathcal{F}_1 \otimes \mathcal{F}_2$ reposant sur l'hypothèse de $\sigma$-finitude se démontre rigoureusement en utilisant le théorème $\pi$-$\lambda$ de Dynkin.

**Étape 1 : Le $\pi$-système des rectangles**
Posons $\mathcal{R} = \{ A_1 \times A_2 \mid A_1 \in \mathcal{F}_1, A_2 \in \mathcal{F}_2 \}$.
$\mathcal{R}$ est stable par intersection finie car :
$$ (A_1 \times A_2) \cap (B_1 \times B_2) = (A_1 \cap B_1) \times (A_2 \cap B_2) $$
Comme les intersections $A_1 \cap B_1$ et $A_2 \cap B_2$ sont dans $\mathcal{F}_1$ et $\mathcal{F}_2$ respectivement, $\mathcal{R}$ est bien un $\pi$-système. Par définition, la tribu engendrée $\sigma(\mathcal{R})$ est $\mathcal{F}_1 \otimes \mathcal{F}_2$.

**Étape 2 : Le cas fini**
Supposons dans un premier temps que $\mu_1(X_1) < \infty$ et $\mu_2(X_2) < \infty$.
Soient $\pi_1$ et $\pi_2$ deux mesures sur $\mathcal{F}_1 \otimes \mathcal{F}_2$ telles que pour tout $R = A_1 \times A_2 \in \mathcal{R}$, $\pi_1(R) = \pi_2(R) = \mu_1(A_1)\mu_2(A_2)$.
Posons $\mathcal{L} = \{ E \in \mathcal{F}_1 \otimes \mathcal{F}_2 \mid \pi_1(E) = \pi_2(E) \}$.
Montrons que $\mathcal{L}$ est un système de Dynkin (ou $\lambda$-système) :
1. L'espace total $X_1 \times X_2 \in \mathcal{R} \subset \mathcal{L}$.
2. Stabilité par complémentaire : Si $E \in \mathcal{L}$, alors $\pi_1(E^c) = \pi_1(X_1 \times X_2) - \pi_1(E) = \mu_1(X_1)\mu_2(X_2) - \pi_1(E)$. Puisque $\pi_1(E) = \pi_2(E)$ et les mesures sont finies (donc $\pi_1(E) < \infty$), on déduit que $\pi_1(E^c) = \pi_2(E^c)$, d'où $E^c \in \mathcal{L}$.
3. Stabilité par union dénombrable disjointe : Si $(E_n)_{n \in \mathbb{N}}$ est une suite d'ensembles de $\mathcal{L}$ disjoints deux à deux, alors par $\sigma$-additivité, $\pi_1\left(\bigcup_{n} E_n\right) = \sum_{n} \pi_1(E_n) = \sum_{n} \pi_2(E_n) = \pi_2\left(\bigcup_{n} E_n\right)$, donc $\bigcup_{n} E_n \in \mathcal{L}$.

Puisque $\mathcal{L}$ est un $\lambda$-système contenant le $\pi$-système $\mathcal{R}$, le théorème $\pi$-$\lambda$ de Dynkin garantit que $\sigma(\mathcal{R}) \subset \mathcal{L}$. Autrement dit, $\mathcal{F}_1 \otimes \mathcal{F}_2 = \mathcal{L}$, ce qui signifie que $\pi_1 = \pi_2$ sur l'ensemble de la tribu produit.

**Étape 3 : Extension aux espaces $\sigma$-finis**
Si les espaces sont $\sigma$-finis, il existe des suites d'ensembles croissantes $(X_{1,n})_{n}$ et $(X_{2,n})_{n}$ tels que $\mu_1(X_{1,n}) < \infty$, $\mu_2(X_{2,n}) < \infty$ et $\bigcup_n X_{1,n} = X_1$, $\bigcup_n X_{2,n} = X_2$.
Pour chaque entier $n$, l'ensemble $Y_n = X_{1,n} \times X_{2,n}$ est un rectangle de mesure finie. On définit sur $\mathcal{F}_1 \otimes \mathcal{F}_2$ la mesure restreinte $\pi_i^{(n)}(E) = \pi_i(E \cap Y_n)$ pour $i \in \{1,2\}$.
On applique le résultat de l'étape 2 : on obtient que pour tout $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$, $\pi_1^{(n)}(E) = \pi_2^{(n)}(E)$, c'est-à-dire $\pi_1(E \cap Y_n) = \pi_2(E \cap Y_n)$.
La suite d'ensembles $(E \cap Y_n)_n$ est croissante et son union est $E$. Par continuité croissante des mesures, en passant à la limite quand $n \to \infty$, on a :
$$ \pi_1(E) = \lim_{n \to \infty} \pi_1(E \cap Y_n) = \lim_{n \to \infty} \pi_2(E \cap Y_n) = \pi_2(E) $$
L'unicité de la mesure produit est ainsi entièrement établie.

## Applications en Physique, Logique et Intelligence Artificielle

### Probabilités et Indépendance
La mesure produit est la fondation théorique de la notion d'indépendance en théorie des probabilités. Deux variables aléatoires $X$ et $Y$ définies sur le même espace probabilisé sont dites indépendantes si leur loi jointe $P_{(X,Y)}$ (qui est une mesure de probabilité sur l'espace produit des valeurs) est égale au produit tensoriel de leurs lois marginales : $P_{(X,Y)} = P_X \otimes P_Y$. Cela signifie formellement que la probabilité que $X \in A$ et $Y \in B$ est exactement $P_X(A) \cdot P_Y(B)$. Sans la construction rigoureuse de la tribu produit et de la mesure produit, la théorie moderne des probabilités (axiomatisée par Kolmogorov) ne pourrait pas exprimer correctement l'indépendance de variables aléatoires à valeurs dans des espaces mesurables arbitraires.

### Intelligence Artificielle : Espace des Données et Risque Empirique
Dans le cadre de l'apprentissage automatique (PAC learning, minimisation du risque empirique), l'espace sur lequel on apprend est fondamentalement un produit : $\mathcal{X} \times \mathcal{Y}$, où $\mathcal{X}$ est l'espace des caractéristiques (features) et $\mathcal{Y}$ l'espace des étiquettes (labels). La distribution sous-jacente des données génératrices est modélisée par une mesure $\mathbb{P}$ sur $\mathcal{X} \times \mathcal{Y}$.
L'hypothèse d'indépendance conditionnelle dans de nombreux modèles (comme le classificateur Naïf de Bayes) revient mathématiquement à factoriser certaines désintégrations de cette mesure jointe en un produit de mesures sur les composantes de $\mathcal{X}$.

De plus, l'échantillonnage de points i.i.d. (Indépendants et Identiquement Distribués) pour former un jeu d'entraînement de taille $N$ correspond à considérer une variable aléatoire tirée selon la mesure produit $\mathbb{P}^{\otimes N}$ sur le vaste espace tensoriel $(\mathcal{X} \times \mathcal{Y})^N$. C'est exclusivement cette structure géométrique de mesure produit qui permet l'application d'inégalités de concentration de la mesure (comme l'inégalité de Hoeffding, de McDiarmid ou le lemme de Sanov), outils cardinaux permettant de borner l'écart de généralisation entre le risque empirique estimé et le risque structurel véritable d'un réseau de neurones profond.
