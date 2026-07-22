# Exercice 3 : Réduction sans carrés initiaux

## Énoncé
Réduire en somme de carrés la forme quadratique $q$ définie sur $\mathbb{R}^3$ par :
$$ q(x,y,z) = xy + xz + yz $$
Donner son rang et sa signature.

## Correction Détaillée (Zéro Ellipse)

La forme $q(x,y,z) = xy + xz + yz$ ne possède aucun terme au carré ($x^2, y^2, z^2$). Nous ne pouvons donc pas appliquer directement le procédé de complétion du carré sur une variable.
L'astuce standard consiste à polariser un terme croisé. Prenons $xy$.
On pose le changement de variables inversible :
$x = u + v$
$y = u - v$
$z = w$
Ce qui donne $u = \frac{x+y}{2}$ et $v = \frac{x-y}{2}$.
Remplaçons dans $q$ :
$$ q(u,v,w) = (u+v)(u-v) + (u+v)w + (u-v)w $$
$$ q(u,v,w) = u^2 - v^2 + uw + vw + uw - vw $$
$$ q(u,v,w) = u^2 - v^2 + 2uw $$
Nous avons maintenant fait apparaître des carrés. Appliquons la réduction de Gauss classique, en commençant par regrouper les termes en $u$.
$$ q(u,v,w) = (u^2 + 2uw) - v^2 $$
On complète le carré sur $u$ :
$$ u^2 + 2uw = (u+w)^2 - w^2 $$
Donc :
$$ q(u,v,w) = (u+w)^2 - w^2 - v^2 $$
Il ne reste plus qu'à revenir aux variables initiales $(x,y,z)$.
$u+w = \frac{x+y}{2} + z$
$w = z$
$v = \frac{x-y}{2}$
On remplace :
$$ q(x,y,z) = \left( \frac{1}{2}x + \frac{1}{2}y + z \right)^2 - z^2 - \left( \frac{1}{2}x - \frac{1}{2}y \right)^2 $$
Les trois formes linéaires $\ell_1 = \frac{1}{2}x + \frac{1}{2}y + z$, $\ell_2 = z$, $\ell_3 = \frac{1}{2}x - \frac{1}{2}y$ sont linéairement indépendantes (leur déterminant est non nul).
- **Rang** : Il y a 3 carrés, donc $\text{rg}(q) = 3$.
- **Signature** : Il y a un signe $+$ et deux signes $-$. La signature est donc $(1, 2)$. $\blacksquare$
