# Exercice 1 : Topologie discrète \quad $\bigstar\star\star\star\star$

\textbf{Énoncé :}
Soit $X$ un ensemble. Démontrer que la topologie discrète $\mathcal{T} = \mathcal{P}(X)$ vérifie bien les trois axiomes d'une topologie. Quels sont les fermés de cette topologie ?

\textbf{Correction exhaustive :}
1. Par définition, l'ensemble vide $\emptyset$ et $X$ sont des sous-ensembles de $X$, donc $\emptyset \in \mathcal{P}(X)$ et $X \in \mathcal{P}(X)$. L'axiome 1 est vérifié.
2. Soit $O_1, \dots, O_n$ une famille finie d'ouverts (donc de sous-ensembles de $X$). Leur intersection $\bigcap_{i=1}^n O_i$ est un sous-ensemble de $X$, donc elle appartient à $\mathcal{P}(X)$. L'axiome 2 est vérifié.
3. Soit $(O_i)_{i \in I}$ une famille quelconque d'ouverts (sous-ensembles de $X$). Leur réunion $\bigcup_{i \in I} O_i$ est composée d'éléments de $X$, donc c'est un sous-ensemble de $X$, et elle appartient à $\mathcal{P}(X)$. L'axiome 3 est vérifié.
Conclusion : $\mathcal{P}(X)$ est bien une topologie sur $X$.
Fermés : Un sous-ensemble $F \subset X$ est fermé si son complémentaire $X \setminus F$ est ouvert. Or, tout sous-ensemble de $X$ est ouvert. Donc pour tout $F \subset X$, $X \setminus F$ est ouvert, ce qui implique que $F$ est fermé. Ainsi, dans la topologie discrète, tout sous-ensemble est à la fois ouvert et fermé (clopen).
