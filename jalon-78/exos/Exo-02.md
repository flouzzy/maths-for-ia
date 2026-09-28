# Exercice 2 : Identité remarquable via Dirichlet \quad $\bigstar\star\star\star\star$

**Énoncé :**
En utilisant la série de Fourier du signal triangulaire (Exercice 1), déduire la valeur de la somme $\sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2}$.

**Correction Détaillée :**

1. \textbf{Régularité de $f$ :}
   La fonction $f$ (signal triangulaire) est continue et de classe $C^1$ par morceaux sur $\mathbb{R}$.
   D'après le théorème de Dirichlet, la série de Fourier de $f$ converge vers $f(t)$ pour tout $t \in \mathbb{R}$.

2. \textbf{Évaluation en un point astucieux :}
   Prenons $t = 0$. On a $f(0) = 0$.
   La série évaluée en $0$ donne :
   $$ S(f)(0) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{\cos(0)}{(2p+1)^2} = \frac{\pi}{2} - \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2} $$

3. \textbf{Conclusion :}
   Puisque $S(f)(0) = f(0) = 0$, on obtient :
   $$ \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2} = \frac{\pi}{2} $$
   Ce qui donne finalement la célèbre somme :
   $$ \sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2} = \frac{\pi^2}{8} $$
