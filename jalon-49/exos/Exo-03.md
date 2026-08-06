# Exercice 3 : Topologie cofinie \quad $\bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Sur un ensemble infini $X$, on définit $\mathcal{T}_{cof} = \{\emptyset\} \cup \{U \subset X \mid X \setminus U \text{ est fini}\}$. Montrer que c'est une topologie.

\textbf{Correction exhaustive :}
Vérifions les axiomes de la topologie :
1. $\emptyset \in \mathcal{T}_{cof}$ par définition. Le complémentaire de $X$ est $X \setminus X = \emptyset$. L'ensemble vide a pour cardinal $0$, qui est fini, donc $X \in \mathcal{T}_{cof}$.
2. Soit $(U_i)_{i \in I}$ une famille d'ouverts. Si tous les $U_i$ sont vides, leur réunion est vide, donc dans $\mathcal{T}_{cof}$. Supposons qu'il existe $i_0 \in I$ tel que $U_{i_0} \neq \emptyset$. Alors $X \setminus U_{i_0}$ est fini. Le complémentaire de la réunion est $X \setminus \left(\bigcup_{i \in I} U_i\right) = \bigcap_{i \in I} (X \setminus U_i)$. Cet ensemble est inclus dans $X \setminus U_{i_0}$, qui est fini. Donc $X \setminus \left(\bigcup_{i \in I} U_i\right)$ est fini, ce qui prouve que $\bigcup_{i \in I} U_i \in \mathcal{T}_{cof}$.
3. Soient $U, V \in \mathcal{T}_{cof}$. Si $U = \emptyset$ ou $V = \emptyset$, $U \cap V = \emptyset \in \mathcal{T}_{cof}$. Sinon, $X \setminus U$ et $X \setminus V$ sont finis. Le complémentaire de l'intersection est $X \setminus (U \cap V) = (X \setminus U) \cup (X \setminus V)$. L'union de deux ensembles finis est finie. Donc $U \cap V \in \mathcal{T}_{cof}$. Par récurrence, cela s'étend à toute intersection finie.
La famille $\mathcal{T}_{cof}$ est donc bien une topologie.
