---
uuid: "jalon-56"
title: "Espaces métriques complets"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/convergence
prev: "[[Jalon-55.md]]"
next: "[[Jalon 57 (Théorème du point fixe de Banach).md]]"
---

# Espaces métriques complets

## Introduction et genèse du concept

La construction de la théorie de la convergence nécessite un cadre où les suites qui "devraient" converger le font effectivement. Historiquement, l'insuffisance de l'ensemble des rationnels $\mathbb{Q}$ s'est manifestée lorsque des suites rationnelles s'approchant indéfiniment de $\sqrt{2}$ ne trouvaient aucune limite dans $\mathbb{Q}$. Cette "absence de trou" dans l'espace est le cœur de la complétude.

Une suite dont les termes se rapprochent arbitrairement les uns des autres (suite de Cauchy) possède un comportement intrinsèque de convergence, indépendamment du point limite. Un espace métrique est dit complet si ce comportement intrinsèque garantit l'existence effective d'une limite au sein de cet espace.

## Définitions, Théorèmes et Exemples Immédiats

Soit $(X, d)$ un espace métrique.

\textbf{Définition (Suite de Cauchy) :}
Une suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $X$ est dite de Cauchy si, pour tout seuil d'éloignement, les termes de la suite finissent par être tous proches les uns des autres. Formellement :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}, \forall p, q \geq N, \quad d(x_p, x_q) < \epsilon $$

\textbf{Définition (Espace Complet) :}
Un espace métrique $(X, d)$ est complet si toute suite de Cauchy d'éléments de $X$ converge vers un élément de $X$.
Un espace vectoriel normé complet est appelé espace de Banach. Un espace préhilbertien complet est un espace de Hilbert.

\textbf{Exemple concret immédiat : L'espace $\mathbb{R}$}
La droite réelle $(\mathbb{R}, |\cdot|)$ est complète. C'est le théorème fondamental de l'analyse réelle, qui découle de l'axiome de la borne supérieure. Ainsi, la suite définie par $x_{n+1} = \frac{1}{2}(x_n + \frac{2}{x_n})$ avec $x_0 = 1$ est de Cauchy et converge vers $\sqrt{2} \in \mathbb{R}$.

\textbf{Exemple concret de non-complétude : L'espace $\mathbb{Q}$}
L'espace des rationnels $(\mathbb{Q}, |\cdot|)$ n'est pas complet. Reprenons la suite $x_{n+1} = \frac{1}{2}(x_n + \frac{2}{x_n})$. Les termes $(x_n)$ sont tous rationnels. On a $|x_p - x_q| \to 0$ : la suite est de Cauchy. Cependant, elle n'admet aucune limite dans $\mathbb{Q}$ (puisque $\sqrt{2} \notin \mathbb{Q}$).

\textbf{Exemple géométrique : Les sous-espaces de $\mathbb{R}$}
- L'intervalle fermé $[0, 1]$ est complet (tout sous-espace fermé d'un complet est complet).
- L'intervalle ouvert $]0, 1[$ n'est pas complet. La suite $x_n = \frac{1}{n}$ est de Cauchy (car $x_n \to 0$ dans $\mathbb{R}$), mais elle ne converge pas dans $]0, 1[$ puisque $0 \notin ]0, 1[$.

\textbf{Illustration géométrique : Complétion d'un espace}
\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Espaces
  \draw[thick, blue] (-2,0) -- (-0.1,0);
  \draw[thick, blue] (0.1,0) -- (2,0);
  \fill[white] (0,0) circle (0.1);
  \draw[red, dashed] (0,0) circle (0.1);

  % Suite
  \fill[black] (-1.5,0) circle (1pt) node[below] {$x_0$};
  \fill[black] (-0.8,0) circle (1pt) node[below] {$x_1$};
  \fill[black] (-0.4,0) circle (1pt) node[below] {$x_2$};
  \fill[black] (-0.2,0) circle (1pt) node[below] {$x_3$};

  % Flèches
  \draw[->, gray] (-1.4, 0.1) to[bend left=20] (-0.9, 0.1);
  \draw[->, gray] (-0.7, 0.1) to[bend left=20] (-0.5, 0.1);
  \draw[->, gray] (-0.3, 0.1) to[bend left=20] (-0.25, 0.1);

  \node[above, text width=6cm, align=center] at (0, 0.5) {Suite de Cauchy dans un espace percé (non complet). La limite "virtuelle" n'appartient pas à l'espace.};
\end{tikzpicture}
\end{center}

\textbf{Théorème (Fermé d'un complet) :}
Soit $(X, d)$ un espace métrique complet et $F$ une partie de $X$.
Alors $(F, d)$ est complet si et seulement si $F$ est fermée dans $X$.

\textbf{Exemple immédiat :}
Soit $X = \mathbb{R}$ qui est complet. L'intervalle $F = [0, 1]$ est fermé dans $\mathbb{R}$, il est donc complet. En revanche, l'intervalle $]0, 1]$ n'est pas fermé (le point $0$ est adhérent mais pas dans l'ensemble), donc il n'est pas complet (la suite $1/n$ est de Cauchy mais ne converge pas dans l'ensemble).

