---
uuid: "jalon-64"
title: "Construction de la mesure de Lebesgue"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/abstraction
prev: "[[Jalon 63 (Définition axiomatique d'une mesure).md]]"
next: "[[Jalon 65 (Fonctions mesurables).md]]"
---

# Introduction

La théorie de l'intégration de Riemann souffre de limitations fondamentales. Elle échoue à mesurer des ensembles denses ou présentant de multiples discontinuités, comme l'ensemble des rationnels $\mathbb{Q}$ dans $\mathbb{R}$. Pour surmonter cet écueil et asseoir une théorie de l'intégration complète et stable par passage à la limite, il est impératif de concevoir une fonction d'ensemble capable d'attribuer une "taille" cohérente à la plus vaste classe possible de sous-ensembles de $\mathbb{R}$.

La démarche, formalisée par Henri Lebesgue et Constantin Carathéodory, procède en deux temps :
1. Définir une fonction, la \textbf{mesure extérieure}, applicable à toute partie de $\mathbb{R}$, en optimisant le recouvrement de cet ensemble par des intervalles ouverts.
2. Restreindre cette fonction à une classe spécifique d'ensembles, la tribu des \textbf{ensembles mesurables}, pour garantir la propriété cruciale de $\sigma$-additivité, indispensable à toute théorie de la mesure robuste.

