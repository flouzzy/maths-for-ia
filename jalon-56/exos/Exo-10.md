## Exercice 10 : Complétude et suites de Cauchy (Avancé) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Théorème de Baire (cas particulier). Montrer qu'un espace métrique complet sans point isolé est non dénombrable.

\textbf{Correction Détaillée :}
1. Raisonnons par l'absurde. Supposons $(X, d)$ complet, sans point isolé (chaque point est limite d'une suite), et dénombrable : $X = \{x_1, x_2, \ldots\}$.
2. Posons $O_n = X \setminus \{x_n\}$. Chaque $O_n$ est ouvert car $\{x_n\}$ est fermé (dans un espace métrique, les singletons sont fermés).
3. Chaque $O_n$ est dense dans $X$. En effet, si $O_n$ n'était pas dense, l'intérieur de son complémentaire $\{x_n\}$ serait non vide, donc $\{x_n\}$ serait un ouvert. $x_n$ serait alors un point isolé, contredisant l'hypothèse.
4. Par le théorème de Baire, une intersection dénombrable d'ouverts denses dans un espace complet est dense.
5. Donc $\cap_{n=1}^\infty O_n$ est dense dans $X$.
6. Or, $\cap_{n=1}^\infty O_n = X \setminus \cup_{n=1}^\infty \{x_n\} = X \setminus X = \emptyset$.
7. C'est une contradiction car l'ensemble vide ne peut pas être dense dans $X$ (si $X \neq \emptyset$).
8. L'espace $X$ doit donc être non dénombrable.
