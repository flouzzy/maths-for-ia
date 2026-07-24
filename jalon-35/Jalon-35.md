---
uuid: "jalon-35"
title: "Caractérisation séquentielle des ouverts, des fermés et des compacts"
year: 1
trimester: 3
tags:
  - math/topologie
  - ia/convergence
prev: "[[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]]"
next: "[[Jalon 36 (Livrable IA).md]]"
---
# Jalon 35 : Caractérisation séquentielle des ouverts, des fermés et des compacts

## 1. Genèse et Motivation (Échafaudage Cognitif)

L'intuition topologique originelle repose sur la notion de voisinage et d'espace continu. Historiquement, des mathématiciens comme Weierstrass, Bolzano et Cantor ont cherché à formaliser les fondements de l'analyse réelle pour échapper aux paradoxes de l'infini et aux intuitions géométriques parfois trompeuses. Au lieu de décrire des "formes", ils ont choisi de définir la structure de l'espace à travers le comportement des suites qui l'habitent.

Pourquoi les suites ? Parce qu'elles incarnent le mouvement discret vers une limite. La caractérisation séquentielle traduit des propriétés globales (être un ouvert, un fermé, ou un compact) en un test local : que fait une suite infinie de points lorsqu'elle s'accumule ? Cette approche permet de transposer des concepts de $\mathbb{R}^n$ à des espaces fonctionnels de dimension infinie, où l'intuition visuelle échoue, mais où la logique des suites demeure implacable.

## 2. Le Protocole d'Exégèse Conceptuelle (Formalisation)

Soit $(E, \| \cdot \|)$ un espace vectoriel normé sur le corps $\mathbb{K}$ (où $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$).

### A. Caractérisation Séquentielle des Ouverts

**Énoncé Symbolique Strict :**
Une partie $U \subset E$ est un ouvert si et seulement si pour toute suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $E$ convergeant vers une limite $x \in U$, il existe un rang $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $x_n \in U$.

**Anatomie et Typage Chirurgical :**
- $U \subset E$ : La partie candidate à être ouverte.
- $(x_n)_{n \in \mathbb{N}} \in E^\mathbb{N}$ : Une suite quelconque de l'espace global $E$.
- $x \in U$ : La limite de la suite, qui se trouve à l'intérieur de l'ensemble $U$.
- $N \in \mathbb{N}$ : Le rang de "capture". À partir de cet instant discret, la suite ne quitte plus l'ensemble $U$.

**Exemples de Validation :**
- *Trivial :* $U = E$. Toute suite convergeant vers $x \in E$ est dans $E$, donc $E$ est ouvert.
- *Complexe :* $U = \mathbb{R} \setminus \{0\}$. Soit $x_n \to x \in U$. Alors $x \neq 0$. Si $x > 0$, pour $n$ assez grand, $x_n > x/2 > 0$, donc $x_n \in U$.

**Cas Pathologiques et Contre-exemples :**
- $U = [0, 1[$. Soit la suite $x_n = -1/n$. $x_n \to 0 \in U$. Cependant, pour tout $n \ge 1$, $x_n < 0$, donc $x_n \notin U$. Ainsi, $U$ n'est pas ouvert dans $\mathbb{R}$.

### B. Caractérisation Séquentielle des Fermés

**Énoncé Symbolique Strict :**
Une partie $F \subset E$ est un fermé si et seulement si pour toute suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $F$ convergeant vers une limite $x \in E$, alors $x \in F$.

**Anatomie et Typage Chirurgical :**
- $F \subset E$ : La partie candidate à être fermée.
- $(x_n)_{n \in \mathbb{N}} \in F^\mathbb{N}$ : Une suite entièrement contenue dans $F$.
- $x \in E$ : La limite de la suite dans l'espace ambiant $E$. Le critère exige que ce point limite "ne puisse pas s'échapper" de $F$.

**Exemples de Validation :**
- *Trivial :* $F = \emptyset$. Il n'y a pas de suite, la condition est trivialement vérifiée (vacuité).
- *Complexe :* Le segment $[a, b] \subset \mathbb{R}$. Si $x_n \in [a, b]$ et $x_n \to x$, le passage à la limite dans les inégalités $a \le x_n \le b$ donne $a \le x \le b$, donc $x \in [a, b]$.

**Cas Pathologiques et Contre-exemples :**
- $F = ]0, 1]$. La suite $x_n = 1/n$ vérifie $x_n \in F$ pour tout $n \ge 1$, et $x_n \to 0 \in \mathbb{R}$. Mais $0 \notin F$, donc $F$ n'est pas fermé.

### C. Caractérisation Séquentielle des Compacts (Propriété de Bolzano-Weierstrass)

**Énoncé Symbolique Strict :**
Une partie $K \subset E$ est compacte si et seulement si de toute suite $(x_n)_{n \in \mathbb{N}} \in K^\mathbb{N}$, on peut extraire une sous-suite $(x_{\phi(n)})_{n \in \mathbb{N}}$ qui converge vers une limite $x \in K$.

