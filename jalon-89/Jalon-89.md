---
uuid: "jalon-89"
title: "Lemmes de Borel-Cantelli"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon-88.md]]"
next: "[[Jalon 90 (Les modes de convergence).md]]"
---

# Lemmes de Borel-Cantelli

## 1. Introduction à la limite supérieure d'événements

Le comportement asymptotique d'une suite infinie d'événements probabilistes est au cœur de l'analyse stochastique. L'étude des lemmes de Borel-Cantelli s'intéresse à la réalisation "infiniment souvent" d'événements au sein d'une suite infinie.

### A. L'événement "Infiniment Souvent"

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité et $(A_n)_{n \in \mathbb{N}}$ une suite d'événements de la tribu $\mathcal{F}$. On s'intéresse à l'ensemble des résultats (les éléments $\omega \in \Omega$) qui appartiennent à une infinité d'ensembles $A_n$.

**Définition (Limite supérieure d'événements) :**
On définit la limite supérieure de la suite $(A_n)_{n \in \mathbb{N}}$, notée $\limsup_{n \to \infty} A_n$ (ou encore $\{A_n \text{ i.s.}\}$ pour "infiniment souvent"), par :

$$ \limsup_{n \to \infty} A_n = \bigcap_{n=0}^\infty \bigcup_{k=n}^\infty A_k $$

Concrètement, $\omega \in \limsup_{n \to \infty} A_n$ si et seulement si, pour tout entier $n \ge 0$, il existe un indice $k \ge n$ tel que $\omega \in A_k$. Cela signifie exactement que l'événement $A_n$ se réalise pour une infinité d'indices $n$.

**Exemple 1 :**
Considérons une suite infinie de lancers d'une pièce de monnaie équilibrée. Soit $A_n$ l'événement "Le $n$-ième lancer donne Pile". L'événement $\limsup_{n \to \infty} A_n$ correspond à "On obtient Pile une infinité de fois". Puisque chaque lancer donne "Pile" avec une probabilité $1/2$, la probabilité d'obtenir une infinité de fois "Pile" est de 1.
Si l'on définit $B_n$ comme "Le $n$-ième lancer donne Pile", on peut calculer :
Pour un $n$ fixé, la probabilité qu'aucun lancer de l'indice $n$ à l'indice $n+N$ ne soit "Pile" est $(1/2)^{N+1}$.
Lorsque $N \to \infty$, cette probabilité tend vers 0. Ainsi, la probabilité que "Pile" apparaisse au moins une fois après l'indice $n$ est 1, et ce pour tout $n$. Donc l'intersection de ces événements presque certains est presque certaine : $\mathbb{P}(\limsup B_n) = 1$.

\begin{tikzpicture}[baseline=0]
\draw[thick,->] (0,0) -- (10,0) node[right] {$n$};
\foreach \x in {1,2,3,4,5,6,7,8,9} {
    \draw (\x,0.1) -- (\x,-0.1) node[below] {\small $\x$};
}
\filldraw[blue] (2,0) circle (3pt) node[above] {$A_2$};
\filldraw[blue] (4,0) circle (3pt) node[above] {$A_4$};
\filldraw[blue] (5,0) circle (3pt) node[above] {$A_5$};
\filldraw[blue] (7,0) circle (3pt) node[above] {$A_7$};
\filldraw[blue] (9,0) circle (3pt) node[above] {$A_9$};
\node at (5, -1) {Réalisations des événements $A_n$};
\end{tikzpicture}


## 2. Définitions, Théorèmes et Exemples

Les lemmes de Borel-Cantelli fournissent des conditions suffisantes pour que la probabilité de $\limsup A_n$ soit 0 ou 1.

### A. Premier Lemme de Borel-Cantelli (Cas général)

**Théorème (Premier Lemme de Borel-Cantelli) :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements. Si la série des probabilités converge, c'est-à-dire si :
$$ \sum_{n=0}^\infty \mathbb{P}(A_n) < +\infty $$
alors la probabilité que les événements se produisent infiniment souvent est nulle :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0 $$
Presque sûrement, seuls un nombre fini d'événements $A_n$ se réalisent. Ce lemme ne requiert aucune hypothèse d'indépendance entre les événements.

**Exemple 2 :**
Soit une variable aléatoire $X$ suivant une loi exponentielle de paramètre $\lambda = 1$. Considérons les événements $A_n = \{X \ge n\}$.
Calculons la probabilité de $A_n$ :
$$ \mathbb{P}(A_n) = \int_n^\infty e^{-x} dx = e^{-n} $$
La série de terme général $e^{-n}$ est une série géométrique de raison $e^{-1} < 1$, donc elle converge :
$$ \sum_{n=0}^\infty \mathbb{P}(A_n) = \sum_{n=0}^\infty e^{-n} = \frac{1}{1 - e^{-1}} < +\infty $$
D'après le premier lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 0$.
Cela signifie que, presque sûrement, $X$ ne dépasse pas une infinité de fois la valeur de $n$. En effet, une variable aléatoire suivant une loi exponentielle prend presque sûrement une valeur finie.


**Exemple 5 (Erreurs de transmission) :**
Un signal binaire est transmis à travers un canal bruité. Soit $A_n$ l'événement "Le n-ième bit est altéré".
Si la probabilité d'altération décroît de telle sorte que $\mathbb{P}(A_n) = \frac{1}{n^2}$,
la somme des probabilités converge ($\sum \frac{1}{n^2} = \frac{\pi^2}{6}$).
Par le premier lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 0$.
Cela implique qu'il n'y aura presque sûrement qu'un nombre fini d'erreurs au total sur l'infinité de bits transmis. À partir d'un certain temps, la transmission deviendra parfaite.



### B. Second Lemme de Borel-Cantelli (Cas des événements indépendants)

**Théorème (Second Lemme de Borel-Cantelli) :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements mutuellement **indépendants**. Si la série des probabilités diverge, c'est-à-dire si :
$$ \sum_{n=0}^\infty \mathbb{P}(A_n) = +\infty $$
alors la probabilité que les événements se produisent infiniment souvent est certaine :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1 $$
Presque sûrement, une infinité de $A_n$ se réalisent.

**Exemple 3 (Le Paradoxe du Singe Savant) :**
Supposons qu'un singe tape au hasard sur un clavier d'ordinateur comportant $M$ touches (les 26 lettres de l'alphabet, l'espace, la ponctuation, disons $M = 50$). La probabilité que le singe tape le mot "HAMLET" (6 lettres) en une tentative de 6 frappes est $p = \frac{1}{50^6} > 0$.
Divisons le temps infini en blocs de 6 frappes indépendantes.
Soit $A_n$ l'événement : "Le singe tape exactement HAMLET dans le $n$-ième bloc de 6 frappes".
Les événements $A_n$ sont mutuellement indépendants car les blocs ne se chevauchent pas et chaque frappe est indépendante.
La probabilité de chaque événement est $\mathbb{P}(A_n) = p$.
La série des probabilités est :
$$ \sum_{n=1}^\infty \mathbb{P}(A_n) = \sum_{n=1}^\infty p = +\infty $$
D'après le second lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 1$. Le singe tapera donc le mot "HAMLET" une infinité de fois presque sûrement.


**Exemple 4 (Tirages avec remise) :**
Imaginons que l'on tire une carte avec remise dans un jeu de 52 cartes. L'événement $A_n$ est "Tirer l'As de Pique au n-ième tirage".
Ici $\mathbb{P}(A_n) = \frac{1}{52}$.
Puisque la somme $\sum_{n=1}^\infty \frac{1}{52} = +\infty$ et que les tirages sont indépendants, le second lemme de Borel-Cantelli garantit que l'As de Pique sera tiré une infinité de fois.


## 3. Démonstrations

### A. Démonstration du Premier Lemme de Borel-Cantelli

**Hypothèse :** $\sum_{n=0}^\infty \mathbb{P}(A_n) < +\infty$

1. **Réécriture de l'événement limite supérieure :**
   Par définition, $\limsup_{n \to \infty} A_n = \bigcap_{n=0}^\infty B_n$ où $B_n = \bigcup_{k=n}^\infty A_k$.

2. **Monotonie de la suite d'événements :**
   La suite $(B_n)_{n \ge 0}$ est décroissante pour l'inclusion. En effet :
   $$ B_{n+1} = \bigcup_{k=n+1}^\infty A_k \subset A_n \cup \bigcup_{k=n+1}^\infty A_k = \bigcup_{k=n}^\infty A_k = B_n $$

3. **Continuité décroissante de la mesure de probabilité :**
   Puisque la mesure de probabilité $\mathbb{P}$ est finie (mesure finie car $\mathbb{P}(\Omega) = 1$), le théorème de continuité décroissante s'applique :
   $$ \mathbb{P}\left( \limsup_{n \to \infty} A_n \right) = \mathbb{P}\left( \bigcap_{n=0}^\infty B_n \right) = \lim_{n \to \infty} \mathbb{P}(B_n) $$

4. **Majoration par sous-additivité (Inégalité de Boole) :**
   Par la propriété de sous-additivité d'une mesure, pour tout entier $n$ :
   $$ \mathbb{P}(B_n) = \mathbb{P}\left( \bigcup_{k=n}^\infty A_k \right) \le \sum_{k=n}^\infty \mathbb{P}(A_k) $$

5. **Utilisation de l'hypothèse de convergence :**
   L'hypothèse $\sum_{n=0}^\infty \mathbb{P}(A_n) < +\infty$ implique que le reste de la série convergente tend vers $0$ lorsque $n \to \infty$. Ainsi :
   $$ \lim_{n \to \infty} \sum_{k=n}^\infty \mathbb{P}(A_k) = 0 $$

6. **Conclusion par encadrement :**
   Puisque $0 \le \mathbb{P}(B_n) \le \sum_{k=n}^\infty \mathbb{P}(A_k)$, par passage à la limite, on obtient :
   $$ 0 \le \lim_{n \to \infty} \mathbb{P}(B_n) \le 0 $$
   Ce qui entraîne :
   $$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0 $$
   Ceci achève la démonstration du premier lemme.


### B. Démonstration du Second Lemme de Borel-Cantelli

**Hypothèse :** $\sum_{n=0}^\infty \mathbb{P}(A_n) = +\infty$ et les événements $A_n$ sont indépendants.

1. **Passage au complémentaire :**
   Nous cherchons à montrer que $\mathbb{P}(\limsup A_n) = 1$. Cela équivaut à montrer que la probabilité du complémentaire est nulle.
   Par les lois de De Morgan :
   $$ \left( \limsup_{n \to \infty} A_n \right)^c = \left( \bigcap_{n=0}^\infty \bigcup_{k=n}^\infty A_k \right)^c = \bigcup_{n=0}^\infty \bigcap_{k=n}^\infty A_k^c $$
   Cet événement correspond à $\liminf_{n \to \infty} A_n^c$ (les $A_n^c$ se réalisent pour tous les indices à partir d'un certain rang).

2. **Propriété de sous-additivité :**
   $$ \mathbb{P}\left( \bigcup_{n=0}^\infty \bigcap_{k=n}^\infty A_k^c \right) \le \sum_{n=0}^\infty \mathbb{P}\left( \bigcap_{k=n}^\infty A_k^c \right) $$
   Il suffit donc de montrer que pour tout entier $n$, $\mathbb{P}\left( \bigcap_{k=n}^\infty A_k^c \right) = 0$.

3. **Utilisation de l'indépendance et passage à la limite finie :**
   Puisque les $A_k$ sont mutuellement indépendants, leurs complémentaires $A_k^c$ le sont également.
   Pour tout entier $m > n$ :
   $$ \mathbb{P}\left( \bigcap_{k=n}^m A_k^c \right) = \prod_{k=n}^m \mathbb{P}(A_k^c) = \prod_{k=n}^m (1 - \mathbb{P}(A_k)) $$

4. **Inégalité élémentaire et passage à l'exponentielle :**
   On utilise l'inégalité classique $1 - x \le e^{-x}$ pour $x \ge 0$.
   En posant $x = \mathbb{P}(A_k)$, on a $1 - \mathbb{P}(A_k) \le \exp(-\mathbb{P}(A_k))$.
   Ainsi,
   $$ \prod_{k=n}^m (1 - \mathbb{P}(A_k)) \le \prod_{k=n}^m \exp(-\mathbb{P}(A_k)) = \exp\left( - \sum_{k=n}^m \mathbb{P}(A_k) \right) $$

5. **Passage à la limite $m \to \infty$ :**
   Par continuité décroissante de la mesure :
   $$ \mathbb{P}\left( \bigcap_{k=n}^\infty A_k^c \right) = \lim_{m \to \infty} \mathbb{P}\left( \bigcap_{k=n}^m A_k^c \right) \le \lim_{m \to \infty} \exp\left( - \sum_{k=n}^m \mathbb{P}(A_k) \right) $$
   D'après l'hypothèse, la série diverge, c'est-à-dire $\lim_{m \to \infty} \sum_{k=n}^m \mathbb{P}(A_k) = +\infty$.
   Par conséquent,
   $$ \lim_{m \to \infty} \exp\left( - \sum_{k=n}^m \mathbb{P}(A_k) \right) = \exp(-\infty) = 0 $$
   D'où pour tout $n$, $\mathbb{P}\left( \bigcap_{k=n}^\infty A_k^c \right) = 0$.

6. **Conclusion finale :**
   $$ \mathbb{P}\left( \left( \limsup_{n \to \infty} A_n \right)^c \right) \le \sum_{n=0}^\infty 0 = 0 $$
   Donc la probabilité de l'événement complémentaire est nulle, ce qui prouve que $\mathbb{P}(\limsup A_n) = 1$. La démonstration est complète.


## 4. Applications en Physique, Logique et Intelligence Artificielle

### A. La Loi Zéro-Un de Kolmogorov
Les lemmes de Borel-Cantelli fournissent le cadre théorique pour la loi zéro-un de Kolmogorov, qui stipule que tout événement de la "tribu de queue" (un événement dont la réalisation ne dépend d'aucun sous-ensemble fini de variables aléatoires indépendantes) a une probabilité de 0 ou 1. C'est l'un des piliers qui permet d'étudier la convergence asymptotique de processus aléatoires en physique statistique.

### B. Convergence Presque Sûre des Algorithmes Stochastiques
En apprentissage automatique, le premier lemme de Borel-Cantelli est souvent utilisé pour prouver la **convergence presque sûre** des suites de variables aléatoires. Si l'on dispose d'une suite d'estimateurs $X_n$ de l'algorithme d'optimisation, montrer que la série $\sum_{n} \mathbb{P}(\|X_n - X^*\| > \epsilon)$ converge assure que presque sûrement, à partir d'un certain rang, la distance entre l'estimateur et l'optimum sera inférieure à $\epsilon$. Cela constitue le fondement de la validité de l'algorithme de Descente de Gradient Stochastique (SGD).

### C. Exploration et Compromis Exploration/Exploitation
Dans le cadre de l'apprentissage par renforcement (Reinforcement Learning), une stratégie d'exploration comme la stratégie $\epsilon$-gloutonne nécessite que l'agent continue d'explorer indéfiniment (la condition de type "infiniment souvent") afin de découvrir l'action optimale, mais la probabilité d'exploration doit tendre vers $0$ de manière à ce que l'agent converge vers une politique d'exploitation. Le deuxième lemme de Borel-Cantelli s'applique ici : la condition pour une exploration complète de l'espace d'états et d'actions est que la série des probabilités d'exploration diverge, $\sum \epsilon_n = +\infty$.
