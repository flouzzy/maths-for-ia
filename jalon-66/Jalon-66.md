---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-65.md]]"
next: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"
---

# Jalon 66 : Intégrale de Lebesgue pour les fonctions mesurables positives

## 1. La Genèse : Élever l'Intégration d'une Partition du Domaine à une Partition de l'Image

Au cœur du XIXe siècle, l'intégrale de Riemann a triomphé pour capturer l'aire sous la courbe des fonctions "suffisamment régulières" (continues, ou continues par morceaux). Son approche reposait sur un découpage vertical : subdiviser le domaine de départ $[a, b]$ en minuscules intervalles et élever des rectangles jusqu'à la courbe.

Cependant, face aux pathologiques, l'édifice Riemannien s'effondre. La fonction indicatrice des rationnels $\mathbf{1}_{\mathbb{Q}}$ sur $[0, 1]$ (la fonction de Dirichlet) en est l'illustration fulgurante. Dans tout intervalle, aussi petit soit-il, on trouve à la fois des rationnels (valeur 1) et des irrationnels (valeur 0). Les sommes de Darboux inférieures stagnent à 0, tandis que les supérieures plafonnent à 1. La fonction n'est pas Riemann-intégrable.

Henri Lebesgue, en 1902, renverse le paradigme. Au lieu de partitionner le domaine (l'axe des abscisses), il propose de **partitionner l'image** (l'axe des ordonnées). Comme l'illustre la comparaison classique : pour compter l'argent d'une caisse, un boutiquier Riemannien prendrait les pièces dans l'ordre où elles se présentent (somme par tranches du domaine), tandis qu'un boutiquier Lebesguien trierait d'abord les pièces par valeur (partition de l'image), comptant tous les 1 centime ensemble, puis tous les 5 centimes, etc.

Cette approche exige de pouvoir "mesurer" l'ensemble des points $x$ du domaine pour lesquels la fonction prend une valeur donnée $y$. C'est ici que la théorie de la mesure de Lebesgue intervient, permettant d'attribuer une "taille" (une mesure) aux sous-ensembles extrêmement fracturés de la droite réelle. En partant des fonctions les plus élémentaires (les fonctions dites "étagées" ou "simples"), Lebesgue construit pas à pas une intégrale d'une puissance colossale, absorbant la fonction de Dirichlet (dont l'intégrale vaudra 0, car la mesure des rationnels est nulle) et offrant de puissants théorèmes de passage à la limite.

Dans cette leçon, nous allons bâtir rigoureusement l'intégrale de Lebesgue pour les fonctions mesurables positives, pierre angulaire qui soutiendra tout l'édifice fonctionnel moderne (espaces $L^p$, probabilités de Kolmogorov).

## 2. Définitions Fondamentales et Premières Intégrales

La construction de l'intégrale de Lebesgue se déploie en deux étapes rigoureuses et ascendantes : d'abord sur les fonctions simples (où l'intégration se ramène à une somme finie), puis sur toutes les fonctions mesurables positives par un processus de supremum (limite croissante).

### 2.1 Intégrale des Fonctions Étagées (Simples) Positives

On se place dans un espace mesuré abstrait $(X, \mathcal{F}, \mu)$.
Une fonction $s : X \to \mathbb{R}_+$ est dite **simple (ou étagée) positive** si elle ne prend qu'un nombre fini de valeurs, toutes positives ou nulles. Elle peut s'écrire sous forme canonique :
$$s(x) = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}(x)$$
où $\alpha_1, \dots, \alpha_n$ sont des réels strictement positifs distincts (plus éventuellement 0), et les $A_i = \{x \in X \mid s(x) = \alpha_i\}$ forment une partition finie de l'ensemble de niveau de la fonction (tous mesurables, $A_i \in \mathcal{F}$). Notons $\mathcal{E}_+$ l'ensemble de ces fonctions.

**Définition 1 (Intégrale d'une fonction simple positive) :**
Pour une fonction simple $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i} \in \mathcal{E}_+$ sous sa forme canonique, on définit son intégrale de Lebesgue par rapport à la mesure $\mu$ par :
$$\int_X s \, d\mu = \sum_{i=1}^n \alpha_i \mu(A_i)$$
Cette valeur appartient à $[0, +\infty]$. On utilise la convention fondamentale de la théorie de la mesure : **$0 \cdot (+\infty) = 0$**.

**Exemple Calculatoire Immédiat :**
Plaçons-nous sur $X = \mathbb{R}$ avec la mesure de Lebesgue $\mu = \lambda$.
Soit $s = 3 \cdot \mathbf{1}_{[0, 2]} + 5 \cdot \mathbf{1}_{[4, 5]} + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus ([0, 2] \cup [4, 5])}$.
C'est une fonction étagée positive sous sa forme canonique.
Son intégrale vaut :
$$\int_{\mathbb{R}} s \, d\lambda = 3 \cdot \lambda([0, 2]) + 5 \cdot \lambda([4, 5]) = 3 \cdot (2 - 0) + 5 \cdot (5 - 4) = 6 + 5 = 11$$

**Cas pathologique (Convention $0 \cdot \infty = 0$) :**
Considérons la fonction identiquement nulle sur $\mathbb{R}$, $s = 0 \cdot \mathbf{1}_{\mathbb{R}}$.
Ici, $A_1 = \mathbb{R}$ et $\mu(A_1) = +\infty$. L'intégrale est :
$\int_{\mathbb{R}} 0 \, d\lambda = 0 \cdot \lambda(\mathbb{R}) = 0 \cdot (+\infty) = 0$.
Géométriquement, l'aire d'un "rectangle" de hauteur 0 et de largeur infinie est strictement nulle dans cette théorie.

### 2.2 Intégrale des Fonctions Mesurables Positives

La force de la mesure de Lebesgue réside dans sa capacité à approcher toute fonction mesurable positive par une suite croissante de fonctions simples.

**Définition 2 (Intégrale de Lebesgue) :**
Soit $f : X \to [0, +\infty]$ une fonction mesurable positive. (Notons cet espace $\mathcal{M}_+$).
L'intégrale de $f$ sur $X$ par rapport à $\mu$ est définie comme le supremum des intégrales de toutes les fonctions simples positives qui minorant $f$ :
$$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \ \middle| \ s \in \mathcal{E}_+, \ 0 \le s(x) \le f(x) \ \forall x \in X \right\rbrace$$
Cette intégrale est un élément de $[0, +\infty]$. Si $\int_X f \, d\mu < +\infty$, on dit que $f$ est **Lebesgue-intégrable**.

\begin{center}
\begin{tikzpicture}[scale=1.2]
\draw[->] (-0.5,0) -- (5.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,4.5) node[above] {$f(x)$};
\draw[thick, domain=0.5:5, smooth, samples=100] plot (\x, {0.5*sin(\x*100) + 2.5 + sin(\x*50)});
\node at (2.5, 4) {$f(x)$};

% Rectangles for simple function
\draw[fill=blue!20, opacity=0.7] (0.5,0) rectangle (1.5,1.5);
\draw[fill=blue!20, opacity=0.7] (1.5,0) rectangle (2.5,2.0);
\draw[fill=blue!20, opacity=0.7] (2.5,0) rectangle (3.5,1.8);
\draw[fill=blue!20, opacity=0.7] (3.5,0) rectangle (4.5,2.5);

\node at (1, 0.75) {$s_1$};
\node at (2, 1) {$s_2$};
\node at (3, 0.9) {$s_3$};
\node at (4, 1.25) {$s_4$};

\node at (2.5, -0.5) {Approximation par une fonction étagée $s \le f$};
\end{tikzpicture}
\end{center}

**Exemple Calculatoire Immédiat : La fonction de Dirichlet.**
Considérons $f = \mathbf{1}_{\mathbb{Q}}$ sur l'espace mesuré $([0, 1], \mathcal{B}([0,1]), \lambda)$.
$f$ est en réalité déjà une fonction simple positive. L'ensemble de niveau pour la valeur 1 est $A_1 = \mathbb{Q} \cap [0,1]$, et pour la valeur 0, c'est $A_2 = ([0,1] \setminus \mathbb{Q})$.
La mesure de Lebesgue des rationnels (un ensemble dénombrable) est nulle : $\lambda(A_1) = 0$.
Ainsi :
$$\int_{[0,1]} \mathbf{1}_{\mathbb{Q}} \, d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0,1]) + 0 \cdot \lambda([0,1] \setminus \mathbb{Q}) = 1 \cdot 0 + 0 \cdot 1 = 0$$
L'intégrale de Lebesgue absorbe sans effort les fonctions pathologiquement discontinues.

