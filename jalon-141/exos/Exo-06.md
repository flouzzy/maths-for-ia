# Exercice 6 : Dimension VC des demi-espaces en 2D
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}^2$. Prouver que la classe des demi-espaces fermés délimités par des droites a une dimension VC de 3.
**Correction Détaillée :**
* *Analyse de l'énoncé :* L'équation d'un demi-espace est $\omega_1 x_1 + \omega_2 x_2 + b \ge 0$.
* *Résolution pas-à-pas :*
**Étape 1 : Pulvérisation de trois points.**
Choisissons 3 points non alignés : $p_1=(0,0), p_2=(1,0), p_3=(0,1)$.
Leurs 8 sous-ensembles peuvent être obtenus par des droites :
- $\emptyset$ : $x_1 + x_2 \le -1$.
- $\{p_1\}$ : $x_1 + x_2 \le 0.5$.
- $\{p_2\}$ : $x_1 - x_2 \ge 0.5$.
- $\{p_3\}$ : $-x_1 + x_2 \ge 0.5$.
- $\{p_1, p_2\}$ : $x_2 \le 0.5$.
- $\{p_1, p_3\}$ : $x_1 \le 0.5$.
- $\{p_2, p_3\}$ : $x_1 + x_2 \ge 0.5$.
- $\{p_1, p_2, p_3\}$ : $x_1 + x_2 \ge -1$.
Ainsi, au moins un ensemble de 3 points est pulvérisable. $VC \ge 3$.

**Étape 2 : Impossibilité pour quatre points.**
Soient 4 points quelconques dans $\mathbb{R}^2$. Deux cas géométriques existent par le théorème de Radon :
Cas 1 : Un point est à l'intérieur du triangle formé par les 3 autres. Soit $p_4$ dans le triangle $(p_1, p_2, p_3)$. Pour isoler $\{p_1, p_2, p_3\}$, le demi-espace doit inclure les 3 sommets. Par convexité, tout le triangle est inclus, donc $p_4$ aussi. Il est impossible de former $\{p_1, p_2, p_3\}$.
Cas 2 : Les 4 points forment un quadrilatère convexe $p_1, p_2, p_3, p_4$. Prenons les points opposés $\{p_1, p_3\}$. Tout demi-espace contenant $p_1$ et $p_3$ contient nécessairement le segment $[p_1, p_3]$. Puisque les diagonales se croisent, toute droite séparant $p_1, p_3$ de $p_2, p_4$ devrait traverser les deux diagonales en leur point d'intersection, ce qui implique que la droite passe par le point d'intersection. Les segments $[p_1, p_3]$ et $[p_2, p_4]$ s'intersectent. Un demi-espace contenant $p_1$ et $p_3$ est convexe, il contient le segment $[p_1, p_3]$. Un demi-espace fermé opposé contenant $p_2$ et $p_4$ contient $[p_2, p_4]$. L'intersection des deux diagonales serait à la fois dans le demi-espace et dans son complément, ce qui est absurde.
Ainsi, aucun ensemble de 4 points ne peut être pulvérisé.
$VC(\mathcal{F}) = 3$. $\blacksquare$
