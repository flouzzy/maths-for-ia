# Exercice 9 : Mesure et limites supérieures

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Pour une suite d'ensembles $(A_n)$, on définit la limite supérieure $\limsup A_n = \bigcap_{N=1}^\infty \bigcup_{n \ge N} A_n$. Si $\sum_{n=1}^\infty \lambda(A_n) < \infty$, montrer que $\lambda(\limsup A_n) = 0$ (Lemme de Borel-Cantelli).

## Correction Détaillée

1. Posons $E_N = \bigcup_{n \ge N} A_n$. La suite $(E_N)$ est décroissante par rapport à $N$.
2. La limite supérieure est $A = \bigcap E_N$.
3. Évaluons la mesure de $E_N$ par sous-additivité : $\lambda(E_N) = \lambda(\bigcup_{n \ge N} A_n) \le \sum_{n=N}^\infty \lambda(A_n)$.
4. L'hypothèse dit que la série globale $\sum_{n=1}^\infty \lambda(A_n)$ converge. Donc le reste de la série tend vers zéro : $\lim_{N \to \infty} \sum_{n=N}^\infty \lambda(A_n) = 0$.
5. Ceci implique que $\lim_{N \to \infty} \lambda(E_N) = 0$.
6. Comme $A \subset E_N$ pour tout $N$, on a $\lambda(A) \le \lambda(E_N)$.
À la limite, $\lambda(A) = 0$. En d'autres termes, la probabilité (la mesure) d'appartenir à une infinité d'ensembles $A_n$ est nulle si la somme de leurs mesures converge.
