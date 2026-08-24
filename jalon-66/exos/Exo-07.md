# Exercice 7 : Croissance de l'intégrale (Théorème) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $f, g \in \mathcal{M}_+$ telles que $f \le g$ sur $X$. En utilisant uniquement la définition formelle de l'intégrale (avec le supremum sur les fonctions simples), démontrer rigoureusement que $\int_X f \, d\mu \le \int_X g \, d\mu$.

**Correction :**
Ceci est une démonstration purement algébrique sur les ensembles.
1. Par définition, $\int_X f \, d\mu = \sup S_f$, où $S_f = \left\lbrace \int_X s \, d\mu \mid s \in \mathcal{S}_+, 0 \le s \le f \right\rbrace$.
2. De même, $\int_X g \, d\mu = \sup S_g$, où $S_g = \left\lbrace \int_X s \, d\mu \mid s \in \mathcal{S}_+, 0 \le s \le g \right\rbrace$.
3. Soit $s$ un élément arbitraire de l'ensemble d'indexation du premier supremum, c'est-à-dire que $s$ est une fonction simple telle que $0 \le s \le f$.
4. Par transitivité de l'inégalité ponctuelle, puisque $f \le g$, on a nécessairement $0 \le s \le g$.
5. Cela implique que cette même fonction $s$ appartient à l'ensemble d'indexation du second supremum. Donc $S_f \subset S_g$.
6. Si un ensemble de nombres réels $A$ est inclus dans un ensemble $B$, alors $\sup(A) \le \sup(B)$.
7. On conclut immédiatement que $\int_X f \, d\mu \le \int_X g \, d\mu$.