\textbf{Théorème de prolongement des applications uniformément continues :}
Soit $(X, d_X)$ un espace métrique, $A$ une partie dense de $X$. Soit $(Y, d_Y)$ un espace métrique \textbf{complet}. Si $f : A \to Y$ est uniformément continue, alors $f$ admet un unique prolongement continu $\tilde{f} : X \to Y$, et $\tilde{f}$ est uniformément continue.

\textbf{Exemple immédiat :}
Considérons $X = \mathbb{R}$, $Y = \mathbb{R}$, et $A = \mathbb{Q}$ (qui est dense dans $\mathbb{R}$). Soit $f : \mathbb{Q} \to \mathbb{R}$ définie par $f(x) = \sin(x)$. La fonction $f$ est uniformément continue sur $\mathbb{Q}$ car sa dérivée est bornée par 1, ce qui implique $|f(x) - f(y)| \le |x - y|$. Puisque $\mathbb{R}$ est complet, le théorème garantit qu'il existe un unique prolongement continu $\tilde{f}$ défini sur tout $\mathbb{R}$. Ce prolongement est bien sûr la fonction sinus usuelle sur les réels.

## Démonstrations

\textbf{Démonstration : Un fermé d'un complet est complet}
1. \textit{Hypothèse :} Soit $(X, d)$ un espace complet et $F \subset X$ un fermé. Montrons que $F$ est complet.
2. \textit{Initialisation :} Soit $(x_n)_{n \in \mathbb{N}}$ une suite de Cauchy d'éléments de $F$.
3. \textit{Complétude de l'espace ambiant :} Puisque $(x_n)$ est une suite de Cauchy dans l'espace complet $X$, elle admet une limite $l \in X$.
4. \textit{Fermeture :} Par caractérisation séquentielle des fermés (les limites de suites de $F$ appartiennent à $F$), puisque $x_n \in F$ pour tout $n$ et $x_n \to l$, alors $l \in F$.
5. \textit{Conclusion :} Toute suite de Cauchy de $F$ converge vers un élément de $F$. Donc $F$ est complet.

\textbf{Démonstration : Toute suite convergente est de Cauchy}
1. \textit{Hypothèse :} Soit $(x_n)$ une suite convergeant vers $l \in X$.
2. \textit{Majoration :} Soit $\epsilon > 0$. Par définition de la limite, il existe $N \in \mathbb{N}$ tel que pour tout $n \geq N$, $d(x_n, l) < \frac{\epsilon}{2}$.
3. \textit{Inégalité triangulaire :} Pour tout $p, q \geq N$, on a :
$$ d(x_p, x_q) \leq d(x_p, l) + d(l, x_q) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon $$
4. \textit{Conclusion :} La suite est bien de Cauchy.

## Applications en Physique, Logique et IA

\textbf{Intelligence Artificielle et Optimisation :}
Dans l'entraînement des réseaux de neurones, la descente de gradient génère une suite de paramètres $\theta_n$. La théorie garantit que si cette suite est de Cauchy (la variation des paramètres tend vers zéro), l'espace des paramètres $\mathbb{R}^k$ étant complet, la suite convergera vers un point $\theta^*$ (un minimum local). Sans la complétude, l'algorithme pourrait chercher éternellement un minimum n'existant pas dans l'espace de recherche.

\textbf{Espaces de Hilbert en Machine Learning (RKHS) :}
Les méthodes à noyaux (Support Vector Machines) opèrent dans des espaces de fonctions appelés RKHS (Reproducing Kernel Hilbert Spaces). La complétude de ces espaces de Hilbert est fondamentale pour garantir l'existence du classifieur optimal (Théorème de représentation).

\textbf{Équations aux Dérivées Partielles (EDP) :}
En physique (mécanique des fluides, quantique), les solutions des EDP sont cherchées comme limites de suites de fonctions approximantes. La complétude des espaces fonctionnels sous-jacents (espaces de Sobolev $H^s$, espaces $L^p$) est ce qui garantit mathématiquement que la solution existe rigoureusement.
