---
uuid: "jalon-62"
title: "Algèbres et Tribus (sigma-algèbres)"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/probabilites
prev: "[[Jalon 61 (Insuffisances de l'intégrale de Riemann).md]]"
next: "[[Jalon 63 (Définition axiomatique d'une mesure).md]]"
---

# Genèse et motivation conceptuelle

La théorie de la mesure vise à assigner un "volume" (ou longueur, aire, masse, probabilité) aux sous-ensembles d'un espace donné. Intuitivement, on souhaiterait pouvoir mesurer n'importe quel sous-ensemble de $\mathbb{R}$. Cependant, l'axiome du choix et la géométrie de l'espace tridimensionnel conduisent à des paradoxes majeurs, tel que le paradoxe de Banach-Tarski, démontrant qu'il est impossible de définir une mesure consistante et invariante par translation sur toutes les parties de $\mathbb{R}^n$.

Pour pallier ce problème fondamental, l'approche axiomatique moderne restreint la collection des sous-ensembles que l'on s'autorise à mesurer. On ne mesure pas tout, mais seulement une famille d'ensembles dits "mesurables". Cette famille doit posséder une structure algébrique robuste vis-à-vis des opérations ensemblistes fondamentales : le passage au complémentaire et l'union dénombrable, permettant ainsi de définir des processus limites continus. C'est l'essence même du concept de tribu, ou $\sigma$-algèbre, introduit formellement par Émile Borel et Henri Lebesgue.

# Algèbres et Tribus

Soit $X$ un ensemble non vide.

## Définitions et Théorèmes

\textbf{Définition (Algèbre) :}
Une famille $\mathcal{A}$ de parties de $X$ est une \textbf{algèbre} sur $X$ si elle vérifie les trois propriétés suivantes :
1. $X \in \mathcal{A}$.
2. Stabilité par passage au complémentaire : Si $A \in \mathcal{A}$, alors $X \setminus A \in \mathcal{A}$.
3. Stabilité par union finie : Si $A, B \in \mathcal{A}$, alors $A \cup B \in \mathcal{A}$.

\textbf{Définition (Tribu ou $\sigma$-algèbre) :}
Une famille $\mathcal{F}$ de parties de $X$ est une \textbf{tribu} (ou $\sigma$-algèbre) sur $X$ si elle vérifie :
1. $X \in \mathcal{F}$.
2. Stabilité par passage au complémentaire : Si $A \in \mathcal{F}$, alors $X \setminus A \in \mathcal{F}$.
3. Stabilité par union dénombrable : Si $(A_n)_{n \in \mathbb{N}}$ est une suite d'éléments de $\mathcal{F}$, alors $\bigcup_{n \in \mathbb{N}} A_n \in \mathcal{F}$.

Le couple $(X, \mathcal{F})$ est alors appelé un \textbf{espace mesurable}.

