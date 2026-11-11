---
uuid: "jalon-90"
title: "Les modes de convergence en probabilités"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon-89.md]]"
next: "[[Jalon 91 (Inégalités de concentration).md]]"
---

# Les modes de convergence en probabilités

## 1. Origines et intuitions asymptotiques

L'étude des phénomènes aléatoires, initialement circonscrite aux jeux de hasard, a pris une dimension analytique rigoureuse au tournant des XIXe et XXe siècles grâce aux travaux de mathématiciens russes tels que Pafnuty Chebyshev, Andrey Markov et Andrey Kolmogorov, ainsi que l'économiste et statisticien Eugen Slutsky. La question centrale qui animait ces chercheurs était de comprendre le comportement asymptotique des suites de variables aléatoires : lorsqu'une expérience est répétée une infinité de fois, de quelle manière la moyenne empirique converge-t-elle vers son espérance théorique ?

En mathématiques classiques, la convergence d'une suite de nombres réels est univoque et absolue. En probabilités, du fait de l'existence d'événements de mesure nulle (les fameux ensembles $\omega \in \Omega$ pour lesquels la propriété peut faire défaut sans affecter la probabilité globale), le concept de "proximité" entre variables aléatoires se décline sous plusieurs topologies distinctes. Il a fallu forger un arsenal d'outils analytiques pour mesurer si une suite de variables aléatoires $(X_n)$ s'approche d'une limite $X$ presque partout, en mesure, en moyenne ou seulement au niveau de ses répartitions (loi). Cette hiérarchie des modes de convergence permet d'isoler la nature exacte de la stabilité asymptotique d'un système.

\begin{center}
\begin{tikzpicture}[scale=1.2, >=stealth, thick]
  % Espace L^p
  \draw[fill=blue!10, draw=blue!50!black, rounded corners=3mm] (-1.5,-2.5) rectangle (1.5,0.5);
  \node[blue!50!black] at (0, 0.2) {$L^p$ ($p \ge 1$)};

  % Convergence presque sûre
  \draw[fill=green!10, draw=green!50!black, rounded corners=3mm] (-3.5,-2.5) rectangle (-1.8, 0.5);
  \node[green!50!black] at (-2.65, 0.2) {Presque sûre};

  % Convergence en probabilité
  \draw[fill=orange!10, draw=orange!50!black, rounded corners=3mm] (-4,-3) rectangle (2,-5);
  \node[orange!50!black] at (-1, -3.4) {En probabilité};

  % Convergence en loi
  \draw[fill=purple!10, draw=purple!50!black, rounded corners=3mm] (-4.5,-5.5) rectangle (2.5,-7.5);
  \node[purple!50!black] at (-1, -5.9) {En loi (distribution)};

  % Flèches d'implication
  \draw[->, blue!80!black, ultra thick] (0, -2.5) -- (0, -3) node[midway, right] {Implication};
  \draw[->, green!80!black, ultra thick] (-2.65, -2.5) -- (-2.65, -3);
  \draw[->, orange!80!black, ultra thick] (-1, -5) -- (-1, -5.5);

\end{tikzpicture}
\end{center}

## 2. Définitions formelles et exemples fondamentaux

Dans ce qui suit, on considère un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$. Toutes les variables aléatoires considérées sont à valeurs réelles et définies sur cet espace. On s'intéresse à la convergence d'une suite $(X_n)_{n \in \mathbb{N}}$ vers une variable aléatoire $X$.

### 2.1 Convergence Presque Sûre (p.s.)

La convergence presque sûre est le mode de convergence le plus fort au sens des trajectoires. Il stipule que la suite de fonctions $X_n(\omega)$ converge ponctuellement vers $X(\omega)$ pour presque toutes les réalisations $\omega \in \Omega$.

**Définition :**
La suite $(X_n)$ converge presque sûrement vers $X$, noté $X_n \xrightarrow{p.s.} X$, si :
$$ \mathbb{P}\left(\left\{\omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = X(\omega)\right\}\right) = 1 $$
Ceci est équivalent à affirmer que l'événement sur lequel la convergence ponctuelle fait défaut est de probabilité nulle.

