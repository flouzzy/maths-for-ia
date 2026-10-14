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

# Jalon 90 : Les modes de convergence en probabilités

## Introduction historique et physique

La notion de convergence d'une suite de variables aléatoires est au coeur de la théorie asymptotique en probabilités et en statistiques. Historiquement, l'étude des jeux de hasard et la nécessité de quantifier la précision d'une moyenne empirique par rapport à l'espérance théorique ont conduit à la formulation de la loi faible des grands nombres par Jacques Bernoulli (1713). Plus tard, Émile Borel (1909) introduit une notion beaucoup plus forte, affirmant que certains événements se produisent avec une certitude absolue, formalisant la convergence presque sûre et la loi forte des grands nombres. Enfin, la convergence en loi a été développée pour formaliser le théorème central limite, où l'on ne s'intéresse plus aux variables elles-mêmes, mais à la forme limite de leur distribution.

D'un point de vue physique, ces modes de convergence reflètent différentes manières dont un système aléatoire se stabilise:
- La **convergence presque sûre** correspond à une trajectoire physique qui finit par se confondre exactement avec la trajectoire limite, l'ensemble des trajectoires aberrantes étant de probabilité nulle (comme un système dissipatif qui s'arrête).
- La **convergence en probabilité** signifie que la probabilité d'observer le système loin de son état limite à un instant donné s'estompe, bien qu'il puisse y avoir sporadiquement de grandes fluctuations.
- La **convergence en moyenne ($L^p$)** indique que l'énergie moyenne (pour p=2) de l'écart au système limite tend vers zéro.
- La **convergence en loi** décrit un état macroscopique stationnaire: l'état microscopique peut fluctuer, mais la fraction du temps passée dans chaque région de l'espace des phases (la distribution statistique) se fige.

## Définitions, Théorèmes et Exemples

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé. Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires réelles et $X$ une variable aléatoire réelle.

### Convergence Presque Sûre

**Définition (Convergence presque sûre).**
La suite $(X_n)$ converge presque sûrement vers $X$, noté $X_n \xrightarrow{p.s.} X$, si et seulement si l'ensemble des $\omega \in \Omega$ pour lesquels la suite numérique $(X_n(\omega))$ converge vers $X(\omega)$ est de probabilité 1 :
$$ \mathbb{P}\left(\left\{ \omega \in \Omega \mid \lim_{n \to +\infty} X_n(\omega) = X(\omega) \right\}\right) = 1. $$

