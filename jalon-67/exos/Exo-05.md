# Exercice 5 : Passage de Riemann à Lebesgue ★☆☆☆☆

**Énoncé :**
Prouver que la fonction de Dirichlet $f(x) = 1$ si $x \in \mathbb{Q} \cap [0,1]$, et $0$ sinon, n'est pas intégrable au sens de Riemann mais l'est au sens de Lebesgue via une limite de fonctions étagées.

**Correction :**
1. Au sens de Riemann, toute somme de Darboux supérieure vaut $1$ et toute somme inférieure vaut $0$ car $\mathbb{Q}$ et $\mathbb{R} \setminus \mathbb{Q}$ sont denses dans $[0,1]$. L'intégrale de Riemann n'existe pas.
2. Au sens de Lebesgue, on peut énumérer les rationnels de $[0,1]$ : $q_1, q_2, \dots$. Soit $f_n(x) = \chi_{\{q_1, \dots, q_n\}}(x)$.
3. Les $f_n$ sont des fonctions étagées positives, et la suite est croissante.
4. $\int f_n d\lambda = \sum_{k=1}^n \lambda(\{q_k\}) = \sum 0 = 0$.
5. La limite de $f_n$ est exactement $f$. Par Beppo Levi, $\int f d\lambda = \lim \int f_n d\lambda = 0$. La fonction est donc intégrable au sens de Lebesgue et son intégrale est nulle.
