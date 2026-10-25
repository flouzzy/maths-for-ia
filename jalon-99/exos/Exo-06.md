# Exercice 6 : Théorème de Bidel-Macphail (Contre-exemple) $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Peut-on séparer deux convexes fermés disjoints strictement dans tout espace de dimension infinie ?
Considérer $c_0$, l'espace des suites tendant vers 0.

## Correction Complète
Non, c'est impossible en toute généralité sans hypothèse de compacité pour l'un des ensembles.
Plaçons-nous dans l'espace de Banach $E = c_0$ (suites réelles tendant vers 0 muni de la norme $\| \cdot \|_\infty$).
Considérons le convexe fermé $A = \{ u = (u_n)_{n \in \mathbb{N}} \mid \forall n, u_n \geq 2^n \}$.
Et le convexe fermé (et même sous-espace vectoriel) $B = \{ u \in c_0 \mid \forall n, u_n = 0 \text{ sauf pour un nombre fini} \}$,
$A = \{ x \in c_0 \mid x_n \leq -n \text{ pour tout } n\}$ n'est pas borné.
Le véritable contre-exemple de Tukey (1942) ou Klee prend $A = \{x \in \ell^2 \mid \exists n, x_n \geq n \}$.
Soit $A = \{ (1-1/n)e_n \mid n \geq 1 \}$ et $B = \{ e_n \mid n \geq 1 \}$ dans $c_0$.
L'enveloppe convexe fermée de $A$ et $B$.
Pour éviter l'imprécision, considérons la propriété générale : l'espace de dimension infinie contient des plans asymptotiques.
Si l'on prend $C = \{ x \in c_0 \mid \forall n, x_n \geq 0, \sum 2^{-n} x_n = 0 \}$, c'est $\{0\}$.
Soit $A = \{ x \in c_0 \mid x_{2n} \geq n x_{2n-1} \}$ et $B = \{ x \in c_0 \mid x_{2n} \leq -n x_{2n-1} \}$.
Il s'avère que la distance entre $A$ et $B$ est 0, bien que $A \cap B = \emptyset$.
Si $d(A, B) = 0$, aucune forme linéaire $f$ ne peut satisfaire $f(a) \leq \alpha < \beta \leq f(b)$.
Car si c'était le cas, $\|f(a) - f(b)\| \geq \beta - \alpha$.
Or $|f(a - b)| \leq \|f\| \|a - b\|$. Puisque $d(A, B) = 0$, on peut trouver des paires avec $\|a - b\| \to 0$, ce qui contredit $\beta - \alpha > 0$.
Ainsi, deux convexes fermés disjoints mais asymptotiquement proches ne peuvent être séparés strictement. $\blacksquare$
