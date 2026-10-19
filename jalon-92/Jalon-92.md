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

# Démonstration rigoureuse de la loi forte des grands nombres

## 1. Introduction historique et physique

La Loi Forte des Grands Nombres (LFGN) constitue l'un des piliers fondamentaux de la théorie des probabilités modernes. Son histoire remonte à Jacob Bernoulli, qui a publié la première version (la loi faible) en 1713, mais c'est Émile Borel (1909) puis Andrey Kolmogorov (1930) qui lui ont donné sa forme forte et rigoureuse.

D'un point de vue physique, elle formalise une intuition fondamentale de la nature : les fluctuations chaotiques individuelles s'annulent à l'échelle macroscopique. Lorsqu'on observe le mouvement brownien des particules dans un fluide, bien que la trajectoire d'une seule particule soit imprévisible, le comportement global de milliards de particules obéit à des lois déterministes strictes (comme l'équation de la chaleur). La LFGN est le pont mathématique qui permet de justifier le passage du microscopique aléatoire (l'observation d'un lancer de dé ou d'une collision moléculaire) au macroscopique prévisible.

Concrètement, la LFGN affirme que la moyenne empirique d'une suite de variables aléatoires indépendantes et identiquement distribuées converge vers leur espérance mathématique, non seulement en probabilité, mais presque sûrement.

## 2. Définitions, Théorèmes \& Exemples

### Définition : Variables Aléatoires I.I.D.
On dit qu'une suite de variables aléatoires $(X_n)_{n \in \mathbb{N}^*}$ définies sur un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$ est indépendante et identiquement distribuée (I.I.D.) si :
1. Pour tout ensemble fini d'indices $I \subset \mathbb{N}^*$, les variables $(X_i)_{i \in I}$ sont mutuellement indépendantes.
2. Toutes les variables $X_n$ suivent la même loi de probabilité (elles ont la même fonction de répartition).

**Exemple :** Lancer de pièce. Soit $(X_n)$ la suite définie par $X_n = 1$ si le $n$-ième lancer donne Pile, et $X_n = 0$ s'il donne Face. Si les lancers sont effectués dans des conditions identiques et sans interaction, les $X_n$ sont I.I.D. suivant une loi de Bernoulli $\mathcal{B}(p)$ où $p$ est la probabilité d'obtenir Pile. L'espérance est $\mathbb{E}[X_1] = p$. Si $p = 1/2$, $\mathbb{E}[X_1] = 0.5$.

### Définition : Moyenne Empirique
Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires. On appelle moyenne empirique d'ordre $n$ la variable aléatoire $\overline{X}_n$ définie par :
$$ \overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i $$

**Exemple :** Si l'on obtient les résultats successifs $1, 0, 1, 1, 0$, alors $\overline{X}_5 = \frac{1+0+1+1+0}{5} = \frac{3}{5} = 0.6$.

### Théorème : Loi Forte des Grands Nombres (Théorème de Kolmogorov)
Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires I.I.D.
Si $\mathbb{E}[|X_1|] < +\infty$ (i.e. les variables sont intégrables, avec $\mathbb{E}[X_1] = \mu$), alors la suite des moyennes empiriques $(\overline{X}_n)$ converge presque sûrement vers $\mu$ lorsque $n$ tend vers l'infini.
Autrement dit :
$$ \mathbb{P} \left( \left\{ \omega \in \Omega \, \middle| \, \lim_{n \to +\infty} \frac{1}{n} \sum_{i=1}^n X_i(\omega) = \mu \right\} \right) = 1 $$
Réciproquement, si la suite $(\overline{X}_n)$ converge presque sûrement vers une constante $C$, alors $\mathbb{E}[|X_1|] < +\infty$ et $\mathbb{E}[X_1] = C$.

**Exemple :** Si on lance un dé équilibré à 6 faces à l'infini, l'espérance du résultat est $\mu = \frac{1+2+3+4+5+6}{6} = 3.5$. Le théorème garantit que, avec une probabilité de $1$, la moyenne de vos lancers s'approchera infiniment de $3.5$.

**Exemple 4 (Le contre-exemple de Cauchy) :** Si $(X_n)$ est une suite I.I.D. suivant une loi de Cauchy (densité $f(x) = \frac{1}{\pi(1+x^2)}$), alors $\mathbb{E}[|X_1|] = +\infty$. Dans ce cas, la moyenne empirique $\overline{X}_n$ suit exactement la même loi de Cauchy que $X_1$, pour tout $n$. Elle ne converge pas, elle continue de fluctuer violemment à l'infini, brisant ainsi l'intuition naive de la stabilisation statistique.

### Théorème : Loi Forte sous condition de moment d'ordre 4
Il est souvent plus aisé de démontrer une version légèrement plus faible de la LFGN en supposant l'existence d'un moment d'ordre 4.
Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires I.I.D. telles que $\mathbb{E}[X_1^4] < +\infty$. Soit $\mu = \mathbb{E}[X_1]$.
Alors $\overline{X}_n \xrightarrow{p.s.} \mu$.

\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1]
    % Axes
    \draw[->] (0,0) -- (10,0) node[right] {$n$};
    \draw[->] (0,0) -- (0,5) node[above] {$\overline{X}_n$};

    % Asymptote / Mean
    \draw[dashed, red, thick] (0, 3) -- (10, 3) node[right] {$\mu = \mathbb{E}[X]$};

    % Random walk / empirical mean
    \draw[blue, thick] (0, 1) -- (1, 4.5) -- (2, 2.1) -- (3, 3.8) -- (4, 2.5) -- (5, 3.3) -- (6, 2.8) -- (7, 3.1) -- (8, 2.95) -- (9, 3.05) -- (9.8, 3);

    % Tolerance band
    \draw[gray, dotted] (0, 3.5) -- (10, 3.5);
    \draw[gray, dotted] (0, 2.5) -- (10, 2.5);

    % Labels
    \node[left] at (0, 3.5) {$\mu + \epsilon$};
    \node[left] at (0, 2.5) {$\mu - \epsilon$};
