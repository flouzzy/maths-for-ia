# Indépendance et incompatibilité

**Difficulté :** $\bigstar\star\star\star\star$

Soient $A$ et $B$ deux événements d'un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$, tels que $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$.
Montrer que $A$ et $B$ ne peuvent pas être à la fois indépendants et incompatibles (mutuellement exclusifs).

### Correction

Soient $A$ et $B$ deux événements tels que $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$.

1. Supposons que $A$ et $B$ soient incompatibles. Cela signifie par définition que $A \cap B = \emptyset$.
2. Par conséquent, la probabilité de leur intersection est nulle : $\mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0$.
3. Supposons maintenant que $A$ et $B$ soient également indépendants. La définition de l'indépendance donne : $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$.
4. En combinant les deux propriétés, nous obtenons : $\mathbb{P}(A)\mathbb{P}(B) = 0$.
5. Or, nous savons que dans le corps des réels, le produit de deux nombres est nul si et seulement si l'un au moins des deux facteurs est nul. Donc, $\mathbb{P}(A) = 0$ ou $\mathbb{P}(B) = 0$.
6. Ceci est en contradiction flagrante avec l'hypothèse initiale $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$.

Nous pouvons donc conclure qu'il est impossible que deux événements de probabilité non nulle soient à la fois indépendants et incompatibles.
