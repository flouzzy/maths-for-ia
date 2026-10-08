## Simulation d'une loi par la méthode de la transformée inverse \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $X$ une variable aléatoire dont la loi est définie par la fonction de répartition continue et strictement croissante sur son support :
$$F_X(x) = \begin{cases} 0 & \text{si } x < 1 \\ 1 - \frac{1}{x^3} & \text{si } x \geq 1 \end{cases}$$
Soit $U$ une variable aléatoire suivant la loi uniforme sur l'intervalle $]0, 1[$.
Montrer que la variable aléatoire définie par $Y = F_X^{-1}(U)$ suit la même loi que $X$, et expliciter la fonction $F_X^{-1}$.

**Correction Explicative :**
1. La méthode de la transformée inverse est un résultat fondamental permettant de générer n'importe quelle loi de probabilité continue à partir d'une source d'aléa uniforme.
2. Démontrons d'abord le résultat théorique général. Soit $F_Y$ la fonction de répartition de $Y = F_X^{-1}(U)$. Par définition :
   $F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(F_X^{-1}(U) \leq y)$.
3. Puisque $F_X$ est une fonction de répartition, elle est par nature croissante. Par hypothèse, elle est strictement croissante sur son support, ce qui garantit l'existence de son inverse $F_X^{-1}$, qui est également strictement croissante. Nous pouvons donc appliquer la fonction $F_X$ de part et d'autre de l'inégalité sans en changer le sens :
   $\mathbb{P}(F_X^{-1}(U) \leq y) = \mathbb{P}(F_X(F_X^{-1}(U)) \leq F_X(y)) = \mathbb{P}(U \leq F_X(y))$.
4. Or, $U$ suit une loi uniforme $\mathcal{U}(]0, 1[)$. La fonction de répartition d'une variable uniforme standard, notée $F_U(u)$, vaut exactement $u$ pour tout $u \in ]0, 1[$.
   Étant donné que $F_X(y)$ est une probabilité, sa valeur est toujours comprise dans $[0, 1]$. On a donc :
   $\mathbb{P}(U \leq F_X(y)) = F_U(F_X(y)) = F_X(y)$.
   Ainsi, $F_Y(y) = F_X(y)$ pour tout $y \in \mathbb{R}$. Les variables $Y$ et $X$ ont la même fonction de répartition, elles suivent donc la même loi. Le théorème est démontré.
5. Procédons maintenant au calcul explicite de l'application mesurable $F_X^{-1}$ pour la loi spécifique donnée dans l'énoncé (qui est une loi de Pareto).
   Nous devons résoudre l'équation $u = F_X(x)$ pour trouver $x$ en fonction de $u \in ]0, 1[$.
   $$u = 1 - \frac{1}{x^3}$$
6. Isolons $x$ algébriquement :
   $$\frac{1}{x^3} = 1 - u$$
   $$x^3 = \frac{1}{1 - u}$$
   Puisque $x \geq 1$ et $u \in ]0, 1[$, on peut extraire la racine cubique :
   $$x = \left(\frac{1}{1 - u}\right)^{1/3} = (1 - u)^{-1/3}$$
7. Conclusion : L'application mesurable recherchée est $F_X^{-1}(u) = (1 - u)^{-1/3}$. Ainsi, la variable aléatoire $Y = (1 - U)^{-1/3}$ a exactement la même loi que $X$. Notons au passage que puisque $U$ et $1-U$ ont la même loi uniforme sur $]0, 1[$, on pourrait tout aussi bien utiliser la transformation plus simple $Y = U^{-1/3}$ en pratique informatique.
