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

# Jalon 89 : Lemmes de Borel-Cantelli

## 1. Origine et intuition : la loi du tout ou rien à l'infini

La question fondamentale qui anime les lemmes de Borel-Cantelli s'enracine dans l'étude des événements extrêmes et de leur récurrence sur un temps infiniment long. Formulés indépendamment par Émile Borel en 1909 dans le cadre de ses travaux sur les probabilités dénombrables, puis généralisés par Francesco Paolo Cantelli en 1917, ces résultats visent à quantifier l'intuition asymptotique. Imaginons une séquence infinie d'expériences aléatoires, par exemple le lancer répété d'une pièce de monnaie potentiellement biaisée où la probabilité de succès évolue au fil du temps. La question géométrique et physique sous-jacente est la suivante : la somme de nos probabilités de succès au fil du temps est-elle suffisante pour garantir un nombre infini de succès, ou bien finira-t-on inexorablement par ne plus jamais observer de succès après un certain stade ?

Le génie de Borel et Cantelli a été de relier le comportement "à l'infini" d'une suite d'événements aléatoires à la simple convergence ou divergence de la série numérique de leurs probabilités. Si la "réserve totale" de probabilité est finie, l'événement ne se réalisera qu'un nombre fini de fois. S'il est infini et que les événements sont indépendants, le succès apparaîtra inexorablement une infinité de fois. Ces deux lemmes fondent ce que l'on appelle les lois du "zéro-un" en théorie de la mesure, dictant que certains comportements limites se produisent soit avec une probabilité de 1, soit avec une probabilité de 0, excluant toute incertitude intermédiaire.

## 2. Définitions et structures : l'événement limite supérieure

Pour appréhender rigoureusement ces lemmes, il est impératif de définir la notion d'un événement se réalisant "une infinité de fois" dans le formalisme de la théorie de la mesure.

### La limite supérieure d'ensembles

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé. Considérons une suite d'événements $(A_n)_{n \in \mathbb{N}} \in \mathcal{F}^{\mathbb{N}}$.

**Définition 1 (Limite supérieure) :**
On définit la limite supérieure de la suite $(A_n)_{n \in \mathbb{N}}$, notée $\limsup_{n \to \infty} A_n$ ou $\{A_n \text{ infiniment souvent (i.s.)}\}$, par :
$$ \limsup_{n \to \infty} A_n = \bigcap_{n=0}^{\infty} \bigcup_{k=n}^{\infty} A_k $$

En termes ensemblistes, $\omega \in \limsup_{n \to \infty} A_n$ si et seulement si, pour tout entier $n \ge 0$, il existe un entier $k \ge n$ tel que $\omega \in A_k$. Cela équivaut rigoureusement à dire que $\omega$ appartient à une infinité d'ensembles $A_n$.

### Exemple concret 1 : Limite supérieure

Considérons l'espace $\Omega = [0, 1]$ muni de la tribu borélienne et de la mesure de Lebesgue $\lambda$.
Soit la suite d'événements $A_n = [0, \frac{1}{n}]$.
Calculons $\limsup_{n \to \infty} A_n$.
D'abord, posons $B_n = \bigcup_{k=n}^{\infty} A_k = \bigcup_{k=n}^{\infty} [0, \frac{1}{k}]$.
Puisque pour tout $k \ge n$, $[0, \frac{1}{k}] \subseteq [0, \frac{1}{n}]$, on obtient $B_n = [0, \frac{1}{n}]$.
Ensuite, $\limsup_{n \to \infty} A_n = \bigcap_{n=1}^{\infty} B_n = \bigcap_{n=1}^{\infty} [0, \frac{1}{n}]$.
Le seul élément appartenant à tous ces intervalles est $\{0\}$. Donc $\limsup_{n \to \infty} A_n = \{0\}$, et $\lambda(\{0\}) = 0$.

## 3. Théorèmes fondamentaux et exemples

### Premier lemme de Borel-Cantelli

Le premier lemme établit une condition suffisante pour qu'un événement ne se produise qu'un nombre fini de fois presque sûrement.

**Théorème 1 (Premier lemme de Borel-Cantelli) :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements dans $\mathcal{F}$.
Si la série des probabilités converge, i.e.,
$$ \sum_{n=0}^{\infty} \mathbb{P}(A_n) < +\infty $$
alors la probabilité que les $A_n$ se réalisent infiniment souvent est nulle :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0 $$

### Exemple concret 2 : Application du premier lemme

