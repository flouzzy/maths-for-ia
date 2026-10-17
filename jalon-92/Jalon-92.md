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
# Jalon 92 : Loi Forte des Grands Nombres (LFGN)

## 1. Introduction à la genèse du concept

Historiquement, l'appréhension mathématique du hasard s'est construite sur la notion de fréquence empirique. Depuis les travaux de Gerolamo Cardano au XVIe siècle et de Jacob Bernoulli au début du XVIIIe siècle, on pressentait qu'en répétant une expérience aléatoire un grand nombre de fois, la moyenne des résultats observés devait se rapprocher d'une valeur théorique : l'espérance.

Bernoulli formula la Loi Faible des Grands Nombres, qui assure une convergence en probabilité. Cependant, cette loi n'exclut pas l'existence de fluctuations occasionnelles arbitrairement grandes pour un nombre d'expériences très élevé. C'est Andrey Kolmogorov en 1933, dans ses "Fondements de la théorie des probabilités", qui a doté cette intuition d'une structure rigoureuse via la théorie de la mesure et l'intégrale de Lebesgue, formulant ainsi la **Loi Forte des Grands Nombres**. Elle garantit que la probabilité d'observer de telles déviations pour un nombre infini de lancers est strictement nulle.

Ce théorème justifie la méthode statistique elle-même. Il permet de passer de l'induction expérimentale (les fréquences observées) à la déduction théorique (les probabilités intrinsèques du modèle), assurant que les fluctuations chaotiques individuelles s'effacent inexorablement devant la loi de masse.

## 2. Définitions, Théorèmes et Exemples

Nous nous plaçons sur un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$.

> **Définition 1 (Suite de variables aléatoires I.I.D.)**
> Une suite de variables aléatoires $(X_n)_{n \in \mathbb{N}^*}$ est dite indépendante et identiquement distribuée (I.I.D.) si :
> 1. Pour toute partie finie $J \subset \mathbb{N}^*$ et tout sous-ensemble borélien $B_j \subset \mathbb{R}$, on a : $\mathbb{P}\left(\bigcap_{j \in J} \{X_j \in B_j\}\right) = \prod_{j \in J} \mathbb{P}(X_j \in B_j)$
> 2. Il existe une loi de probabilité $\mu_X$ telle que pour tout $n \in \mathbb{N}^*$, la loi de $X_n$ est $\mu_X$.

> **Définition 2 (Convergence presque sûre)**
> Une suite de variables aléatoires $(Y_n)_{n \in \mathbb{N}^*}$ converge presque sûrement vers une variable aléatoire $Y$, notée $Y_n \xrightarrow{p.s.} Y$, si :
> $$\mathbb{P}\left(\left\{\omega \in \Omega \mid \lim_{n \to \infty} Y_n(\omega) = Y(\omega)\right\}\right) = 1$$

> **Théorème 1 (Loi Forte des Grands Nombres de Kolmogorov)**
> Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles I.I.D.
> Si $\mathbb{E}[|X_1|] < +\infty$, alors en notant $\mu = \mathbb{E}[X_1]$, on a la convergence de la moyenne empirique :
> $$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{p.s.} \mu$$
> Réciproquement, si la moyenne empirique converge presque sûrement, alors $\mathbb{E}[|X_1|] < +\infty$.

**Exemple 1 : Lancer de dé équilibré**
Soit $X_i$ le résultat du $i$-ème lancer d'un dé parfait à 6 faces.
- Les variables $(X_i)$ sont I.I.D. suivant une loi uniforme discrète sur $\{1, 2, 3, 4, 5, 6\}$.
- L'espérance est $\mu = \mathbb{E}[X_1] = \frac{1+2+3+4+5+6}{6} = 3.5$.
La LFGN affirme que la moyenne des $n$ premiers lancers, $\frac{1}{n} \sum_{i=1}^n X_i$, va converger presque sûrement vers $3.5$. Si l'on obtient $(1, 6, 2, 6)$ pour $n=4$, la moyenne est $3.75$. Si l'on lance le dé 10 000 fois, la probabilité que la moyenne soit éloignée de $3.5$ est pratiquement nulle.