*Exemple 1 : L'archer infaillible asymptotiquement.*
Soit $\Omega = [0, 1]$ muni de la mesure de Lebesgue. Définissons $X_n(\omega) = \omega^n$. Pour tout $\omega \in [0, 1[$, $\lim_{n \to \infty} \omega^n = 0$. Pour $\omega = 1$, $\lim_{n \to \infty} 1^n = 1$. L'ensemble des $\omega$ où la limite est 0 est $[0, 1[$, de mesure 1. Donc $X_n \xrightarrow{p.s.} 0$. L'événement exceptionnel $\{\omega = 1\}$ a une probabilité nulle.

### Convergence en Probabilité

**Définition (Convergence en probabilité).**
La suite $(X_n)$ converge en probabilité vers $X$, noté $X_n \xrightarrow{\mathbb{P}} X$, si pour tout $\varepsilon > 0$, la probabilité que l'écart entre $X_n$ et $X$ dépasse $\varepsilon$ tend vers 0 lorsque $n \to +\infty$ :
$$ \forall \varepsilon > 0, \quad \lim_{n \to +\infty} \mathbb{P}(|X_n - X| > \varepsilon) = 0. $$

*Exemple 2 : Le promeneur farfelu.*
Considérons une suite $X_n$ valant $n$ avec probabilité $\frac{1}{n}$, et $0$ avec probabilité $1 - \frac{1}{n}$. Soit $\varepsilon \in ]0, 1[$.
L'événement $\{|X_n - 0| > \varepsilon\}$ se réduit à l'événement $\{X_n = n\}$, car pour $n \ge 1$, $n > \varepsilon$.
La probabilité est $\mathbb{P}(X_n = n) = \frac{1}{n}$. Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, nous avons $X_n \xrightarrow{\mathbb{P}} 0$.
Cependant, l'écart peut être immense ($n$), mais cela se produit de plus en plus rarement.

### Convergence en Moyenne d'Ordre p ($L^p$)

**Définition (Convergence dans $L^p$).**
Soit $p \ge 1$. Supposons que $\mathbb{E}[|X_n|^p] < +\infty$ et $\mathbb{E}[|X|^p] < +\infty$. La suite $(X_n)$ converge dans $L^p$ vers $X$, noté $X_n \xrightarrow{L^p} X$, si l'espérance de la puissance $p$-ième de l'écart tend vers 0 :
$$ \lim_{n \to +\infty} \mathbb{E}[|X_n - X|^p] = 0. $$
Si $p=1$, on parle de convergence en moyenne. Si $p=2$, on parle de convergence en moyenne quadratique.

*Exemple 3 : Calcul explicite d'erreur quadratique.*
Soit $X_n$ une variable de loi uniforme sur $[0, \frac{1}{n}]$. Étudions la convergence vers 0 dans $L^2$.
$\mathbb{E}[|X_n - 0|^2] = \int_0^{1/n} x^2 \cdot (n) \,dx = n \left[\frac{x^3}{3}\right]_0^{1/n} = n \frac{1}{3n^3} = \frac{1}{3n^2}$.
Comme $\lim_{n \to \infty} \frac{1}{3n^2} = 0$, nous avons $X_n \xrightarrow{L^2} 0$.

### Convergence en Loi

**Définition (Convergence en loi).**
La suite $(X_n)$ converge en loi vers $X$, noté $X_n \xrightarrow{\mathcal{L}} X$ ou $X_n \implies X$, si pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée :
$$ \lim_{n \to +\infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]. $$

*Exemple 4 : Convergence des distributions.*
Soit $X_n = \frac{1}{n}$. La variable $X_n$ est déterministe. Soit $X = 0$.
Pour toute fonction $f$ continue, $\lim_{n \to \infty} f(X_n) = f(0)$ (par continuité).
Ici, $\mathbb{E}[f(X_n)] = f(\frac{1}{n})$ et $\mathbb{E}[f(X)] = f(0)$.
Donc $\lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$. Ainsi, la constante $\frac{1}{n}$ converge en loi vers 0.

### Théorème des Hiérarchies de Convergence

**Théorème.**
Les implications suivantes sont strictement vraies :
1. $X_n \xrightarrow{p.s.} X \implies X_n \xrightarrow{\mathbb{P}} X$
2. $X_n \xrightarrow{L^p} X \implies X_n \xrightarrow{\mathbb{P}} X$
3. $X_n \xrightarrow{\mathbb{P}} X \implies X_n \xrightarrow{\mathcal{L}} X$

De plus, si $p > q \ge 1$, alors $X_n \xrightarrow{L^p} X \implies X_n \xrightarrow{L^q} X$.

Les réciproques sont fausses en général. Cependant, si $X_n \xrightarrow{\mathbb{P}} X$, on peut extraire une sous-suite $(X_{\phi(n)})$ telle que $X_{\phi(n)} \xrightarrow{p.s.} X$. De plus, si $X_n \xrightarrow{\mathcal{L}} c$ où $c$ est une constante, alors $X_n \xrightarrow{\mathbb{P}} c$.

*Exemple 5 : Contre-exemple $L^p$ n'implique pas presque sûre.*
L'exemple 2 montre que $X_n \xrightarrow{\mathbb{P}} 0$. Regardons $L^1$ : $\mathbb{E}[|X_n|] = n \times \frac{1}{n} = 1 \neq 0$.
Donc la convergence en probabilité n'implique pas la convergence dans $L^p$.

\begin{tikzpicture}[scale=1.5, every node/.style={transform shape}]
  \node (Lp) at (0, 2) [rectangle, draw=blue, thick, fill=blue!10, rounded corners, align=center] {Convergence dans $L^p$ \\ $X_n \xrightarrow{L^p} X$};
  \node (PS) at (0, -2) [rectangle, draw=red, thick, fill=red!10, rounded corners, align=center] {Convergence Presque Sûre \\ $X_n \xrightarrow{p.s.} X$};
  \node (P) at (4, 0) [rectangle, draw=purple, thick, fill=purple!10, rounded corners, align=center] {Convergence en Probabilité \\ $X_n \xrightarrow{\mathbb{P}} X$};
  \node (L) at (8, 0) [rectangle, draw=green!70!black, thick, fill=green!10, rounded corners, align=center] {Convergence en Loi \\ $X_n \xrightarrow{\mathcal{L}} X$};

  \draw[->, thick, blue] (Lp) to[out=0, in=120] (P);
  \draw[->, thick, red] (PS) to[out=0, in=-120] (P);
  \draw[->, thick, purple] (P) to (L);

  \node at (2, 1.2) [rotate=-25] {Inégalité de Markov};
  \node at (2, -1.2) [rotate=25] {Lemme de Borel-Cantelli};
  \node at (6, 0.3) {Lemme de Portmanteau};
\end{tikzpicture}

## Démonstrations

### Démonstration : $L^p \implies \mathbb{P}$

**Théorème.** Soit $p \ge 1$. Si $X_n \xrightarrow{L^p} X$, alors $X_n \xrightarrow{\mathbb{P}} X$.

**Preuve rigoureuse.**
Supposons que $X_n \xrightarrow{L^p} X$. Cela signifie par définition que $\lim_{n \to +\infty} \mathbb{E}[|X_n - X|^p] = 0$.
Soit $\varepsilon > 0$ fixé arbitrairement. Nous cherchons à évaluer $\mathbb{P}(|X_n - X| > \varepsilon)$.
Considérons la variable aléatoire positive ou nulle $Y_n = |X_n - X|^p$.
Puisque la fonction $x \mapsto x^p$ est strictement croissante sur $\mathbb{R}_+$, l'événement $\{|X_n - X| > \varepsilon\}$ est exactement l'événement $\{|X_n - X|^p > \varepsilon^p\}$, c'est-à-dire $\{Y_n > \varepsilon^p\}$.
Appliquons l'inégalité de Markov à la variable aléatoire $Y_n$ qui est à valeurs positives, pour le seuil $a = \varepsilon^p > 0$ :
$$ \mathbb{P}(Y_n > a) \le \frac{\mathbb{E}[Y_n]}{a} $$
En substituant $Y_n$ et $a$ par leurs expressions :
$$ \mathbb{P}(|X_n - X|^p > \varepsilon^p) \le \frac{\mathbb{E}[|X_n - X|^p]}{\varepsilon^p} $$
Ce qui se réécrit :
$$ \mathbb{P}(|X_n - X| > \varepsilon) \le \frac{\mathbb{E}[|X_n - X|^p]}{\varepsilon^p} $$
Puisque $X_n$ converge dans $L^p$ vers $X$, le numérateur $\mathbb{E}[|X_n - X|^p]$ tend vers $0$ lorsque $n$ tend vers l'infini.
Comme $\varepsilon^p$ est une constante strictement positive, le terme de droite de l'inégalité tend vers $0$.
Par le théorème des gendarmes, sachant qu'une probabilité est minorée par $0$ :
$$ 0 \le \lim_{n \to +\infty} \mathbb{P}(|X_n - X| > \varepsilon) \le 0 $$
Ainsi, pour tout $\varepsilon > 0$, $\lim_{n \to +\infty} \mathbb{P}(|X_n - X| > \varepsilon) = 0$.
La convergence en probabilité est donc démontrée. \qed

### Démonstration : $\mathbb{P} \implies \mathcal{L}$

**Théorème.** Si $X_n \xrightarrow{\mathbb{P}} X$, alors $X_n \xrightarrow{\mathcal{L}} X$.

**Preuve rigoureuse.**
Supposons que $X_n \xrightarrow{\mathbb{P}} X$. Nous devons montrer que pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée, $\lim_{n \to +\infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$.
Soit $f$ une fonction continue et bornée. Il existe $M > 0$ tel que pour tout $x \in \mathbb{R}$, $|f(x)| \le M$.
Soit $\varepsilon > 0$ fixé.
La difficulté réside dans le fait que $f$ n'est a priori pas uniformément continue. Cependant, on peut restreindre le problème à un compact.
Puisque $X$ est une vraie variable aléatoire (à valeurs réelles finies presque sûrement), il existe un compact $K = [-A, A]$ tel que $\mathbb{P}(X \notin K) < \frac{\varepsilon}{6M}$.
La fonction $f$ étant continue sur $\mathbb{R}$, elle est uniformément continue sur le compact $[-A - 1, A + 1]$ (théorème de Heine).
Donc il existe $\delta > 0$ (avec $\delta < 1$) tel que pour tous $x, y \in [-A-1, A+1]$, si $|x - y| < \delta$, alors $|f(x) - f(y)| < \frac{\varepsilon}{3}$.
Nous évaluons l'écart en espérance :
$$ |\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| \le \mathbb{E}[|f(X_n) - f(X)|] $$
Décomposons l'espace $\Omega$ en fonction de deux critères: l'écart entre $X_n$ et $X$, et la position de $X$.
Considérons l'événement $E_n = \{|X_n - X| < \delta\}$ et l'événement $C = \{X \in K\}$.
Nous découpons l'intégrale (l'espérance) en trois parties :
$$ \mathbb{E}[|f(X_n) - f(X)|] = \mathbb{E}[|f(X_n) - f(X)| \cdot \mathbb{I}_{E_n \cap C}] + \mathbb{E}[|f(X_n) - f(X)| \cdot \mathbb{I}_{E_n^c}] + \mathbb{E}[|f(X_n) - f(X)| \cdot \mathbb{I}_{E_n \cap C^c}] $$
1. Sur $E_n \cap C$, on a $X \in K$ donc $|X| \le A$. Puisque $|X_n - X| < \delta < 1$, on a $|X_n| \le A + 1$. Ainsi, $X$ et $X_n$ sont dans le compact $[-A-1, A+1]$ et sont distants de moins de $\delta$. Par continuité uniforme, $|f(X_n) - f(X)| < \frac{\varepsilon}{3}$.
   L'espérance sur cette partie est majorée par $\frac{\varepsilon}{3} \mathbb{P}(E_n \cap C) \le \frac{\varepsilon}{3}$.
2. Sur $E_n^c$, $|X_n - X| \ge \delta$. L'écart $|f(X_n) - f(X)|$ est brutalement majoré par $2M$.
   L'espérance sur cette partie est majorée par $2M \mathbb{P}(|X_n - X| \ge \delta)$.
   Puisque $X_n \xrightarrow{\mathbb{P}} X$, il existe un rang $N$ tel que pour tout $n \ge N$, $\mathbb{P}(|X_n - X| \ge \delta) < \frac{\varepsilon}{6M}$.
   Donc pour $n \ge N$, cette partie est majorée par $2M \frac{\varepsilon}{6M} = \frac{\varepsilon}{3}$.
3. Sur $C^c$, on a $X \notin K$. L'écart est à nouveau majoré par $2M$.
   L'espérance est majorée par $2M \mathbb{P}(X \notin K)$. Par choix de $K$, ceci est strictement inférieur à $2M \frac{\varepsilon}{6M} = \frac{\varepsilon}{3}$.

En additionnant ces trois majorations pour $n \ge N$ :
$$ |\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon $$
Ceci étant vrai pour tout $\varepsilon > 0$, on a bien $\lim_{n \to +\infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$. La convergence en loi est démontrée. \qed

## Applications en Physique, Logique et Intelligence Artificielle

### Application en Physique Statistique

Dans l'étude des gaz, le théorème de limite centrale illustre comment une grandeur macroscopique comme la pression ou la température émerge d'un ensemble astronomique de collisions microscopiques indépendantes. La vitesse d'une particule au hasard suit une distribution complexe, mais la vitesse moyenne de $10^{23}$ particules converge en loi vers une distribution gaussienne (Maxwell-Boltzmann). C'est la convergence en loi qui fonde la thermodynamique, car on ne regarde plus les trajectoires individuelles (presque sûres) qui sont chaotiques, mais la statistique stabilisée du système.

### Application en Logique

En théorie des modèles aléatoires, la loi du zéro-un (qui repose sur des événements limites de probabilité 0 ou 1) utilise les modes de convergence forte. Une propriété logique du premier ordre exprimée sur un graphe aléatoire de taille $n$ (par exemple "le graphe contient un triangle") aura une probabilité de vérité qui converge, lorsque $n \to \infty$, soit vers 0, soit vers 1. La convergence presque sûre traduit alors une certitude sémantique à la limite asymptotique.

### Application en Intelligence Artificielle (Deep Learning)

En apprentissage automatique, un modèle (réseau de neurones) est entraîné via l'algorithme de Descente de Gradient Stochastique (SGD). Les poids du réseau $W_n$ à l'étape $n$ sont des variables aléatoires. L'objectif est que $W_n$ converge vers les poids optimaux $W^*$.
- Si le taux d'apprentissage $\eta$ est constant, on montre que $W_n$ ne converge pas presque sûrement ni en probabilité, mais converge en loi vers une distribution stationnaire autour de $W^*$ (le bruit stochastique empêche une immobilisation parfaite).
- Si on décroît le taux d'apprentissage (ex: $\eta_n = \frac{1}{n}$), alors l'algorithme vérifie les conditions de Robbins-Monro, et $W_n \xrightarrow{p.s.} W^*$. Cette convergence forte garantit (théoriquement) la consistance de l'apprentissage sur un temps infini, assurant que l'intelligence artificielle a effectivement appris le concept cible sans ambiguïté résiduelle.
