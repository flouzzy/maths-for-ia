# Exercice 8 : Intérieur et adhérence \quad $\bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Soit $A$ une partie de $X$. L'intérieur $\mathring{A}$ est la réunion de tous les ouverts inclus dans $A$. L'adhérence $\bar{A}$ est l'intersection de tous les fermés contenant $A$. Montrer que $X \setminus \mathring{A} = \overline{X \setminus A}$.

\textbf{Correction exhaustive :}
L'intérieur de $A$ est défini par :
$\mathring{A} = \bigcup \{O \in \mathcal{T} \mid O \subset A\}$.
Passons au complémentaire dans $X$ et utilisons les lois de De Morgan généralisées :
$X \setminus \mathring{A} = X \setminus \left( \bigcup_{O \in \mathcal{T}, O \subset A} O \right) = \bigcap_{O \in \mathcal{T}, O \subset A} (X \setminus O)$.
Posons $F = X \setminus O$. Comme $O$ est ouvert, $F$ est un fermé.
La condition $O \subset A$ est équivalente, par passage au complémentaire, à $X \setminus A \subset X \setminus O$, c'est-à-dire $X \setminus A \subset F$.
Ainsi, la famille des complémentaires des ouverts inclus dans $A$ correspond exactement à la famille des fermés contenant le complémentaire de $A$.
L'intersection de ces fermés est, par définition, l'adhérence de $X \setminus A$.
On obtient donc : $X \setminus \mathring{A} = \bigcap_{F \text{ ferm\'{e}}, X \setminus A \subset F} F = \overline{X \setminus A}$.
