---
uuid: "exo-11-04"
title: "Exercice 4: Intersection d'hyperplans indépendants"
---
# Exercice 4: Intersection d'hyperplans indépendants (Difficulté $\star \star \star$)

## Énoncé
Soit $E$ un espace vectoriel de dimension $n \ge 2$. Soient $H_1$ et $H_2$ deux hyperplans de $E$ dictés par les formes linéaires $\phi_1, \phi_2 \in E^*$. On suppose que $H_1 \neq H_2$. Démontrer avec la plus grande rigueur que la dimension de l'intersection $H_1 \cap H_2$ est égale à $n-2$.

## Correction détaillée

1. **Caractérisation de l'indépendance des formes :**
   Les hyperplans sont donnés par $H_1 = \ker \phi_1$ et $H_2 = \ker \phi_2$.
   Puisque les hyperplans sont distincts ($H_1 \neq H_2$), les formes linéaires $\phi_1$ et $\phi_2$ ne sont pas colinéaires. La famille $(\phi_1, \phi_2)$ est donc une famille libre dans l'espace dual $E^*$.

2. **Construction de l'application conjointe :**
   Définissons l'application linéaire $\Phi : E \to \mathbb{K}^2$ par $\Phi(x) = (\phi_1(x), \phi_2(x))$.
   La linéarité de $\Phi$ découle directement de la linéarité de ses composantes.

3. **Détermination du noyau de l'application conjointe :**
   Le noyau de $\Phi$ est l'ensemble des vecteurs $x \in E$ tels que $\Phi(x) = (0, 0)$.
   Cela signifie $\phi_1(x) = 0$ et $\phi_2(x) = 0$.
   Donc $x \in \ker \phi_1 \cap \ker \phi_2$.
   Par conséquent, $\ker \Phi = H_1 \cap H_2$.

4. **Détermination du rang de l'application conjointe :**
   L'image $\text{Im }\Phi$ est un sous-espace vectoriel de $\mathbb{K}^2$.
   Supposons par l'absurde que $\text{Im }\Phi$ ne soit pas $\mathbb{K}^2$ tout entier. Alors sa dimension serait 0 ou 1.
   Si $\dim(\text{Im }\Phi) = 1$, il existerait $(a, b) \in \mathbb{K}^2 \setminus \{(0,0)\}$ tel que pour tout $x \in E$, l'image soit orthogonale à $(a,b)$ au sens du produit scalaire canonique, soit $a\phi_1(x) + b\phi_2(x) = 0$.
   Cela impliquerait que la combinaison linéaire $a\phi_1 + b\phi_2 = 0_{E^*}$, ce qui contredit formellement la liberté de la famille $(\phi_1, \phi_2)$.
   L'hypothèse est donc absurde. $\Phi$ est surjective, et $\text{rg}(\Phi) = 2$.

5. **Application du théorème du rang :**
   Appliquons le théorème du rang à l'application $\Phi$ :
   $$\dim(E) = \dim(\ker \Phi) + \text{rg}(\Phi)$$
   En substituant les résultats établis :
   $$n = \dim(H_1 \cap H_2) + 2$$
   $$\dim(H_1 \cap H_2) = n - 2$$

**Conclusion :**
L'intersection de deux hyperplans distincts dans un espace de dimension $n$ crée structurellement un sous-espace de dimension $n-2$.
