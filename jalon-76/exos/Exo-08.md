# Exercice 8 : Espace $L^2$ (★★★★☆)

**Énoncé :**
Soit $K(x, y)$ une fonction continue sur $[0, 1] \times [0, 1]$.
On définit l'opérateur intégral $T$ sur $L^2([0, 1])$ par :
$$ Tf(x) = \int_0^1 K(x, y) f(y) dy $$
Montrer que $Tf \in L^2([0, 1])$ pour tout $f \in L^2([0, 1])$ et donner une majoration de $\|Tf\|_{L^2}$ en fonction de $K$ et $\|f\|_{L^2}$.

**Correction Détaillée :**
*Analyse de l'énoncé :* On doit majorer $|Tf(x)|$ puis intégrer. L'inégalité de Cauchy-Schwarz va être essentielle.

*Résolution pas-à-pas :*
Soit $f \in L^2([0, 1])$. Fixons $x \in [0, 1]$.
Appliquons l'inégalité de Cauchy-Schwarz dans $L^2$ par rapport à la variable $y$ pour la fonction produit $y \mapsto K(x, y) \cdot f(y)$ :
$$ |Tf(x)| = \left| \int_0^1 K(x, y) f(y) dy \right| \le \left( \int_0^1 |K(x, y)|^2 dy \right)^{1/2} \left( \int_0^1 |f(y)|^2 dy \right)^{1/2} $$
On note $\|f\|_{L^2}$ la norme de $f$, indépendante de $x$.
$$ |Tf(x)|^2 \le \left( \int_0^1 |K(x, y)|^2 dy \right) \|f\|_{L^2}^2 $$

Pour vérifier que $Tf \in L^2$, intégrons sur $x \in [0, 1]$ :
$$ \|Tf\|_{L^2}^2 = \int_0^1 |Tf(x)|^2 dx \le \int_0^1 \left( \int_0^1 |K(x, y)|^2 dy \right) \|f\|_{L^2}^2 dx $$
$$ \|Tf\|_{L^2}^2 \le \|f\|_{L^2}^2 \int_0^1 \int_0^1 |K(x, y)|^2 dy dx $$

$K$ étant continue sur un compact, elle y est bornée par $M = \max |K(x, y)|$, ou simplement de carré intégrable. Soit $C = \left( \int_0^1 \int_0^1 |K(x, y)|^2 dy dx \right)^{1/2}$ la norme de Hilbert-Schmidt de $K$.
On a alors :
$$ \|Tf\|_{L^2}^2 \le C^2 \|f\|_{L^2}^2 \implies \|Tf\|_{L^2} \le C \|f\|_{L^2} $$
L'intégrale converge, donc $Tf \in L^2$, et l'opérateur est borné de norme au plus $C$.