Soit une suite de variables aléatoires indépendantes $(X_n)_{n \ge 1}$ suivant des lois normales centrées réduites $\mathcal{N}(0, 1)$. Étudions la probabilité de l'événement $A_n = \{ |X_n| > 2\sqrt{\ln n} \}$.
D'après les propriétés de la queue de la loi normale, $\mathbb{P}(A_n) \le \frac{2}{\sqrt{2\pi}} \frac{e^{-2\ln n}}{2\sqrt{\ln n}} \le \frac{c}{n^2\sqrt{\ln n}}$.
La série de terme général $u_n = \frac{1}{n^2\sqrt{\ln n}}$ est convergente (critère de Riemann).
Ainsi, $\sum_{n=1}^{\infty} \mathbb{P}(A_n) < +\infty$.
D'après le premier lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 0$. Presque sûrement, il n'existe qu'un nombre fini d'indices $n$ pour lesquels $|X_n| > 2\sqrt{\ln n}$.

### Second lemme de Borel-Cantelli

Le second lemme traite de la divergence de la série, mais requiert une hypothèse d'indépendance.

**Théorème 2 (Second lemme de Borel-Cantelli) :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements **mutuellement indépendants** dans $\mathcal{F}$.
Si la série des probabilités diverge, i.e.,
$$ \sum_{n=0}^{\infty} \mathbb{P}(A_n) = +\infty $$
alors la probabilité que les $A_n$ se réalisent infiniment souvent est certaine :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1 $$

### Cas pathologique : Absence d'indépendance

Si l'hypothèse d'indépendance est relâchée dans le second lemme, le résultat s'effondre. Prenons un espace $\Omega = [0,1]$ muni de la mesure de Lebesgue. Soit l'événement fixe $A_n = [0, \frac{1}{2}]$ pour tout $n$.
$\mathbb{P}(A_n) = \frac{1}{2}$. La série $\sum \mathbb{P}(A_n) = \sum \frac{1}{2} = +\infty$.
Cependant, $\limsup A_n = \bigcap_{n} \bigcup_{k \ge n} [0, \frac{1}{2}] = [0, \frac{1}{2}]$.
Sa probabilité est $\mathbb{P}(\limsup A_n) = \frac{1}{2} \neq 1$. Les événements sont identiques, donc fortement corrélés, violant l'hypothèse d'indépendance.

## 4. Démonstrations rigoureuses

### Démonstration du premier lemme

Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements telle que $\sum_{n=0}^{\infty} \mathbb{P}(A_n) < +\infty$.
Par définition, $\limsup_{n \to \infty} A_n = \bigcap_{n=0}^{\infty} B_n$ où $B_n = \bigcup_{k=n}^{\infty} A_k$.
On remarque que la suite d'événements $(B_n)_{n \in \mathbb{N}}$ est décroissante pour l'inclusion :
$$ B_{n+1} = \bigcup_{k=n+1}^{\infty} A_k \subseteq \bigcup_{k=n}^{\infty} A_k = B_n $$
Puisque la mesure de probabilité $\mathbb{P}$ est continue par intersection décroissante et que $\mathbb{P}(B_0) \le 1 < \infty$, nous pouvons écrire :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = \mathbb{P}\left(\bigcap_{n=0}^{\infty} B_n\right) = \lim_{n \to \infty} \mathbb{P}(B_n) $$
En utilisant la sous-additivité (ou inégalité de Boole) de la mesure de probabilité, nous avons pour tout entier $n$ :
$$ \mathbb{P}(B_n) = \mathbb{P}\left(\bigcup_{k=n}^{\infty} A_k\right) \le \sum_{k=n}^{\infty} \mathbb{P}(A_k) $$
Puisque la série $\sum_{k=0}^{\infty} \mathbb{P}(A_k)$ est supposée convergente, la somme des restes tend vers zéro lorsque $n$ tend vers l'infini :
$$ \lim_{n \to \infty} \sum_{k=n}^{\infty} \mathbb{P}(A_k) = 0 $$
Il s'ensuit que :
$$ 0 \le \lim_{n \to \infty} \mathbb{P}(B_n) \le 0 $$
Ce qui démontre rigoureusement que $\mathbb{P}(\limsup_{n \to \infty} A_n) = 0$.

