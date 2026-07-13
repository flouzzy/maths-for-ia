---
uuid: "jalon-16"
title: "Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/sommation-infinie
prev: "[[Jalon-15.md]]"
next: "[[Jalon-17.md]]"
---
# Jalon 16 : Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy

## 1. Genèse du concept et intuition mathématique

L'idée de sommer une infinité de quantités remonte à l'Antiquité, avec les fameux paradoxes de Zénon d'Élée. Comment Achille peut-il rattraper la tortue s'il doit d'abord parcourir la moitié de la distance qui les sépare, puis le quart, puis le huitième, et ce à l'infini ? Cette aporie repose sur une confusion fondamentale entre l'infinité du nombre de termes sommés et la finitude potentielle de leur somme totale.

Historiquement, le besoin de formaliser la sommation infinie a émergé avec le développement du calcul infinitésimal par Newton et Leibniz, pour calculer des aires, des volumes, et résoudre des équations différentielles. Une somme infinie, que nous appelons aujourd'hui une série, n'est rien d'autre que la limite de la suite de ses sommes partielles. L'étude des séries à termes positifs est le point de départ de la théorie, car l'absence de compensation de signes simplifie l'analyse : la suite des sommes partielles est nécessairement croissante. Par le théorème de convergence monotone, l'unique question est de savoir si l'accumulation de ces grandeurs reste bornée ou s'échappe vers l'infini.

## 2. Énoncé symbolique et typage chirurgical

### A. Définitions Formelles

Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle.

**Définition 1 (Série numérique).** On appelle *série de terme général* $u_n$ la suite $(S_N)_{N \in \mathbb{N}}$ des sommes partielles définie par l'opérateur de sommation discrète :
$$S_N = \sum_{n=0}^N u_n$$