**Exemple concret immédiat (Variable aléatoire sur le segment unité) :**
Soit $\Omega = [0, 1]$ muni de sa tribu borélienne $\mathcal{B}([0, 1])$ et de la mesure de Lebesgue $\mathbb{P}$.
Considérons la suite de variables aléatoires $X_n : \Omega \to \mathbb{R}$ définie par $X_n(\omega) = \omega^n$.
Fixons $\omega \in \Omega$.
- Si $\omega \in [0, 1[$, alors $\lim_{n \to \infty} \omega^n = 0$.
- Si $\omega = 1$, alors $\lim_{n \to \infty} 1^n = 1$.
Ainsi, la suite $(X_n)$ converge ponctuellement vers la variable aléatoire $X$ définie par $X(\omega) = 0$ sur $[0, 1[$ et $X(1) = 1$.
Puisque $\mathbb{P}(\{1\}) = 0$, nous avons $X_n \xrightarrow{p.s.} 0$.

### 2.2 Convergence en Probabilité

La convergence en probabilité est plus faible que la convergence presque sûre. Elle garantit que, pour un $n$ assez grand, la probabilité que $X_n$ s'éloigne de $X$ d'une distance macroscopique devient arbitrairement faible.

**Définition :**
La suite $(X_n)$ converge en probabilité vers $X$, noté $X_n \xrightarrow{\mathbb{P}} X$, si pour tout réel $\epsilon > 0$ :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$

**Théorème d'implication (Presque sûre $\implies$ En probabilité) :**
Si $X_n \xrightarrow{p.s.} X$, alors $X_n \xrightarrow{\mathbb{P}} X$.

**Exemple concret immédiat (La machine à écrire glissante) :**
Considérons à nouveau $\Omega = [0, 1]$ muni de la mesure de Lebesgue.
Pour chaque $n \ge 1$, il existe un unique entier $k \ge 0$ et un entier $j \in \{0, \dots, 2^k - 1\}$ tels que $n = 2^k + j$.
Définissons $X_n(\omega) = \mathbf{1}_{\left[\frac{j}{2^k}, \frac{j+1}{2^k}\right]}(\omega)$.
Pour tout $\epsilon \in ]0, 1[$, $\mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n = 1) = \frac{1}{2^k}$.
Comme $k \to \infty$ lorsque $n \to \infty$, on a $\lim_{n \to \infty} \mathbb{P}(|X_n| > \epsilon) = 0$. Donc $X_n \xrightarrow{\mathbb{P}} 0$.
Cependant, pour tout $\omega \in [0, 1]$, $X_n(\omega)$ alternera entre $0$ et $1$ une infinité de fois. Donc $(X_n)$ ne converge ponctuellement pour aucun $\omega$. Cela prouve que la convergence en probabilité n'implique pas la convergence presque sûre.

### 2.3 Convergence dans $L^p$ (en moyenne d'ordre $p$)

Ce mode mesure la convergence fonctionnelle globale au sens des espaces normés $L^p$.

**Définition :**
Soit $p \ge 1$. On suppose que $X_n \in L^p$ pour tout $n$ (c'est-à-dire $\mathbb{E}[|X_n|^p] < \infty$).
La suite $(X_n)$ converge vers $X$ dans $L^p$, noté $X_n \xrightarrow{L^p} X$, si $X \in L^p$ et :
$$ \lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0 $$

**Exemple concret immédiat (La bosse fuyante) :**
Soit $\Omega = [0, 1]$ et $X_n(\omega) = n \cdot \mathbf{1}_{[0, 1/n]}(\omega)$.
- Convergence en probabilité : $\mathbb{P}(|X_n - 0| > \epsilon) \le \mathbb{P}(X_n \neq 0) = \frac{1}{n} \to 0$. Donc $X_n \xrightarrow{\mathbb{P}} 0$.
- Convergence $L^1$ : $\mathbb{E}[|X_n|] = n \cdot \frac{1}{n} = 1$. L'espérance ne tend pas vers $0$. Ainsi $X_n$ ne converge pas vers $0$ dans $L^1$.
Cet exemple montre qu'une suite peut converger en probabilité vers une limite sans pour autant converger en moyenne d'ordre $p$.

### 2.4 Convergence en Loi (ou en Distribution)

La convergence en loi est de nature fondamentalement différente. Elle exprime que la répartition probabiliste globale de $X_n$ tend vers la répartition de $X$, indépendamment de toute corrélation trajectorielle.

**Définition (par les fonctions de répartition) :**
Soient $F_n(t) = \mathbb{P}(X_n \le t)$ et $F_X(t) = \mathbb{P}(X \le t)$ les fonctions de répartition respectives.
On dit que $X_n \xrightarrow{\mathcal{L}} X$ si, en tout point de continuité $t$ de $F_X$ :
$$ \lim_{n \to \infty} F_n(t) = F_X(t) $$

**Théorème de Portmanteau (caractérisation par l'espérance) :**
$X_n \xrightarrow{\mathcal{L}} X$ si et seulement si pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée :
$$ \lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)] $$

**Exemple concret immédiat (Symétrie et loi normale) :**
Soit $X \sim \mathcal{N}(0, 1)$. Définissons $X_n = -X$ pour tout $n$.
Puisque la loi normale standard est symétrique, $-X \sim \mathcal{N}(0, 1)$.
Les variables $X_n$ et $X$ ont rigoureusement la même loi. Ainsi, de façon triviale, $X_n \xrightarrow{\mathcal{L}} X$.
En revanche, $|X_n - X| = |-2X| = 2|X|$. La distance est strictement positive, donc $X_n$ ne converge vers $X$ ni en probabilité, ni presque sûrement.

\begin{center}
\begin{tikzpicture}[scale=1.2, >=stealth, thick]
  % Axe des x
  \draw[->] (-3, 0) -- (3, 0) node[right] {$x$};
  % Axe des y (Densité)
  \draw[->] (0, 0) -- (0, 2.5) node[above] {$f(x)$};

  % Courbe Loi Normale (Approximation)
  \draw[blue, thick, domain=-2.5:2.5, samples=100] plot (\x, {2*exp(-\x*\x)});
  \node[blue] at (1.5, 1.8) {$X \sim \mathcal{N}(0, 1)$};

  % Visualisation de -X
  \draw[dashed, red, thick] (1, 0) -- (1, {2*exp(-1)});
  \fill[red] (1, {2*exp(-1)}) circle (2pt) node[right] {$x$};

  \draw[dashed, red, thick] (-1, 0) -- (-1, {2*exp(-1)});
  \fill[red] (-1, {2*exp(-1)}) circle (2pt) node[left] {$-x$};

  \node[red] at (-1.5, 1) {Symétrie : loi de $-X$};

\end{tikzpicture}
\end{center}

## 3. Démonstrations exhaustives

Le théorème fondamental de hiérarchie s'énonce comme suit :
$X_n \xrightarrow{L^p} X \implies X_n \xrightarrow{\mathbb{P}} X \implies X_n \xrightarrow{\mathcal{L}} X$

### 3.1 Démonstration : $L^p \implies$ Convergence en probabilité

Nous devons prouver que si $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$, alors pour tout $\epsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0$.

**Preuve pas à pas :**
Soit $\epsilon > 0$ fixé. L'événement $E_n = \{\omega \in \Omega \mid |X_n(\omega) - X(\omega)| > \epsilon\}$ est équivalent à l'événement $\{\omega \in \Omega \mid |X_n(\omega) - X(\omega)|^p > \epsilon^p\}$, puisque la fonction $x \mapsto x^p$ est strictement croissante sur $\mathbb{R}^+$.
Considérons la variable aléatoire positive $Y_n = |X_n - X|^p$.
Appliquons l'inégalité de Markov à $Y_n$ avec la constante $a = \epsilon^p > 0$ :
$$ \mathbb{P}(Y_n \ge a) \le \frac{\mathbb{E}[Y_n]}{a} $$
En remplaçant par nos variables :
$$ \mathbb{P}(|X_n - X|^p > \epsilon^p) \le \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p} $$
Par hypothèse, $X_n \xrightarrow{L^p} X$, donc $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$.
Puisque $\epsilon$ est fixé (et donc $\epsilon^p > 0$ est constant), le membre de droite tend vers $0$ :
$$ \lim_{n \to \infty} \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p} = 0 $$
Puisque les probabilités sont toujours minorées par $0$, le théorème des gendarmes nous assure que :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$
Ceci achève la démonstration. $\blacksquare$

### 3.2 Démonstration : Convergence en probabilité $\implies$ Convergence en loi

Nous voulons prouver que si $X_n \xrightarrow{\mathbb{P}} X$, alors pour toute fonction continue et bornée $f$, $\lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$.

**Preuve pas à pas :**
Soit $f : \mathbb{R} \to \mathbb{R}$ continue et bornée. Soit $M > 0$ tel que $|f(x)| \le M$ pour tout $x \in \mathbb{R}$.
Soit $\eta > 0$ un seuil de tolérance.
Puisque $X$ est une variable aléatoire réelle, ses valeurs se concentrent. Il existe un intervalle compact $K = [-A, A]$ tel que $\mathbb{P}(X \notin K) < \eta$.
La fonction $f$ étant continue sur le segment compact $K$, elle y est uniformément continue d'après le théorème de Heine-Cantor.
Il existe donc $\delta > 0$ tel que pour tout $x \in K$ et $y \in \mathbb{R}$, si $|x - y| < \delta$, alors $|f(x) - f(y)| < \eta$.

Majorons la différence d'espérance :
$$ |\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| \le \mathbb{E}[|f(X_n) - f(X)|] $$
Partitionnons l'espace d'intégration $\Omega$ selon deux critères : l'éloignement de $X_n$ et $X$, et l'appartenance de $X$ au compact $K$.
Soient les événements :
$E_1 = \{\omega \in \Omega \mid |X_n(\omega) - X(\omega)| \ge \delta\}$
$E_2 = \{\omega \in \Omega \mid |X_n(\omega) - X(\omega)| < \delta \text{ et } X(\omega) \notin K\}$
$E_3 = \{\omega \in \Omega \mid |X_n(\omega) - X(\omega)| < \delta \text{ et } X(\omega) \in K\}$

Décomposons l'intégrale (espérance) selon cette partition :
$$ \mathbb{E}[|f(X_n) - f(X)|] = \mathbb{E}[|f(X_n) - f(X)| \cdot \mathbf{1}_{E_1}] + \mathbb{E}[|f(X_n) - f(X)| \cdot \mathbf{1}_{E_2}] + \mathbb{E}[|f(X_n) - f(X)| \cdot \mathbf{1}_{E_3}] $$
1. Sur $E_1$, on majore brutalement avec la borne de $f$ : $|f(X_n) - f(X)| \le |f(X_n)| + |f(X)| \le 2M$.
   Donc $\mathbb{E}[|f(X_n) - f(X)| \cdot \mathbf{1}_{E_1}] \le 2M \cdot \mathbb{P}(E_1) \le 2M \cdot \mathbb{P}(|X_n - X| \ge \delta)$.
2. Sur $E_2$, on majore aussi brutalement : $|f(X_n) - f(X)| \le 2M$.
   Donc $\mathbb{E}[|f(X_n) - f(X)| \cdot \mathbf{1}_{E_2}] \le 2M \cdot \mathbb{P}(E_2) \le 2M \cdot \mathbb{P}(X \notin K) \le 2M\eta$.
3. Sur $E_3$, on exploite la continuité uniforme : $|f(X_n) - f(X)| < \eta$.
   Donc $\mathbb{E}[|f(X_n) - f(X)| \cdot \mathbf{1}_{E_3}] \le \eta \cdot \mathbb{P}(E_3) \le \eta \cdot 1 = \eta$.

En sommant, nous obtenons :
$$ \mathbb{E}[|f(X_n) - f(X)|] \le 2M \cdot \mathbb{P}(|X_n - X| \ge \delta) + 2M\eta + \eta = 2M \cdot \mathbb{P}(|X_n - X| \ge \delta) + (2M+1)\eta $$
Puisque $X_n \xrightarrow{\mathbb{P}} X$, nous savons que pour ce $\delta > 0$ fixé, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| \ge \delta) = 0$.
En passant à la limite supérieure lorsque $n \to \infty$ :
$$ \limsup_{n \to \infty} \mathbb{E}[|f(X_n) - f(X)|] \le (2M+1)\eta $$
Or, $\eta > 0$ a été choisi de manière arbitraire. Cette inégalité étant valide pour tout $\eta > 0$, cela force la limite à être nulle :
$$ \lim_{n \to \infty} \mathbb{E}[|f(X_n) - f(X)|] = 0 $$
Ainsi, la convergence en loi est démontrée. $\blacksquare$

