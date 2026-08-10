# Exercice 3 : Équivalence de distances : Produit cartésien
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé formel
Sur $\mathbb{R}^2$, on définit $d_1(x,y) = |x_1 - y_1| + |x_2 - y_2|$ et $d_{\infty}(x,y) = \max(|x_1 - y_1|, |x_2 - y_2|)$. Montrer que ces deux distances sont uniformément équivalentes.

## Résolution pas à pas
**Étape 1 : Définition de l'équivalence**

Il faut trouver deux constantes strictement positives $c, C$ telles que pour tout $x,y \in \mathbb{R}^2$, $c \cdot d_{\infty}(x,y) \le d_1(x,y) \le C \cdot d_{\infty}(x,y)$.

**Étape 2 : Majoration**

Par définition du maximum, $|x_1 - y_1| \le d_{\infty}(x,y)$ et $|x_2 - y_2| \le d_{\infty}(x,y)$.
En sommant ces deux inégalités, on obtient : $d_1(x,y) = |x_1 - y_1| + |x_2 - y_2| \le d_{\infty}(x,y) + d_{\infty}(x,y) = 2 \cdot d_{\infty}(x,y)$. On pose $C = 2$.

**Étape 3 : Minoration**

Puisque $|x_1 - y_1| \ge 0$ et $|x_2 - y_2| \ge 0$, la somme est nécessairement supérieure ou égale au plus grand des deux termes. Autrement dit :
$d_{\infty}(x,y) = \max(|x_1 - y_1|, |x_2 - y_2|) \le |x_1 - y_1| + |x_2 - y_2| = d_1(x,y)$.
Ceci correspond à poser $c = 1$.

**Conclusion :** Nous avons montré que $1 \cdot d_{\infty} \le d_1 \le 2 \cdot d_{\infty}$. Les métriques sont équivalentes, ce qui implique que les pavés ($d_{\infty}$) et les losanges ($d_1$) définissent la même topologie usuelle sur le plan. $\blacksquare$
