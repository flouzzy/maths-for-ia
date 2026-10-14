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

## 2. Définitions et Théorèmes Fondamentaux

Dans ce qui suit, on considère un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$. Toutes les variables aléatoires considérées sont à valeurs réelles et définies sur cet espace. On s'intéresse à la convergence d'une suite $(X_n)_{n \in \mathbb{N}}$ vers une variable aléatoire $X$.

### 2.1 Convergence Presque Sûre

La convergence presque sûre est le mode de convergence le plus fort. Il stipule que la suite de fonctions $X_n(\omega)$ converge ponctuellement vers $X(\omega)$ pour presque toutes les réalisations $\omega$.

**Définition (Convergence Presque Sûre) :**
La suite $(X_n)$ converge presque sûrement vers $X$, noté $X_n \xrightarrow{p.s.} X$, si l'événement sur lequel la convergence ponctuelle a lieu possède une probabilité égale à $1$.
$$ \mathbb{P}\left( \left\{ \omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = X(\omega) \right\} \right) = 1 $$

**Exemple Concret :**
Soit un espace $\Omega = [0, 1]$ muni de la mesure de Lebesgue $\mathbb{P}$. Définissons la variable aléatoire $X_n(\omega) = \omega^n$.
Pour tout $\omega \in [0, 1[$, on a $\lim_{n \to \infty} \omega^n = 0$.
Pour $\omega = 1$, on a $X_n(1) = 1$ pour tout $n$, donc $\lim_{n \to \infty} X_n(1) = 1$.
La limite simple est donc $X(\omega) = 0$ sur $[0, 1[$ et $X(1) = 1$.
Posons $Y = 0$ (variable aléatoire constante et égale à 0). On remarque que :
$$ \{ \omega \in [0, 1] \mid \lim_{n \to \infty} X_n(\omega) = Y(\omega) \} = [0, 1[ $$
Or, $\mathbb{P}([0, 1[) = 1$. Par conséquent, $X_n \xrightarrow{p.s.} 0$. Le singleton $\{1\}$ où la convergence fait défaut est de mesure nulle.

### 2.2 Convergence en Probabilité

La convergence en probabilité est plus faible. Elle exige que pour tout seuil d'erreur fixé, la probabilité que l'écart entre $X_n$ et $X$ dépasse ce seuil tende vers zéro lorsque $n$ croît.

**Définition (Convergence en Probabilité) :**
La suite $(X_n)$ converge en probabilité vers $X$, noté $X_n \xrightarrow{\mathbb{P}} X$, si pour tout réel $\epsilon > 0$ :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$

**Théorème (Implication p.s. $\implies$ en probabilité) :**
Si $X_n \xrightarrow{p.s.} X$, alors $X_n \xrightarrow{\mathbb{P}} X$. La réciproque est fausse en général.

**Contre-exemple (Convergence en probabilité n'implique pas presque sûre) :**
Définissons une suite d'événements sur $\Omega = [0, 1]$ muni de la mesure de Lebesgue. Considérons les intervalles mouvants ("machine à écrire") :
Pour $n \ge 1$, soit $k$ tel que $2^k \le n < 2^{k+1}$. Posons $m = n - 2^k$.
On définit l'intervalle $I_n = \left[ \frac{m}{2^k}, \frac{m+1}{2^k} \right]$.
Soit $X_n = \mathbf{1}_{I_n}$ (la fonction indicatrice de cet intervalle).
- Calculons la probabilité : $\mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n = 1) = \text{longueur}(I_n) = \frac{1}{2^k}$.
Puisque $k \to \infty$ lorsque $n \to \infty$, la probabilité tend vers $0$. Donc $X_n \xrightarrow{\mathbb{P}} 0$.
- Cependant, pour tout $\omega \in [0, 1]$, la valeur $X_n(\omega)$ alternera entre $0$ et $1$ une infinité de fois, car pour chaque $k$, $\omega$ appartient à l'un des intervalles de la subdivision. Ainsi, $\limsup X_n(\omega) = 1$ et $\liminf X_n(\omega) = 0$. La suite ne converge ponctuellement pour **aucun** $\omega$. Donc $X_n$ ne converge pas presque sûrement.

### 2.3 Convergence dans $L^p$ (en moyenne d'ordre $p$)

Ce mode quantifie la "distance" fonctionnelle entre les variables.

**Définition (Convergence $L^p$) :**
Soit $p \ge 1$. On suppose que pour tout $n$, $\mathbb{E}[|X_n|^p] < \infty$ et $\mathbb{E}[|X|^p] < \infty$. La suite $(X_n)$ converge dans $L^p$ vers $X$, noté $X_n \xrightarrow{L^p} X$, si :
$$ \lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0 $$

**Exemple Concret (La "bosse" qui s'échappe) :**
Soit $X_n$ telle que $\mathbb{P}(X_n = n) = \frac{1}{n^2}$ et $\mathbb{P}(X_n = 0) = 1 - \frac{1}{n^2}$.
- Convergence en probabilité : Pour $\epsilon \in ]0, 1[$, $\mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n = n) = \frac{1}{n^2} \to 0$. Donc $X_n \xrightarrow{\mathbb{P}} 0$.
- Convergence $L^1$ : $\mathbb{E}[|X_n - 0|] = n \cdot \frac{1}{n^2} = \frac{1}{n} \to 0$. Donc $X_n \xrightarrow{L^1} 0$.
- Convergence $L^2$ : $\mathbb{E}[|X_n - 0|^2] = n^2 \cdot \frac{1}{n^2} = 1$. Cette valeur ne tend pas vers $0$, donc $X_n$ ne converge pas vers $0$ dans $L^2$.

### 2.4 Convergence en Loi (ou en Distribution)

La convergence en loi est de nature fondamentalement différente. Elle ne compare pas les variables $X_n$ et $X$ sur le même espace d'états ponctuellement, mais se contente d'indiquer que la distribution statistique des valeurs de $X_n$ s'approche de celle de $X$.

**Définition (Convergence en Loi) :**
La suite $(X_n)$ converge en loi vers $X$, noté $X_n \xrightarrow{\mathcal{L}} X$, si pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée :
$$ \lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)] $$
Ceci est équivalent à dire que la suite des fonctions de répartition $F_{X_n}(t) = \mathbb{P}(X_n \le t)$ converge vers $F_X(t) = \mathbb{P}(X \le t)$ en tout point $t$ où $F_X$ est continue.

**Exemple Concret :**
Soit $X \sim \mathcal{N}(0, 1)$ et $X_n = -X$. Évidemment, les variables sont identiques en loi pour tout $n$, donc $X_n$ converge en loi vers $X$ de manière triviale (la loi est $\mathcal{N}(0, 1)$ pour toutes).
Toutefois, $|X_n - X| = |-2X| = 2|X|$. La distance est constante et strictement positive avec probabilité 1, donc $X_n$ ne converge vers $X$ ni en probabilité, ni p.s.

## 3. Démonstrations et Hiérarchie Strictes

Le théorème suivant structure les relations d'implication entre les différents modes.

**Théorème (Hiérarchie de la Convergence) :**
1. La convergence dans $L^p$ implique la convergence en probabilité.
2. La convergence en probabilité implique la convergence en loi.

### 3.1 Démonstration : $L^p \implies \text{Probabilité}$

Nous voulons prouver que si $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$, alors pour tout $\epsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0$.

**Preuve :**
Fixons $\epsilon > 0$. L'événement $\{|X_n - X| > \epsilon\}$ est strictement équivalent à $\{|X_n - X|^p > \epsilon^p\}$ car $x \mapsto x^p$ est strictement croissante pour $x \ge 0$ et $p \ge 1$.
Appliquons l'inégalité de Markov sur la variable aléatoire positive $Y_n = |X_n - X|^p$ et le seuil $a = \epsilon^p$ :
$$ \mathbb{P}(|X_n - X|^p > \epsilon^p) \le \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p} $$
Par hypothèse de convergence dans $L^p$, on a $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$.
Puisque le terme de droite tend vers $0$ (avec $\epsilon$ fixé), par encadrement, la probabilité du membre de gauche tend également vers $0$.
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$
La convergence en probabilité est démontrée.

### 3.2 Démonstration : $\text{Probabilité} \implies \text{Loi}$

Nous voulons prouver que si $X_n \xrightarrow{\mathbb{P}} X$, alors pour toute fonction continue et bornée $f$, $\mathbb{E}[f(X_n)] \to \mathbb{E}[f(X)]$.

**Preuve :**
Soit $f$ une fonction continue et bornée, disons bornée par $M > 0$ (soit $|f(x)| \le M$ pour tout $x$).
Fixons un réel $\eta > 0$. Bien que $f$ soit continue, elle n'est pas uniformément continue sur tout $\mathbb{R}$. Mais en restreignant $X$ à un segment borné, nous pourrons contrôler les écarts.
Puisque $X$ est une variable aléatoire réelle, il existe un intervalle fini $K = [-A, A]$ tel que $\mathbb{P}(X \notin K) < \eta$.
Sur ce segment compact $K$, $f$ est uniformément continue (Théorème de Heine). Il existe donc $\delta > 0$ tel que pour tout $x \in K$ et $y \in \mathbb{R}$ vérifiant $|x - y| < \delta$, on ait $|f(x) - f(y)| < \eta$.

Décomposons l'espérance de la différence :
$$ |\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| \le \mathbb{E}[|f(X_n) - f(X)|] $$
Introduisons les événements suivants pour partitionner $\Omega$ :
$E_1 = \{ |X_n - X| \ge \delta \}$
$E_2 = \{ |X_n - X| < \delta \} \cap \{ X \notin K \}$
$E_3 = \{ |X_n - X| < \delta \} \cap \{ X \in K \}$

Sur $E_1$, on majore brutalement par la borne : $|f(X_n) - f(X)| \le 2M$.
Sur $E_2$, on majore brutalement par $2M$.
Sur $E_3$, par uniforme continuité, $|f(X_n) - f(X)| \le \eta$.

En séparant l'espérance, on obtient :
$$ \mathbb{E}[|f(X_n) - f(X)|] \le 2M \cdot \mathbb{P}(E_1) + 2M \cdot \mathbb{P}(E_2) + \eta \cdot \mathbb{P}(E_3) $$
$$ \mathbb{E}[|f(X_n) - f(X)|] \le 2M \cdot \mathbb{P}(|X_n - X| \ge \delta) + 2M \cdot \mathbb{P}(X \notin K) + \eta \cdot 1 $$
Par hypothèse de convergence en probabilité, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| \ge \delta) = 0$.
Par choix de $K$, $\mathbb{P}(X \notin K) < \eta$.
Donc, pour $n$ suffisamment grand :
$$ \mathbb{E}[|f(X_n) - f(X)|] \le 2M \cdot \eta + 2M \cdot \eta + \eta = (4M + 1)\eta $$
Puisque $\eta$ est arbitrairement petit, la limite supérieure de l'écart est nulle, ce qui prouve la convergence en loi.

## 4. Applications en Physique, Logique et Intelligence Artificielle

L'architecture conceptuelle des modes de convergence est la pierre angulaire de l'analyse asymptotique des algorithmes en IA et en physique statistique.

### A. Consistance des Estimateurs (Machine Learning)
En théorie de l'apprentissage (PAC Learning), on construit des estimateurs $\hat{\theta}_n$ à partir d'un jeu de données de taille $n$. Un algorithme est dit **consistant** si l'estimateur converge en probabilité vers la vraie valeur des paramètres de la population, c'est-à-dire $\hat{\theta}_n \xrightarrow{\mathbb{P}} \theta^*$. Si la convergence a lieu presque sûrement ($\hat{\theta}_n \xrightarrow{p.s.} \theta^*$), on parle de **consistance forte**. La consistance garantit que l'accumulation de données est structurellement capable de débusquer la vérité.

### B. Descente de Gradient Stochastique (SGD)
L'optimisation des réseaux de neurones profonds repose sur la minimisation d'une fonction de perte empirique via la descente de gradient stochastique. Sous des hypothèses strictes d'atténuation du pas d'apprentissage (condition de Robbins-Monro : $\sum \eta_n = \infty$ et $\sum \eta_n^2 < \infty$), on utilise des martingales pour démontrer que la suite des poids synaptiques $\theta_n$ converge **presque sûrement** vers un minimum local de la fonction d'erreur, assurant la stabilité finale du modèle d'IA malgré le bruit intrinsèque des mini-batchs.

### C. Théorèmes de Convergence en Loi en Physique Statistique
En physique des particules, l'évolution macroscopique d'un gaz parfait résulte de l'agrégation de millions de variables aléatoires microscopiques. Le Théorème Central Limite (qui stipule que la moyenne de variables indépendantes et identiquement distribuées converge **en loi** vers une distribution normale) justifie mathématiquement pourquoi la distribution des vitesses des particules obéit universellement à la loi normale de Maxwell-Boltzmann, indépendamment des spécificités dynamiques sous-jacentes.
