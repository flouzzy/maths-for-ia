---
uuid: "jalon-91"
title: "Inégalités de concentration"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/theorie
prev: "[[Jalon 90 (Les modes de convergence).md]]"
next: "[[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]]"
---

# Jalon 91 : Inégalités de concentration

## 1. Introduction aux inégalités de concentration

Dans de nombreux domaines allant de la physique statistique à l'informatique théorique, il est fréquent de manipuler des systèmes complexes composés d'un très grand nombre de variables aléatoires (comme les particules d'un gaz, ou les échantillons de données en apprentissage automatique). La connaissance exacte de la distribution de probabilité globale de tels systèmes est généralement inaccessible. Néanmoins, on dispose souvent d'informations globales simples telles que l'espérance mathématique ou la variance.

C'est dans ce contexte que naissent les inégalités de concentration, dont les premiers jalons ont été posés par Andrey Markov et Pafnuty Chebyshev au XIXe siècle, avant d'être profondément développées par Herman Chernoff et Wassily Hoeffding au milieu du XXe siècle. Leur objet fondamental est de fournir des garanties mathématiques quantitatives sur la probabilité qu'une variable aléatoire s'écarte significativement de son espérance. En d'autres termes, ces inégalités expliquent comment, et à quelle vitesse, la mesure de probabilité "se concentre" autour de la moyenne.

L'intuition physique sous-jacente est simple : plus l'écart à la moyenne exigé est grand, plus la configuration du système qui produirait cet écart devient rare et contrainte, faisant s'effondrer sa probabilité de réalisation. La force de ces outils est d'être totalement agnostiques quant à la loi exacte sous-jacente, reposant uniquement sur quelques moments ou bornes de la variable aléatoire.

## 2. L'Inégalité de Markov

L'inégalité de Markov est la fondation sur laquelle reposent presque toutes les autres inégalités de concentration. Elle donne une majoration de la queue de distribution d'une variable positive en ne connaissant que son espérance.

**Théorème (Inégalité de Markov) :**
Soit $X$ une variable aléatoire réelle définie sur un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$, telle que $X \ge 0$ presque sûrement. On suppose que son espérance $\mathbb{E}[X]$ est finie. Alors, pour tout réel $a > 0$ :

$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$

**Démonstration exhaustive :**
La preuve repose sur l'intégration de la variable $X$ en restreignant l'espace sur l'événement d'intérêt $\{X \ge a\}$.
On peut décomposer l'espérance de $X$ sur les deux ensembles disjoints $\{X \ge a\}$ et $\{X < a\}$ :
$$ \mathbb{E}[X] = \int_{\Omega} X(\omega) d\mathbb{P}(\omega) $$
$$ \mathbb{E}[X] = \int_{\{X \ge a\}} X(\omega) d\mathbb{P}(\omega) + \int_{\{X < a\}} X(\omega) d\mathbb{P}(\omega) $$
Puisque $X \ge 0$ presque sûrement, la seconde intégrale est positive ou nulle :
$$ \int_{\{X < a\}} X(\omega) d\mathbb{P}(\omega) \ge 0 $$
Ce qui implique :
$$ \mathbb{E}[X] \ge \int_{\{X \ge a\}} X(\omega) d\mathbb{P}(\omega) $$
Or, sur l'ensemble $\{X \ge a\}$, on a par définition $X(\omega) \ge a$. On peut donc minorer l'intégrale :
$$ \int_{\{X \ge a\}} X(\omega) d\mathbb{P}(\omega) \ge \int_{\{X \ge a\}} a \, d\mathbb{P}(\omega) = a \int_{\{X \ge a\}} d\mathbb{P}(\omega) $$
L'intégrale de l'indicatrice correspond à la probabilité de l'événement :
$$ a \int_{\{X \ge a\}} d\mathbb{P}(\omega) = a \, \mathbb{P}(X \ge a) $$
On obtient ainsi :
$$ \mathbb{E}[X] \ge a \, \mathbb{P}(X \ge a) $$
En divisant par $a > 0$, la conclusion s'impose :
$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$
$\blacksquare$

**Exemple concret (Markov) :**
Considérons une usine où le salaire moyen des employés est de $2000$ euros par mois. On s'intéresse à la proportion d'employés gagnant plus de $6000$ euros par mois. Soit $X$ la variable aléatoire représentant le salaire d'un employé tiré au hasard. On a $X \ge 0$ et $\mathbb{E}[X] = 2000$.
On applique l'inégalité de Markov avec $a = 6000$ :
$$ \mathbb{P}(X \ge 6000) \le \frac{\mathbb{E}[X]}{6000} = \frac{2000}{6000} = \frac{1}{3} $$
Ainsi, au maximum un tiers des employés peut gagner $6000$ euros ou plus.

## 3. L'Inégalité de Bienaymé-Chebyshev

Si l'on dispose d'une information supplémentaire sur la dispersion de la variable, à savoir sa variance, on peut obtenir une borne beaucoup plus fine sur la probabilité que la variable s'éloigne de sa moyenne.

**Théorème (Inégalité de Bienaymé-Chebyshev) :**
Soit $Y$ une variable aléatoire réelle de variance $\text{Var}(Y) = \sigma^2 < \infty$ et d'espérance $\mathbb{E}[Y] = \mu$. Alors pour tout réel $\epsilon > 0$ :

$$ \mathbb{P}(|Y - \mu| \ge \epsilon) \le \frac{\text{Var}(Y)}{\epsilon^2} $$

**Démonstration exhaustive :**
Nous allons utiliser l'inégalité de Markov sur une transformation astucieuse de $Y$.
Posons la variable aléatoire $X = (Y - \mu)^2$.
Par définition, $X \ge 0$ presque sûrement.
L'espérance de $X$ correspond exactement à la définition de la variance de $Y$ :
$$ \mathbb{E}[X] = \mathbb{E}[(Y - \mu)^2] = \text{Var}(Y) $$
Soit $\epsilon > 0$. Les événements $\{|Y - \mu| \ge \epsilon\}$ et $\{(Y - \mu)^2 \ge \epsilon^2\}$ sont rigoureusement équivalents, car la fonction carrée est strictement croissante sur $\mathbb{R}^+$.
Ainsi :
$$ \mathbb{P}(|Y - \mu| \ge \epsilon) = \mathbb{P}((Y - \mu)^2 \ge \epsilon^2) $$
Ce qui équivaut à :
$$ \mathbb{P}(X \ge \epsilon^2) $$
On applique l'inégalité de Markov sur $X$ avec la constante $a = \epsilon^2$ (qui est strictement positive) :
$$ \mathbb{P}(X \ge \epsilon^2) \le \frac{\mathbb{E}[X]}{\epsilon^2} $$
En remplaçant $X$ et $\mathbb{E}[X]$ par leurs expressions initiales :
$$ \mathbb{P}(|Y - \mu| \ge \epsilon) \le \frac{\text{Var}(Y)}{\epsilon^2} $$
$\blacksquare$

\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1]
  \draw[->] (-4,0) -- (4,0) node[right] {$y$};
  \draw[->] (0,-0.5) -- (0,4) node[above] {Densité $f(y)$};

  \draw[thick, blue, domain=-3:3, samples=100] plot (\x, {3.5*exp(-\x*\x/2)});

  \draw[dashed, red, thick] (1.5, 0) -- (1.5, {3.5*exp(-1.5*1.5/2)});
  \draw[dashed, red, thick] (-1.5, 0) -- (-1.5, {3.5*exp(-1.5*1.5/2)});

  \node[below] at (0,0) {$\mu$};
  \node[below] at (1.5,0) {$\mu + \epsilon$};
  \node[below] at (-1.5,0) {$\mu - \epsilon$};

  \fill[red, opacity=0.3, domain=1.5:3, samples=50] (1.5,0) -- plot (\x, {3.5*exp(-\x*\x/2)}) -- (3,0) -- cycle;
  \fill[red, opacity=0.3, domain=-3:-1.5, samples=50] (-3,0) -- plot (\x, {3.5*exp(-\x*\x/2)}) -- (-1.5,0) -- cycle;

  \node[red, align=center] at (2.5, 1) {Surface totale \\ $\le \frac{\text{Var}(Y)}{\epsilon^2}$};