\end{tikzpicture}
\caption{Illustration de la Loi Forte des Grands Nombres : la trajectoire de la moyenne empirique (en bleu) est absorbée presque sûrement dans le corridor $[\mu-\epsilon, \mu+\epsilon]$ et y reste définitivement pour $n$ assez grand.}
\end{figure}

**Exemple :** Supposons une loi de Rademacher $X \in \{-1, 1\}$ avec $\mathbb{P}(X=1) = \mathbb{P}(X=-1) = \frac{1}{2}$. $\mathbb{E}[X] = 0$. $\mathbb{E}[X^4] = 1 < +\infty$. La condition d'ordre 4 est vérifiée, on sait que la LFGN s'applique et $\overline{X}_n \to 0$ p.s.

## 3. Démonstrations

### Démonstration : Loi Forte sous condition d'un moment d'ordre 4 fini

Cette preuve utilise l'inégalité de Markov, le développement algébrique de puissances, et le lemme de Borel-Cantelli.

**Hypothèses :**
Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires I.I.D.
Supposons que $\mathbb{E}[X_1^4] = K < +\infty$.
Pour simplifier l'écriture sans perte de généralité, considérons des variables centrées, c'est-à-dire $\mathbb{E}[X_1] = \mu = 0$. Si ce n'est pas le cas, on applique la démonstration à la suite $Y_n = X_n - \mu$.
Posons $S_n = \sum_{i=1}^n X_i$. L'objectif est de montrer que $\frac{S_n}{n} \xrightarrow{p.s.} 0$.

