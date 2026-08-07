# Exercice 2 : Topologie grossière \quad $\bigstar\star\star\star\star$

\textbf{Énoncé :}
Soit $X$ un ensemble non vide. Montrer que $\mathcal{T} = \{\emptyset, X\}$ est une topologie. Détailler les propriétés de ses voisinages.

\textbf{Correction exhaustive :}
1. L'axiome 1 exige que $\emptyset \in \mathcal{T}$ et $X \in \mathcal{T}$. C'est explicitement le cas par définition de $\mathcal{T}$.
2. Les intersections finies possibles d'éléments de $\mathcal{T}$ sont $\emptyset \cap \emptyset = \emptyset$, $X \cap X = X$, et $\emptyset \cap X = \emptyset$. Toutes ces intersections sont dans $\mathcal{T}$. L'axiome 2 est vérifié.
3. Les réunions quelconques possibles sont $\emptyset \cup \emptyset = \emptyset$, $X \cup X = X$, et $\emptyset \cup X = X$. Elles sont toutes dans $\mathcal{T}$. L'axiome 3 est vérifié.
Voisinages : Soit $x \in X$. Un voisinage de $x$ est un sous-ensemble $V \subset X$ contenant un ouvert contenant $x$. Le seul ouvert de $\mathcal{T}$ contenant $x$ est $X$ (car $\emptyset$ ne contient pas $x$). Ainsi, on doit avoir $x \in X \subset V$. Comme $V \subset X$, la seule possibilité est $V = X$.
Conclusion : Le seul voisinage possible pour n'importe quel point $x \in X$ est l'espace entier $X$ lui-même.