### Démonstration du second lemme

Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'événements mutuellement indépendants telle que $\sum_{n=0}^{\infty} \mathbb{P}(A_n) = +\infty$.
Nous allons démontrer que $\mathbb{P}\left((\limsup_{n \to \infty} A_n)^c\right) = 0$, où l'exposant $c$ dénote le complémentaire.
Par les lois de De Morgan :
$$ (\limsup_{n \to \infty} A_n)^c = \left(\bigcap_{n=0}^{\infty} \bigcup_{k=n}^{\infty} A_k\right)^c = \bigcup_{n=0}^{\infty} \bigcap_{k=n}^{\infty} A_k^c $$
Par sous-additivité, nous avons :
$$ \mathbb{P}\left((\limsup_{n \to \infty} A_n)^c\right) \le \sum_{n=0}^{\infty} \mathbb{P}\left(\bigcap_{k=n}^{\infty} A_k^c\right) $$
Fixons un entier $n \ge 0$. Par continuité par intersection décroissante de la probabilité, nous évaluons :
$$ \mathbb{P}\left(\bigcap_{k=n}^{\infty} A_k^c\right) = \lim_{m \to \infty} \mathbb{P}\left(\bigcap_{k=n}^{m} A_k^c\right) $$
L'indépendance mutuelle des événements $(A_k)$ implique l'indépendance de leurs complémentaires $(A_k^c)$. Ainsi :
$$ \mathbb{P}\left(\bigcap_{k=n}^{m} A_k^c\right) = \prod_{k=n}^{m} \mathbb{P}(A_k^c) = \prod_{k=n}^{m} (1 - \mathbb{P}(A_k)) $$
On utilise l'inégalité fondamentale pour tout réel $x \in \mathbb{R}$, $1 - x \le e^{-x}$. En l'appliquant pour $x = \mathbb{P}(A_k) \ge 0$, on obtient :
$$ \prod_{k=n}^{m} (1 - \mathbb{P}(A_k)) \le \prod_{k=n}^{m} e^{-\mathbb{P}(A_k)} = \exp\left(-\sum_{k=n}^{m} \mathbb{P}(A_k)\right) $$
En passant à la limite lorsque $m \to \infty$, comme par hypothèse $\sum_{k=n}^{\infty} \mathbb{P}(A_k) = +\infty$ pour tout $n$, la somme dans l'exponentielle tend vers l'infini, d'où :
$$ \lim_{m \to \infty} \exp\left(-\sum_{k=n}^{m} \mathbb{P}(A_k)\right) = e^{-\infty} = 0 $$
Il en résulte que pour tout $n$, $\mathbb{P}\left(\bigcap_{k=n}^{\infty} A_k^c\right) = 0$.
En sommant ces termes nuls sur $n$, on obtient :
$$ \mathbb{P}\left((\limsup_{n \to \infty} A_n)^c\right) \le 0 $$
Comme une probabilité est positive, $\mathbb{P}\left((\limsup_{n \to \infty} A_n)^c\right) = 0$, et par passage au complémentaire :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1 $$

## 5. Applications en Physique, Logique & Intelligence Artificielle

Les lemmes de Borel-Cantelli trouvent des applications profondes dans l'architecture algorithmique et la mécanique stochastique.

### Convergence des algorithmes d'apprentissage (SGD)

En Intelligence Artificielle, la Descente de Gradient Stochastique (SGD) repose sur la mise à jour des poids d'un réseau via une séquence de pas d'apprentissage $\eta_t$. La garantie que les itérés du gradient convergent presque sûrement vers un optimum local repose sur des conditions de Robbins-Monro (ex: $\sum \eta_t = \infty$ et $\sum \eta_t^2 < \infty$). Le premier lemme de Borel-Cantelli est mobilisé pour montrer que les déviations significatives de l'algorithme par rapport à sa trajectoire moyenne d'optimum ont une probabilité cumulée finie, et ne se produiront par conséquent qu'un nombre fini de fois presque sûrement.

### Percolation et modèles de graphes aléatoires

En physique statistique, et dans les réseaux de neurones en graphes (GNN), on étudie la connectivité de grands graphes aléatoires. Les lemmes de Borel-Cantelli permettent d'établir des seuils précis (phase transitions). Si la probabilité qu'un sous-graphe isolé apparaisse décroît suffisamment vite en fonction de sa taille, le premier lemme assure qu'il n'existera qu'un nombre fini de telles anomalies. Inversement, sous certaines conditions d'indépendance, la présence de structures infinies connectées est presque sûrement garantie par le second lemme.

### Complexité en logique formelle et SAT-Solvers

Dans l'analyse des solveurs de satisfiabilité booléenne (SAT), on injecte des variables aléatoires pour modéliser des clauses. En étudiant la probabilité qu'un ensemble de clauses mène à une contradiction, on utilise le premier lemme pour prouver que si un problème SAT comporte suffisamment de variables par rapport au nombre de clauses, la probabilité d'obtenir une configuration insoluble décroît suffisamment vite pour qu'asymptotiquement, la formule soit presque toujours satisfiable.