## 3. Démonstrations et Théorèmes de Propriétés Éléments

Avant d'aborder la convergence (qui sera le cœur du prochain jalon), démontrons rigoureusement les propriétés immédiates mais cruciales de cette intégrale.

**Théorème 1 (Positivité et Croissance) :**
Soient $f, g \in \mathcal{M}_+$.
1. Positivité : $f \ge 0 \implies \int_X f \, d\mu \ge 0$.
2. Croissance (Monotonie) : Si $f \le g$ sur $X$, alors $\int_X f \, d\mu \le \int_X g \, d\mu$.

**Démonstration détaillée (Croissance) :**
Soient $f, g \in \mathcal{M}_+$ telles que pour tout $x \in X$, $f(x) \le g(x)$.
Soit $s \in \mathcal{E}_+$ une fonction simple telle que $0 \le s \le f$.
Puisque $f \le g$, il s'ensuit que $0 \le s \le g$.
Ainsi, l'ensemble des fonctions simples minorant $f$ est un sous-ensemble des fonctions simples minorant $g$ :
$$\{s \in \mathcal{E}_+ \mid 0 \le s \le f\} \subseteq \{s \in \mathcal{E}_+ \mid 0 \le s \le g\}$$
Or, le supremum d'un ensemble de nombres est inférieur ou égal au supremum de tout sur-ensemble contenant ces nombres. Donc :
$$\sup \left\lbrace \int_X s \, d\mu \ \middle| \ 0 \le s \le f \right\rbrace \le \sup \left\lbrace \int_X s \, d\mu \ \middle| \ 0 \le s \le g \right\rbrace$$
Ce qui équivaut par définition à :
$$\int_X f \, d\mu \le \int_X g \, d\mu$$
CQFD.

