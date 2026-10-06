---
uuid: "jalon-85"
title: "Axiomes de Kolmogorov"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 84 (Livrable IA).md]]"
next: "[[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]]"
---

# Jalon 85 : Axiomes de Kolmogorov

## 1. Introduction historique et genèse géométrique

Avant 1933, la théorie des probabilités était vue par beaucoup de mathématiciens comme une collection de recettes empiriques sans fondement rigoureux. Andreï Kolmogorov a radicalement changé ce paradigme en réalisant qu'une probabilité n'est fondamentalement rien d'autre qu'une mesure (comme une longueur, une aire, ou une masse) définie sur un espace abstrait, normalisée à 1.

Géométriquement, imaginez un univers $\Omega$ (le gâteau) représentant l'ensemble de tous les événements possibles. La probabilité d'un événement $A$ est la fraction du "poids" total de l'univers concentrée sur cet événement, le poids total de $\Omega$ valant exactement 1. Cette approche constructive a permis d'appliquer les outils puissants de la théorie de la mesure de Lebesgue et de Borel aux probabilités.

## 2. Définitions, Théorèmes & Exemples

### A. L'Espace de Probabilité

Soit $\Omega$ un ensemble appelé univers (l'ensemble des résultats possibles).

> **Définition 1 (Espace de Probabilité) :**
> Un espace de probabilité est un triplet $(\Omega, \mathcal{F}, \mathbb{P})$ où :
> 1. $\mathcal{F}$ est une tribu sur $\Omega$ (le catalogue de tous les événements mesurables).
> 2. $\mathbb{P}$ est une mesure de probabilité sur $(\Omega, \mathcal{F})$ vérifiant la condition stricte de normalisation : $\mathbb{P}(\Omega) = 1$.

> **Définition 2 (Les Axiomes de Kolmogorov) :**
> Une application $\mathbb{P} : \mathcal{F} \to [0, 1]$ est une probabilité si et seulement si elle vérifie :
> 1. Positivité : $\forall A \in \mathcal{F}, \mathbb{P}(A) \ge 0$.
> 2. Masse totale : $\mathbb{P}(\Omega) = 1$.
> 3. $\sigma$-additivité : Pour toute suite d'événements $(A_n)_{n \in \mathbb{N}^*}$ deux à deux disjoints (i.e. $i \neq j \implies A_i \cap A_j = \emptyset$) :
>    $$ \mathbb{P}\left( \bigcup_{n=1}^\infty A_n \right) = \sum_{n=1}^\infty \mathbb{P}(A_n) $$

**Exemple 1 : Lancer d'un dé parfait**
Considérons le jet d'un dé à 6 faces. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}$.
La tribu est $\mathcal{F} = \mathcal{P}(\Omega)$, l'ensemble de toutes les parties.
La mesure de probabilité pour chaque face singleton est $\mathbb{P}(\{k\}) = \frac{1}{6}$.
L'événement $A = \text{"Obtenir un résultat pair"} = \{2, 4, 6\}$.
Comme les éléments sont disjoints, par $\sigma$-additivité finie :
$$ \mathbb{P}(A) = \mathbb{P}(\{2\}) + \mathbb{P}(\{4\}) + \mathbb{P}(\{6\}) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = \frac{3}{6} = \frac{1}{2} $$
Cet exemple simple illustre la conservation de la masse totale.

### B. Propriétés géométriques fondamentales

> **Théorème (Conséquences directes des axiomes) :**
> Soient $A, B \in \mathcal{F}$. Les propriétés suivantes sont vérifiées :
> 1. $\mathbb{P}(\emptyset) = 0$.
> 2. $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$.
> 3. Monotonie : Si $A \subset B$, alors $\mathbb{P}(A) \le \mathbb{P}(B)$ et $\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A)$.
> 4. Formule du crible pour deux événements : $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$.
> 5. Continuité monotone : Si $(A_n)$ est une suite croissante d'événements ($A_1 \subset A_2 \subset \dots$), alors $\mathbb{P}(\bigcup A_n) = \lim_{n \to \infty} \mathbb{P}(A_n)$.

**Exemple 2 : L'implication et événements inclus**
Si on lance un dé, soit $A = \text{"Obtenir 2"}$ et $B = \text{"Obtenir un nombre pair"}$.
Clairement, $A \subset B$, car si $A$ est réalisé, $B$ l'est automatiquement. L'implication logique "Si j'ai fait 2, alors j'ai fait un nombre pair" se traduit ensemblistement par une inclusion.
Ainsi, par monotonie, $\mathbb{P}(A) = \frac{1}{6} \le \mathbb{P}(B) = \frac{3}{6}$. L'aire de $A$ est entièrement contenue dans l'aire de $B$.

