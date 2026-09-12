# Exercice 6 : Continuité décroissante et ensembles de mesure infinie

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

Soit $(A_n)$ une suite décroissante d'ensembles mesurables ($A_{n+1} \subset A_n$) avec $A = \bigcap A_n$. Montrer que si $\lambda(A_1) < +\infty$, alors $\lambda(A) = \lim \lambda(A_n)$. Donner un contre-exemple si $\lambda(A_1) = +\infty$.

**Correction Détaillée :**
Puisque $\lambda(A_1) < \infty$, on peut écrire $A_1 \setminus A_n$ qui forme une suite croissante de mesurables. La réunion de ces différences est $A_1 \setminus A$.
Par continuité croissante (Exercice 5) :
$\lambda(A_1 \setminus A) = \lim \lambda(A_1 \setminus A_n)$.
Puisque $\lambda(A_1)$ est finie, $\lambda(A_1 \setminus A_n) = \lambda(A_1) - \lambda(A_n)$, d'où $\lambda(A_1) - \lambda(A) = \lambda(A_1) - \lim \lambda(A_n)$. On simplifie par $\lambda(A_1)$ pour obtenir l'égalité.
**Contre-exemple :** Soit $A_n = [n, +\infty[$. Les $A_n$ sont décroissants. $A = \emptyset$, donc $\lambda(A) = 0$. Mais pour tout $n$, $\lambda(A_n) = +\infty$, dont la limite est $+\infty \neq 0$.
