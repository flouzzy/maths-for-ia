# Exercice 7

**Difficulté :** $\star\star\star\☆☆$

**Énoncé :**
Soit l'espace $\ell^1$ des suites sommables réelles muni de la norme $\|u\|_1 = \sum_{n=0}^\infty |u_n|$. On définit l'opérateur de décalage à droite (shift) $S : \ell^1 \to \ell^1$ par $S(u) = (0, u_0, u_1, u_2, \dots)$. Montrer que $S$ est une isométrie linéaire, et déterminer sa norme $\|S\|$.

**Correction Détaillée :**
1. L'opérateur associe à la suite $u = (u_0, u_1, \dots)$ la suite $v = S(u)$ telle que $v_0 = 0$ et $v_n = u_{n-1}$ pour $n \ge 1$.
2. **Linéarité :** Trivialement vérifiée par les opérations terme à terme sur les suites.
3. **Isométrie :** Calculons la norme de l'image $S(u)$ :
   $$ \|S(u)\|_1 = \sum_{n=0}^\infty |v_n| = |0| + \sum_{n=1}^\infty |u_{n-1}|. $$
4. En posant le changement d'indice $k = n - 1$, on obtient :
   $$ \|S(u)\|_1 = \sum_{k=0}^\infty |u_k| = \|u\|_1. $$
5. Puisque $\|S(u)\|_1 = \|u\|_1$ pour tout $u \in \ell^1$, $S$ préserve les distances. C'est une isométrie linéaire.
6. **Norme de l'opérateur :** Il découle immédiatement de l'isométrie que le ratio $\frac{\|S(u)\|_1}{\|u\|_1} = 1$ pour tout $u \neq 0$.
7. Par conséquent, la norme de l'opérateur est $\|S\|_{\mathcal{L}(\ell^1, \ell^1)} = 1$.