**Étape 1 : Calcul de $\mathbb{E}[S_n^4]$**
Développons $(S_n)^4 = \left(\sum_{i=1}^n X_i\right)^4$.
Le développement donne une somme de monômes de la forme $X_i X_j X_k X_l$ pour les indices $i, j, k, l \in \{1, \dots, n\}$.
$$ (S_n)^4 = \sum_{i,j,k,l=1}^n X_i X_j X_k X_l $$
Par linéarité de l'espérance, on a :
$$ \mathbb{E}[S_n^4] = \sum_{i,j,k,l=1}^n \mathbb{E}[X_i X_j X_k X_l] $$
Comme les variables sont indépendantes et de moyenne nulle ($\mathbb{E}[X_i] = 0$), dès qu'un indice apparaît une seule fois dans le produit, l'espérance du monôme s'annule.
Par exemple, si $i \neq j, k, l$, alors $\mathbb{E}[X_i X_j X_k X_l] = \mathbb{E}[X_i] \mathbb{E}[X_j X_k X_l] = 0$.
Les seuls termes non nuls dans la somme sont ceux où chaque indice apparaît au moins deux fois. Il y a exactement deux configurations possibles pour ces termes :
1. **Un seul indice apparaît quatre fois :** Les termes de la forme $X_i^4$. Il y en a exactement $n$.
   Pour ces termes, l'espérance est $\mathbb{E}[X_i^4] = \mathbb{E}[X_1^4]$.
2. **Deux indices distincts apparaissent deux fois chacun :** Les termes de la forme $X_i^2 X_j^2$ avec $i \neq j$.
   Pour un couple $(i,j)$ donné ($i \neq j$), le nombre de façons d'arranger les indices dans le produit $X_i X_j X_k X_l$ correspond au nombre de combinaisons de 2 éléments parmi 4, soit $\binom{4}{2} = 6$.
   Le nombre de couples $(i,j)$ avec $i < j$ est $\binom{n}{2} = \frac{n(n-1)}{2}$.
   Il y a donc $6 \times \frac{n(n-1)}{2} = 3n(n-1)$ termes de cette forme.
   Par indépendance, $\mathbb{E}[X_i^2 X_j^2] = \mathbb{E}[X_i^2] \mathbb{E}[X_j^2] = (\mathbb{E}[X_1^2])^2$.

En sommant ces termes, on obtient :
$$ \mathbb{E}[S_n^4] = n \mathbb{E}[X_1^4] + 3n(n-1) (\mathbb{E}[X_1^2])^2 $$
Puisque $\mathbb{E}[X_1^4] = K < +\infty$, par l'inégalité de Cauchy-Schwarz (ou Jensen), $(\mathbb{E}[X_1^2])^2 \leq \mathbb{E}[X_1^4] = K$.
On peut donc majorer par un polynôme de degré 2 en $n$ :
$$ \mathbb{E}[S_n^4] \leq n K + 3n(n-1) K = K(n + 3n^2 - 3n) = K(3n^2 - 2n) \leq 3K n^2 $$
Ainsi, il existe une constante $C = 3K > 0$ telle que $\mathbb{E}[S_n^4] \leq C n^2$.

**Étape 2 : Inégalité de Markov et concentration**
Nous voulons montrer que $\frac{S_n}{n}$ s'écarte de $0$. Fixons $\epsilon > 0$.
Appliquons l'inégalité de Markov à la variable aléatoire positive $\left|\frac{S_n}{n}\right|^4$ :
$$ \mathbb{P}\left( \left| \frac{S_n}{n} \right| \geq \epsilon \right) = \mathbb{P}\left( \left| \frac{S_n}{n} \right|^4 \geq \epsilon^4 \right) \leq \frac{\mathbb{E}\left[ \left| \frac{S_n}{n} \right|^4 \right]}{\epsilon^4} $$
Or, $\mathbb{E}\left[ \left| \frac{S_n}{n} \right|^4 \right] = \frac{1}{n^4} \mathbb{E}[S_n^4]$.
En utilisant la majoration de l'Étape 1 :
$$ \mathbb{P}\left( \left| \frac{S_n}{n} \right| \geq \epsilon \right) \leq \frac{C n^2}{n^4 \epsilon^4} = \frac{C}{\epsilon^4 n^2} $$

