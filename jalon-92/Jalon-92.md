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

## Introduction historique et fondements physiques

La loi forte des grands nombres (LFGN) constitue l'un des piliers monumentaux de la théorie des probabilités modernes. Historiquement, l'intuition que la moyenne empirique converge vers l'espérance mathématique remonte à Gerolamo Cardano et Jacob Bernoulli. Cependant, c'est au XXe siècle, avec la rigueur axiomatique d'Andrey Kolmogorov (1933) basée sur la théorie de la mesure, que la loi "forte" a pu être démontrée formellement.

Contrairement à la loi faible (qui garantit une convergence en probabilité), la loi forte garantit une convergence presque sûre (avec probabilité 1). Géométriquement et physiquement, cela signifie que, dans l'espace infini des trajectoires possibles d'un processus stochastique, les trajectoires qui s'écartent asymptotiquement de la moyenne théorique constituent un ensemble de mesure de Lebesgue nulle. C'est le triomphe de la stabilité macroscopique sur le chaos microscopique, fondamental pour la physique statistique, l'ergodicité, et l'apprentissage automatique où la fonction de perte empirique doit asymptotiquement refléter l'erreur de généralisation.

\begin{tikzpicture}[scale=1]
  \draw[->] (0,0) -- (10,0) node[right] {$n$ (nombre d'essais)};
  \draw[->] (0,0) -- (0,4) node[above] {$\bar{X}_n$};

  \draw[dashed, red, thick] (0,2) -- (10,2) node[right] {$\mu$ (Espérance)};

  \draw[blue, thick] (0,0.5) -- (1,3.5) -- (2,1) -- (3,2.8) -- (4,1.5) -- (5,2.3) -- (6,1.8) -- (7,2.1) -- (8,1.95) -- (9,2.05) -- (10,2);

  \node at (5, 3.5) {\textit{Trajectoire empirique convergeant vers l'espérance}};
\end{tikzpicture}

## Définitions, Théorèmes & Exemples

### Définition 1 : Convergence presque sûre

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé et $(Y_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires réelles. On dit que $Y_n$ converge presque sûrement vers une variable aléatoire $Y$, et on note $Y_n \xrightarrow{p.s.} Y$, si :
$$ \mathbb{P}\left(\left\{\omega \in \Omega \mid \lim_{n \to \infty} Y_n(\omega) = Y(\omega)\right\}\right) = 1 $$

**Exemple concret 1 :**
Considérons une suite de lancers de pièces équilibrées où $X_i \in \{0, 1\}$.
L'espace $\Omega$ est l'ensemble de toutes les suites infinies de $\{0, 1\}^{\mathbb{N}}$.
Soit $\omega = (0, 1, 0, 1, 0, 1, \dots)$.
La moyenne empirique est $\bar{X}_n(\omega) = \frac{1}{n} \sum_{i=1}^n X_i(\omega)$.
Pour $n=2$, $\bar{X}_2 = \frac{0+1}{2} = 0.5$.
Pour $n=4$, $\bar{X}_4 = 0.5$.
La limite est exactement $0.5$. La probabilité de tirer une séquence comme $\omega = (1, 1, 1, 1, \dots)$ infinie est $0$.

### Théorème (Loi Forte des Grands Nombres de Kolmogorov)

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.) définies sur $(\Omega, \mathcal{F}, \mathbb{P})$.
Si $\mathbb{E}[|X_1|] < +\infty$ (les variables sont intégrables, soit $X_1 \in L^1$), et si l'on note $\mu = \mathbb{E}[X_1]$, alors la moyenne empirique $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ converge presque sûrement vers $\mu$ :
$$ \bar{X}_n \xrightarrow{p.s.} \mu \quad \text{lorsque } n \to \infty $$

**Exemple concret 2 (Calcul de Monte-Carlo) :**
On souhaite calculer l'intégrale $I = \int_0^1 e^{-x^2} dx$.
On tire $n$ variables $U_i$ i.i.d. de loi uniforme sur $[0,1]$. On pose $X_i = e^{-U_i^2}$.
Alors $\mathbb{E}[X_1] = \int_0^1 e^{-x^2} \cdot 1 \,dx = I$.
Pour $n=1000$, les tirages donnent $\sum_{i=1}^{1000} e^{-u_i^2} \approx 746.8$.
La moyenne $\bar{X}_{1000} = 0.7468$.
La loi forte assure que lorsque $n \to \infty$, la moyenne empirique convergera vers la vraie valeur de l'intégrale (environ $0.746824\dots$).

**Exemple concret 3 (Cas non-intégrable) :**
Soit $(C_n)_{n \ge 1}$ une suite de variables i.i.d. suivant une loi de Cauchy de densité $f(x) = \frac{1}{\pi(1+x^2)}$.
L'espérance $\mathbb{E}[|C_1|]$ est divergente.
La somme $\frac{C_1 + \dots + C_n}{n}$ suit elle-même une loi de Cauchy stricte. Elle ne converge vers aucune constante. La LFGN s'effondre sans la condition d'intégrabilité absolue.

## Démonstrations

### Preuve de la LFGN sous l'hypothèse d'un moment d'ordre 4 fini ($L^4$)

Bien que le théorème de Kolmogorov ne requiert qu'un moment d'ordre 1, la démonstration classique abordable et tout aussi instructive repose sur l'hypothèse plus forte que $X_1 \in L^4$, c'est-à-dire $\mathbb{E}[X_1^4] < +\infty$.

**Étape 1 : Centrage des variables**
Sans perte de généralité, on peut supposer que $\mu = \mathbb{E}[X_i] = 0$. (Si $\mu \neq 0$, on pose $Y_i = X_i - \mu$ qui vérifie $\mathbb{E}[Y_i]=0$ et $\mathbb{E}[Y_i^4] < \infty$).
On pose $S_n = \sum_{i=1}^n X_i$. Le but est de montrer que $\frac{S_n}{n} \xrightarrow{p.s.} 0$.

**Étape 2 : Développement du moment d'ordre 4 de $S_n$**
Calculons $\mathbb{E}[S_n^4]$.
$$ S_n^4 = \left( \sum_{i=1}^n X_i \right)^4 = \sum_{i,j,k,l \in \{1,\dots,n\}} X_i X_j X_k X_l $$
On prend l'espérance de cette somme. Par linéarité :
$$ \mathbb{E}[S_n^4] = \sum_{i,j,k,l} \mathbb{E}[X_i X_j X_k X_l] $$

Analysons les termes en fonction des indices :
1. *Quatre indices distincts ($i \neq j \neq k \neq l$)* : Par indépendance, $\mathbb{E}[X_i X_j X_k X_l] = \mathbb{E}[X_i]\mathbb{E}[X_j]\mathbb{E}[X_k]\mathbb{E}[X_l] = 0$.
2. *Un indice apparaît une fois, un autre trois fois* (ex: $i=j=k \neq l$) : $\mathbb{E}[X_i^3 X_l] = \mathbb{E}[X_i^3]\mathbb{E}[X_l] = 0$.
3. *Deux indices distincts apparaissant une fois, et un autre deux fois* (ex: $i=j \neq k \neq l$) : $\mathbb{E}[X_i^2 X_k X_l] = \mathbb{E}[X_i^2]\mathbb{E}[X_k]\mathbb{E}[X_l] = 0$.
4. *Un indice apparaît quatre fois* ($i=j=k=l$) : $\mathbb{E}[X_i^4]$. Il y a $n$ tels termes.
5. *Deux indices apparaissent deux fois chacun* ($i=j \neq k=l$) : $\mathbb{E}[X_i^2 X_k^2] = \mathbb{E}[X_i^2]\mathbb{E}[X_k^2]$. Le nombre de paires possibles est $\binom{n}{2} = \frac{n(n-1)}{2}$, et pour chaque paire, il y a $\binom{4}{2} = 6$ façons de choisir les places. Il y a donc $3n(n-1)$ tels termes.

Posons $M = \max(\mathbb{E}[X_1^4], 3(\mathbb{E}[X_1^2])^2) < +\infty$.
Ainsi, $\mathbb{E}[S_n^4] \le n \mathbb{E}[X_1^4] + 3n(n-1) (\mathbb{E}[X_1^2])^2 \le n M + 3n^2 M \le C n^2$ pour une certaine constante $C$.

**Étape 3 : Application de l'inégalité de Markov**
On cherche à borner la probabilité que la moyenne s'éloigne de $0$. Pour tout $\epsilon > 0$, l'inégalité de Markov (appliquée à la variable positive $(S_n/n)^4$) donne :
$$ \mathbb{P}\left( \left| \frac{S_n}{n} \right| \ge \epsilon \right) = \mathbb{P}\left( \left( \frac{S_n}{n} \right)^4 \ge \epsilon^4 \right) \le \frac{\mathbb{E}[(S_n/n)^4]}{\epsilon^4} $$

Remplaçons $\mathbb{E}[(S_n/n)^4]$ par sa valeur :
$$ \mathbb{P}\left( \left| \frac{S_n}{n} \right| \ge \epsilon \right) \le \frac{1}{\epsilon^4 n^4} \mathbb{E}[S_n^4] \le \frac{C n^2}{\epsilon^4 n^4} = \frac{C}{\epsilon^4 n^2} $$

**Étape 4 : Utilisation du Lemme de Borel-Cantelli**
Soit $\epsilon > 0$ fixé. Posons les événements $A_n = \left\{ \left| \frac{S_n}{n} \right| \ge \epsilon \right\}$.
Nous venons de montrer que $\mathbb{P}(A_n) \le \frac{C}{\epsilon^4 n^2}$.
La série $\sum_{n=1}^\infty \mathbb{P}(A_n)$ est donc majorée par $\sum_{n=1}^\infty \frac{C}{\epsilon^4 n^2}$, qui est une série de Riemann convergente ($2 > 1$).

Puisque la somme des probabilités est finie ($\sum \mathbb{P}(A_n) < +\infty$), le lemme de Borel-Cantelli implique que :
$$ \mathbb{P}\left( \limsup_{n \to \infty} A_n \right) = 0 $$
Cela signifie que, presque sûrement, l'événement $A_n$ ne se produit qu'un nombre fini de fois. Donc pour un $n$ assez grand, $\left| \frac{S_n}{n} \right| < \epsilon$.
Ceci étant vrai pour tout $\epsilon > 0$, on conclut que $\frac{S_n}{n} \xrightarrow{p.s.} 0$. $\blacksquare$

## Applications en Physique, Logique & Intelligence Artificielle

En physique statistique, la loi forte des grands nombres justifie l'hypothèse ergodique : la moyenne temporelle d'un système thermodynamique équivaut asymptotiquement à sa moyenne spatiale (sur l'ensemble des configurations possibles). La pression exercée par un gaz sur une paroi n'est qu'une application macroscopique de la LFGN sur les milliards de chocs moléculaires microscopiques.

En intelligence artificielle, la LFGN est la pierre d'angle de la théorie de l'apprentissage statistique de Vapnik-Chervonenkis. Lors de la minimisation du risque empirique, le concepteur du réseau de neurones calcule le gradient sur un mini-batch (ou l'intégralité du jeu de données d'entraînement) pour estimer le vrai gradient sur la distribution de données inconnue $\mathcal{D}$. La LFGN garantit formellement que :
$$ \frac{1}{N} \sum_{i=1}^N \nabla_\theta \mathcal{L}(f_\theta(x_i), y_i) \xrightarrow{p.s.} \mathbb{E}_{(x,y)\sim \mathcal{D}} [\nabla_\theta \mathcal{L}(f_\theta(x), y)] $$
Sans cette garantie asymptotique, aucune méthode d'optimisation par descente de gradient stochastique (SGD) ne serait fondée mathématiquement.