**Exemple 2 : Méthode de Monte-Carlo pour estimer une intégrale**
Considérons l'intégrale $I = \int_0^1 \sin(\pi x) dx$.
On sait que la valeur exacte est $\left[ -\frac{\cos(\pi x)}{\pi} \right]_0^1 = \frac{2}{\pi} \approx 0.6366$.
Prenons une suite $(U_i)$ de variables aléatoires I.I.D. de loi uniforme sur $[0, 1]$.
Posons $X_i = \sin(\pi U_i)$. Alors $X_i$ sont I.I.D. et $\mathbb{E}[X_1] = \int_0^1 \sin(\pi x) dx = I$.
Selon la LFGN, l'estimateur $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n \sin(\pi U_i)$ convergera presque sûrement vers $\frac{2}{\pi}$. C'est la base de l'intégration de Monte-Carlo.

**Exemple 3 : Pièce truquée (Loi de Bernoulli)**
Une pièce a une probabilité $p=0.3$ de tomber sur Pile.
Posons $X_i = 1$ pour Pile, et $X_i = 0$ pour Face.
Les $X_i$ sont I.I.D. de loi $\mathcal{B}(p)$. L'espérance est $\mathbb{E}[X_1] = p = 0.3$.
La fréquence empirique des "Pile", qui est exactement $\frac{1}{n} \sum_{i=1}^n X_i$, converge presque sûrement vers $0.3$.