**Exemple 3 : Événement complémentaire**
Pour une loi exponentielle $\mathcal{E}(\lambda)$ sur $\Omega = \mathbb{R}_+$, on a $\mathbb{P}([0, t]) = 1 - e^{-\lambda t}$.
L'événement "La durée de vie dépasse $t$" est le complémentaire $([0, t])^c = ]t, \infty[$.
Par le théorème : $\mathbb{P}(]t, \infty[) = 1 - \mathbb{P}([0, t]) = 1 - (1 - e^{-\lambda t}) = e^{-\lambda t}$.

**Exemple 4 : La formule du crible (Union)**
Prenons un jeu de 32 cartes, on tire une carte au hasard.
Soit $A = \text{"Tirer un As"}$ (4 cartes) et $B = \text{"Tirer un Cœur"}$ (8 cartes).
L'intersection $A \cap B = \text{"Tirer l'As de Cœur"}$ (1 carte).
$\mathbb{P}(A \cup B) = \frac{4}{32} + \frac{8}{32} - \frac{1}{32} = \frac{11}{32}$.
La soustraction de $\mathbb{P}(A \cap B)$ empêche de compter deux fois l'As de Cœur.

**Exemple 5 : Borne de l'union (Boole)**
Souvent, on ne connait pas l'intersection exacte. Dans ce cas on utilise :
$\mathbb{P}(A \cup B) \le \mathbb{P}(A) + \mathbb{P}(B)$. Si $A$ et $B$ ont de très faibles chances d'arriver (ex: $0.01$ chacun), la probabilité qu'au moins l'un arrive est majorée par $0.02$.

\begin{center}
\begin{tikzpicture}
    \draw (0,0) circle (1.5cm) node[above left=0.7cm] {$A$};
    \draw (2,0) circle (1.5cm) node[above right=0.7cm] {$B$};
    \node at (1,0) {$A \cap B$};
    \draw[dashed, thick] (-2,-2) rectangle (4,2);
    \node at (3.5, 1.5) {$\Omega$};
\end{tikzpicture}
\end{center}

## 3. Démonstrations

### Démonstration de la Formule de l'Union

Nous allons démontrer la propriété fondamentale $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$ pas à pas en utilisant l'additivité finie.

1. **Décomposition en sous-ensembles disjoints :**
   Nous ne pouvons pas directement utiliser l'axiome d'additivité sur $A$ et $B$ car ils ne sont pas nécessairement disjoints. Il faut découper $A \cup B$ en régions sans chevauchement.
   On remarque que $B$ peut s'écrire comme l'union de deux ensembles disjoints : la partie de $B$ qui est dans $A$, et la partie de $B$ qui n'est pas dans $A$.
   $$B = (A \cap B) \cup (B \setminus A)$$
   Ces deux ensembles sont disjoints, donc par additivité (cas $n=2$ des axiomes de Kolmogorov) :
   $$\mathbb{P}(B) = \mathbb{P}(A \cap B) + \mathbb{P}(B \setminus A)$$
   D'où nous isolons :
   $$\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B)$$

2. **Écriture de l'union :**
   De la même manière, on peut exprimer $A \cup B$ comme une union disjointe. Tout élément de l'union appartient soit à $A$, soit à la partie de $B$ qui n'est pas dans $A$ :
   $$A \cup B = A \cup (B \setminus A)$$
   Puisque $A$ et $(B \setminus A)$ sont disjoints, on peut à nouveau appliquer l'additivité :
   $$\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B \setminus A)$$

3. **Substitution et conclusion :**
   Il suffit de substituer l'expression de $\mathbb{P}(B \setminus A)$ obtenue à l'étape 1 dans la formule de l'étape 2 :
   $$\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$$
   Ce qui clôt la preuve. La surface d'intersection, comptée dans $\mathbb{P}(A)$ et de nouveau dans $\mathbb{P}(B)$, est ainsi soustraite une fois pour obtenir la mesure géométrique exacte de l'union.

### Démonstration : Probabilité de l'ensemble vide

Prouvons que $\mathbb{P}(\emptyset) = 0$.
Soit une suite d'événements $A_n$ définie par $A_n = \emptyset$ pour tout $n \in \mathbb{N}^*$.
Ces événements sont deux à deux disjoints (puisque $\emptyset \cap \emptyset = \emptyset$).
La réunion de ces événements est : $\bigcup_{n=1}^\infty \emptyset = \emptyset$.
D'après l'axiome de $\sigma$-additivité :
$$ \mathbb{P}(\emptyset) = \mathbb{P}\left(\bigcup_{n=1}^\infty \emptyset \right) = \sum_{n=1}^\infty \mathbb{P}(\emptyset) $$
La seule possibilité pour qu'une série de termes réels positifs constants converge et soit égale au terme constant initial est que ce terme vaille $0$.
Ainsi, $\mathbb{P}(\emptyset) = 0$.