\end{tikzpicture}
\caption{Inégalité de Bienaymé-Chebyshev : contrôle des queues de distribution}
\end{figure}

**Exemple concret (Chebyshev) :**
Supposons que la durée de vie d'une machine a une espérance de $\mu = 1000$ heures et une variance de $\text{Var}(Y) = 400$ heures$^2$ (soit un écart-type $\sigma = 20$ heures).
On veut majorer la probabilité que la machine tombe en panne avant $900$ heures ou dépasse les $1100$ heures, soit $|Y - 1000| \ge 100$.
On applique Bienaymé-Chebyshev avec $\epsilon = 100$ :
$$ \mathbb{P}(|Y - 1000| \ge 100) \le \frac{400}{100^2} = \frac{400}{10000} = 0.04 $$
La probabilité de s'écarter de la moyenne de plus de $100$ heures est donc garantie d'être inférieure à $4\%$.

## 4. Bornes de Chernoff et Fonction Génératrice des Moments

L'inégalité de Chebyshev exploite le deuxième moment (la variance). L'idée des bornes de Chernoff est d'utiliser la fonction génératrice des moments (lorsqu'elle existe) pour exploiter simultanément tous les moments de la variable aléatoire, conduisant à des décroissances exponentielles des probabilités d'écart.

**Définition (Fonction génératrice des moments) :**
La fonction génératrice des moments d'une variable aléatoire $X$ est définie par $M_X(t) = \mathbb{E}[e^{tX}]$, pour $t \in \mathbb{R}$.

**Théorème (Méthode de Chernoff) :**
Soit $X$ une variable aléatoire et $a \in \mathbb{R}$. Alors pour tout $t > 0$ tel que $\mathbb{E}[e^{tX}] < \infty$ :
$$ \mathbb{P}(X \ge a) \le e^{-ta} \mathbb{E}[e^{tX}] $$

