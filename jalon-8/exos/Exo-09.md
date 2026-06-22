---
uuid: "jalon-8-exo-09"
title: "Exercice 9 : Propriétés du Noyau et de l'Image d'une Composition d'Applications Linéaires"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 9 : Propriétés du Noyau et de l'Image d'une Composition d'Applications Linéaires (Difficulté : ★★★★★)

## Énoncé
Soient $E, F, G$ des $\mathbb{K}$-espaces vectoriels de dimension finie.
Soient $f \in \mathcal{L}(E, F)$ et $g \in \mathcal{L}(F, G)$ deux applications linéaires.
On considère l'application composée $g \circ f : E \to G$.

1.  Démontrer que $\ker f \subseteq \ker(g \circ f)$.
2.  Démontrer que $\text{Im}(g \circ f) \subseteq \text{Im } g$.
3.  Démontrer que $\text{rg}(g \circ f) \le \text{rg } f$.
4.  Démontrer que $\text{rg}(g \circ f) \le \text{rg } g$.
5.  Démontrer la formule suivante : $\text{rg}(g \circ f) = \text{rg } f - \dim(\text{Im } f \cap \ker g)$.
6.  En déduire que $\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\text{Im } f \cap \ker g)$.

## Correction Détaillée

**1. Démontrer que $\ker f \subseteq \ker(g \circ f)$.**
Soit $x \in \ker f$.
Par définition du noyau d'une application linéaire, $f(x) = 0_F$, où $0_F$ est le vecteur nul de l'espace vectoriel $F$.
Appliquons l'application linéaire $g$ à cette égalité :
$g(f(x)) = g(0_F)$.
Puisque $g$ est une application linéaire, elle préserve le vecteur nul, c'est-à-dire $g(0_F) = 0_G$, où $0_G$ est le vecteur nul de l'espace vectoriel $G$.
Par conséquent, nous avons $(g \circ f)(x) = 0_G$.
D'après la définition du noyau de l'application linéaire $g \circ f$, cela signifie que $x \in \ker(g \circ f)$.
Ainsi, tout élément de $\ker f$ est également un élément de $\ker(g \circ f)$, ce qui prouve l'inclusion $\ker f \subseteq \ker(g \circ f)$.

**2. Démontrer que $\text{Im}(g \circ f) \subseteq \text{Im } g$.**
Soit $y \in \text{Im}(g \circ f)$.
Par définition de l'image d'une application linéaire, il existe un vecteur $x \in E$ tel que $y = (g \circ f)(x)$.
Nous pouvons réécrire cette expression en utilisant la définition de la composition d'applications : $y = g(f(x))$.
Posons $z = f(x)$. Puisque $x \in E$ et $f \in \mathcal{L}(E, F)$, le vecteur $z$ appartient à l'espace vectoriel $F$.
L'expression de $y$ devient alors $y = g(z)$.
D'après la définition de l'image de l'application linéaire $g$, puisque $z \in F$ et $y = g(z)$, cela signifie que $y \in \text{Im } g$.
Ainsi, tout élément de $\text{Im}(g \circ f)$ est également un élément de $\text{Im } g$, ce qui prouve l'inclusion $\text{Im}(g \circ f) \subseteq \text{Im } g$.

**3. Démontrer que $\text{rg}(g \circ f) \le \text{rg } f$.**
Nous avons $\text{Im}(g \circ f) = \{ (g \circ f)(x) \mid x \in E \}$.
En utilisant la définition de la composition, ceci est égal à $\{ g(f(x)) \mid x \in E \}$.
L'ensemble $\{ f(x) \mid x \in E \}$ est, par définition, l'image de $f$, notée $\text{Im } f$.
Donc, $\text{Im}(g \circ f)$ est l'image de l'ensemble $\text{Im } f$ par l'application $g$. On peut écrire $\text{Im}(g \circ f) = g(\text{Im } f)$.
Soit $\mathcal{B}_{\text{Im } f} = (u_1, ..., u_k)$ une base de $\text{Im } f$, où $k = \dim(\text{Im } f) = \text{rg } f$.
Tout vecteur $v \in \text{Im } f$ peut s'écrire comme une combinaison linéaire $v = \sum_{i=1}^k \lambda_i u_i$.
Alors, pour tout $y \in \text{Im}(g \circ f)$, il existe $v \in \text{Im } f$ tel que $y = g(v)$.
Donc $y = g(\sum_{i=1}^k \lambda_i u_i)$.
Par linéarité de $g$, $y = \sum_{i=1}^k \lambda_i g(u_i)$.
Ceci montre que la famille $(g(u_1), ..., g(u_k))$ est une famille génératrice de $\text{Im}(g \circ f)$.
La dimension d'un espace vectoriel est le cardinal minimal d'une famille génératrice.
Puisque $\text{Im}(g \circ f)$ est engendré par une famille de $k$ vecteurs, sa dimension est au plus $k$.
Donc, $\dim(\text{Im}(g \circ f)) \le k$.
En substituant les définitions du rang, nous obtenons $\text{rg}(g \circ f) \le \text{rg } f$.

