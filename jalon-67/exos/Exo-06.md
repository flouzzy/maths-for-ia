# Exercice 6 : Théorème de Beppo Levi pour des ensembles $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $(A_n)_{n \in \mathbb{N}}$ une suite croissante d'ensembles mesurables (i.e., $A_n \subset A_{n+1}$).
En utilisant le Théorème de Convergence Monotone, prouver que $\mu\left(\bigcup_{n \in \mathbb{N}} A_n\right) = \lim_{n \to \infty} \mu(A_n)$.

## Correction Détaillée
1. Considérons les fonctions indicatrices $f_n(x) = \mathbf{1}_{A_n}(x)$.
2. Ces fonctions sont mesurables (car les $A_n$ le sont) et positives.
3. Comme $A_n \subset A_{n+1}$, on a pour tout $x \in X$, $f_n(x) \le f_{n+1}(x)$. La suite de fonctions est donc croissante.
4. Déterminons la limite ponctuelle $f(x) = \lim_{n \to \infty} f_n(x)$.
   - Si $x \in \bigcup_{n \in \mathbb{N}} A_n$, alors il existe un rang $N$ tel que $x \in A_N$. Par croissance, $x \in A_n$ pour tout $n \ge N$.
     Donc $f_n(x) = 1$ pour $n \ge N$, et la limite est $1$.
   - Si $x \notin \bigcup_{n \in \mathbb{N}} A_n$, alors pour tout $n$, $x \notin A_n$. Donc $f_n(x) = 0$ pour tout $n$, et la limite est $0$.
   Ainsi, $f(x) = \mathbf{1}_{\bigcup_{n} A_n}(x)$.
5. Le Théorème de Convergence Monotone donne alors :
   $$ \int_X f(x) d\mu = \lim_{n \to \infty} \int_X f_n(x) d\mu $$
6. Par définition de l'intégrale d'une fonction indicatrice, $\int_X \mathbf{1}_E d\mu = \mu(E)$.
   On obtient donc bien $\mu\left(\bigcup_{n} A_n\right) = \lim_{n \to \infty} \mu(A_n)$.
