# Exercice 2 : Invariance par translation de la mesure extérieure

**Difficulté :** $\bigstar\star\star\star\star$

Soit $A \subset \mathbb{R}$ et $x \in \mathbb{R}$. Montrer que $\lambda^*(A + x) = \lambda^*(A)$.

**Correction Détaillée :**
Considérons un recouvrement de $A$ par des intervalles ouverts $I_n = ]a_n, b_n[$. Alors les intervalles $I_n + x = ]a_n + x, b_n + x[$ forment un recouvrement ouvert de $A + x$.
La longueur d'un tel intervalle est $\ell(I_n + x) = (b_n + x) - (a_n + x) = b_n - a_n = \ell(I_n)$.
En passant à l'infimum sur tous les recouvrements possibles, on obtient $\lambda^*(A + x) \le \lambda^*(A)$.
Par symétrie, en considérant $A = (A + x) - x$, on obtient $\lambda^*(A) \le \lambda^*(A + x)$. D'où l'égalité stricte.
