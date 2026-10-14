\subsection*{Exercice 3 : Convergence en probabilité n'implique pas presque sûre \quad $\bigstar\bigstar\star\star\star$}

On se place sur l'espace $\Omega = [0,1[$, muni de la tribu borélienne et de la mesure de Lebesgue $\lambda$.
On définit les variables $X_{n,k} = \mathbf{1}_{[\frac{k}{n}, \frac{k+1}{n}[}$ pour $n \ge 1$ et $0 \le k < n$.
Soit $Y_m$ la suite obtenue en énumérant les $X_{n,k}$ dans l'ordre lexicographique.
1. Montrer que $Y_m \xrightarrow{\mathbb{P}} 0$.
2. Montrer que $Y_m$ ne converge presque sûrement pour aucun $\omega \in \Omega$.

**Correction :**
1. Soit $\varepsilon \in ]0, 1[$. L'événement $\{Y_m > \varepsilon\}$ est exactement le support de l'indicatrice $X_{n,k}$ correspondante.
   La probabilité (qui est la mesure de Lebesgue) est $\frac{1}{n}$.
   Lorsque $m \to \infty$, l'indice $n$ associé tend aussi vers $\infty$.
   Donc $\mathbb{P}(Y_m > \varepsilon) = \frac{1}{n} \to 0$. Ainsi, $Y_m \xrightarrow{\mathbb{P}} 0$.
2. Pour tout $\omega \in [0, 1[$, fixons-le.
   Pour chaque niveau $n$, il existe un unique $k \in \{0, \dots, n-1\}$ tel que $\omega \in [\frac{k}{n}, \frac{k+1}{n}[$.
   Pour ce $k$, on a $X_{n,k}(\omega) = 1$. Pour les autres, $X_{n,j}(\omega) = 0$.
   Donc, dans la suite numérique $(Y_m(\omega))_{m \ge 1}$, la valeur $1$ apparaît une infinité de fois, et la valeur $0$ apparaît une infinité de fois.
   La suite ne converge pas pour $\omega$. Puisque ceci est vrai pour tout $\omega \in \Omega$, il n'y a pas convergence presque sûre vers 0 (ni vers aucune limite).
