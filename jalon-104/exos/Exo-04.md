# Exercice 4 : Densité et Complétude $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $H$ un espace de Hilbert et $(e_n)_{n \in \mathbb{N}}$ une famille orthonormée. On définit le sous-espace $F = \text{vect}(e_n)_{n \in \mathbb{N}}$.
Montrer que si $x \in H$ est tel que $x \in F^\perp$, alors $x = 0$ si et seulement si $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne.

**Correction détaillée :**
1. **Sens $\Leftarrow$ (Si c'est une base hilbertienne, alors $x=0$) :**
   Supposons que $(e_n)_{n \in \mathbb{N}}$ soit une base hilbertienne de $H$. Par définition, cela signifie que $\overline{F} = H$.
   Soit $x \in F^\perp$. Alors pour tout $n \in \mathbb{N}$, $\langle x, e_n \rangle = 0$.
   Par linéarité du produit scalaire, pour tout $y \in F$, $\langle x, y \rangle = 0$.
   Soit maintenant $z \in H$. Puisque $F$ est dense dans $H$, il existe une suite $(y_k)_{k \in \mathbb{N}}$ d'éléments de $F$ telle que $y_k \to z$ lorsque $k \to \infty$.
   Par continuité du produit scalaire par rapport à la deuxième variable :
   $\langle x, z \rangle = \langle x, \lim_{k \to \infty} y_k \rangle = \lim_{k \to \infty} \langle x, y_k \rangle = \lim_{k \to \infty} 0 = 0$.
   Cette relation étant vraie pour tout $z \in H$, prenons $z = x$. On obtient $\langle x, x \rangle = \|x\|^2 = 0$.
   Donc $x = 0$. L'orthogonal de $F$ est réduit au vecteur nul.

2. **Sens $\Rightarrow$ (Si $F^\perp = \{0\}$, alors c'est une base hilbertienne) :**
   Supposons que $F^\perp = \{0\}$.
   Soit $M = \overline{F}$. Puisque $H$ est un espace de Hilbert et $M$ est un sous-espace vectoriel fermé de $H$, le théorème de projection orthogonale s'applique.
   On a la décomposition en somme directe orthogonale : $H = M \oplus M^\perp$.
   Or, $M^\perp = (\overline{F})^\perp$. Par continuité du produit scalaire, l'orthogonal d'un ensemble est égal à l'orthogonal de son adhérence, donc $M^\perp = F^\perp$.
   Par hypothèse, $F^\perp = \{0\}$. Donc $M^\perp = \{0\}$.
   Ainsi, $H = M \oplus \{0\} = M = \overline{F}$.
   L'espace engendré par la famille orthonormée $(e_n)$ est dense dans $H$, ce qui est exactement la définition d'une base hilbertienne.
