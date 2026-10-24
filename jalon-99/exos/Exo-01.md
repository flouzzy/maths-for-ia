\subsection*{Exercice 1 : Séparation dans R^2 \quad $\bigstar\star\star\star\star$}

Soient $A = \{ (x,y) \in \mathbb{R}^2 \mid x < 0 \}$ et $B = \{ (x,y) \in \mathbb{R}^2 \mid y \ge 1/x, x > 0 \}$. Montrer que $A$ et $B$ peuvent être séparés, mais pas strictement.

**Correction :**

1. Les ensembles $A$ et $B$ sont convexes et disjoints. $A$ est ouvert et $B$ est fermé.
2. D'après la première forme géométrique de Hahn-Banach, il existe un hyperplan séparateur au sens large.
3. Considérons la forme linéaire $L(x,y) = x$.
   Pour tout $a = (x,y) \in A$, on a $L(a) = x < 0$.
   Pour tout $b = (x,y) \in B$, on a $L(b) = x > 0$.
   L'hyperplan d'équation $x=0$ sépare $A$ et $B$.
4. Séparation stricte : Supposons qu'il existe $L(x,y) = \alpha x + \beta y$ et $\epsilon > 0$ tels que $\forall a \in A, L(a) \le c - \epsilon < c + \epsilon \le L(b)$.
   En prenant $a_n = (-1/n, 0) \in A$, on a $-\alpha/n \le c - \epsilon$, donc en passant à la limite $0 \le c - \epsilon$.
   En prenant $b_n = (n, 1/n) \in B$, on a $\alpha n + \beta/n \ge c + \epsilon$.
   Si $\beta \neq 0$, cela empêche l'inégalité d'être vraie pour $n$ grand (les points de $B$ s'approchent asymptotiquement de l'axe des abscisses). Ainsi, aucune marge stricte ne peut exister.