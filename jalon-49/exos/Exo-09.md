# Exercice 9 : Voisinages dans la topologie cofinie \quad $\bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Dans la topologie cofinie sur un ensemble infini $X$, quels sont les voisinages d'un point $x \in X$ ? En déduire que l'espace n'est pas séparé (pas de Hausdorff).

\textbf{Correction exhaustive :}
1. Voisinages :
Soit $x \in X$. Un sous-ensemble $V \subset X$ est un voisinage de $x$ s'il contient un ouvert $U$ contenant $x$.
Dans la topologie cofinie, un ouvert non vide $U$ est tel que son complémentaire $X \setminus U$ est fini.
Si $U \subset V$, alors $X \setminus V \subset X \setminus U$. Comme $X \setminus U$ est fini, tout sous-ensemble d'un ensemble fini est fini. Donc $X \setminus V$ doit être fini.
Réciproquement, si $V$ est tel que $x \in V$ et $X \setminus V$ est fini, alors $V$ est un ouvert (donc $U=V$) contenant $x$.
Les voisinages de $x$ sont donc exactement les parties de $X$ contenant $x$ et dont le complémentaire est fini.

2. Espace non séparé :
Un espace est séparé (Hausdorff) si pour tous points distincts $x \neq y$, il existe des voisinages $V_x$ et $V_y$ tels que $V_x \cap V_y = \emptyset$.
Prenons $x \neq y$ dans $X$. Soit $V_x$ un voisinage de $x$ et $V_y$ un voisinage de $y$.
Leurs complémentaires $C_x = X \setminus V_x$ et $C_y = X \setminus V_y$ sont finis.
Le complémentaire de leur intersection est $X \setminus (V_x \cap V_y) = C_x \cup C_y$.
L'union de deux ensembles finis est finie. Ainsi $V_x \cap V_y$ a un complémentaire fini.
Or, par hypothèse, $X$ est infini. Un sous-ensemble dont le complémentaire est fini dans un ensemble infini ne peut pas être vide (sinon le complémentaire de l'ensemble vide, qui est $X$, serait fini, ce qui est absurde).
Donc $V_x \cap V_y \neq \emptyset$. On ne peut jamais séparer deux points.
