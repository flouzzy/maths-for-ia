\subsection*{Exercice 2 : La masse qui fuit à l'infini \quad $\bigstar\star\star\star\star$}

Soit $X_n$ une suite de variables aléatoires de loi de probabilité donnée par :
$\mathbb{P}(X_n = n) = \frac{1}{n^2}$ et $\mathbb{P}(X_n = 0) = 1 - \frac{1}{n^2}$.
1. Montrer que $X_n$ converge en probabilité vers 0.
2. Étudier la convergence dans $L^1$.
3. Étudier la convergence presque sûre.

**Correction :**
1. Soit $\varepsilon \in ]0, 1[$. Pour $n \ge 1$, $\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}(X_n = n) = \frac{1}{n^2}$.
   Comme $\lim_{n \to \infty} \frac{1}{n^2} = 0$, $X_n$ converge en probabilité vers 0.
2. Évaluons l'espérance de $|X_n|$ : $\mathbb{E}[|X_n|] = n \times \mathbb{P}(X_n = n) + 0 = n \times \frac{1}{n^2} = \frac{1}{n}$.
   Comme $\lim_{n \to \infty} \mathbb{E}[|X_n|] = \lim_{n \to \infty} \frac{1}{n} = 0$, la suite $X_n$ converge dans $L^1$ vers 0.
3. Pour la convergence presque sûre, posons $A_n = \{X_n = n\}$. Nous avons $\sum_{n=1}^\infty \mathbb{P}(A_n) = \sum_{n=1}^\infty \frac{1}{n^2} < \infty$.
   Par le lemme de Borel-Cantelli, la probabilité que les événements $A_n$ se réalisent une infinité de fois est nulle : $\mathbb{P}(\limsup A_n) = 0$.
   Donc, avec probabilité 1, $X_n = 0$ pour un rang assez grand, ce qui implique $X_n \to 0$. $X_n$ converge presque sûrement vers 0.
