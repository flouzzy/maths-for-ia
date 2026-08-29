## Exercice 4 : Croissance de l'intégrale \quad $$\bigstar\bigstar\star$$

**Énoncé :**
Soient $f, g \in \mathcal{M}_+$ telles que $f \le g$ sur $X$.
Montrer directement via la définition que $\int_X f \, d\mu \le \int_X g \, d\mu$.

**Correction :**
1. Par définition : $\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \mid s \in \mathcal{E}_+, 0 \le s \le f \right\rbrace$.
2. Soit un élément arbitraire $s \in \mathcal{E}_+$ tel que $0 \le s \le f$.
3. Par hypothèse $f \le g$, on a par transitivité $0 \le s \le g$.
4. Cela implique que $s$ est également une fonction étagée minorant $g$.
5. Ainsi, l'ensemble des fonctions étagées minorant $f$ est inclus dans l'ensemble des fonctions étagées minorant $g$ :
   $$\{ s \in \mathcal{E}_+ \mid s \le f \} \subset \{ s \in \mathcal{E}_+ \mid s \le g \}$$
6. Le supremum sur un sous-ensemble étant inférieur ou égal au supremum sur l'ensemble complet, on a :
   $$\sup \left\lbrace \int_X s \, d\mu \mid s \le f \right\rbrace \le \sup \left\lbrace \int_X s \, d\mu \mid s \le g \right\rbrace$$
7. D'où $\int_X f \, d\mu \le \int_X g \, d\mu$.