\begin{tikzpicture}[scale=1]
  \draw[->, thick] (-1,0) -- (8,0) node[right] {$\mathbb{R}$};
  \fill[blue, opacity=0.3] (0.5,0) rectangle (2.5,0.5);
  \fill[blue, opacity=0.3] (3.0,0) rectangle (4.2,0.5);
  \fill[blue, opacity=0.3] (5.0,0) rectangle (7.0,0.5);

  \draw[red, thick, dashed] (0.3,-0.2) rectangle (2.7,0.7);
  \draw[red, thick, dashed] (2.8,-0.2) rectangle (4.4,0.7);
  \draw[red, thick, dashed] (4.8,-0.2) rectangle (7.2,0.7);

  \node[blue] at (1.5, 0.25) {$A_1$};
  \node[blue] at (3.6, 0.25) {$A_2$};
  \node[blue] at (6.0, 0.25) {$A_3$};

  \node[red] at (1.5, 0.9) {$I_1$};
  \node[red] at (3.6, 0.9) {$I_2$};
  \node[red] at (6.0, 0.9) {$I_3$};

  \node at (3.5, -1) {Recouvrement d'un ensemble $A = A_1 \cup A_2 \cup A_3$ par des intervalles ouverts $I_n$.};
\end{tikzpicture}

# Définitions, Théorèmes et Exemples Concrets

## Mesure extérieure de Lebesgue

Soit $\mathcal{P}(\mathbb{R})$ l'ensemble des parties de $\mathbb{R}$.
Pour tout intervalle ouvert $I = ]a, b[$, on définit sa longueur $\ell(I) = b - a$.

**Définition (Mesure extérieure) :**
Pour toute partie $A \subset \mathbb{R}$, la mesure extérieure de Lebesgue $\lambda^*(A)$ est définie comme l'infimum de la somme des longueurs des intervalles d'un recouvrement dénombrable ouvert de $A$. Formellement :
$$\lambda^*(A) = \inf \left\lbrace \sum_{n=1}^\infty \ell(I_n) \mid A \subset \bigcup_{n=1}^\infty I_n, \ I_n \text{ intervalles ouverts} \right\rbrace$$

Cette fonction $\lambda^* : \mathcal{P}(\mathbb{R}) \to [0, +\infty]$ possède des propriétés fondamentales :
- Positivité : $\lambda^*(A) \ge 0$.
- Monotonie : Si $A \subset B$, alors $\lambda^*(A) \le \lambda^*(B)$.
- Sous-additivité dénombrable : Pour toute suite $(A_n)_{n \in \mathbb{N}}$, $\lambda^*\left(\bigcup_{n=1}^\infty A_n\right) \le \sum_{n=1}^\infty \lambda^*(A_n)$.

**Exemple 1 : Mesure extérieure d'un point**
Soit $A = \{x\}$ un singleton. Pour tout $\epsilon > 0$, l'intervalle ouvert $I = ]x - \frac{\epsilon}{2}, x + \frac{\epsilon}{2}[$ recouvre $A$ et possède une longueur $\ell(I) = \epsilon$. L'infimum sur tous les recouvrements possibles est donc $0$. Ainsi, $\lambda^*(\{x\}) = 0$.

**Exemple 2 : Mesure extérieure d'un ensemble dénombrable**
Soit $\mathbb{Q} \subset \mathbb{R}$. $\mathbb{Q}$ est dénombrable, on peut l'énumérer : $\mathbb{Q} = \{q_1, q_2, \dots\}$. Fixons $\epsilon > 0$. Pour chaque $q_n$, définissons l'intervalle ouvert $I_n = \left] q_n - \frac{\epsilon}{2^{n+1}}, q_n + \frac{\epsilon}{2^{n+1}} \right[$. La suite $(I_n)$ recouvre $\mathbb{Q}$.
La somme des longueurs est $\sum_{n=1}^\infty \ell(I_n) = \sum_{n=1}^\infty \frac{\epsilon}{2^n} = \epsilon$. L'infimum étant pris sur tous les $\epsilon > 0$, on obtient $\lambda^*(\mathbb{Q}) = 0$.

**Exemple 3 : Mesure extérieure d'un intervalle fermé**
Soit $A = [a, b]$. Pour tout $\epsilon > 0$, l'intervalle ouvert $I = ]a - \frac{\epsilon}{2}, b + \frac{\epsilon}{2}[$ recouvre $A$ et sa longueur est $b - a + \epsilon$. L'infimum est au plus $b - a$. On démontrera formellement plus loin que $\lambda^*([a, b]) = b - a$.

## Le Critère de Carathéodory et les Ensembles Mesurables

La mesure extérieure n'est pas additive sur des ensembles disjoints quelconques. Il est nécessaire de restreindre la classe des ensembles considérés.

**Définition (Ensemble Lebesgue-mesurable) :**
Un ensemble $E \subset \mathbb{R}$ est dit mesurable au sens de Lebesgue s'il divise additivement tout ensemble test (critère de Carathéodory). Pour toute partie $A \subset \mathbb{R}$ :
$$\lambda^*(A) = \lambda^*(A \cap E) + \lambda^*(A \setminus E)$$

La classe de ces ensembles, notée $\mathcal{L}(\mathbb{R})$, forme une tribu, qui contient la tribu borélienne $\mathcal{B}(\mathbb{R})$.

\begin{tikzpicture}[scale=1]
  \draw[thick] (0,0) ellipse (3cm and 2cm);
  \node at (-1.5, 1) {$A \cap E$};
  \node at (1.5, 1) {$A \setminus E$};

  \draw[thick, dashed] (0, -2) -- (0, 2);
  \node[above] at (0, 2) {Frontière de $E$};
  \node at (-3.5, 2) {Ensemble test $A$};
\end{tikzpicture}

**Définition (Mesure de Lebesgue) :**
La mesure de Lebesgue, notée $\lambda$, est la restriction de la mesure extérieure $\lambda^*$ à la tribu $\mathcal{L}(\mathbb{R})$. Le triplet $(\mathbb{R}, \mathcal{L}(\mathbb{R}), \lambda)$ constitue l'espace mesuré de Lebesgue standard, et $\lambda$ est une mesure positive, complète et $\sigma$-additive.

**Exemple 4 : Invariance par translation**
Si $E \in \mathcal{L}(\mathbb{R})$ et $x \in \mathbb{R}$, alors $E + x = \{y + x \mid y \in E\}$ est Lebesgue-mesurable et $\lambda(E + x) = \lambda(E)$. La mesure de Lebesgue est l'unique mesure de Radon invariante par translation sur $\mathbb{R}$ (à une constante multiplicative près), ce qui formalise le concept intuitif de volume invariant.

**Exemple 5 : Mesure d'un segment**
En combinant les propriétés, la mesure de Lebesgue d'un segment fermé $\lambda([a, b]) = b - a$, d'un segment ouvert $\lambda(]a, b[) = b - a$, et d'un intervalle semi-ouvert $\lambda([a, b[) = b - a$.

**Exemple 6 : Ensembles pathologiques**
Il existe des parties de $\mathbb{R}$ qui ne sont pas Lebesgue-mesurables (nécessitant l'Axiome du Choix pour leur construction, tel l'ensemble de Vitali). L'existence de tels ensembles motive la restriction imposée par le critère de Carathéodory. L'ensemble de Cantor est un exemple remarquable d'ensemble non dénombrable, compact, d'intérieur vide, mais de mesure de Lebesgue nulle.

# Démonstrations

**Démonstration : L'ensemble de Cantor est de mesure de Lebesgue nulle**
Construisons l'ensemble triadique de Cantor $C$.
Soit $C_0 = [0, 1]$. On a $\lambda(C_0) = 1$.
Étape 1 : On retire le tiers central ouvert. $C_1 = [0, \frac{1}{3}] \cup [\frac{2}{3}, 1]$.
La mesure est $\lambda(C_1) = \lambda([0, \frac{1}{3}]) + \lambda([\frac{2}{3}, 1]) = \frac{1}{3} + \frac{1}{3} = \frac{2}{3}$.
Étape $n$ : L'ensemble $C_n$ est la réunion de $2^n$ intervalles fermés disjoints, chacun de longueur $(1/3)^n$.
Par additivité, $\lambda(C_n) = 2^n \times \left(\frac{1}{3}\right)^n = \left(\frac{2}{3}\right)^n$.
L'ensemble de Cantor est $C = \bigcap_{n=0}^\infty C_n$.
Puisque $(C_n)$ est une suite décroissante d'ensembles mesurables et $\lambda(C_0) < \infty$, la continuité décroissante de la mesure donne :
$$\lambda(C) = \lim_{n \to \infty} \lambda(C_n) = \lim_{n \to \infty} \left(\frac{2}{3}\right)^n = 0$$
L'ensemble de Cantor est donc non dénombrable (en bijection avec $\{0, 1\}^{\mathbb{N}}$) mais de mesure nulle. C'est une structure fractale fondamentale.

# Applications

La formalisation de la mesure de Lebesgue est un prérequis incontournable pour des fondations solides en probabilités et en apprentissage statistique (Machine Learning).

- **Espaces de probabilité et variables aléatoires :** En théorie des probabilités (Axiomatisation de Kolmogorov), l'espace fondamental $(\Omega, \mathcal{F}, \mathbb{P})$ s'appuie structurellement sur la théorie de la mesure. Pour les variables aléatoires continues réelles, la mesure de probabilité s'exprime par intégration (au sens de Lebesgue) d'une fonction de densité par rapport à la mesure de Lebesgue $\lambda$.
- **Garanties de convergence en Apprentissage :** Dans l'apprentissage PAC (Probably Approximately Correct), les théorèmes de convergence du risque empirique (Lois fortes des grands nombres, inégalités de concentration) nécessitent que les fonctions de perte soient mesurables. La robustesse de la théorie de la mesure sous-tend la validité des bornes de généralisation.
- **Réseaux Génératifs Adversariaux (GANs) :** Le support de la distribution des images naturelles plonge dans un espace de très haute dimension (ex: un million de pixels), mais réside sur une variété (manifold) de dimension intrinsèque beaucoup plus faible. L'ensemble des images possibles a donc une mesure de Lebesgue nulle dans l'espace ambiant. Cette propriété explique l'explosion des divergences f-séparables et a motivé l'introduction de la distance de Wasserstein (Transport Optimal) qui se fonde sur des mesures plus complexes.
