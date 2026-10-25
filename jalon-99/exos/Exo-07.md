# Exercice 7 : Prolongement des formes linéaires continues $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $E$ un espace normé et $F$ un sous-espace vectoriel. Démontrer que pour tout $x_0 \notin F$, il existe $f \in E'$ (dual topologique) telle que $f_{|F} = 0$, $f(x_0) = 1$ et $\|f\| = \frac{1}{d(x_0, F)}$.

## Correction Complète
Considérons le sous-espace $G = F \oplus \mathbb{R}x_0$.
Tout élément $y \in G$ s'écrit de manière unique $y = x + \lambda x_0$ où $x \in F$.
Définissons une forme linéaire $g$ sur $G$ par $g(x + \lambda x_0) = \lambda$.
On a bien $g(x) = 0$ pour tout $x \in F$ (cas $\lambda = 0$) et $g(x_0) = 1$ (cas $x=0, \lambda=1$).
Calculons la norme de $g$ sur $G$ :
$\|g\|_G = \sup_{y \in G, y \neq 0} \frac{|g(y)|}{\|y\|}$.
Si $\lambda \neq 0$,
$\frac{|g(x + \lambda x_0)|}{\|x + \lambda x_0\|} = \frac{|\lambda|}{\|x + \lambda x_0\|} = \frac{1}{\|x/\lambda + x_0\|}$.
Puisque $x \in F$ et $F$ est un sous-espace vectoriel, $z = -x/\lambda$ parcourt tout $F$.
Ainsi, $\sup_{z \in F} \frac{1}{\|x_0 - z\|} = \frac{1}{\inf_{z \in F} \|x_0 - z\|} = \frac{1}{d(x_0, F)}$.
Donc $\|g\|_G = \frac{1}{d(x_0, F)}$.
Par le théorème de Hahn-Banach analytique généralisé (ou théorème de prolongement de Hahn-Banach, version dominée par la norme), il existe une forme linéaire continue $f$ définie sur $E$ tout entier, prolongeant $g$, telle que :
$f(y) = g(y)$ pour tout $y \in G$, et $\|f\|_E = \|g\|_G = \frac{1}{d(x_0, F)}$.
Les propriétés voulues découlent de ce prolongement préservant la norme. $\blacksquare$
