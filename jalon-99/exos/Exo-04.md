# Exercice 4
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer, par un contre-exemple explicite dans le plan affine $\mathbb{R}^2$, que si les deux ensembles $A$ et $B$ sont fermés, disjoints, et convexes, mais qu'aucun des deux n'est compact, ils ne peuvent pas nécessairement être séparés **strictement**.

**Correction :**
1. **Construction des ensembles :**
   Considérons l'espace vectoriel euclidien usuel $\mathbb{R}^2$.
   Posons $A$ comme l'épigraphe de la fonction exponentielle : $A = \{ (x, y) \in \mathbb{R}^2 \mid y \ge e^x \}$.
   $A$ est l'image réciproque de $[0, +\infty[$ par l'application continue $(x,y) \mapsto y - e^x$, c'est donc un fermé. La fonction exponentielle étant convexe (sa dérivée seconde est strictement positive), son épigraphe est un ensemble convexe.
   Posons $B$ comme le demi-plan inférieur : $B = \{ (x, y) \in \mathbb{R}^2 \mid y \le 0 \}$.
   $B$ est trivialement fermé et convexe.
2. **Disjonction :**
   Pour tout point de $A$, $y \ge e^x > 0$. Pour tout point de $B$, $y \le 0$. Ainsi, il n'existe aucun point $(x,y)$ appartenant à la fois à $A$ et à $B$. $A \cap B = \emptyset$.
3. **Absence de compacité :**
   $A$ contient la suite de points $(n, e^n)$ pour $n \in \mathbb{N}$, dont la norme tend vers l'infini. $A$ n'est pas borné, donc n'est pas compact (par le théorème de Borel-Lebesgue). De même pour $B$.
4. **Preuve de l'impossibilité d'une séparation stricte :**
   Supposons par l'absurde qu'il existe un hyperplan (une droite affine) strictement séparateur. Il existerait $(u,v) \ne (0,0)$, $\alpha \in \mathbb{R}$ et $\varepsilon > 0$ tels que :
   $\forall (x,y) \in A, \, ux + vy \ge \alpha + \varepsilon$
   $\forall (x,y) \in B, \, ux + vy \le \alpha - \varepsilon$
   Puisque pour tout $x \in \mathbb{R}$, le point $(x, 0)$ est dans $B$, on a $ux \le \alpha - \varepsilon$. Ceci n'est possible pour tout $x$ (positif et négatif) que si $u = 0$.
   Si $u = 0$, la forme linéaire se réduit à $vy$.
   Pour tout $(x,y) \in B$, $vy \le \alpha - \varepsilon$. En particulier avec $(0,-n) \in B$, on trouve $-nv \le \alpha - \varepsilon$ pour tout $n \in \mathbb{N}$. Ceci impose $v \ge 0$.
   Comme $(u,v) \ne (0,0)$, on doit avoir $v > 0$.
   La condition sur $B$ devient : pour tout $y \le 0$, $vy \le \alpha - \varepsilon$. Le maximum à gauche est pour $y=0$, donc $0 \le \alpha - \varepsilon$, soit $\alpha \ge \varepsilon > 0$.
   Appliquons maintenant la condition sur $A$. Pour tout $x \in \mathbb{R}$, le point $(x, e^x)$ est dans $A$. Donc $v e^x \ge \alpha + \varepsilon$.
   Puisque cette inégalité doit être vraie pour tout $x$, prenons la limite quand $x \to -\infty$. $e^x \to 0$, ce qui donne à la limite $0 \ge \alpha + \varepsilon$.
   Ceci est en contradiction flagrante avec le fait que $\alpha \ge \varepsilon > 0$.
   L'absurdité démontre qu'aucune séparation stricte n'est possible, illustrant la nécessité de la compacité stipulée dans le théorème.