\textbf{Exemples concrets (Tribus) :}
1. La tribu triviale $\mathcal{F} = \{\emptyset, X\}$ est la plus petite tribu sur $X$.
2. La tribu discrète $\mathcal{F} = \mathcal{P}(X)$ (l'ensemble des parties de $X$) est la plus grande tribu sur $X$.
3. Soit $A \subset X$. La famille $\mathcal{F} = \{\emptyset, A, X \setminus A, X\}$ est une tribu.
4. Sur $X = \{1, 2, 3\}$, la famille $\{\emptyset, \{1\}, \{2, 3\}, X\}$ est une tribu.
5. Soit $X$ un ensemble infini. La famille des parties $A \subset X$ telles que $A$ est finie ou $X \setminus A$ est finie forme une algèbre, mais en général pas une tribu.
6. La famille des parties $A \subset X$ telles que $A$ est dénombrable ou $X \setminus A$ est dénombrable forme une tribu.

\textbf{Exemples concrets (Algèbre non Tribu) :}
7. Sur $X = \mathbb{R}$, l'ensemble des réunions finies d'intervalles de la forme $]a, b]$, $]-\infty, a]$, ou $]a, +\infty[$ est une algèbre, mais non une tribu (l'union dénombrable de $]0, 1-1/n]$ donne $]0, 1[$ qui n'est pas de cette forme de base si l'on se restreint à des intervalles semi-ouverts de manière stricte, bien que l'algèbre soit définie différemment usuellement, disons l'algèbre engendrée par les intervalles semi-ouverts). Un meilleur exemple : l'algèbre des parties finies ou cofinies de $\mathbb{N}$. L'union des singletons $\{2n\}$ est l'ensemble des pairs, qui n'est ni fini ni cofini.

\begin{tikzpicture}
\node[draw, circle, minimum size=3cm] (X) at (0,0) {};
\node at (0, 1) {$X$};
\draw[fill=blue!20] (-0.5,-0.5) circle (0.8);
\node at (-0.5,-0.5) {$A$};
\draw[fill=red!20] (0.8,-0.2) circle (0.6);
\node at (0.8,-0.2) {$B$};
\node at (0, -2) {Dans une tribu, $A \cup B, A \cap B, X \setminus A$ sont inclus.};
\end{tikzpicture}

## Démonstrations et Propriétés

\textbf{Propriété :} Une tribu est stable par intersection dénombrable.
\textit{Preuve détaillée :} Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{F}$. Nous voulons montrer que $\bigcap_{n \in \mathbb{N}} A_n \in \mathcal{F}$.
D'après les lois de De Morgan, le complémentaire d'une intersection est l'union des complémentaires :
$$ X \setminus \left( \bigcap_{n \in \mathbb{N}} A_n \right) = \bigcup_{n \in \mathbb{N}} (X \setminus A_n) $$
Puisque $\mathcal{F}$ est une tribu :
- Pour tout $n$, $A_n \in \mathcal{F}$, donc par stabilité par passage au complémentaire, $X \setminus A_n \in \mathcal{F}$.
- Par stabilité par union dénombrable, $\bigcup_{n \in \mathbb{N}} (X \setminus A_n) \in \mathcal{F}$.
- Enfin, par stabilité par passage au complémentaire appliquée à cette union, le complémentaire du complémentaire, c'est-à-dire $\bigcap_{n \in \mathbb{N}} A_n$, appartient à $\mathcal{F}$.

\textbf{Propriété :} Toute tribu est une algèbre.
\textit{Preuve détaillée :} La stabilité par union finie s'obtient en complétant une suite finie $A_1, \dots, A_k$ par l'ensemble vide : pour $n > k$, posons $A_n = \emptyset$. Puisque $\emptyset = X \setminus X \in \mathcal{F}$, la suite $(A_n)$ est dans $\mathcal{F}$, et $\bigcup_{n \in \mathbb{N}} A_n = \bigcup_{i=1}^k A_i \in \mathcal{F}$.

# Tribu engendrée et Tribu de Borel

## Définitions et Théorèmes

Il est souvent difficile de décrire explicitement tous les éléments d'une tribu. On la définit plutôt à partir d'une famille d'ensembles générateurs.

\textbf{Définition (Tribu engendrée) :}
Soit $\mathcal{C}$ une classe (famille) de parties de $X$. La \textbf{tribu engendrée} par $\mathcal{C}$, notée $\sigma(\mathcal{C})$, est la plus petite tribu contenant $\mathcal{C}$. Formellement, c'est l'intersection de toutes les tribus contenant $\mathcal{C}$ :
$$ \sigma(\mathcal{C}) = \bigcap \{ \mathcal{F} \text{ tribu sur } X \mid \mathcal{C} \subset \mathcal{F} \} $$

\textbf{Définition (Tribu borélienne) :}
Soit $(X, \mathcal{T})$ un espace topologique ($\mathcal{T}$ étant la famille des ouverts). La \textbf{tribu borélienne}, ou tribu de Borel, notée $\mathcal{B}(X)$, est la tribu engendrée par les ouverts de $X$ : $\mathcal{B}(X) = \sigma(\mathcal{T})$.
Les éléments de $\mathcal{B}(X)$ sont appelés les \textbf{boréliens}.

\textbf{Exemples concrets (Tribus engendrées) :}
1. Si $\mathcal{C} = \{A\}$ avec $A \subsetneq X, A \neq \emptyset$, alors $\sigma(\mathcal{C}) = \{\emptyset, A, X \setminus A, X\}$.
2. Sur $\mathbb{R}$, $\mathcal{B}(\mathbb{R})$ est générée par les ouverts $]a, b[$.
3. L'ensemble $\{a\}$ est un borélien car $\{a\} = \bigcap_{n \in \mathbb{N}^*} ]a - \frac{1}{n}, a + \frac{1}{n}[$.
4. Tout fermé est un borélien car complémentaire d'un ouvert.
5. Sur un ensemble fini $X$, si on partitionne $X$ en $\{A_i\}$, la tribu engendrée par cette partition contient exactement les unions de ces éléments $A_i$.

## Démonstrations

\textbf{Théorème :} La tribu engendrée $\sigma(\mathcal{C})$ existe et est bien une tribu.
\textit{Preuve détaillée :}
1. L'ensemble des tribus contenant $\mathcal{C}$ n'est pas vide, car la tribu des parties $\mathcal{P}(X)$ contient $\mathcal{C}$ et est une tribu.
2. Montrons que l'intersection d'une famille quelconque de tribus $(\mathcal{F}_i)_{i \in I}$ est une tribu.
   - $\forall i \in I, X \in \mathcal{F}_i$, donc $X \in \bigcap_{i \in I} \mathcal{F}_i$.
   - Si $A \in \bigcap_{i \in I} \mathcal{F}_i$, alors $\forall i \in I, A \in \mathcal{F}_i$. Comme chaque $\mathcal{F}_i$ est une tribu, $\forall i \in I, X \setminus A \in \mathcal{F}_i$, d'où $X \setminus A \in \bigcap_{i \in I} \mathcal{F}_i$.
   - Si $(A_n)$ est une suite dans l'intersection, elle est dans chaque $\mathcal{F}_i$, donc l'union est dans chaque $\mathcal{F}_i$, donc l'union est dans l'intersection.
3. Ainsi $\sigma(\mathcal{C})$ est bien une tribu contenant $\mathcal{C}$, et c'est manifestement la plus petite pour l'inclusion.

\textbf{Théorème :} Sur $\mathbb{R}$, la tribu borélienne $\mathcal{B}(\mathbb{R})$ est engendrée par la classe des intervalles semi-ouverts $\mathcal{C} = \{ ]-\infty, x] \mid x \in \mathbb{R} \}$.
\textit{Preuve détaillée :}
Notons $\mathcal{T}$ l'ensemble des ouverts de $\mathbb{R}$.
- Montrons $\sigma(\mathcal{C}) \subset \mathcal{B}(\mathbb{R})$ : chaque intervalle $]-\infty, x]$ est un fermé, donc son complémentaire $]x, +\infty[$ est un ouvert. Ainsi, $]-\infty, x]$ appartient à $\mathcal{B}(\mathbb{R})$. Puisque $\sigma(\mathcal{C})$ est la plus petite tribu contenant $\mathcal{C}$, $\sigma(\mathcal{C}) \subset \mathcal{B}(\mathbb{R})$.
- Montrons $\mathcal{B}(\mathbb{R}) \subset \sigma(\mathcal{C})$ :
  Pour tout $a < b$, on peut écrire l'intervalle semi-ouvert $]a, b] = ]-\infty, b] \setminus ]-\infty, a] = ]-\infty, b] \cap (]-\infty, a])^c$. Donc $]a, b] \in \sigma(\mathcal{C})$.
  L'intervalle ouvert $]a, b[$ s'écrit $]a, b[ = \bigcup_{n \geq 1} ]a, b - \frac{1}{n}]$. L'union étant dénombrable, $]a, b[ \in \sigma(\mathcal{C})$.
  Puisque tout ouvert de $\mathbb{R}$ s'écrit comme une union dénombrable d'intervalles ouverts, tout ouvert est dans $\sigma(\mathcal{C})$. La tribu de Borel étant engendrée par les ouverts, $\mathcal{B}(\mathbb{R}) \subset \sigma(\mathcal{C})$.
