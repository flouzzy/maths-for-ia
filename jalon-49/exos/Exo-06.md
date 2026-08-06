# Exercice 6 : Union de topologies \quad $\bigstar\bigstar\bigstar\star\star$

\textbf{Énoncé :}
Montrer par un contre-exemple que l'union de deux topologies n'est pas nécessairement une topologie.

\textbf{Correction exhaustive :}
Considérons l'ensemble $X = \{a, b, c\}$.
Définissons deux topologies sur $X$ :
$\mathcal{T}_1 = \{\emptyset, \{a\}, X\}$ (c'est bien une topologie car les unions et intersections de ces éléments y sont).
$\mathcal{T}_2 = \{\emptyset, \{b\}, X\}$.
Considérons l'union des deux familles : $\mathcal{T} = \mathcal{T}_1 \cup \mathcal{T}_2 = \{\emptyset, \{a\}, \{b\}, X\}$.
Si $\mathcal{T}$ était une topologie, elle devrait être stable par réunion.
Or, $\{a\} \in \mathcal{T}$ et $\{b\} \in \mathcal{T}$, mais $\{a\} \cup \{b\} = \{a, b\} \notin \mathcal{T}$.
L'axiome de réunion quelconque (ici finie) n'est pas vérifié. Donc l'union de deux topologies n'est pas nécessairement une topologie.
