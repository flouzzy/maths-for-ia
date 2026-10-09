---
uuid: "jalon-86"
title: "Variables aléatoires et Applications mesurables"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 85 (Axiomes de Kolmogorov).md]]"
next: "[[Jalon 87 (Intégration des variables aléatoires).md]]"
---

# Jalon 86 : Variables Aléatoires et Applications Mesurables

## Introduction (Genèse historique et physique)
Historiquement, la théorie des probabilités s'est développée autour de jeux de hasard (dés, cartes) où l'univers des possibles, noté $\Omega$, est un ensemble fini. Cependant, lorsqu'il s'agit de modéliser des phénomènes continus comme le mouvement brownien en physique, la durée de vie d'un composant électronique, ou les fluctuations d'un marché financier, l'univers $\Omega$ devient infini et complexe.
Andrey Kolmogorov, en 1933, a posé les fondations axiomatiques modernes des probabilités. L'idée géniale a été de ne pas étudier l'univers $\Omega$ directement, mais de s'y intéresser par l'intermédiaire d'applications qui traduisent chaque événement abstrait $\omega \in \Omega$ en un nombre réel. Ce "traducteur" est appelé une **variable aléatoire**.
Cependant, pour que la théorie reste cohérente, on ne peut pas accepter n'importe quelle application. Il est impératif que pour toute question naturelle que l'on se pose sur le résultat (par exemple, "le résultat est-il inférieur à $x$ ?"), la probabilité de cet événement puisse être calculée. C'est ici qu'intervient la notion de **mesurabilité**. Une variable aléatoire n'est donc rien d'autre qu'une application mesurable d'un espace de probabilité vers un espace mesurable, typiquement $\mathbb{R}$ muni de la tribu de Borel.

## Définitions, Théorèmes et Exemples

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. L'ensemble $\Omega$ est l'univers, $\mathcal{F}$ est une tribu (ou $\sigma$-algèbre) sur $\Omega$ (les événements), et $\mathbb{P}$ est une mesure de probabilité.
Soit $(E, \mathcal{E})$ un espace mesurable (l'espace d'arrivée). Le plus souvent, $E = \mathbb{R}$ et $\mathcal{E} = \mathcal{B}(\mathbb{R})$, la tribu de Borel.

**Définition 1 (Variable aléatoire) :**
Une application $X : \Omega \to E$ est appelée une variable aléatoire (ou application mesurable) à valeurs dans $E$, si pour tout ensemble mesurable $B \in \mathcal{E}$, l'image réciproque $X^{-1}(B)$ appartient à la tribu $\mathcal{F}$.
Formellement :
$$ \forall B \in \mathcal{E}, \quad X^{-1}(B) = \{ \omega \in \Omega \mid X(\omega) \in B \} \in \mathcal{F} $$
Si $E = \mathbb{R}$ et $\mathcal{E} = \mathcal{B}(\mathbb{R})$, $X$ est une variable aléatoire réelle (v.a.r.).

*Exemple 1 : Lancer de dé*
Considérons le lancer d'un dé à 6 faces.
- L'univers : $\Omega = \{1, 2, 3, 4, 5, 6\}$.
- La tribu : $\mathcal{F} = \mathcal{P}(\Omega)$ (l'ensemble des parties de $\Omega$).
- La variable aléatoire $X$ : Soit $X(\omega) = 1$ si $\omega$ est pair, et $X(\omega) = 0$ si $\omega$ est impair.
- Espace d'arrivée : $E = \mathbb{R}$ avec la tribu de Borel $\mathcal{B}(\mathbb{R})$.
Vérifions la mesurabilité : Prenons l'ensemble borélien $B = \{1\}$. Son image réciproque est $X^{-1}(\{1\}) = \{2, 4, 6\}$. Cet ensemble appartient bien à $\mathcal{F}$ puisque $\mathcal{F} = \mathcal{P}(\Omega)$. $X$ est donc bien une variable aléatoire.

**Définition 2 (Loi d'une variable aléatoire) :**
Si $X$ est une variable aléatoire de $(\Omega, \mathcal{F}, \mathbb{P})$ dans $(E, \mathcal{E})$, on définit la loi de $X$, notée $\mathbb{P}_X$, comme la mesure de probabilité sur $(E, \mathcal{E})$ donnée par la mesure image :
$$ \forall B \in \mathcal{E}, \quad \mathbb{P}_X(B) = \mathbb{P}(X^{-1}(B)) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) \in B\}) $$
On note souvent cela $\mathbb{P}(X \in B)$.