L'égalité est donc démontrée.

# Applications en Théorie des Probabilités et IA

Dans la formalisation axiomatique de Kolmogorov (1933), un espace de probabilité est un triplet $(\Omega, \mathcal{F}, \mathbb{P})$.
- $\Omega$ est l'univers (les réalisations possibles).
- $\mathcal{F}$ est la tribu des événements (les ensembles auxquels on sait affecter une probabilité).
- $\mathbb{P} : \mathcal{F} \to [0, 1]$ est la mesure de probabilité.

En IA et en apprentissage automatique, les variables aléatoires (comme les poids d'un réseau ou les variables latentes dans un VAE) sont des fonctions mesurables.
Définition : Une fonction $X : \Omega \to E$ entre deux espaces mesurables $(\Omega, \mathcal{F})$ et $(E, \mathcal{E})$ est dite \textbf{mesurable} si pour tout $B \in \mathcal{E}$, on a $X^{-1}(B) \in \mathcal{F}$.
Cela garantit que l'on peut toujours demander la probabilité de l'événement $\{ X \in B \}$ !
Les probabilités modernes sur des espaces complexes (espaces de fonctions, graphes) requièrent l'utilisation méticuleuse des tribus cylindriques et de la tribu borélienne pour assurer une assise rigoureuse.
