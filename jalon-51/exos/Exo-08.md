## Exercice 8 : Produit d'espaces métriques \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $(X, d_X)$ et $(Y, d_Y)$ deux espaces métriques. Sur l'espace produit $X \times Y$, on pose :
$d((x_1, y_1), (x_2, y_2)) = d_X(x_1, x_2) + d_Y(y_1, y_2)$.
Montrer que c'est une distance sur $X \times Y$.

**Correction :**
Notons $u = (x_1, y_1)$, $v = (x_2, y_2)$ et $w = (x_3, y_3)$.
1. **Séparation :**
   $d(u,v) = 0 \iff d_X(x_1, x_2) + d_Y(y_1, y_2) = 0$.
   Comme les deux termes sont positifs, cela implique $d_X(x_1, x_2) = 0$ et $d_Y(y_1, y_2) = 0$.
   Donc $x_1=x_2$ et $y_1=y_2$, soit $u=v$.
2. **Symétrie :**
   $d(u,v) = d_X(x_1, x_2) + d_Y(y_1, y_2) = d_X(x_2, x_1) + d_Y(y_2, y_1) = d(v,u)$.
3. **Inégalité triangulaire :**
   $d(u,w) = d_X(x_1, x_3) + d_Y(y_1, y_3)$.
   Par inégalité triangulaire dans $X$ et $Y$ :
   $d_X(x_1, x_3) \le d_X(x_1, x_2) + d_X(x_2, x_3)$
   $d_Y(y_1, y_3) \le d_Y(y_1, y_2) + d_Y(y_2, y_3)$
   En sommant ces deux inégalités :
   $d(u,w) \le (d_X(x_1, x_2) + d_Y(y_1, y_2)) + (d_X(x_2, x_3) + d_Y(y_2, y_3))$
   Soit $d(u,w) \le d(u,v) + d(v,w)$. $\blacksquare$
