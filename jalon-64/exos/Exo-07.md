# Exercice 7 : Limite d'une suite décroissante d'ensembles

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Soit $(A_n)$ une suite décroissante d'ensembles mesurables ($A_{n+1} \subset A_n$) avec $\lambda(A_1) < \infty$. Démontrer que $\lambda(\bigcap A_n) = \lim_{n \to \infty} \lambda(A_n)$.

## Correction Détaillée

1. Soit $A = \bigcap A_n$. Posons $E_n = A_1 \setminus A_n$.
2. La suite $(E_n)$ est une suite croissante d'ensembles mesurables ($E_1 \subset E_2 \subset \dots$).
L'union des $E_n$ est $\bigcup E_n = A_1 \setminus (\bigcap A_n) = A_1 \setminus A$.
3. Pour une suite croissante, la mesure de la limite est la limite des mesures :
$\lambda(\bigcup E_n) = \lim_{n \to \infty} \lambda(E_n)$.
4. Puisque tous les ensembles sont inclus dans $A_1$ de mesure finie, on peut soustraire :
$\lambda(A_1 \setminus A) = \lambda(A_1) - \lambda(A)$
$\lambda(E_n) = \lambda(A_1) - \lambda(A_n)$
5. L'équation de l'étape 3 devient :
$\lambda(A_1) - \lambda(A) = \lim_{n \to \infty} (\lambda(A_1) - \lambda(A_n))$
$\lambda(A_1) - \lambda(A) = \lambda(A_1) - \lim_{n \to \infty} \lambda(A_n)$
6. En simplifiant $\lambda(A_1)$ (qui est fini, c'est crucial !), on obtient $\lambda(A) = \lim_{n \to \infty} \lambda(A_n)$.