**Théorème 2 (Intégrale Nulle et Presque Partout) :**
Soit $f \in \mathcal{M}_+$.
$$\int_X f \, d\mu = 0 \iff f = 0 \quad \mu\text{-presque partout (p.p.)}$$

**Démonstration détaillée :**
$\impliedby$ : Supposons que $f = 0$ $\mu$-p.p. Posons $E = \{x \in X \mid f(x) > 0\}$. Par hypothèse, $\mu(E) = 0$.
Soit $s \in \mathcal{E}_+$ une fonction simple telle que $0 \le s \le f$.
Écrivons $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$. Si pour un certain $i$, $\alpha_i > 0$, alors sur $A_i$, $s(x) > 0$. Puisque $s \le f$, on a $f(x) \ge s(x) > 0$ sur $A_i$. Donc $A_i \subseteq E$.
Par monotonie de la mesure, $\mu(A_i) \le \mu(E) = 0$, donc $\mu(A_i) = 0$.
Ainsi, dans l'expression de $\int_X s \, d\mu$, chaque terme $\alpha_i \mu(A_i)$ est nul. Donc $\int_X s \, d\mu = 0$ pour tout $s \le f$.
En passant au supremum, $\int_X f \, d\mu = 0$.

$\implies$ : Supposons que $\int_X f \, d\mu = 0$.
Définissons les ensembles $E = \{x \in X \mid f(x) > 0\}$ et $E_n = \{x \in X \mid f(x) \ge \frac{1}{n}\}$ pour $n \ge 1$.
On observe que $E = \bigcup_{n=1}^\infty E_n$.
Sur $E_n$, $f(x) \ge \frac{1}{n}$. Considérons la fonction simple $s_n(x) = \frac{1}{n} \mathbf{1}_{E_n}(x)$.
Clairement, $0 \le s_n(x) \le f(x)$ pour tout $x$.
Par croissance de l'intégrale (Théorème 1) :
$$0 = \int_X f \, d\mu \ge \int_X s_n \, d\mu = \frac{1}{n} \mu(E_n)$$
Puisque $\frac{1}{n} > 0$, on en déduit que $\mu(E_n) = 0$ pour tout $n$.
Par sous-additivité dénombrable de la mesure $\mu$ :
$$\mu(E) = \mu\left(\bigcup_{n=1}^\infty E_n\right) \le \sum_{n=1}^\infty \mu(E_n) = \sum_{n=1}^\infty 0 = 0$$
Donc $f$ est nulle presque partout. CQFD.

