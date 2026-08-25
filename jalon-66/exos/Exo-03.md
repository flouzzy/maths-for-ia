## Exercice 3 : Mesure de Dirac \quad $\bigstar\bigstar\star\star\star$

**Énoncé :** Soit $\delta_a$ la mesure de Dirac au point $a \in \mathbb{R}$, définie par $\delta_a(A) = 1$ si $a \in A$ et $0$ sinon. Calculer $\int_\mathbb{R} f d\delta_a$ pour une fonction mesurable positive $f$.

**Correction Détaillée :**
1. Considérons d'abord le cas où $f$ est une fonction indicatrice, c'est-à-dire $f = \mathbf{1}_A$.
   Par définition, $\int_\mathbb{R} \mathbf{1}_A d\delta_a = \delta_a(A)$.
   Si $a \in A$, $\delta_a(A) = 1 = \mathbf{1}_A(a)$. Si $a \notin A$, $\delta_a(A) = 0 = \mathbf{1}_A(a)$.
   Donc, $\int_\mathbb{R} \mathbf{1}_A d\delta_a = \mathbf{1}_A(a)$.
2. Par linéarité, pour toute fonction simple $s = \sum_{i=1}^n c_i \mathbf{1}_{A_i}$, on a :
   $$\int_\mathbb{R} s d\delta_a = \sum_{i=1}^n c_i \delta_a(A_i) = \sum_{i=1}^n c_i \mathbf{1}_{A_i}(a) = s(a)$$
3. Pour une fonction mesurable positive $f$ quelconque, il existe une suite de fonctions simples positives $(s_n)$ croissant vers $f$.
   On a $\int_\mathbb{R} s_n d\delta_a = s_n(a)$.
4. En passant à la limite (ou en utilisant la définition par le supremum) :
   $$\int_\mathbb{R} f d\delta_a = \sup_{s \le f} \int_\mathbb{R} s d\delta_a = \sup_{s \le f} s(a) = f(a)$$
   Ainsi, l'intégrale par rapport à la mesure de Dirac en $a$ évalue simplement la fonction en $a$.
