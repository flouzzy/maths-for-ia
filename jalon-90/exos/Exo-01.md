\subsection*{Exercice 1 : Convergence d'une variable déterministe par morceaux \quad $\bigstar\star\star\star\star$}

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires définie par $\mathbb{P}(X_n = 1/n) = 1$.
1. Étudier la convergence de $X_n$ en probabilité.
2. Étudier la convergence de $X_n$ presque sûre.

**Correction :**
1. Soit $\varepsilon > 0$. Pour $n > 1/\varepsilon$, nous avons $1/n < \varepsilon$, ce qui implique $|X_n| < \varepsilon$ presque sûrement.
   Par conséquent, $\mathbb{P}(|X_n| > \varepsilon) = 0$ pour tout $n > 1/\varepsilon$.
   Ainsi, $\lim_{n \to \infty} \mathbb{P}(|X_n| > \varepsilon) = 0$. La suite $X_n$ converge en probabilité vers la constante $0$.
2. Par définition, l'événement $\{\omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = 0\}$ est de probabilité 1, car $X_n = 1/n$ est une suite numérique déterministe qui converge vers 0.
   Donc $X_n$ converge presque sûrement vers 0.
