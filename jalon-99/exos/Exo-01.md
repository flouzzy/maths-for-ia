# Exercice 1
**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Dans le plan euclidien $\mathbb{R}^2$, on considère les deux sous-ensembles :
$$ A = \{ (x_1, x_2) \in \mathbb{R}^2 \mid x_1^2 + x_2^2 < 1 \} $$
$$ B = \{ (x_1, x_2) \in \mathbb{R}^2 \mid x_1 + x_2 \ge 4 \} $$
Démontrer rigoureusement que $A$ et $B$ peuvent être séparés strictement par un hyperplan et déterminer une équation cartésienne explicite d'un tel hyperplan.

**Correction :**
1. **Convexité :**
   $A$ est la boule unité ouverte pour la norme euclidienne. Toute boule est convexe.
   $B$ est un demi-plan fermé, défini par l'inégalité affine $x_1 + x_2 - 4 \ge 0$. C'est l'intersection d'un nombre fini de demi-plans, donc un convexe.
2. **Disjonction :**
   Si $(x_1, x_2) \in A$, par l'inégalité de Cauchy-Schwarz appliquée aux vecteurs $(x_1, x_2)$ et $(1,1)$ :
   $|x_1 \cdot 1 + x_2 \cdot 1| \le \sqrt{x_1^2 + x_2^2} \sqrt{1^2 + 1^2}$.
   Puisque $(x_1, x_2) \in A$, $x_1^2 + x_2^2 < 1$, donc $x_1 + x_2 \le |x_1 + x_2| < 1 \cdot \sqrt{2} = \sqrt{2}$.
   Or, pour tout point de $B$, $x_1 + x_2 \ge 4$. Comme $\sqrt{2} < 4$, l'intersection $A \cap B$ est vide.
3. **Topologie :**
   $A$ est défini par une inégalité stricte de fonction continue, c'est donc un ensemble ouvert.
   (Remarque : bien que $B$ ne soit pas compact, le fait que $A$ soit ouvert permet d'appliquer la première forme de Hahn-Banach. Pour la séparation stricte, on note que la distance $d(A,B) > 0$, ce qui dans $\mathbb{R}^n$ pour des convexes fermés dont l'un est borné — l'adhérence de A est compacte — suffit).
4. **Détermination de l'hyperplan :**
   Considérons la forme linéaire $f(x) = x_1 + x_2$.
   Pour tout $x \in A$, on a vu que $f(x) < \sqrt{2}$. Posons $\alpha = 2$.
   Ainsi, $\forall x \in A, \, f(x) < \alpha$.
   Pour tout $y \in B$, $f(y) \ge 4$.
   On a bien $\sup_{x \in A} f(x) = \sqrt{2} \le 2 < 4 = \inf_{y \in B} f(y)$.
   L'hyperplan affine d'équation cartésienne $x_1 + x_2 = 2$ sépare strictement $A$ et $B$.