**4. Démontrer que $\text{rg}(g \circ f) \le \text{rg } g$.**
D'après la question 2, nous avons établi que $\text{Im}(g \circ f) \subseteq \text{Im } g$.
Puisque $\text{Im}(g \circ f)$ est un sous-espace vectoriel de $\text{Im } g$, la dimension de $\text{Im}(g \circ f)$ ne peut pas être strictement supérieure à la dimension de $\text{Im } g$.
Par conséquent, $\dim(\text{Im}(g \circ f)) \le \dim(\text{Im } g)$.
En utilisant la définition du rang, cela se traduit par $\text{rg}(g \circ f) \le \text{rg } g$.

**5. Démontrer la formule suivante : $\text{rg}(g \circ f) = \text{rg } f - \dim(\text{Im } f \cap \ker g)$.**
Considérons l'application linéaire $g$ restreinte au sous-espace vectoriel $\text{Im } f$.
Définissons une nouvelle application linéaire $g' : \text{Im } f \to G$ par $g'(x) = g(x)$ pour tout $x \in \text{Im } f$.
L'espace de départ de $g'$ est $\text{Im } f$, qui est un sous-espace vectoriel de $F$ et est de dimension finie $\text{rg } f$.
Calculons l'image de $g'$ :
$\text{Im } g' = \{ g'(x) \mid x \in \text{Im } f \} = \{ g(x) \mid x \in \text{Im } f \}$.
Par définition, cet ensemble est exactement $\text{Im}(g \circ f)$.
Calculons le noyau de $g'$ :
$\ker g' = \{ x \in \text{Im } f \mid g'(x) = 0_G \} = \{ x \in \text{Im } f \mid g(x) = 0_G \}$.
Par définition, cet ensemble est l'intersection de $\text{Im } f$ et $\ker g$, c'est-à-dire $\text{Im } f \cap \ker g$.
Nous pouvons appliquer le théorème du rang à l'application linéaire $g' : \text{Im } f \to G$.
Le théorème du rang stipule que la dimension de l'espace de départ est égale à la somme de la dimension du noyau et de la dimension de l'image.
Donc, $\dim(\text{Im } f) = \dim(\ker g') + \dim(\text{Im } g')$.
En substituant les expressions que nous avons trouvées pour $\dim(\text{Im } f)$, $\ker g'$ et $\text{Im } g'$ :
$\text{rg } f = \dim(\text{Im } f \cap \ker g) + \text{rg}(g \circ f)$.
En réarrangeant les termes pour isoler $\text{rg}(g \circ f)$, nous obtenons la formule désirée :
$$ \text{rg}(g \circ f) = \text{rg } f - \dim(\text{Im } f \cap \ker g) $$

**6. En déduire que $\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\text{Im } f \cap \ker g)$.**
Appliquons le théorème du rang à l'application linéaire $f : E \to F$. L'espace de départ est $E$.
$$ \dim E = \dim(\ker f) + \text{rg } f \quad (*)$$
Appliquons le théorème du rang à l'application linéaire $g \circ f : E \to G$. L'espace de départ est également $E$.
$$ \dim E = \dim(\ker(g \circ f)) + \text{rg}(g \circ f) \quad (**)$$
De l'équation $(*)$, nous pouvons exprimer $\text{rg } f$ :
$\text{rg } f = \dim E - \dim(\ker f)$.
De l'équation $(**)$, nous pouvons exprimer $\text{rg}(g \circ f)$ :
$\text{rg}(g \circ f) = \dim E - \dim(\ker(g \circ f))$.
Maintenant, substituons ces expressions dans la formule démontrée à la question 5 :
$\text{rg}(g \circ f) = \text{rg } f - \dim(\text{Im } f \cap \ker g)$
$(\dim E - \dim(\ker(g \circ f))) = (\dim E - \dim(\ker f)) - \dim(\text{Im } f \cap \ker g)$.
Nous pouvons simplifier le terme $\dim E$ de chaque côté de l'égalité :
$-\dim(\ker(g \circ f)) = -\dim(\ker f) - \dim(\text{Im } f \cap \ker g)$.
En multipliant toute l'équation par $-1$, nous obtenons le résultat final :
$$ \dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\text{Im } f \cap \ker g) $$