---
uuid: "jalon-63"
title: "Définition axiomatique d'une mesure"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/probabilites
prev: "[[Jalon 62 (Algèbres).md]]"
next: "[[Jalon 64 (Construction pas à pas de la mesure de Lebesgue sur Rn via la mesure extérieure.).md]]"
---

# 1. Naissance d'une géométrie universelle

L'histoire de la mesure est d'abord celle de l'échec de l'intuition naïve. Depuis l'Antiquité, de la quadrature de la parabole par Archimède à l'intégrale de Riemann, les mathématiciens ont cherché à attribuer de manière univoque et consistante une notion de "volume", d'"aire" ou de "longueur" aux sous-ensembles de $\mathbb{R}^n$. L'intégrale de Riemann a permis de quantifier des aires sous des courbes continues, mais elle se fracasse violemment sur des fonctions rugueuses, partout discontinues, comme la fonction indicatrice de $\mathbb{Q}$ (fonction de Dirichlet).

Le passage à la limite sous le signe intégral devenait souvent illégitime. En 1902, Henri Lebesgue, s'appuyant sur les travaux de Borel, change de paradigme. Au lieu de partitionner l'axe des abscisses (Riemann), il partitionne l'axe des ordonnées. Mais pour que cela fonctionne, il fallait pouvoir "mesurer" l'ensemble des points d'abscisse dont l'image tombe dans un certain intervalle. Or, cet ensemble peut être horriblement fragmenté.

L'axiomatisation d'une "mesure" ne cherche plus à définir *a priori* comment calculer le volume, mais pose les **règles universelles** auxquelles tout procédé d'attribution de volume doit obéir. Kolmogorov, en 1933, réalisera que cette théorie de la mesure est le langage absolu des probabilités. La probabilité d'un événement n'est rien d'autre que la mesure de cet événement dans l'univers de tous les possibles, unifiant ainsi la géométrie et l'aléatoire.

# 2. Théorie axiomatique et structure mesurable

Le cadre d'étude est un **espace mesurable** $(X, \mathcal{A})$, où $X$ est un ensemble et $\mathcal{A}$ est une tribu (ou $\sigma$-algèbre) sur $X$. Les éléments de $\mathcal{A}$ sont appelés les ensembles mesurables.

## Définition formelle de la mesure

> **Définition 1 (Mesure positive) :**
> Une application $\mu : \mathcal{A} \to [0, +\infty]$ est appelée **mesure** (ou mesure positive) sur l'espace mesurable $(X, \mathcal{A})$ si elle vérifie les deux axiomes fondamentaux suivants :
> 1. **Mesure de l'ensemble vide :** $\mu(\emptyset) = 0$.
> 2. **$\sigma$-additivité :** Pour toute suite $(A_n)_{n \in \mathbb{N}}$ d'éléments de $\mathcal{A}$, deux à deux disjoints (i.e. $A_i \cap A_j = \emptyset$ pour $i \neq j$), on a :
>    $$ \mu\left( \bigcup_{n=0}^{+\infty} A_n \right) = \sum_{n=0}^{+\infty} \mu(A_n) $$
>
> Le triplet $(X, \mathcal{A}, \mu)$ est alors appelé un **espace mesuré**.

L'axiome de $\sigma$-additivité est le cœur battant de l'analyse moderne : il autorise le passage à la limite infinie en convertissant une union dénombrable géométrique en une série numérique.

**Exemple de mesure de Dirac sur $(\mathbb{R}, \mathcal{P}(\mathbb{R}))$**
Soit $a \in \mathbb{R}$. La mesure de Dirac au point $a$, notée $\delta_a$, est définie pour tout $A \in \mathcal{P}(\mathbb{R})$ par :
$$ \delta_a(A) = \left\lbrace \begin{array}{ll} 1 & \text{si } a \in A \\ 0 & \text{si } a \notin A \end{array} \right. $$