**Définition 2 (Convergence).** La série $\sum u_n$ converge si et seulement si la suite réelle $(S_N)_{N \in \mathbb{N}}$ admet une limite finie $S \in \mathbb{R}$. Dans ce cas, cette limite est appelée la *somme* de la série et est notée :
$$S = \sum_{n=0}^\infty u_n$$
Si la suite $(S_N)_{N \in \mathbb{N}}$ diverge (vers $\pm\infty$ ou n'admet pas de limite), on dit que la série diverge.

**Définition 3 (Série à termes positifs).** Une série $\sum u_n$ est dite à termes positifs si $\forall n \in \mathbb{N}, u_n \ge 0$.
*Remarque structurelle :* Pour une série à termes positifs, la suite des sommes partielles $(S_N)_{N \in \mathbb{N}}$ est strictement croissante (ou croissante). En effet, $S_{N+1} - S_N = u_{N+1} \ge 0$. D'après le théorème de la limite monotone, la série converge si et seulement si la suite $(S_N)_{N \in \mathbb{N}}$ est majorée. Sinon, elle diverge vers $+\infty$.

### B. Théorèmes Fondamentaux

**Théorème 1 (Critère de Comparaison).**
Soient $(u_n)_{n \in \mathbb{N}}$ et $(v_n)_{n \in \mathbb{N}}$ deux suites réelles telles que $0 \le u_n \le v_n$ à partir d'un certain rang $n_0 \in \mathbb{N}$.
1. Si la série $\sum v_n$ converge, alors la série $\sum u_n$ converge.
2. Si la série $\sum u_n$ diverge, alors la série $\sum v_n$ diverge.

**Théorème 2 (Règle de d'Alembert).**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle à termes strictement positifs ($\forall n \in \mathbb{N}, u_n > 0$).
Si la limite $\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = L$ existe dans $\mathbb{R}^+ \cup \{+\infty\}$ :
1. Si $L < 1$, la série $\sum u_n$ converge.
2. Si $L > 1$, la série $\sum u_n$ diverge.
3. Si $L = 1$, le critère est muet (aucune conclusion stricte ne peut être tirée).

**Théorème 3 (Règle de Cauchy).**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle à termes positifs.
Si la limite $\lim_{n \to \infty} \sqrt[n]{u_n} = L$ existe dans $\mathbb{R}^+ \cup \{+\infty\}$ :
1. Si $L < 1$, la série $\sum u_n$ converge.
2. Si $L > 1$, la série $\sum u_n$ diverge.
3. Si $L = 1$, le critère est muet.

## 3. Démonstrations et Cas Pathologiques

### A. Démonstration de la convergence de la série géométrique

Considérons la série géométrique $\sum q^n$ pour une raison $q \in [0, 1[$. Démontrons sa convergence absolue.

**Preuve.**
Soit $N \in \mathbb{N}$. Posons la somme partielle d'ordre $N$ :
$$S_N = \sum_{n=0}^N q^n = 1 + q + q^2 + \dots + q^N$$

Multiplions l'expression par $q$ :
$$q S_N = q + q^2 + q^3 + \dots + q^{N+1}$$

Soustrayons la seconde équation à la première pour faire apparaître une somme télescopique :
$$S_N - q S_N = (1 + q + q^2 + \dots + q^N) - (q + q^2 + q^3 + \dots + q^{N+1})$$

En regroupant et annulant les termes de même degré, il vient :
$$(1 - q) S_N = 1 - q^{N+1}$$

Puisque nous supposons $q < 1$, nous avons $1 - q \neq 0$. Nous pouvons isoler $S_N$ :
$$S_N = \frac{1 - q^{N+1}}{1 - q}$$

Étudions à présent le comportement limite lorsque $N \to +\infty$. Puisque la valeur absolue du scalaire $q$ vérifie $|q| < 1$, la limite de la suite géométrique $q^{N+1}$ est nulle :
$$\lim_{N \to \infty} q^{N+1} = 0$$

Par continuité des opérations algébriques sur les limites :
$$\lim_{N \to \infty} S_N = \lim_{N \to \infty} \frac{1 - q^{N+1}}{1 - q} = \frac{1 - 0}{1 - q} = \frac{1}{1 - q}$$

La limite étant finie, la série géométrique converge vers $\frac{1}{1 - q}$. $\blacksquare$

### B. Cas Pathologiques

Il est crucial d'étudier les limites des critères. Considérons le cas $L=1$ pour la règle de d'Alembert.

**Exemple de convergence (Série de Riemann pour $\alpha=2$) :**
Soit $u_n = \frac{1}{n^2}$. On a $u_{n+1} / u_n = \frac{n^2}{(n+1)^2} = \left(1 + \frac{1}{n}\right)^{-2}$.
La limite est $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{-2} = 1$. Et pourtant, cette série converge.

**Exemple de divergence (Série harmonique pour $\alpha=1$) :**
Soit $v_n = \frac{1}{n}$. On a $v_{n+1} / v_n = \frac{n}{n+1} = \left(1 + \frac{1}{n}\right)^{-1}$.
La limite est $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{-1} = 1$. Et pourtant, cette série diverge.

Cela prouve rigoureusement que le cas $L=1$ ne permet aucune conclusion immédiate sur la nature asymptotique de la série.

## 4. Application en Intelligence Artificielle et Sciences de l'Information

En apprentissage automatique, les séries infinies jouent un rôle sous-jacent central dans l'évaluation des processus stochastiques infinis et dans la conception des algorithmes d'optimisation.

Dans le cadre de l'**Apprentissage par Renforcement (Reinforcement Learning)**, modélisé par des Processus de Décision de Markov (MDP), un agent évolue dans un environnement et reçoit des récompenses $R_t$ à chaque pas de temps discret $t$. L'objectif est de maximiser la somme totale des récompenses. Or, si l'horizon temporel est infini (épisodes continus), la somme brute $\sum_{t=0}^\infty R_t$ divergerait trivialement vers $+\infty$, rendant la comparaison de politiques (fonctions de choix d'actions) mathématiquement indécidable.

Pour pallier ce problème de divergence asymptotique, on introduit un **facteur d'escompte (discount factor)** $\gamma \in [0, 1[$. Le retour cumulé (Discounted Return) est alors défini comme une série :
$$G_t = \sum_{k=0}^\infty \gamma^k R_{t+k+1}$$

Si les récompenses sont bornées, c'est-à-dire s'il existe une constante $R_{max}$ telle que $\forall t, |R_t| \le R_{max}$, alors par valeur absolue, le terme général de la série est majoré :
$$|\gamma^k R_{t+k+1}| \le \gamma^k R_{max}$$

La série majorante $\sum_{k=0}^\infty \gamma^k R_{max} = R_{max} \sum_{k=0}^\infty \gamma^k$ est proportionnelle à une série géométrique de raison $\gamma < 1$, qui est formellement convergente et vaut $\frac{R_{max}}{1 - \gamma}$.
En vertu du Critère de Comparaison, la série définissant $G_t$ converge absolument. Cette garantie théorique garantit que la fonction de valeur d'état (State-Value Function) $V^\pi(s) = \mathbb{E}^\pi[G_t | S_t = s]$ est bien définie, autorisant l'utilisation du théorème du point fixe de Banach pour les itérations de la fonction de valeur de Bellman.

## 5. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 13 (Structure de R)]], [[Jalon 14 (Suites réelles et complexes)]]
- **Concepts Futurs dépendants :** [[Jalon 17 (Séries absolument convergentes)]], [[Jalon 22 (Séries de fonctions)]], [[Jalon 23 (Séries entières)]], [[Jalon 85 (Axiomes de Kolmogorov)]]
