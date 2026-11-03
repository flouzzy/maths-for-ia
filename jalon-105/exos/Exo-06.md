# Exercice 6 : Noyau, Image et Adjoint $\bigstar\bigstar\bigstar\star\star$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$.
On note $\ker(T)$ le noyau de $T$ et $\text{Im}(T)$ l'image de $T$.
1. Démontrer que $\ker(T^*) = (\text{Im}(T))^\perp$.
2. En déduire que $\overline{\text{Im}(T)} = (\ker(T^*))^\perp$.
3. Démontrer que $\ker(T^* T) = \ker(T)$.

## Correction
1. Soit $y \in H$. Prouvons l'équivalence pas à pas :
$$ y \in \ker(T^*) \iff T^*y = 0_H $$
Cela signifie que le vecteur $T^*y$ est nul, ce qui est équivalent à dire qu'il est orthogonal à tout vecteur de l'espace $H$ :
$$ \iff \forall x \in H, \quad \langle x, T^*y \rangle = 0 $$
Par la définition de l'opérateur adjoint, nous pouvons faire passer l'opérateur sur le côté gauche du produit scalaire :
$$ \iff \forall x \in H, \quad \langle Tx, y \rangle = 0 $$
L'ensemble des éléments de la forme $Tx$ lorsque $x$ parcourt $H$ constitue exactement l'image de $T$, notée $\text{Im}(T)$.
Donc, l'équation $\langle Tx, y \rangle = 0$ pour tout $x$ signifie que le vecteur $y$ est orthogonal à tous les vecteurs de $\text{Im}(T)$ :
$$ \iff \forall z \in \text{Im}(T), \quad \langle z, y \rangle = 0 $$
$$ \iff y \in (\text{Im}(T))^\perp $$
Nous avons ainsi démontré l'égalité ensembliste : $\ker(T^*) = (\text{Im}(T))^\perp$.

2. Prenons l'orthogonal des deux membres de l'égalité précédente :
$$ (\ker(T^*))^\perp = ((\text{Im}(T))^\perp)^\perp $$
Dans un espace de Hilbert, d'après le théorème du bipolaire (ou double orthogonal), pour tout sous-espace vectoriel $M$, on a $(M^\perp)^\perp = \overline{M}$ (l'adhérence de $M$).
En appliquant ce théorème à $M = \text{Im}(T)$, on obtient immédiatement :
$$ (\ker(T^*))^\perp = \overline{\text{Im}(T)} $$

3. Montrons l'égalité des noyaux par double inclusion.
- Sens $\supseteq$ (inclusion triviale) :
Si $x \in \ker(T)$, alors $Tx = 0$. Donc $T^*(Tx) = T^*(0) = 0$. Donc $x \in \ker(T^* T)$.
- Sens $\subseteq$ :
Soit $x \in \ker(T^* T)$. Alors $T^* T x = 0$.
Par conséquent, son produit scalaire avec $x$ est nul :
$$ \langle T^* T x, x \rangle = 0 $$
En utilisant la définition de l'adjoint $T^*$ pour le passer de l'autre côté du produit scalaire :
$$ \langle Tx, (T^*)^* x \rangle = 0 $$
Puisque $(T^*)^* = T$, on obtient :
$$ \langle Tx, Tx \rangle = 0 $$
$$ \|Tx\|^2 = 0 \implies Tx = 0 \implies x \in \ker(T) $$
Les deux inclusions prouvent que $\ker(T^* T) = \ker(T)$.