*Exemple 2 : Calcul de loi*
Reprenons l'exemple 1 avec un dé équilibré : $\mathbb{P}(\{\omega\}) = 1/6$ pour tout $\omega \in \Omega$.
Calculons la loi de $X$. $X$ prend ses valeurs dans $\{0, 1\}$.
- $\mathbb{P}_X(\{1\}) = \mathbb{P}(X = 1) = \mathbb{P}(\{2, 4, 6\}) = \frac{3}{6} = \frac{1}{2}$.
- $\mathbb{P}_X(\{0\}) = \mathbb{P}(X = 0) = \mathbb{P}(\{1, 3, 5\}) = \frac{3}{6} = \frac{1}{2}$.
$X$ suit donc une loi de Bernoulli de paramètre $p = 1/2$.

**Théorème 1 (Caractérisation de la mesurabilité) :**
Soit $\mathcal{E}$ la tribu engendrée par une famille de parties $\mathcal{C}$ de $E$, c'est-à-dire $\mathcal{E} = \sigma(\mathcal{C})$.
Pour qu'une application $X : \Omega \to E$ soit mesurable (i.e. soit une variable aléatoire), il suffit que pour tout $C \in \mathcal{C}$, on ait $X^{-1}(C) \in \mathcal{F}$.

*Exemple 3 : Variables aléatoires réelles*
Pour $E = \mathbb{R}$, la tribu de Borel $\mathcal{B}(\mathbb{R})$ est engendrée par les intervalles de la forme $]-\infty, x]$ pour $x \in \mathbb{R}$.
D'après le Théorème 1, $X : \Omega \to \mathbb{R}$ est une variable aléatoire réelle si et seulement si pour tout $x \in \mathbb{R}$, l'ensemble $\{ \omega \in \Omega \mid X(\omega) \leq x \}$ appartient à la tribu $\mathcal{F}$.

**Définition 3 (Fonction de répartition) :**
La loi d'une variable aléatoire réelle $X$ est entièrement caractérisée par sa fonction de répartition $F_X : \mathbb{R} \to [0, 1]$ définie par :
$$ F_X(x) = \mathbb{P}_X(]-\infty, x]) = \mathbb{P}(X \leq x) $$

*Exemple 4 : Fonction de répartition de la loi exponentielle*
Soit $X$ une variable aléatoire suivant une loi exponentielle de paramètre $\lambda > 0$. Sa densité de probabilité est $f_X(t) = \lambda e^{-\lambda t} \mathbf{1}_{\{t \geq 0\}}$.
Calculons sa fonction de répartition $F_X(x)$ pour $x \geq 0$ :
$$ F_X(x) = \mathbb{P}(X \leq x) = \int_{-\infty}^{x} f_X(t) dt = \int_{0}^{x} \lambda e^{-\lambda t} dt = \left[ -e^{-\lambda t} \right]_0^x = 1 - e^{-\lambda x} $$
Pour $x < 0$, $F_X(x) = 0$.

