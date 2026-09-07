# Exercice 8 : Produit de probabilités croissantes \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit des ensembles mesurables $A_1 \subset A_2 \subset A_3 \dots$. Prouver que $\mu(\cup A_n) = \lim \mu(A_n)$ en utilisant TCM.

**Correction :**
Soit $f_n = \mathbb{1}_{A_n}$. Comme les ensembles sont croissants, $f_n \le f_{n+1}$. La limite est $f = \mathbb{1}_{\cup A_n}$. Par Beppo Levi, $\int f = \lim \int f_n$, ce qui équivaut par définition à $\mu(\cup A_n) = \lim \mu(A_n)$.
