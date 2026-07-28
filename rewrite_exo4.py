with open("jalon-26/exos/Exo-04.md", "r") as f:
    text = f.read()

if "## Démonstration Rigoureuse à Blanc\n\n1." in text:
    pass
else:
    new_text = r"""---
uuid: "jalon-26-exo-04"
title: "Distance à un sous-espace vectoriel"
difficulty: 4
---

# Exercice 4 : Distance à un sous-espace vectoriel (Difficulté ★★★★☆)

Dans l'espace euclidien $E = \mathbb{R}^4$ muni du produit scalaire canonique, on considère le sous-espace vectoriel $F$ défini par le système d'équations :
$x_1 + x_2 + x_3 + x_4 = 0$
$x_1 - x_2 + x_3 - x_4 = 0$

1. Déterminer une base orthonormée de l'orthogonal $F^\perp$.
2. Déterminer la projection orthogonale du vecteur $v = (1, 2, 3, 4)$ sur $F^\perp$.
3. En déduire rigoureusement la distance du vecteur $v$ au sous-espace $F$.

## Démonstration Rigoureuse à Blanc

1. Le sous-espace $F$ est défini comme l'intersection de deux hyperplans. Autrement dit, c'est le noyau de l'application linéaire définie par les deux équations. Par définition du produit scalaire usuel, les équations peuvent se réécrire comme des conditions d'orthogonalité :
   $x \in F \iff \langle x, u_1 \rangle = 0 \text{ et } \langle x, u_2 \rangle = 0$
   avec $u_1 = (1, 1, 1, 1)$ et $u_2 = (1, -1, 1, -1)$.
   Cela signifie que $F = \{u_1, u_2\}^\perp$. Par les propriétés de l'orthogonalité en dimension finie, on a $F^\perp = (\{u_1, u_2\}^\perp)^\perp = \text{Vect}(u_1, u_2)$.
   Pour trouver une base orthonormée de $F^\perp$, appliquons Gram-Schmidt à la famille $(u_1, u_2)$.
   - Norme de $u_1$ : $\|u_1\|^2 = 1^2 + 1^2 + 1^2 + 1^2 = 4 \implies \|u_1\| = 2$.
   - Posons $e_1 = \frac{u_1}{\|u_1\|} = \frac{1}{2}(1, 1, 1, 1)$.
   - Calculons $\langle u_2, e_1 \rangle = \frac{1}{2}(1 - 1 + 1 - 1) = 0$.
   De manière remarquable, $u_2$ est déjà orthogonal à $u_1$. Il suffit donc de le normaliser.
   - Norme de $u_2$ : $\|u_2\|^2 = 1^2 + (-1)^2 + 1^2 + (-1)^2 = 4 \implies \|u_2\| = 2$.
   - Posons $e_2 = \frac{u_2}{\|u_2\|} = \frac{1}{2}(1, -1, 1, -1)$.
   La famille $(e_1, e_2)$ est une base orthonormée de $F^\perp$.

2. Le théorème de la projection orthogonale stipule que la projection $p_{F^\perp}(v)$ d'un vecteur $v$ sur le sous-espace $F^\perp$ (dont $(e_1, e_2)$ est une base orthonormée) est donnée par la formule :
   $$ p_{F^\perp}(v) = \langle v, e_1 \rangle e_1 + \langle v, e_2 \rangle e_2 $$
   Calculons les produits scalaires partiels pour $v = (1, 2, 3, 4)$ :
   - $\langle v, e_1 \rangle = \frac{1}{2} (1\cdot 1 + 2\cdot 1 + 3\cdot 1 + 4\cdot 1) = \frac{1}{2} (10) = 5$.
   - $\langle v, e_2 \rangle = \frac{1}{2} (1\cdot 1 + 2\cdot(-1) + 3\cdot 1 + 4\cdot(-1)) = \frac{1}{2} (1 - 2 + 3 - 4) = \frac{1}{2} (-2) = -1$.
   Substituons ces valeurs dans la formule de la projection :
   $$ p_{F^\perp}(v) = 5 \cdot \frac{1}{2}(1, 1, 1, 1) - 1 \cdot \frac{1}{2}(1, -1, 1, -1) $$
   $$ p_{F^\perp}(v) = (\frac{5}{2}, \frac{5}{2}, \frac{5}{2}, \frac{5}{2}) - (\frac{1}{2}, -\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}) $$
   $$ p_{F^\perp}(v) = (\frac{4}{2}, \frac{6}{2}, \frac{4}{2}, \frac{6}{2}) = (2, 3, 2, 3) $$
   La projection de $v$ sur $F^\perp$ est le vecteur $(2, 3, 2, 3)$.

3. Par le théorème de projection orthogonale, on sait que l'espace $E$ se décompose en somme directe orthogonale $E = F \oplus^\perp F^\perp$.
   Tout vecteur $v \in E$ s'écrit de manière unique $v = p_F(v) + p_{F^\perp}(v)$.
   La distance $d(v, F)$ du vecteur $v$ au sous-espace $F$ est définie par $d(v, F) = \|v - p_F(v)\|$.
   Puisque $v - p_F(v) = p_{F^\perp}(v)$, il s'ensuit que :
   $$ d(v, F) = \|p_{F^\perp}(v)\| $$
   Calculons cette norme en utilisant le résultat de la question précédente :
   $$ \|p_{F^\perp}(v)\|^2 = \|(2, 3, 2, 3)\|^2 = 2^2 + 3^2 + 2^2 + 3^2 = 4 + 9 + 4 + 9 = 26 $$
   Ainsi, la distance de $v$ à $F$ est :
   $$ d(v, F) = \sqrt{26} $$
   $\blacksquare$
"""
    with open("jalon-26/exos/Exo-04.md", "w", encoding='utf-8') as f:
        f.write(new_text)