**Anatomie et Typage Chirurgical :**
- $K \subset E$ : La partie compacte.
- $(x_n)_{n \in \mathbb{N}} \in K^\mathbb{N}$ : Une suite infinie de points confinés dans $K$.
- $\phi : \mathbb{N} \to \mathbb{N}$ : Une extractrice, c'est-à-dire une application strictement croissante.
- $x_{\phi(n)}$ : La sous-suite extraite.
- $x \in K$ : La limite de la sous-suite, qui doit impérativement se trouver dans $K$.

**Exemples de Validation :**
- *Trivial :* Un ensemble fini $K = \{a_1, \dots, a_p\}$. Toute suite prend une infinité de fois la même valeur (principe des tiroirs), fournissant une sous-suite constante, donc convergente dans $K$.

**Cas Pathologiques et Contre-exemples :**
- $K = \mathbb{R}$. La suite $x_n = n$ ne possède aucune sous-suite convergente. Donc $\mathbb{R}$ n'est pas compact.
- Dans l'espace $\ell^2(\mathbb{N})$ (suites de carré sommable), la sphère unité fermée n'est pas compacte. La suite des vecteurs de base $(e_n)$ vérifie $\|e_n - e_m\| = \sqrt{2}$ pour $n \neq m$. Aucune sous-suite ne peut être de Cauchy, donc aucune ne peut converger. Le théorème de Heine-Borel s'effondre en dimension infinie.

## 3. Démonstrations (Zéro Ellipse)

### Théorème : Une partie est fermée si et seulement si elle contient les limites de ses suites convergentes.

**Preuve :**
Soit $(E, \| \cdot \|)$ un espace vectoriel normé et $F \subset E$.

**Sens direct ($\implies$) :**
Supposons $F$ fermé. Par définition topologique, le complémentaire $C_E F = E \setminus F$ est un ouvert.
Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments de $F$ convergeant vers un élément $x \in E$.
Raisonnons par l'absurde et supposons que $x \notin F$.
Cela implique que $x \in E \setminus F$.
Puisque $E \setminus F$ est un ouvert contenant $x$, il existe un rayon $r > 0$ tel que la boule ouverte $B(x, r)$ est incluse dans $E \setminus F$.
Puisque la suite $(x_n)_{n \in \mathbb{N}}$ converge vers $x$, par définition de la limite pour $\epsilon = r > 0$, il existe un rang $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $\|x_n - x\| < r$.
Cela signifie que pour $n \ge N$, $x_n \in B(x, r)$.
Or, $B(x, r) \subset E \setminus F$, donc $x_n \in E \setminus F$.
Mais nous avions supposé que la suite $(x_n)_{n \in \mathbb{N}}$ est à valeurs dans $F$. Nous avons donc $x_N \in F$ et $x_N \notin F$, ce qui constitue une contradiction.
Conclusion : l'hypothèse $x \notin F$ est fausse. Par conséquent, $x \in F$.

**Sens réciproque ($\impliedby$) :**
Supposons que toute suite de $F$ convergeant dans $E$ admet sa limite dans $F$.
Montrons que $F$ est fermé, c'est-à-dire que $E \setminus F$ est ouvert.
Raisonnons par l'absurde et supposons que $E \setminus F$ n'est pas ouvert.
Par définition d'un ouvert, cela signifie qu'il existe un point $x \in E \setminus F$ tel que pour tout rayon $r > 0$, la boule ouverte $B(x, r)$ n'est pas incluse dans $E \setminus F$.
C'est-à-dire que pour tout $r > 0$, l'intersection $B(x, r) \cap F \neq \emptyset$.
Appliquons ceci pour une suite de rayons $r_n = \frac{1}{n+1}$ pour tout $n \in \mathbb{N}$.
Pour chaque $n \in \mathbb{N}$, il existe au moins un élément $x_n \in B(x, \frac{1}{n+1}) \cap F$.
Nous venons de construire une suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $F$.
Évaluons la distance de $x_n$ à $x$ : $0 \le \|x_n - x\| < \frac{1}{n+1}$.
En passant à la limite quand $n \to \infty$, le théorème des gendarmes implique que $\lim_{n \to \infty} \|x_n - x\| = 0$.
Donc la suite $(x_n)_{n \in \mathbb{N}}$ converge vers $x$ dans $E$.
D'après l'hypothèse de départ, puisque $(x_n)_{n \in \mathbb{N}} \in F^\mathbb{N}$ et $x_n \to x$, nous devons avoir $x \in F$.
Or, notre point $x$ a été choisi tel que $x \in E \setminus F$. Nous avons donc $x \in F$ et $x \notin F$, ce qui est une contradiction.
Conclusion : $E \setminus F$ est bien un ouvert. Par conséquent, $F$ est un fermé. $\blacksquare$
