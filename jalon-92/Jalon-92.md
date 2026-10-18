---
uuid: "jalon-92"
title: "Loi forte des grands nombres (LFGN)"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon 91 (Inégalités de concentration).md]]"
next: "[[Jalon 93 (Fonctions caractéristiques).md]]"
---

# Jalon 92 : Loi forte des grands nombres (LFGN)

## 1. Introduction (Genèse et Intuition)

Imaginons une pièce de monnaie truquée qui tombe sur "Pile" avec une probabilité de $1/3$. Si on la lance trois fois, on pourrait très bien n'obtenir que des "Face". La fréquence observée serait de $0\%$. Cependant, si l'on répète l'expérience un grand nombre de fois, disons un million, la fréquence de "Pile" s'approchera inexorablement de $33.33\%$.
La Loi forte des grands nombres (LFGN) est le théorème qui mathématise cette intuition : elle affirme que la moyenne empirique d'une suite de variables aléatoires indépendantes et identiquement distribuées converge, presque sûrement, vers leur espérance mathématique. C'est le fondement théorique qui légitime l'usage des statistiques en permettant d'estimer des probabilités inobservables à partir de fréquences observées empiriquement.

\begin{tikzpicture}[scale=1.5, >=stealth]
    % Axes
    \draw[->] (0,0) -- (6,0) node[right] {$n$ (nombre d'essais)};
    \draw[->] (0,0) -- (0,3) node[above] {$\bar{X}_n$ (moyenne empirique)};

    % Valeur théorique (Espérance)
    \draw[dashed, red, thick] (0,1.5) -- (6,1.5) node[right] {$\mu$};

    % Trajectoire 1 (bleue)
    \draw[blue, thick] (0.1,0.5) -- (0.5,2.5) -- (1,0.8) -- (1.5,1.8) -- (2,1.2) -- (2.5,1.6) -- (3,1.4) -- (4,1.55) -- (5,1.48) -- (5.8,1.51);

    % Trajectoire 2 (verte)
    \draw[green!60!black, thick] (0.1,2.8) -- (0.6,0.3) -- (1.2,2.0) -- (1.8,1.1) -- (2.3,1.7) -- (3.2,1.45) -- (4.2,1.52) -- (5.2,1.49) -- (5.8,1.5);

    \node at (3, 2.5) {Convergence presque sûre vers $\mu$};
\end{tikzpicture}

## 2. Définitions, Théorèmes et Exemples

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles définies sur un même espace de probabilité $(\Omega, \mathcal{F}, P)$.
On pose $S_n = \sum_{i=1}^n X_i$ et $\bar{X}_n = \frac{S_n}{n}$ la moyenne empirique des $n$ premières variables.

**Définition (Variables I.I.D.)**
On dit que la suite $(X_n)$ est indépendante et identiquement distribuée (I.I.D.) si :
1. Pour toute famille finie d'indices, les variables correspondantes sont mutuellement indépendantes.
2. Toutes les variables $X_n$ suivent la même loi de probabilité (et ont donc, si elles existent, même espérance et même variance).

**Théorème (Loi Forte des Grands Nombres - Kolmogorov)**
Soit $(X_n)$ une suite de variables aléatoires I.I.D.
Si $X_1$ est intégrable (c'est-à-dire $\mathbb{E}[|X_1|] < \infty$), alors en posant $\mu = \mathbb{E}[X_1]$, la moyenne empirique $\bar{X}_n$ converge presque sûrement vers $\mu$ :
$$P\left( \lim_{n \to \infty} \bar{X}_n = \mu \right) = 1$$
Ce que l'on note aussi : $\bar{X}_n \xrightarrow{p.s.} \mu$.

*Remarque :* La loi forte (convergence presque sûre) implique la loi faible (convergence en probabilité étudiée au Jalon 91), mais l'inverse est faux. La LFGN affirme que l'ensemble des trajectoires $\omega \mapsto \bar{X}_n(\omega)$ qui ne convergent pas vers $\mu$ est de probabilité nulle.

**Exemple Concret (Lancer de dé équilibré)**
Soit $X_i$ le résultat du $i$-ème lancer d'un dé à 6 faces. Les variables $(X_n)$ sont I.I.D. selon une loi uniforme sur $\{1, 2, 3, 4, 5, 6\}$.
L'espérance est $\mu = \mathbb{E}[X_1] = \frac{1+2+3+4+5+6}{6} = 3.5$.
La LFGN garantit que si on lance le dé une infinité de fois, la moyenne des résultats convergera, pour presque toutes les séquences de lancers, vers $3.5$.

**Cas Pathologique : Le piège de la loi de Cauchy**
Si $(X_n)$ suit une loi de Cauchy de densité $f(x) = \frac{1}{\pi(1+x^2)}$, alors $\int_{-\infty}^\infty |x| f(x) dx$ diverge. Les variables n'admettent pas d'espérance. Dans ce cas, la moyenne empirique $\bar{X}_n$ ne converge pas. Au contraire, $\bar{X}_n$ suit elle-même la même loi de Cauchy que $X_1$ pour tout $n$, exhibant des variations sauvages (des valeurs extrêmes qui empêchent toute stabilisation) quelle que soit la taille de $n$.

## 3. Démonstrations

Nous démontrons ici une version légèrement plus faible du théorème, en supposant que les variables aléatoires possèdent un moment d'ordre 4 fini. Cette approche permet de mettre en lumière l'utilisation des inégalités de concentration et du lemme de Borel-Cantelli.

**Théorème (Loi Forte sous hypothèse de moment d'ordre 4 fini)**
Soit $(X_n)$ une suite de variables I.I.D. telles que $\mathbb{E}[X_1^4] < \infty$. Alors, $\bar{X}_n \xrightarrow{p.s.} \mathbb{E}[X_1]$.

**Démonstration pas à pas :**
Quitte à considérer $Y_n = X_n - \mathbb{E}[X_1]$, on peut supposer sans perte de généralité que $\mathbb{E}[X_i] = 0$. On pose $\mu = 0$ et $S_n = \sum_{i=1}^n X_i$.

1. *Calcul de $\mathbb{E}[S_n^4]$ :*
On développe $S_n^4 = (\sum_{i=1}^n X_i)^4$. La somme contient $n^4$ termes de la forme $X_i X_j X_k X_l$.
Par linéarité de l'espérance et par indépendance des $X_i$, l'espérance d'un produit est le produit des espérances.
Comme $\mathbb{E}[X_i] = 0$, tout terme contenant une variable à la puissance 1 (par exemple $X_1^3 X_2$, $X_1^2 X_2 X_3$, etc.) aura une espérance nulle.
Les seuls termes non nuls dans $\mathbb{E}[S_n^4]$ sont :
- Les termes de la forme $X_i^4$. Il y en a $n$, chacun d'espérance $\mathbb{E}[X_1^4]$.
- Les termes de la forme $X_i^2 X_j^2$ (avec $i \neq j$). Pour les choisir, on sélectionne 2 indices parmi $n$ (soit $\frac{n(n-1)}{2}$ choix), et le coefficient multinomial associé est $\frac{4!}{2!2!} = 6$. Il y a donc $3n(n-1)$ tels termes, chacun d'espérance $\mathbb{E}[X_1^2 X_2^2] = \mathbb{E}[X_1^2]\mathbb{E}[X_2^2] = (\mathbb{E}[X_1^2])^2$.
Ainsi :
$$\mathbb{E}[S_n^4] = n \mathbb{E}[X_1^4] + 3n(n-1)(\mathbb{E}[X_1^2])^2$$
Puisque $\mathbb{E}[X_1^4] < \infty$, $(\mathbb{E}[X_1^2])^2$ est également fini (par l'inégalité de Cauchy-Schwarz). On peut donc majorer par une constante $C > 0$ :
$$\mathbb{E}[S_n^4] \leq C n^2$$

2. *Inégalité de concentration :*
Fixons un écart $\epsilon > 0$. On cherche à borner la probabilité $P(|\bar{X}_n| \geq \epsilon)$.
$$P(|\bar{X}_n| \geq \epsilon) = P\left(\left|\frac{S_n}{n}\right| \geq \epsilon\right) = P(|S_n| \geq n\epsilon) = P(S_n^4 \geq n^4 \epsilon^4)$$
Appliquons l'inégalité de Markov à la variable aléatoire positive $S_n^4$ :
$$P(S_n^4 \geq n^4 \epsilon^4) \leq \frac{\mathbb{E}[S_n^4]}{n^4 \epsilon^4} \leq \frac{C n^2}{n^4 \epsilon^4} = \frac{C}{\epsilon^4} \frac{1}{n^2}$$

3. *Application du lemme de Borel-Cantelli :*
Considérons la série des probabilités de ces événements.
$$\sum_{n=1}^\infty P(|\bar{X}_n| \geq \epsilon) \leq \sum_{n=1}^\infty \frac{C}{\epsilon^4 n^2}$$
Comme la série de Riemann $\sum \frac{1}{n^2}$ est convergente, la série $\sum P(|\bar{X}_n| \geq \epsilon)$ converge.
D'après le premier lemme de Borel-Cantelli, la probabilité que l'événement $\{|\bar{X}_n| \geq \epsilon\}$ se réalise une infinité de fois est nulle.
Ainsi, presque sûrement, pour $n$ assez grand, on a $|\bar{X}_n| < \epsilon$.

4. *Conclusion :*
L'événement "$\lim_{n \to \infty} \bar{X}_n = 0$" s'écrit $\bigcap_{k \in \mathbb{N}^*} \bigcup_{N \in \mathbb{N}} \bigcap_{n \geq N} \{|\bar{X}_n| < 1/k\}$.
L'intersection dénombrable d'événements de probabilité 1 étant de probabilité 1, on conclut que $\bar{X}_n \xrightarrow{p.s.} 0$, soit $\bar{X}_n \xrightarrow{p.s.} \mu$.

## 4. Applications en Physique, Logique et IA

### A. Intégration de Monte-Carlo
La méthode de Monte-Carlo repose entièrement sur la LFGN pour estimer des intégrales complexes en grande dimension.
Soit $f$ une fonction définie sur $[0,1]^d$. L'intégrale $I = \int_{[0,1]^d} f(x) dx$ peut être vue comme l'espérance $\mathbb{E}[f(U)]$ où $U$ suit une loi uniforme sur $[0,1]^d$.
En tirant $(U_1, \dots, U_n)$ I.I.D. selon cette loi, la moyenne empirique $\frac{1}{n}\sum_{i=1}^n f(U_i)$ converge presque sûrement vers $I$. Cela permet d'estimer des aires ou des volumes de manière algorithmique.

\begin{tikzpicture}[scale=2, >=stealth]
    % Carré unité
    \draw (0,0) rectangle (1,1);
    % Quart de cercle
    \draw[fill=blue!10, domain=0:1] plot (\x, {sqrt(1-\x*\x)}) -- (0,0) -- cycle;
    % Points
    \foreach \i in {1,...,40} {
        \pgfmathsetmacro{\x}{rnd}
        \pgfmathsetmacro{\y}{rnd}
        \pgfmathparse{\x*\x+\y*\y<=1 ? "blue" : "red"}
        \fill[\pgfmathresult] (\x,\y) circle (0.015);
    }
    \node at (0.5, -0.2) {Estimation de $\pi/4$ par Monte-Carlo};
\end{tikzpicture}

### B. Apprentissage Automatique et Validation Croisée
Dans le modèle d'apprentissage PAC (Probably Approximately Correct), l'objectif est de minimiser le risque théorique (ou espérance de la perte sur toute la distribution des données). Ce risque étant inaccessible, on minimise à la place le risque empirique (la moyenne de la perte sur l'ensemble d'entraînement). La LFGN garantit que, pour un classifieur donné, le risque empirique converge vers le risque théorique lorsque la taille du jeu de données tend vers l'infini. C'est ce qui justifie l'évaluation des modèles par validation croisée.

### C. Entraînement par Batch (Stochastic Gradient Descent)
Lors de l'entraînement des réseaux de neurones, le vrai gradient de la fonction de coût s'exprime comme une espérance sur toute la distribution des données. On l'estime sur un "batch" (lot) de taille $B$.
$$g_{batch} = \frac{1}{B} \sum_{i=1}^B \nabla_{\theta} L(f_\theta(x_i), y_i)$$
Par la LFGN, plus la taille du batch $B$ est grande, plus $g_{batch}$ converge presque sûrement vers le vrai gradient théorique. C'est le compromis fondamental entre la stochasticité (pour échapper aux minima locaux) et la précision du gradient (pour converger stablement).