## 4. Applications en Physique, Logique & IA

### En Mathématiques et IA

L'Intelligence Artificielle moderne, particulièrement le domaine de l'apprentissage profond (Deep Learning) et des modèles de langage, repose fondamentalement sur la théorie probabiliste.

Lorsqu'un réseau de neurones avec une couche de sortie Softmax traite une image ou un mot, il ne produit pas directement un résultat scalaire arbitraire, mais il génère un vecteur $(p_1, p_2, \dots, p_k)$ qui vérifie scrupuleusement $p_i \ge 0$ et $\sum p_i = 1$. Cette sortie est donc formellement une mesure de probabilité définie sur un espace discret de classes.

Les axiomes de Kolmogorov assurent que l'espace des modèles probabilistes est structuré correctement. En apprentissage automatique, le fait que la probabilité d'un événement rare puisse être formellement majorée par la somme de ses constituants permet d'établir des bornes mathématiques dures sur le risque d'erreur en généralisation (théorie PAC - Probably Approximately Correct).

### Théorème de Continuité en Apprentissage (Continuité Monotone)

En IA, de nombreuses preuves de convergence s'appuient sur l'axiome de $\sigma$-additivité. Considérons par exemple la probabilité qu'un algorithme dépasse un certain seuil d'erreur. Si on note $E_n$ l'événement où l'algorithme fait une erreur avec $n$ données d'entraînement, et que $E_{n+1} \subset E_n$ (l'ajout de données rend l'erreur stricte moins probable), alors l'intersection $\bigcap E_n$ correspond à l'événement de faire toujours des erreurs même avec une infinité de données. La théorie de la mesure de Kolmogorov nous garantit la continuité descendante :
$$ \mathbb{P}\left(\bigcap_{n=1}^\infty E_n\right) = \lim_{n \to \infty} \mathbb{P}(E_n) $$
Si le membre de gauche est nul (le modèle apprend asymptotiquement), alors les erreurs tendent vers zéro, confirmant ainsi la convergence théorique de l'apprentissage.

### Continuité croissante et descendante des probabilités

> **Théorème (Continuité des probabilités) :**
> 1. Si $(A_n)$ est une suite croissante d'événements ($A_1 \subset A_2 \subset \dots$), alors :
>    $$ \mathbb{P}\left(\bigcup_{n=1}^\infty A_n\right) = \lim_{n \to \infty} \mathbb{P}(A_n) $$
> 2. Si $(A_n)$ est une suite décroissante d'événements ($A_1 \supset A_2 \supset \dots$), alors :
>    $$ \mathbb{P}\left(\bigcap_{n=1}^\infty A_n\right) = \lim_{n \to \infty} \mathbb{P}(A_n) $$

**Exemple 6 : Continuité descendante géométrique**
Considérons une cible de fléchettes de rayon $R=1$ (aire totale $\pi$, normalisons pour que $\mathbb{P}(\Omega) = 1$). On s'intéresse à la probabilité de toucher le centre exact.
Soit $A_n$ l'événement "La fléchette tombe à une distance inférieure ou égale à $1/n$ du centre".
Géométriquement, $A_n$ est un disque de rayon $1/n$.
Nous avons $A_1 \supset A_2 \supset A_3 \dots$
L'aire (probabilité) de $A_n$ est $\mathbb{P}(A_n) = \frac{\pi (1/n)^2}{\pi} = \frac{1}{n^2}$.
L'événement "Toucher exactement le centre" est l'intersection infinie $\bigcap_{n=1}^\infty A_n$.
Par le théorème de continuité descendante :
$$ \mathbb{P}\left( \text{Centre} \right) = \mathbb{P}\left( \bigcap_{n=1}^\infty A_n \right) = \lim_{n \to \infty} \frac{1}{n^2} = 0 $$
Ainsi, la probabilité d'atteindre un point mathématique précis (une cible d'aire nulle) est de $0$, bien que l'événement ne soit pas strictement impossible au sens physique.

\begin{center}
\begin{tikzpicture}
    \draw (0,0) circle (2cm);
    \draw (0,0) circle (1.2cm);
    \draw (0,0) circle (0.6cm);
    \draw (0,0) circle (0.2cm);
    \fill[black] (0,0) circle (2pt) node[below=0.2cm] {Centre};
    \node at (1.5, 1.5) {$A_1$};
    \node at (0.8, 0.8) {$A_2$};
    \node at (0.3, 0.4) {$A_3$};
    \draw[->, thick] (2.5, 0) -- (3.5, 0) node[midway, above] {$n \to \infty$};
    \fill[black] (4.5,0) circle (2pt) node[below=0.2cm] {$\bigcap A_n$};
\end{tikzpicture}
\end{center}
