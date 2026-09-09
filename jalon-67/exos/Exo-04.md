# Exercice 4 : Interversion limite et intégrale avec fonction indicatrice \quad $\bigstar\star\star\star$

## Énoncé
Calculer $\lim_{n \to \infty} \int_0^n (1-\frac{x}{n})^n e^{x/2} dx$.

## Correction Détaillée
\begin{itemize}
\item Soit $f_n(x) = \chi_{[0,n]}(x) (1-x/n)^n e^{x/2}$. 2. $f_n(x)$ converge vers $e^{-x} e^{x/2} = e^{-x/2}$. 3. La suite $f_n$ est croissante en $n$. 4. Par TCM, $\int f = \int e^{-x/2} = [-2e^{-x/2}]_0^\infty = 2$.
\end{itemize}