**Exemple 4 : Estimation de la variance (Méthode des moments)**
Si les $(X_i)$ sont I.I.D. avec $\mathbb{E}[X_1] = \mu$ et $\text{Var}(X_1) = \sigma^2 < \infty$.
Posons $Y_i = (X_i - \mu)^2$. Les $(Y_i)$ sont I.I.D., intégrables, avec $\mathbb{E}[Y_1] = \text{Var}(X_1) = \sigma^2$.
Par la LFGN, $\frac{1}{n} \sum_{i=1}^n (X_i - \mu)^2 \xrightarrow{p.s.} \sigma^2$.
Si $\mu$ est inconnu, on prouve (avec l'estimateur sans biais) que $\frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}_n)^2$ converge aussi presque sûrement vers $\sigma^2$.

**Exemple 5 : Contre-exemple pathologique (La loi de Cauchy)**
La loi de Cauchy standard a pour densité de probabilité $f(x) = \frac{1}{\pi(1+x^2)}$.
Calculons son espérance : $\mathbb{E}[|X_1|] = \int_{-\infty}^{\infty} |x| \frac{1}{\pi(1+x^2)} dx = \frac{2}{\pi} \int_0^\infty \frac{x}{1+x^2} dx$.
Cette intégrale diverge car une primitive est $\frac{1}{2}\ln(1+x^2)$, qui tend vers l'infini.
L'espérance n'est donc pas définie (non intégrable).
Si on génère $(X_1, ..., X_n)$ I.I.D. de Cauchy et on calcule $\bar{X}_n$, cette moyenne a *exactement* la même distribution de Cauchy que $X_1$ ! Elle ne se "resserre" jamais. Elle subira perpétuellement des sauts arbitrairement grands occasionnés par l'apparition de valeurs extrêmes.

**Exemple 6 : Processus de Poisson empirique**
Considérons l'arrivée des bus à une station. Le temps d'attente $T_i$ entre le $(i-1)$-ème et le $i$-ème bus est modélisé par une variable exponentielle $\mathcal{E}(\lambda)$, d'espérance $\frac{1}{\lambda}$.
Le temps total d'attente pour $n$ bus est $S_n = \sum_{i=1}^n T_i$.
La LFGN garantit que le temps moyen d'attente par bus $\frac{S_n}{n}$ converge vers $\frac{1}{\lambda}$.
En inversant, le nombre de bus par unité de temps convergera presque sûrement vers $\lambda$.

## 3. Démonstration de la Loi Forte des Grands Nombres (cas d'un moment d'ordre 4 fini)

Bien que le théorème de Kolmogorov requière uniquement $\mathbb{E}[|X_1|] < +\infty$, la démonstration de ce résultat général est extrêmement technique et repose sur des troncatures (Lemme de Kronecker, Inégalité de Kolmogorov). Nous allons présenter ici la démonstration exhaustive sous l'hypothèse (physiquement très commune) que le quatrième moment de la distribution existe, c'est-à-dire $\mathbb{E}[X_1^4] < +\infty$.

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles I.I.D. admettant un moment d'ordre 4, $\mathbb{E}[X_1^4] < +\infty$.
Puisque le moment d'ordre 4 est fini, les moments d'ordres inférieurs (variance et espérance) le sont aussi.
Posons $\mu = \mathbb{E}[X_1]$.
On va poser $Y_i = X_i - \mu$. Les variables $(Y_i)$ sont I.I.D., centrées ($\mathbb{E}[Y_i] = 0$), et $\mathbb{E}[Y_1^4] < +\infty$.

Soit $S_n = \sum_{i=1}^n Y_i$. Nous cherchons à montrer que $\frac{S_n}{n} \xrightarrow{p.s.} 0$.

**Étape 1 : Calcul du moment d'ordre 4 de la somme $S_n$**
$$\mathbb{E}[S_n^4] = \mathbb{E}\left[ \left( \sum_{i=1}^n Y_i \right)^4 \right]$$

Développons le polynôme $(Y_1 + Y_2 + \dots + Y_n)^4$. Ce développement donne des termes de différentes formes :
$$S_n^4 = \sum_{i,j,k,l=1}^n Y_i Y_j Y_k Y_l$$
Puisque l'espérance est linéaire, on calcule $\mathbb{E}[Y_i Y_j Y_k Y_l]$.
On va analyser les différents cas de regroupement des indices, en utilisant l'indépendance des $Y_i$.
Si $i, j, k, l$ sont tous distincts : par indépendance, $\mathbb{E}[Y_i Y_j Y_k Y_l] = \mathbb{E}[Y_i]\mathbb{E}[Y_j]\mathbb{E}[Y_k]\mathbb{E}[Y_l] = 0$ car ils sont centrés.
Si un indice apparaît exactement une fois (et les autres regroupés), par exemple $Y_i^3 Y_j$ (avec $i \neq j$) : $\mathbb{E}[Y_i^3 Y_j] = \mathbb{E}[Y_i^3]\mathbb{E}[Y_j] = 0$.
Si un indice apparaît exactement une fois et un autre deux fois, par exemple $Y_i^2 Y_j Y_k$ (distincts) : $\mathbb{E}[Y_i^2 Y_j Y_k] = \mathbb{E}[Y_i^2]\mathbb{E}[Y_j]\mathbb{E}[Y_k] = 0$.

Il ne reste que deux types de termes non nuls :
- Tous les indices sont égaux : termes de la forme $Y_i^4$. Il y en a $n$. Leur espérance est $\mathbb{E}[Y_1^4]$.
- Les indices sont groupés par paires distinctes : termes de la forme $Y_i^2 Y_j^2$ (avec $i \neq j$).
  Combien y a-t-il de telles paires ? Il faut choisir 2 positions parmi 4 pour l'indice $i$ (soit $\binom{4}{2} = 6$ combinaisons), puis choisir 2 indices distincts $i < j$ parmi $n$ (soit $\binom{n}{2} = \frac{n(n-1)}{2}$ paires).
  Le nombre total de termes de ce type est donc $6 \times \frac{n(n-1)}{2} = 3n(n-1)$.
  Leur espérance est $\mathbb{E}[Y_i^2 Y_j^2] = \mathbb{E}[Y_i^2]\mathbb{E}[Y_j^2] = (\mathbb{E}[Y_1^2])^2$.

En sommant, nous obtenons :
$$\mathbb{E}[S_n^4] = n \mathbb{E}[Y_1^4] + 3n(n-1) (\mathbb{E}[Y_1^2])^2$$
Puisque $\mathbb{E}[Y_1^4]$ et $(\mathbb{E}[Y_1^2])^2$ sont des constantes indépendantes de $n$, il existe une constante $C > 0$ (qui ne dépend que de la distribution de $X_1$) telle que :
$$\mathbb{E}[S_n^4] \le C n^2 \quad \text{pour tout } n \ge 1.$$

**Étape 2 : Majoration par l'inégalité de Markov**
Pour un $\epsilon > 0$ fixé, considérons l'événement $A_n = \{ |\frac{S_n}{n}| > \epsilon \}$.
On remarque que $|\frac{S_n}{n}| > \epsilon \iff \left(\frac{S_n}{n}\right)^4 > \epsilon^4 \iff S_n^4 > n^4 \epsilon^4$.
Puisque $S_n^4$ est une variable aléatoire positive ou nulle, nous appliquons l'inégalité de Markov :
$$\mathbb{P}(A_n) = \mathbb{P}(S_n^4 > n^4 \epsilon^4) \le \frac{\mathbb{E}[S_n^4]}{n^4 \epsilon^4}$$
En utilisant la borne trouvée à l'étape 1 :
$$\mathbb{P}(A_n) \le \frac{C n^2}{n^4 \epsilon^4} = \frac{C}{\epsilon^4 n^2}$$

**Étape 3 : Application du Lemme de Borel-Cantelli**
Considérons la série des probabilités des événements $A_n$ :
$$\sum_{n=1}^\infty \mathbb{P}(A_n) \le \sum_{n=1}^\infty \frac{C}{\epsilon^4 n^2} = \frac{C}{\epsilon^4} \sum_{n=1}^\infty \frac{1}{n^2}$$
Comme la série de Riemann $\sum \frac{1}{n^2}$ est convergente (elle vaut $\frac{\pi^2}{6}$), la série $\sum \mathbb{P}(A_n)$ est convergente.

Par le premier lemme de Borel-Cantelli, si la série des probabilités $\sum \mathbb{P}(A_n)$ converge, alors la probabilité que l'événement $A_n$ se réalise une infinité de fois est nulle.
Formellement, $\mathbb{P}(\limsup_{n \to \infty} A_n) = 0$.
Autrement dit, $\mathbb{P}(\exists n_0 \ge 1, \forall n \ge n_0, |\frac{S_n}{n}| \le \epsilon) = 1$.

**Étape 4 : Conclusion**
Ceci est vrai pour tout $\epsilon > 0$. Considérons une suite $(\epsilon_k)_{k \in \mathbb{N}^*}$ décroissante vers $0$ (par exemple $\epsilon_k = 1/k$).
L'événement "La suite $(\frac{S_n}{n})$ converge vers 0" est l'intersection dénombrable sur $k \ge 1$ des événements "À partir d'un certain rang, $|\frac{S_n}{n}| \le 1/k$".
Une intersection dénombrable d'événements de probabilité 1 a une probabilité de 1.
Donc $\frac{S_n}{n} \xrightarrow{p.s.} 0$, soit $\frac{1}{n}\sum_{i=1}^n X_i - \mu \xrightarrow{p.s.} 0$.
$$\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n X_i = \mu \quad p.s.$$
La démonstration est achevée.

## 4. Applications en Physique, Logique et Intelligence Artificielle

**Physique Statistique : L'équivalence des ensembles thermodynamiques**
En physique statistique (par exemple pour un gaz parfait), un macro-état (température, pression) est la manifestation du comportement combiné de $10^{23}$ molécules. La LFGN justifie rigoureusement l'approche thermodynamique : l'énergie moyenne par particule fluctue d'une façon qui s'évanouit statistiquement avec le nombre de molécules d'Avogadro. Elle justifie ainsi l'équivalence entre l'ensemble microcanonique (énergie fixée) et l'ensemble canonique (température fixée, donc énergie fluctuante mais de variance relative nulle à la limite thermodynamique).

**Intelligence Artificielle : Validation croisée et Risque Empirique**
Dans l'apprentissage automatique, le but d'un modèle (comme un réseau de neurones) est de minimiser le *Risque Réel* : l'espérance de la fonction de perte $\mathcal{L}$ sur la vraie distribution de données (inconnue) $D$.
$$R(w) = \mathbb{E}_{(X,Y) \sim D}[ \mathcal{L}(f_w(X), Y) ]$$
Comme nous n'avons pas accès à l'espérance, on minimise le *Risque Empirique* sur un jeu de données de taille $N$ :
$$\hat{R}_N(w) = \frac{1}{N} \sum_{i=1}^N \mathcal{L}(f_w(x_i), y_i)$$
La LFGN est la pierre angulaire de la théorie de l'apprentissage (théorie Vapnik-Chervonenkis ou PAC) : pour une hypothèse $w$ fixe, $\hat{R}_N(w) \xrightarrow{p.s.} R(w)$ quand $N \to \infty$. L'apprentissage automatique est formellement justifié car notre approximation sur le dataset devient presque sûrement exacte.

**Intelligence Artificielle : Descente de Gradient Stochastique (SGD)**
Le calcul du vrai gradient de la perte sur tout le jeu de données pour un Deep Learning Model est très coûteux. On calcule donc un gradient empirique $\hat{g}$ sur un petit échantillon (*mini-batch*).
Puisque les échantillons du mini-batch sont tirés I.I.D., la LFGN garantit que ce gradient stochastique est un estimateur non biaisé du vrai gradient, et que sa variance diminue linéairement avec la taille du batch. Ainsi, SGD "converge" car, en moyenne, il suit la ligne de plus grande pente, les fluctuations stochastiques du petit batch étant contrebalancées sur le temps long de l'entraînement.