**Démonstration exhaustive :**
L'événement $\{X \ge a\}$ est équivalent à $\{tX \ge ta\}$ car $t > 0$.
Par croissance stricte de la fonction exponentielle, cet événement est aussi équivalent à $\{e^{tX} \ge e^{ta}\}$.
Ainsi :
$$ \mathbb{P}(X \ge a) = \mathbb{P}(e^{tX} \ge e^{ta}) $$
Considérons la variable aléatoire positive $Y = e^{tX}$.
On peut appliquer l'inégalité de Markov à $Y$, pour la constante positive $c = e^{ta}$ :
$$ \mathbb{P}(Y \ge c) \le \frac{\mathbb{E}[Y]}{c} $$
Ce qui se réécrit :
$$ \mathbb{P}(e^{tX} \ge e^{ta}) \le \frac{\mathbb{E}[e^{tX}]}{e^{ta}} $$
Soit finalement :
$$ \mathbb{P}(X \ge a) \le e^{-ta} \mathbb{E}[e^{tX}] $$
$\blacksquare$

L'intérêt majeur de cette méthode est que le paramètre $t > 0$ est libre. On obtiendra la borne la plus fine possible en minimisant l'expression de droite par rapport à $t$, c'est-à-dire en étudiant la transformée de Cramér.

**Exemple concret (Chernoff sur la loi de Poisson) :**
Soit $X \sim \mathcal{P}(\lambda)$. On rappelle que $\mathbb{E}[e^{tX}] = \exp(\lambda(e^t - 1))$.
On cherche à borner $\mathbb{P}(X \ge a)$ pour $a > \lambda$.
D'après la méthode de Chernoff, pour tout $t > 0$ :
$$ \mathbb{P}(X \ge a) \le e^{-ta} \exp(\lambda(e^t - 1)) = \exp(\lambda(e^t - 1) - ta) $$
Pour trouver la meilleure borne, on minimise l'exposant $g(t) = \lambda(e^t - 1) - ta$.
On dérive par rapport à $t$ : $g'(t) = \lambda e^t - a$.
Le minimum est atteint lorsque $g'(t) = 0 \iff e^t = \frac{a}{\lambda} \iff t = \ln(\frac{a}{\lambda})$.
Puisque $a > \lambda$, on a bien $t > 0$.
En remplaçant ce $t$ optimal dans l'inégalité :
$$ \mathbb{P}(X \ge a) \le \exp\left(\lambda\left(\frac{a}{\lambda} - 1\right) - a\ln\left(\frac{a}{\lambda}\right)\right) = e^{a-\lambda} \left(\frac{\lambda}{a}\right)^a $$

## 5. Le Lemme de Hoeffding

Le lemme de Hoeffding est un outil fondamental pour contrôler la fonction génératrice des moments d'une variable aléatoire bornée. Il mène directement à l'inégalité de Hoeffding, reine de l'apprentissage statistique.

**Théorème (Lemme de Hoeffding) :**
Soit $X$ une variable aléatoire d'espérance nulle ($\mathbb{E}[X] = 0$) prenant ses valeurs presque sûrement dans l'intervalle $[a, b]$.
Alors, pour tout $s \in \mathbb{R}$ :
$$ \mathbb{E}[e^{sX}] \le \exp\left(\frac{s^2 (b-a)^2}{8}\right) $$

**Théorème (Inégalité de Hoeffding) :**
Soient $X_1, X_2, \dots, X_n$ des variables aléatoires indépendantes telles que pour tout $i$, $X_i \in [a_i, b_i]$ presque sûrement.
Posons $S_n = \sum_{i=1}^n X_i$. Alors, pour tout $t > 0$ :
$$ \mathbb{P}(S_n - \mathbb{E}[S_n] \ge t) \le \exp\left( - \frac{2t^2}{\sum_{i=1}^n (b_i - a_i)^2} \right) $$

**Exemple concret (Hoeffding pour des variables de Bernoulli) :**
Considérons une urne contenant une proportion $p$ de boules rouges. On effectue $n = 100$ tirages avec remise. Soit $X_i$ la variable valant $1$ si la $i$-ème boule est rouge, $0$ sinon. Les $X_i$ sont indépendantes et bornées dans $[0, 1]$ (donc $b_i - a_i = 1$).
Posons la moyenne empirique $\bar{X}_n = \frac{S_n}{n}$. On a $\mathbb{E}[\bar{X}_n] = p$.
L'inégalité de Hoeffding donne pour l'écart de la moyenne :
$$ \mathbb{P}(\bar{X}_n - p \ge \epsilon) = \mathbb{P}(S_n - np \ge n\epsilon) \le \exp\left( - \frac{2(n\epsilon)^2}{n \times 1^2} \right) = \exp(-2n\epsilon^2) $$
Si on veut garantir que l'écart entre notre estimation empirique et la vraie valeur $p$ dépasse $\epsilon = 0.1$ avec une probabilité, disons pour $n=100$ :
$$ \mathbb{P}(\bar{X}_n - p \ge 0.1) \le \exp(-2 \times 100 \times 0.01) = \exp(-2) \approx 0.135 $$
Ainsi, il y a moins de $13.5\%$ de chances de surestimer $p$ de plus de $0.1$.
