# Exercice 7 : Convexité de l'Entropie Croisée

$\bigstar\bigstar\bigstar\bigstar\star$


On étudie la cross-entropy en tant que fonction de la distribution prédite $q$. Soit une distribution fixe $P$ sur un ensemble fini d'états $i \in \{1, \dots, N\}$ avec des probabilités $p_i > 0$.
Soit la fonction $f: \Delta \to \mathbb{R}$ définie sur le simplexe de probabilité $\Delta = \{q = (q_1, \dots, q_N) \in \mathbb{R}^N : \sum q_i = 1, q_i > 0 \}$ par :
$$f(q) = - \sum_{i=1}^N p_i \ln(q_i)$$

**1.** Calculer le gradient et la matrice Hessienne de la fonction $f$ par rapport au vecteur $q$.
**2.** En déduire que la fonction de perte Cross-Entropy est strictement convexe par rapport aux probabilités prédites.

**Correction :**

**1.** Calculons les dérivées partielles premières :
$$\frac{\partial f}{\partial q_k} = - \frac{p_k}{q_k}$$
Le gradient est donc $\nabla f(q) = \left( - \frac{p_1}{q_1}, \dots, - \frac{p_N}{q_N} \right)^T$.

Calculons les dérivées partielles secondes :
Si $j \neq k$, $\frac{\partial^2 f}{\partial q_k \partial q_j} = 0$.
Si $j = k$, $\frac{\partial^2 f}{\partial q_k^2} = \frac{\partial}{\partial q_k} \left(- \frac{p_k}{q_k} \right) = \frac{p_k}{q_k^2}$.
La matrice Hessienne $H_f(q)$ est donc une matrice diagonale :
$$H_f(q) = \text{Diag} \left( \frac{p_1}{q_1^2}, \dots, \frac{p_N}{q_N^2} \right)$$

**2.** Pour démontrer la stricte convexité, il suffit de montrer que la matrice Hessienne est définie positive.
Soit un vecteur non nul $v \in \mathbb{R}^N$. Considérons la forme quadratique associée :
$$v^T H_f(q) v = \sum_{i=1}^N \frac{p_i}{q_i^2} v_i^2$$
Puisque par hypothèse $p_i > 0$ et $q_i > 0$, chaque terme de la somme est strictement positif si $v_i \neq 0$. Puisque $v$ est non nul, la somme entière est strictement positive.
La Hessienne est donc définie positive sur tout le simplexe $\Delta$. Par conséquent, la fonction de perte Cross-Entropy est strictement convexe. Cela garantit qu'il existe un unique minimum global, qui correspond à $q = p$.