*Calculons $\delta_a(\bigcup_{n=0}^{\infty} A_n)$ avec $A_n = [n, n+1[$ et $a = 2.5$.*
Les intervalles $A_n$ sont deux à deux disjoints. Leur union est $\mathbb{R}_+$.
$\delta_{2.5}(\mathbb{R}_+) = 1$ car $2.5 \in \mathbb{R}_+$.
Par ailleurs, $\sum_{n=0}^\infty \delta_{2.5}(A_n) = \delta_{2.5}([0, 1[) + \delta_{2.5}([1, 2[) + \delta_{2.5}([2, 3[) + \dots = 0 + 0 + 1 + 0 + \dots = 1$. L'égalité est respectée.

## Propriétés fondamentales de continuité

Une mesure, par sa construction, interagit parfaitement avec les suites d'ensembles.

> **Théorème 1 (Croissance et continuité croissante) :**
> Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
> 1. **Monotonie :** Pour tout couple d'ensembles $(A, B) \in \mathcal{A}^2$, si $A \subset B$, alors $\mu(A) \leq \mu(B)$.
> 2. **Continuité croissante (ou continuité par le bas) :** Si $(A_n)_{n \in \mathbb{N}}$ est une suite d'ensembles mesurables **croissante** (i.e. $A_n \subset A_{n+1}$ pour tout $n$), alors :
>    $$ \mu\left( \bigcup_{n=0}^{+\infty} A_n \right) = \lim_{n \to +\infty} \mu(A_n) = \sup_{n \in \mathbb{N}} \mu(A_n) $$

**Exemple concret immédiat :**
Sur $(\mathbb{N}, \mathcal{P}(\mathbb{N}))$, considérons la mesure de comptage $\mu(A) = \text{Card}(A)$.
Soit $A_n = \{0, 1, \dots, n\}$. On a clairement $A_n \subset A_{n+1}$.
La limite géométrique est $A = \bigcup_{n=0}^{\infty} A_n = \mathbb{N}$.
La mesure de cette limite est $\mu(\mathbb{N}) = +\infty$.
La limite des mesures est $\lim_{n \to \infty} \mu(A_n) = \lim_{n \to \infty} (n+1) = +\infty$.
Le théorème opère même avec la valeur infinie.

> **Théorème 2 (Continuité décroissante) :**
> Si $(A_n)_{n \in \mathbb{N}}$ est une suite d'ensembles mesurables **décroissante** (i.e. $A_{n+1} \subset A_n$) telle que la mesure du premier terme est finie, soit **$\mu(A_0) < +\infty$**, alors :
> $$ \mu\left( \bigcap_{n=0}^{+\infty} A_n \right) = \lim_{n \to +\infty} \mu(A_n) = \inf_{n \in \mathbb{N}} \mu(A_n) $$

**Le contre-exemple pathologique en l'absence de condition de finitude :**
Considérons la mesure de Lebesgue sur $\mathbb{R}$ (longueur des intervalles), et la suite décroissante $A_n = [n, +\infty[$.
On a $\mu(A_n) = +\infty$ pour tout $n$. Donc $\lim_{n \to \infty} \mu(A_n) = +\infty$.
Cependant, géométriquement, l'intersection $\bigcap_{n=0}^{\infty} [n, +\infty[ = \emptyset$.
La mesure de l'intersection est $\mu(\emptyset) = 0$.
Ici, $0 \neq +\infty$. La continuité décroissante est brisée car $\mu(A_0) = +\infty$. L'hypothèse de mesure finie initiale est une obligation stricte et non négociable.

# 3. Démonstrations algébriques

Nous démontrons ici le théorème de continuité croissante. L'élégance de cette preuve réside dans la conversion d'une union croissante (qui n'est pas disjointe) en une union disjointe, afin de pouvoir invoquer l'axiome de $\sigma$-additivité.

**Démonstration (Continuité croissante) :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite croissante d'éléments de $\mathcal{A}$. Notons $A = \bigcup_{n=0}^{+\infty} A_n$.
Nous définissons une nouvelle suite $(B_n)_{n \in \mathbb{N}}$ par le procédé d'orthogonalisation ensembliste suivant :
- $B_0 = A_0$
- $B_n = A_n \setminus A_{n-1}$ pour $n \geq 1$.

Par construction, les $B_n$ sont mesurables, et ils sont **deux à deux disjoints**.
De plus, il est clair que pour tout $N \in \mathbb{N}$ :
$$ \bigcup_{n=0}^{N} B_n = A_N $$
Et par passage à la limite, la réunion infinie des $(B_n)$ reconstitue l'ensemble $A$ :
$$ \bigcup_{n=0}^{+\infty} B_n = \bigcup_{n=0}^{+\infty} A_n = A $$

Nous pouvons maintenant invoquer l'axiome de $\sigma$-additivité sur la suite disjointe $(B_n)$ :
$$ \mu(A) = \mu\left( \bigcup_{n=0}^{+\infty} B_n \right) = \sum_{n=0}^{+\infty} \mu(B_n) $$
Par définition de la somme d'une série numérique, c'est la limite de ses sommes partielles :
$$ \sum_{n=0}^{+\infty} \mu(B_n) = \lim_{N \to +\infty} \sum_{n=0}^{N} \mu(B_n) $$
Or, par la propriété d'additivité finie (qui est un corollaire direct de la $\sigma$-additivité en prenant $B_k = \emptyset$ pour $k > N$) :
$$ \sum_{n=0}^{N} \mu(B_n) = \mu\left( \bigcup_{n=0}^{N} B_n \right) = \mu(A_N) $$
En injectant cette égalité, il vient immédiatement :
$$ \mu(A) = \lim_{N \to +\infty} \mu(A_N) $$
Ce qui achève rigoureusement la démonstration. $\blacksquare$

# 4. Injections dans l'Intelligence Artificielle et la Probabilité Théorique

L'axiomatisation de la mesure est la pierre angulaire de l'Apprentissage Automatique Statistique (Statistical Machine Learning) et de la théorie probabiliste moderne.

- **Cadre formel de Kolmogorov :** En 1933, Andreï Kolmogorov définit l'espace de probabilité probabiliste formel $(\Omega, \mathcal{F}, \mathbb{P})$, où la probabilité $\mathbb{P}$ n'est absolument rien d'autre qu'une mesure positive de masse totale $\mathbb{P}(\Omega) = 1$. L'ensemble de la théorie des probabilités s'effondre dans le giron de l'analyse réelle.
- **Divergence de Kullback-Leibler et Théorie de l'Information :** Dans l'entraînement des réseaux de neurones génératifs (GANs, VAEs, Modèles de diffusion), l'objectif est souvent de minimiser une "distance" entre une distribution cible $\mathbb{P}_{data}$ et une distribution générée $\mathbb{P}_\theta$. En théorie de la mesure, on étudie l'absolue continuité d'une mesure par rapport à une autre. La dérivée de Radon-Nikodym $d\mathbb{P}_\theta / d\mathbb{P}_{data}$ permet de définir rigoureusement la Cross-Entropy et la divergence KL.
- **Apprentissage Actif et Mesure de Lebesgue :** Lorsqu'on échantillonne uniformément l'espace des paramètres pour explorer un espace latent continu en IA, on s'appuie implicitement sur la mesure de Lebesgue pour garantir que l'on ne laisse aucune zone de volume non nul inexplorée.
- **Optimisation et sous-ensembles de mesure nulle :** Le célèbre théorème de Rademacher stipule qu'une fonction lipschitzienne est différentiable presque partout. Le "presque partout" (p.p.) signifie que l'ensemble des points de non-différentiabilité a une **mesure nulle** pour la mesure de Lebesgue. Les algorithmes de Descente de Gradient (SGD) sur des fonctions d'activation comme ReLU (non différentiable en 0) sont mathématiquement justifiés précisément parce que la singularité n'occupe qu'une région de mesure de Lebesgue nulle dans l'espace des poids.
