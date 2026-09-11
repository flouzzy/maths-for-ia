# Exercice 2 : Application du Théorème de Convergence Monotone à une gaussienne tronquée \quad $\bigstar\bigstar\star\star$

## Énoncé
Soit $(f_n)$ une suite de fonctions mesurables positives définies sur $\mathbb{R}$ par $f_n(x) = \chi_{[-n, n]}(x) e^{-x^2}$. Calculer la limite de l'intégrale de Lebesgue de $f_n$.

## Correction Détaillée
\begin{itemize}
\item **Mesurabilité et positivité** : Pour tout $n \in \mathbb{N}$, $f_n$ est mesurable et positive.
\item **Croissance** : Pour tout $x$, $f_n(x) \le f_{n+1}(x)$.
\item **Limite** : $\lim f_n(x) = e^{-x^2}$.
\item **Application du TCM** : Par Beppo Levi, $\lim \int f_n = \int e^{-x^2} = \sqrt{\pi}$.
\end{itemize}
