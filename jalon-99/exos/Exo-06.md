# Exercice 6
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer que, dans un espace de Hilbert $\mathcal{H}$, l'existence du projeté orthogonal sur un convexe fermé (Théorème de projection sur un convexe fermé) permet de redémontrer constructivement la deuxième forme géométrique de Hahn-Banach (séparation d'un point et d'un convexe fermé).

**Correction :**
1. **Cadre de la démonstration :**
   Soit $\mathcal{H}$ un espace de Hilbert, muni du produit scalaire $\langle \cdot, \cdot \rangle$. Soit $C$ un convexe fermé non vide de $\mathcal{H}$ et $x_0 \notin C$.
   Le théorème de projection affirme l'existence et l'unicité d'un point $p \in C$ minimisant la distance à $x_0$ : $\|x_0 - p\| = \inf_{y \in C} \|x_0 - y\|$.
   Puisque $x_0 \notin C$ et que $C$ est fermé, cette distance est strictement positive, donc $x_0 - p \ne 0$.
2. **Caractérisation de la projection :**
   La caractérisation variationnelle de la projection sur un convexe $C$ s'écrit :
   $\forall y \in C, \quad \langle x_0 - p, y - p \rangle \le 0$
3. **Construction de l'hyperplan séparateur :**
   On définit le vecteur normal à l'hyperplan comme $v = x_0 - p \ne 0$.
   La forme linéaire associée est $f(x) = \langle v, x \rangle$. Elle est évidemment continue par l'inégalité de Cauchy-Schwarz ($f \in \mathcal{H}^*$).
   Développons l'inégalité caractérisant la projection : pour tout $y \in C$,
   $\langle v, y \rangle - \langle v, p \rangle \le 0 \implies \langle v, y \rangle \le \langle v, p \rangle$.
   Soit $f(y) \le f(p)$ pour tout $y \in C$.
4. **Calcul de la marge stricte :**
   Calculons la valeur de la forme linéaire évaluée en $x_0$ par rapport à $p$ :
   $f(x_0) - f(p) = \langle v, x_0 \rangle - \langle v, p \rangle = \langle v, x_0 - p \rangle = \langle v, v \rangle = \|v\|^2$.
   Posons $\alpha = f(p) + \frac{1}{2} \|v\|^2$ et $\varepsilon = \frac{1}{2} \|v\|^2 > 0$.
   Pour tout $y \in C$, on a :
   $f(y) \le f(p) = \alpha - \varepsilon$.
   Pour le point $x_0$, on a :
   $f(x_0) = f(p) + \|v\|^2 = \alpha + \varepsilon$.
5. **Conclusion :**
   Nous avons explicitement construit une forme linéaire $f$ (définie par le produit scalaire avec le vecteur différence $x_0 - p$) et défini une constante $\alpha$ et une marge $\varepsilon > 0$ vérifiant :
   $f(y) \le \alpha - \varepsilon < \alpha + \varepsilon \le f(x_0)$.
   Ceci est exactement l'énoncé de la séparation stricte d'un point et d'un convexe fermé (cas particulier de la deuxième forme géométrique de Hahn-Banach où $B=\{x_0\}$ est compact), retrouvé ici par l'argument purement géométrique de la projection orthogonale dans les espaces de Hilbert.
