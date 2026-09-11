# Exercice 1 : Intégrale d'une suite de fonctions puissances \quad $\bigstar\star\star\star$

## Énoncé
Soit $f_n(x) = x^n$ sur $[0, 1[$. Montrer que $\lim_{n \to \infty} \int_0^1 f_n(x) dx = 0$ en utilisant le TCM.

## Correction Détaillée
\begin{itemize}
\item **Mesurabilité et positivité** : $f_n$ est mesurable et positive.
\item Cependant, la suite $(f_n)$ est décroissante. Mais on peut utiliser le TCM sur $1 - f_n(x)$ qui est croissante positive.
\item $\lim (1 - f_n(x)) = 1$ p.p. Donc $\int 1 dx = \lim \int (1-x^n)dx \implies 1 = 1 - \lim \int x^n dx \implies \lim \int x^n dx = 0$.
\end{itemize}
