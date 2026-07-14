---
uuid: "jalon-27-exo-07"
title: "Exercice 07 : Rang de l'adjoint"
---
# Exercice 07 : Rang de l'adjoint

**Difficulté :** ★★★★☆

## Énoncé

Déduire que $\operatorname{rg}(f^*) = \operatorname{rg}(f)$.

## Démonstration sans ellipse

On sait que $\ker(f^*) = (\operatorname{Im}(f))^\perp$.
En prenant la dimension de ces espaces :
$$ \dim(\ker(f^*)) = \dim((\operatorname{Im}(f))^\perp) = n - \dim(\operatorname{Im}(f)) = n - \operatorname{rg}(f) $$
Or, par le théorème du rang appliqué à $f^*$ :
$$ \operatorname{rg}(f^*) = n - \dim(\ker(f^*)) $$
En substituant :
$$ \operatorname{rg}(f^*) = n - (n - \operatorname{rg}(f)) = \operatorname{rg}(f) $$
Les rangs sont donc égaux. $\blacksquare$