*Exemple 5 : Transformation d'une variable aléatoire*
Soit $U$ une variable aléatoire suivant une loi uniforme sur $[0, 1]$. Posons $X = -\frac{1}{\lambda} \ln(U)$, avec $\lambda > 0$.
Montrons que $X$ suit une loi exponentielle de paramètre $\lambda$.
Calculons la fonction de répartition de $X$. Puisque $U \in ]0, 1]$, $X$ prend ses valeurs dans $[0, +\infty[$.
Pour $x \geq 0$ :
$$ F_X(x) = \mathbb{P}(X \leq x) = \mathbb{P}\left(-\frac{1}{\lambda} \ln(U) \leq x\right) = \mathbb{P}(\ln(U) \geq -\lambda x) = \mathbb{P}(U \geq e^{-\lambda x}) $$
Comme $U$ est uniforme sur $[0, 1]$, $\mathbb{P}(U \geq c) = 1 - c$ pour $c \in [0, 1]$.
Ainsi, $F_X(x) = 1 - e^{-\lambda x}$. Ceci est exactement la fonction de répartition d'une loi exponentielle $\mathcal{E}(\lambda)$.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Espace Omega
  \draw[fill=blue!10] (0,0) ellipse (1.5 and 1);
  \node at (0, 0.7) {$\Omega$ (Univers abstrait)};

  \filldraw[black] (-0.5, 0.2) circle (1pt) node[anchor=east] {$\omega_1$};
  \filldraw[black] (0.5, -0.3) circle (1pt) node[anchor=west] {$\omega_2$};

  % Flèches de X
  \draw[->, thick, red] (-0.4, 0.2) .. controls (1, 1.5) and (3, 1) .. (4.4, 0.1);
  \draw[->, thick, red] (0.6, -0.3) .. controls (2, -1) and (3, -0.5) .. (5.4, 0.1);
  \node[red] at (2.5, 1) {$X$};

  % Espace R (Droite réelle)
  \draw[->, thick] (4,-0.5) -- (7,-0.5) node[right] {$\mathbb{R}$};
  \draw (4.5,-0.6) -- (4.5,-0.4) node[above] {$X(\omega_1)$};
  \draw (5.5,-0.6) -- (5.5,-0.4) node[above] {$X(\omega_2)$};

  % Borélien B
  \draw[very thick, blue] (4.2, -0.5) -- (5.0, -0.5);
  \node[blue, below] at (4.6, -0.7) {Borélien $B$};

  % Image réciproque
  \draw[dashed, blue] (-1.0, 0.3) ellipse (0.7 and 0.4);
  \node[blue, above] at (-1.0, 0.7) {$X^{-1}(B) \in \mathcal{F}$};
\end{tikzpicture}
\end{center}

**Théorème 2 (Composition et opérations sur les variables aléatoires) :**
1. Si $X : \Omega \to E$ est mesurable et $f : E \to G$ est mesurable (où $G$ est un autre espace mesurable), alors la composition $f \circ X : \Omega \to G$ est une variable aléatoire.
2. Si $X$ et $Y$ sont deux variables aléatoires réelles, alors $X+Y$, $X \cdot Y$, $\max(X, Y)$ et $\min(X, Y)$ sont aussi des variables aléatoires réelles.

*Exemple 6 : Somme de variables de Poisson*
Si $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$ sont indépendantes. D'après le théorème 2, $Z = X + Y$ est une variable aléatoire.
On peut montrer par le calcul des probabilités discrètes que $Z \sim \mathcal{P}(\lambda + \mu)$.

*Exemple 7 : Maximum de deux variables uniformes*
Soient $X_1, X_2$ deux variables indépendantes, uniformément distribuées sur $[0, 1]$. Soit $Y = \max(X_1, X_2)$.
$Y$ est une variable aléatoire (Théorème 2). Calculons sa fonction de répartition $F_Y(y)$ pour $y \in [0,1]$.
$$ F_Y(y) = \mathbb{P}(\max(X_1, X_2) \leq y) = \mathbb{P}(X_1 \leq y \text{ et } X_2 \leq y) $$
Par indépendance, $F_Y(y) = \mathbb{P}(X_1 \leq y)\mathbb{P}(X_2 \leq y) = y \cdot y = y^2$.
La densité de $Y$ est donc $f_Y(y) = F_Y'(y) = 2y$ sur $[0, 1]$.

## Démonstrations

**Démonstration du Théorème 1 (Caractérisation de la mesurabilité) :**

On suppose que pour tout $C \in \mathcal{C}$, on a $X^{-1}(C) \in \mathcal{F}$. On veut montrer que pour tout $B \in \mathcal{E} = \sigma(\mathcal{C})$, $X^{-1}(B) \in \mathcal{F}$.
Soit $\mathcal{G}$ l'ensemble des parties de $E$ dont l'image réciproque par $X$ appartient à $\mathcal{F}$ :
$$ \mathcal{G} = \{ B \subset E \mid X^{-1}(B) \in \mathcal{F} \} $$
Montrons que $\mathcal{G}$ est une tribu sur $E$ :
1. $\emptyset \in \mathcal{G}$ car $X^{-1}(\emptyset) = \emptyset \in \mathcal{F}$.
2. Si $B \in \mathcal{G}$, alors $X^{-1}(B) \in \mathcal{F}$. Considérons le complémentaire $B^c = E \setminus B$.
   $X^{-1}(B^c) = X^{-1}(E \setminus B) = \Omega \setminus X^{-1}(B) = (X^{-1}(B))^c$.
   Puisque $\mathcal{F}$ est une tribu, le complémentaire de $X^{-1}(B)$ est dans $\mathcal{F}$, donc $X^{-1}(B^c) \in \mathcal{F}$, ce qui implique que $B^c \in \mathcal{G}$.
3. Si $(B_n)_{n \in \mathbb{N}}$ est une suite d'éléments de $\mathcal{G}$, alors $X^{-1}(B_n) \in \mathcal{F}$ pour tout $n$.
   $X^{-1}\left(\bigcup_{n \in \mathbb{N}} B_n\right) = \bigcup_{n \in \mathbb{N}} X^{-1}(B_n)$.
   Comme $\mathcal{F}$ est une tribu, l'union dénombrable appartient à $\mathcal{F}$. Donc $\bigcup_{n} B_n \in \mathcal{G}$.
L'ensemble $\mathcal{G}$ est donc une tribu. Par hypothèse, $\mathcal{C} \subset \mathcal{G}$. Or, $\sigma(\mathcal{C})$ est la plus petite tribu contenant $\mathcal{C}$.
Par conséquent, $\sigma(\mathcal{C}) \subset \mathcal{G}$.
Cela signifie que pour tout $B \in \sigma(\mathcal{C}) = \mathcal{E}$, $B \in \mathcal{G}$, donc $X^{-1}(B) \in \mathcal{F}$. La fonction $X$ est bien mesurable. $\blacksquare$

**Démonstration du Théorème 2 (point 1 : Composition) :**

Soient $X : \Omega \to E$ mesurable et $f : E \to G$ mesurable. On veut montrer que $f \circ X : \Omega \to G$ est mesurable.
Soit $\mathcal{G}$ la tribu sur l'espace d'arrivée $G$. Soit $C \in \mathcal{G}$.
L'image réciproque de $C$ par $f \circ X$ est :
$$ (f \circ X)^{-1}(C) = X^{-1}(f^{-1}(C)) $$
Puisque $f$ est mesurable, l'ensemble $B = f^{-1}(C)$ appartient à la tribu $\mathcal{E}$ de $E$.
Ensuite, puisque $X$ est mesurable, l'ensemble $X^{-1}(B)$ appartient à la tribu $\mathcal{F}$ de $\Omega$.
Ainsi, $(f \circ X)^{-1}(C) \in \mathcal{F}$ pour tout $C \in \mathcal{G}$. La fonction composée est donc mesurable. $\blacksquare$


## Applications en Physique, Logique et Intelligence Artificielle

### Physique Statistique
En mécanique statistique classique, l'état d'un système de particules est décrit par un point dans l'espace des phases (l'univers $\Omega$). Les observables physiques macroscopiques telles que l'énergie interne $E$, la pression $P$, ou la température, sont modélisées mathématiquement comme des variables aléatoires (fonctions mesurables sur l'espace des phases). La loi de ces variables, issue d'une mesure de probabilité (comme la mesure de Gibbs canonique), permet d'obtenir les fluctuations statistiques et d'établir les lois de la thermodynamique.

