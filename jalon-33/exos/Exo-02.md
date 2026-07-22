# Exercice 2 : Réduction de Gauss (Cas simple)

## Énoncé
Réduire en somme de carrés (méthode de Gauss) la forme quadratique $q$ définie sur $\mathbb{R}^3$ par :
$$ q(x,y,z) = x^2 + 2y^2 + 5z^2 + 4xy + 2xz + 6yz $$
En déduire le rang et la signature de $q$.

## Correction Détaillée (Zéro Ellipse)

L'algorithme de réduction de Gauss procède par factorisation successive.
**Étape 1 : Regroupement autour de la variable $x$**
Le terme $x^2$ est présent. Nous regroupons tous les termes contenant $x$ :
$$ q(x,y,z) = x^2 + 4xy + 2xz + 2y^2 + 5z^2 + 6yz $$
$$ q(x,y,z) = x^2 + 2x(2y + z) + 2y^2 + 5z^2 + 6yz $$
Nous identifions le début du développement d'un carré : $(x + A)^2 = x^2 + 2xA + A^2$. Ici, $A = 2y + z$.
Nous ajoutons et retranchons $A^2$ :
$$ x^2 + 2x(2y + z) = (x + 2y + z)^2 - (2y + z)^2 $$
En substituant dans $q$ :
$$ q(x,y,z) = (x + 2y + z)^2 - (4y^2 + 4yz + z^2) + 2y^2 + 5z^2 + 6yz $$
$$ q(x,y,z) = (x + 2y + z)^2 - 4y^2 - 4yz - z^2 + 2y^2 + 5z^2 + 6yz $$
$$ q(x,y,z) = (x + 2y + z)^2 - 2y^2 + 2yz + 4z^2 $$

**Étape 2 : Regroupement autour de la variable $y$**
Le reste de l'expression est : $Q(y,z) = -2y^2 + 2yz + 4z^2$.
On factorise le coefficient devant $y^2$ :
$$ Q(y,z) = -2 \left( y^2 - yz - 2z^2 \right) $$
On identifie le début d'un carré : $y^2 - 2y(\frac{z}{2}) = (y - \frac{z}{2})^2 - \frac{z^2}{4}$.
On substitue :
$$ Q(y,z) = -2 \left[ \left(y - \frac{z}{2}\right)^2 - \frac{z^2}{4} - 2z^2 \right] $$
$$ Q(y,z) = -2 \left[ \left(y - \frac{z}{2}\right)^2 - \frac{9z^2}{4} \right] $$
$$ Q(y,z) = -2 \left(y - \frac{z}{2}\right)^2 + \frac{9}{2} z^2 $$

**Conclusion de la réduction**
La forme quadratique s'écrit donc :
$$ q(x,y,z) = (x + 2y + z)^2 - 2 \left(y - \frac{z}{2}\right)^2 + \frac{9}{2} z^2 $$
Les trois formes linéaires $\ell_1(x,y,z) = x + 2y + z$, $\ell_2(x,y,z) = y - \frac{z}{2}$, et $\ell_3(x,y,z) = z$ sont clairement indépendantes (la matrice de passage est triangulaire supérieure avec des 1 sur la diagonale).
Il s'agit donc bien de la réduction de Gauss.
- **Rang** : Le nombre de carrés est de 3. Donc le rang est 3 (forme non dégénérée).
- **Signature** : Nous avons un coefficient strictement positif ($1$ devant $\ell_1^2$), un coefficient strictement négatif ($-2$ devant $\ell_2^2$), et un coefficient strictement positif ($\frac{9}{2}$ devant $\ell_3^2$).
La signature $(s, t)$ est le nombre de signes positifs et négatifs : $(2, 1)$. $\blacksquare$
