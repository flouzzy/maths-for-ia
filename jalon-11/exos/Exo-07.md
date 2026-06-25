# Exercice 7: Trace comme forme linéaire (Difficulté 4/5)
## Énoncé
L'application $\text{Tr} : M_n(\mathbb{K}) \to \mathbb{K}$ est une forme linéaire. Montrer que tout hyperplan $H$ de $M_n(\mathbb{K})$ contient au moins une matrice inversible (pour $n \ge 2$).

## Correction détaillée
1. **Étape 1:** Un hyperplan de $M_n(\mathbb{K})$ est le noyau d'une forme linéaire non nulle $\phi$. Il est connu que toute forme linéaire sur $M_n(\mathbb{K})$ s'écrit $\phi(M) = \text{Tr}(AM)$ pour une unique matrice $A \in M_n(\mathbb{K})$. Ainsi, $H = \{ M \in M_n(\mathbb{K}) \mid \text{Tr}(AM) = 0 \}$.
2. **Étape 2:** On cherche $M \in H$ telle que $\det(M) \neq 0$. Si $A=0$, $\phi=0$ ce qui est exclu. Supposons par l'absurde que $H$ ne contient aucune matrice inversible.
3. **Étape 3:** L'hyperplan $H$ est un sous-espace vectoriel de dimension $n^2-1$. Si $H$ ne contient que des matrices singulières, on a une contradiction avec les résultats de la théorie des espaces de matrices de rang borné (théorème de Dieudonné), car la dimension maximale d'un sous-espace de matrices non-inversibles est $n(n-1)$, et pour $n \ge 2$, $n^2-1 > n(n-1)$.
4. **Conclusion:** L'hypothèse de départ est fausse, donc on en déduit formellement qu'un hyperplan contient toujours des éléments inversibles.
