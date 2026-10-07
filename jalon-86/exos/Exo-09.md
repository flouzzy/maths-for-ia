# Exercice 9 : Théorème de la transformation universelle (Inverse Transform Sampling) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $X$ une variable aléatoire réelle de fonction de répartition $F$ continue et strictement croissante.
On définit la fonction quantile (ou inverse de la fonction de répartition) par $F^{-1} : ]0, 1[ \to \mathbb{R}$.
Soit $U$ une variable aléatoire de loi uniforme sur $]0, 1[$.
Montrer rigoureusement que la variable aléatoire $Y = F^{-1}(U)$ possède exactement $F$ pour fonction de répartition (donc la même loi que $X$).

## Correction

L'objectif est de calculer la fonction de répartition de $Y$, notée $F_Y(y)$, pour tout $y \in \mathbb{R}$.
Par définition :
$$ F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(F^{-1}(U) \leq y) $$

Par hypothèse, la fonction de répartition $F$ de $X$ est continue et strictement croissante. Une telle fonction réalise une bijection de l'ensemble des valeurs possibles de $X$ (un intervalle, éventuellement $\mathbb{R}$ entier) vers l'intervalle $]0, 1[$.
Elle admet donc une fonction réciproque $F^{-1} : ]0, 1[ \to \mathbb{R}$ qui est également strictement croissante.

Puisque $F$ est strictement croissante, elle préserve l'ordre. On peut donc appliquer la fonction $F$ aux deux membres de l'inégalité à l'intérieur de la probabilité sans en changer le sens :
L'inégalité $F^{-1}(U) \leq y$ est mathématiquement strictement équivalente à l'inégalité $F(F^{-1}(U)) \leq F(y)$.

Puisque $U \in ]0, 1[$, l'expression $F(F^{-1}(U))$ se simplifie exactement en $U$.
Ainsi, l'égalité des probabilités devient :
$$ F_Y(y) = \mathbb{P}(U \leq F(y)) $$

La variable aléatoire $U$ suit une loi uniforme sur $]0, 1[$. La fonction de répartition d'une loi uniforme $\mathcal{U}([0,1])$ est donnée par $\mathbb{P}(U \leq t) = t$ pour tout $t \in [0, 1]$.
Ici, $F$ est une fonction de répartition, ce qui signifie que pour tout réel $y$, la valeur de $F(y)$ appartient nécessairement à l'intervalle $[0, 1]$.
Par conséquent, on peut remplacer $t$ par $F(y)$ :
$$ \mathbb{P}(U \leq F(y)) = F(y) $$

Nous venons de prouver que pour tout réel $y$, $F_Y(y) = F(y)$.
La variable aléatoire $Y = F^{-1}(U)$ a donc la même fonction de répartition que $X$, ce qui signifie qu'elle suit exactement la même loi de probabilité. Ce résultat fondamental est à la base de toutes les méthodes informatiques de génération de nombres pseudo-aléatoires selon des lois continues arbitraires. $\blacksquare$
