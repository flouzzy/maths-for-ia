# Exercice 5 : Limite d'une suite croissante de mesurables

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

Soit $(A_n)$ une suite croissante d'ensembles mesurables ($A_n \subset A_{n+1}$). Soit $A = \bigcup_{n=1}^\infty A_n$. Démontrer que $\lambda(A) = \lim_{n \to \infty} \lambda(A_n)$.

**Correction Détaillée :**
On définit une suite d'ensembles disjoints : $B_1 = A_1$, et pour $n \ge 2$, $B_n = A_n \setminus A_{n-1}$.
Les $B_n$ sont mesurables et mutuellement disjoints. De plus, $A_N = \bigcup_{n=1}^N B_n$ et $A = \bigcup_{n=1}^\infty B_n$.
Par additivité dénombrable (démontrée via la théorie des tribus),
$$\lambda(A) = \sum_{n=1}^\infty \lambda(B_n) = \lim_{N \to \infty} \sum_{n=1}^N \lambda(B_n)$$
Or, $\sum_{n=1}^N \lambda(B_n) = \lambda\left(\bigcup_{n=1}^N B_n\right) = \lambda(A_N)$.
D'où $\lambda(A) = \lim_{N \to \infty} \lambda(A_N)$.