**Étape 3 : Application du Lemme de Borel-Cantelli**
Considérons la série des probabilités que l'écart soit supérieur à $\epsilon$ :
$$ \sum_{n=1}^{+\infty} \mathbb{P}\left( \left| \frac{S_n}{n} \right| \geq \epsilon \right) \leq \sum_{n=1}^{+\infty} \frac{C}{\epsilon^4 n^2} = \frac{C}{\epsilon^4} \sum_{n=1}^{+\infty} \frac{1}{n^2} $$
La série de Riemann $\sum \frac{1}{n^2}$ converge. Donc la série $\sum \mathbb{P}\left( \left| \frac{S_n}{n} \right| \geq \epsilon \right)$ est convergente.
D'après le premier Lemme de Borel-Cantelli, si la série des probabilités des événements $A_n = \left\{ \left| \frac{S_n}{n} \right| \geq \epsilon \right\}$ converge, alors la probabilité que ces événements se réalisent une infinité de fois est nulle :
$$ \mathbb{P}\left( \limsup_{n \to +\infty} \left\{ \left| \frac{S_n}{n} \right| \geq \epsilon \right\} \right) = 0 $$
Autrement dit, presque sûrement, il n'existe qu'un nombre fini de $n$ pour lesquels $\left| \frac{S_n}{n} \right| \geq \epsilon$.
Par conséquent, pour presque tout $\omega \in \Omega$, il existe un entier $N(\omega)$ tel que pour tout $n \geq N(\omega)$, $\left| \frac{S_n(\omega)}{n} \right| < \epsilon$.
Puisque cela est vrai pour tout $\epsilon > 0$ (en considérant une suite $\epsilon_k = 1/k$), on en déduit que :
$$ \frac{S_n}{n} \xrightarrow{p.s.} 0 $$
Ce qui achève la démonstration rigoureuse de la loi forte des grands nombres sous hypothèse d'un moment d'ordre 4. \qedsymbol


## 4. Applications en Physique, Logique \& IA

### L'Apprentissage Machine et le Risque Empirique
En Intelligence Artificielle, et plus particulièrement en Apprentissage Statistique, la LFGN est le théorème qui légitime l'entraînement des modèles.
Un modèle d'apprentissage cherche à minimiser un risque théorique (espérance de la fonction de perte sur toute la distribution des données réelles) :
$$ R(f) = \mathbb{E}_{(X,Y)\sim \mathcal{D}} [ L(f(X), Y) ] $$
Cependant, la distribution $\mathcal{D}$ est inconnue. On ne possède qu'un échantillon fini de données $(X_i, Y_i)_{i=1}^n$ (le dataset d'entraînement).
On remplace alors le risque théorique par le **risque empirique** :
$$ \widehat{R}_n(f) = \frac{1}{n} \sum_{i=1}^n L(f(X_i), Y_i) $$
Si les données de l'échantillon sont tirées de manière I.I.D., la LFGN assure que pour un modèle $f$ fixé :
$$ \widehat{R}_n(f) \xrightarrow{p.s.} R(f) $$
Cela garantit que l'évaluation d'un modèle sur un vaste ensemble de test converge vers sa véritable performance en production.

### Méthode de Monte-Carlo
La LFGN justifie l'intégration numérique par la méthode de Monte-Carlo.
Pour calculer une intégrale complexe $I = \int_D g(x) dx$, on peut interpréter cette intégrale comme l'espérance $\mathbb{E}[g(U)]$ où $U$ est une variable aléatoire de loi uniforme sur le domaine $D$.
En générant $n$ échantillons I.I.D. $U_1, \dots, U_n$ dans $D$, on approche l'intégrale par :
$$ I_n = \frac{\text{Vol}(D)}{n} \sum_{i=1}^n g(U_i) $$
La LFGN garantit que $I_n \xrightarrow{p.s.} I$. C'est très utilisé en IA pour approximer des espérances dans les Variational Autoencoders (VAE) ou dans le Reinforcement Learning.
