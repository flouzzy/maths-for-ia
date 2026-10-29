# Exercice 6 : Projection et Convexes

## Énoncé

Soit $H = \mathbb{R}^2$ muni de la norme euclidienne. Trouver la projection de $x = (2, 2)$ sur le convexe fermé $C = \{ (u, v) \in \mathbb{R}^2 \mid u^2 + v^2 \le 1 \}$.

*Niveau de difficulté :* $\bigstar\bigstar\bigstar\star\star$

## Correction

1. **Caractérisation :** $C$ est la boule unité fermée $B(0, 1)$.
2. **Vecteur cible :** $x = (2, 2)$, dont la norme est $\|x\| = \sqrt{2^2+2^2} = \sqrt{8} > 1$. Donc $x \notin C$.
3. **Principe de projection :** La projection sur une boule fermée centrée en l'origine d'un point à l'extérieur s'obtient en le ramenant sur le bord via une homothétie. Le point de projection est colinéaire à $x$ et de norme 1.
4. **Calcul :** $P_C(x) = \frac{x}{\|x\|} = \frac{(2, 2)}{\sqrt{8}} = (\frac{2}{2\sqrt{2}}, \frac{2}{2\sqrt{2}}) = (\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$.
5. **Vérification (Inégalité variationnelle) :** On vérifie que pour tout $y \in C$, $\langle x - P_C(x), y - P_C(x) \rangle \le 0$. C'est vrai car $x - P_C(x)$ est le vecteur normal sortant de la sphère en $P_C(x)$.