## 4. Applications en Physique, Logique et Intelligence Artificielle

### A. Consistance asymptotique (Machine Learning)
En théorie de l'apprentissage statistique, on dit qu'un algorithme fournissant un estimateur paramétrique $\hat{\theta}_n$ (calculé sur $n$ observations) est convergent si cet estimateur approche la "vraie" valeur $\theta^*$ du modèle génératif sous-jacent. Cette convergence est quantifiée mathématiquement par la convergence en probabilité ($\hat{\theta}_n \xrightarrow{\mathbb{P}} \theta^*$), justifiant ainsi théoriquement que l'accumulation massive de données permet l'extraction de signaux constants sans ambiguïté.

### B. Dynamique de la rétropropagation du gradient (SGD)
La descente de gradient stochastique, clé de voûte de l'entraînement des modèles d'IA génératifs (Transformers, CNNs), repose sur une suite de poids synaptiques $\theta_n$. Bien que chaque mise à jour $\nabla L(\theta_n, x_i)$ soit bruitée car évaluée sur un mini-batch aléatoire, la théorie des martingales garantit (sous les conditions de pas de Robbins-Monro) que l'algorithme converge **presque sûrement** vers un point critique (gradient nul) de l'espace de perte.

### C. Théorème Central Limite (Physique statistique)
En mécanique statistique, les variables macroscopiques (comme la pression d'un gaz sur une paroi) résultent de l'accumulation de millions de petites fluctuations (les impacts des molécules microscopiques, que l'on peut modéliser par des variables aléatoires $(X_i)$ i.i.d). Bien qu'il soit impossible de connaître la répartition microscopique individuelle, le Théorème Central Limite garantit que la somme normalisée $\frac{1}{\sqrt{n}} \sum (X_i - \mu)$ converge universellement **en loi** vers une distribution Gaussienne $\mathcal{N}(0, \sigma^2)$, expliquant la prévalence quasi-universelle de la cloche de Gauss dans les phénomènes thermiques et browniens.