## 4. Applications en Théorie de l'Information et Machine Learning

L'intégrale de Lebesgue n'est pas qu'une abstraction d'analyse réelle ; elle est la fondation théorique de toute l'intelligence artificielle probabiliste et statistique.

**1. Espérance Mathématique Unifiée**
En théorie des probabilités de Kolmogorov, une variable aléatoire $X$ est simplement une fonction mesurable d'un espace de probabilité $(\Omega, \mathcal{A}, \mathbb{P})$ vers $\mathbb{R}$. Son espérance mathématique n'est autre que son intégrale de Lebesgue :
$$\mathbb{E}[X] = \int_\Omega X(\omega) \, d\mathbb{P}(\omega)$$
Avant Lebesgue, il fallait traiter séparément les variables discrètes (sommes de séries) et continues (intégrales de Riemann). Lebesgue unifie cela. Mieux, si la distribution de probabilité possède des atomes (parties discrètes) et une densité (partie continue) — typique en Machine Learning avec des activations ReLU qui écrasent une partie de la masse en zéro — l'intégrale de Lebesgue gère la mesure mixte sans le moindre heurt.

**2. Formes Intégrales du Risque (Expected Loss)**
Dans l'apprentissage supervisé, le risque (la perte attendue) d'un modèle $h_\theta$ est défini par :
$$R(\theta) = \mathbb{E}_{(x,y) \sim \mathcal{D}}[L(h_\theta(x), y)] = \int_{\mathcal{X} \times \mathcal{Y}} L(h_\theta(x), y) \, dP(x,y)$$
Ici, $P$ est la véritable distribution (inconnue) des données. Les théorèmes puissants de l'intégration de Lebesgue (comme la convergence dominée, à venir) permettent de justifier sous quelles conditions l'optimisation empirique (sur des échantillons discrets, assimilables à des mesures empiriques $\frac{1}{n}\sum \delta_{x_i}$) converge vers l'optimum théorique, fondement de la théorie PAC (Probably Approximately Correct).

**3. Divergence de Kullback-Leibler**
En théorie de l'information et pour les Auto-Encodeurs Variationnels (VAE), la similarité entre deux distributions $P$ et $Q$ (avec $P$ absolument continue par rapport à $Q$) est donnée par la divergence KL :
$$D_{\text{KL}}(P \parallel Q) = \int \log\left(\frac{dP}{dQ}\right) \, dP$$
La dérivée de Radon-Nikodym $\frac{dP}{dQ}$ et cette forme intégrale nécessitent l'arsenal complet de la mesure de Lebesgue pour être rigoureusement définies sur des espaces de grande dimension (espaces latents) de manière invariante par changement de base topologique.