### Logique et Informatique Théorique
La mesurabilité joue le rôle de pont entre l'information accessible et la décision. En théorie de la décision et du filtrage (comme le filtre de Kalman), une information acquise au cours du temps engendre une suite de tribus emboîtées appelée *filtration*, $(\mathcal{F}_t)_{t \ge 0}$. Une stratégie de décision $u_t$ (par exemple l'achat ou la vente d'une action, ou une instruction de contrôle) doit être une fonction mesurable par rapport à $\mathcal{F}_t$, ce que l'on appelle un processus *adapté*. Cela traduit le fait qu'une décision prise à l'instant $t$ ne peut dépendre que des informations observées jusqu'à $t$, respectant ainsi le principe de causalité.

### Intelligence Artificielle et Machine Learning
L'apprentissage statistique repose entièrement sur la notion de variables aléatoires.
Un modèle de classification (comme un réseau de neurones) cherche à apprendre une application mesurable $f_\theta : \mathcal{X} \to \mathcal{Y}$ qui lie des caractéristiques observables $X$ (image, texte) à un label $Y$.
La mesure de probabilité jointe $\mathbb{P}_{(X,Y)}$ est inconnue, et nous ne disposons que d'un ensemble d'observations (variables aléatoires i.i.d.).
La fonction de perte empirique (par exemple la *Cross-Entropy*) est elle-même une variable aléatoire car elle dépend de l'échantillon. Le fait que les opérations usuelles (somme, produit, fonctions d'activation continues comme ReLU, Sigmoïde, qui sont toutes mesurables) préservent la mesurabilité garantit que la fonction de perte finale et le gradient (via la rétropropagation) sont bien des variables aléatoires rigoureusement définies. Cela légitime l'utilisation des lois des grands nombres pour analyser la convergence de la descente de gradient stochastique (SGD).
