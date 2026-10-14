# Exercice 04

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $U \sim \mathcal{U}([0,1])$. Définissons $Y_n = U^n$.
Étudiez la convergence en probabilité et presque sûre de la suite $Y_n$.

**Correction :**
**Convergence Presque Sûre :**
L'espace des réalisations est $\Omega = [0, 1]$. La variable aléatoire est $Y_n(\omega) = \omega^n$.
Pour tout $\omega \in [0, 1[$, on a $\lim_{n \to \infty} \omega^n = 0$.
Pour $\omega = 1$, $\lim_{n \to \infty} 1^n = 1$.
L'ensemble de convergence vers $0$ est $[0, 1[$. Puisque $U$ suit une loi uniforme, $\mathbb{P}(U = 1) = 0$.
Donc $\mathbb{P}\left(\lim_{n \to \infty} Y_n = 0\right) = 1$.
Ainsi, $Y_n \xrightarrow{p.s.} 0$.

**Convergence en probabilité :**
Puisque la convergence presque sûre implique la convergence en probabilité (Théorème du cours), nous pouvons conclure immédiatement que $Y_n \xrightarrow{\mathbb{P}} 0$.
(On peut aussi le vérifier à la main : $\mathbb{P}(U^n > \epsilon) = \mathbb{P}(U > \epsilon^{1/n}) = 1 - \epsilon^{1/n} \to 1 - 1 = 0$.)
