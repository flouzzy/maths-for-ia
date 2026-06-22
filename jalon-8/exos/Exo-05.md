---
uuid: "jalon-8-exo-05"
title: "Exercice 5 : Analyse d'une application linéaire de $\mathbb{R}^4$ dans $\mathbb{R}^3$"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 5 : Analyse d'une application linéaire de $\mathbb{R}^4$ dans $\mathbb{R}^3$ (Difficulté : ★★★☆☆)

## Énoncé
Soit $f : \mathbb{R}^4 \to \mathbb{R}^3$ l'application définie pour tout $(x,y,z,w) \in \mathbb{R}^4$ par :
$$f(x,y,z,w) = (x+y, y+z, z+w)$$
1. Déterminer le noyau $\ker f$ de $f$. En donner une base et sa dimension.
2. Déterminer le rang de $f$, $\text{rg } f$.
3. En déduire la nature de l'image $\text{Im } f$.

## Correction Détaillée

1.  **Détermination du noyau $\ker f$ :**
    Par définition, le noyau $\ker f$ est l'ensemble des vecteurs $(x,y,z,w) \in \mathbb{R}^4$ tels que $f(x,y,z,w) = (0,0,0)$.
    Cela revient à résoudre le système d'équations linéaires homogènes suivant sur le corps $\mathbb{R}$ :
    $$ \begin{cases} x+y = 0 \quad (L_1) \\ y+z = 0 \quad (L_2) \\ z+w = 0 \quad (L_3) \end{cases} $$

    Nous allons résoudre ce système en exprimant les variables en fonction d'une ou plusieurs variables libres.
    De l'équation $(L_1)$, nous pouvons exprimer $x$ en fonction de $y$ :
    $$ x = -y $$
    De l'équation $(L_2)$, nous pouvons exprimer $z$ en fonction de $y$ :
    $$ z = -y $$
    De l'équation $(L_3)$, nous pouvons exprimer $w$ en fonction de $z$ :
    $$ w = -z $$
    Maintenant, nous substituons l'expression de $z$ dans l'expression de $w$ :
    $$ w = -(-y) $$
    $$ w = y $$

    Ainsi, tout vecteur $(x,y,z,w)$ appartenant à $\ker f$ doit satisfaire les relations $x=-y$, $z=-y$, et $w=y$.
    Les vecteurs de $\ker f$ sont donc de la forme :
    $$ (-y, y, -y, y) $$
    où $y$ est un scalaire réel quelconque, $y \in \mathbb{R}$.

    Nous pouvons factoriser le scalaire $y$ de cette expression vectorielle :
    $$ (-y, y, -y, y) = y \cdot (-1, 1, -1, 1) $$

    Le noyau $\ker f$ est donc l'ensemble des multiples scalaires du vecteur $v_1 = (-1, 1, -1, 1)$.
    $$ \ker f = \text{Vect}((-1, 1, -1, 1)) $$

    Le vecteur $v_1 = (-1, 1, -1, 1)$ est un vecteur non nul de $\mathbb{R}^4$. Par conséquent, la famille constituée uniquement de ce vecteur, $(v_1)$, est une famille libre.
    Puisqu'elle est génératrice de $\ker f$ et qu'elle est libre, elle constitue une base de $\ker f$.
    La dimension de $\ker f$ est le nombre de vecteurs dans cette base.
    $$ \dim(\ker f) = 1 $$

2.  **Détermination du rang de $f$ :**
    L'espace de départ $E = \mathbb{R}^4$ est un espace vectoriel de dimension finie sur $\mathbb{R}$. Sa dimension est $\dim E = 4$.
    Nous pouvons appliquer le Théorème du Rang, qui est un théorème fondamental de l'algèbre linéaire. Il stipule que pour toute application linéaire $f : E \to F$ où $E$ est un espace vectoriel de dimension finie, on a la relation suivante :
    $$ \dim E = \dim(\ker f) + \text{rg}(f) $$
    où $\text{rg}(f)$ est la dimension de l'image de $f$, c'est-à-dire $\dim(\text{Im } f)$.

    En substituant les valeurs que nous avons déterminées :
    $$ 4 = 1 + \text{rg}(f) $$

    Pour trouver la valeur de $\text{rg}(f)$, nous soustrayons 1 des deux côtés de l'équation :
    $$ \text{rg}(f) = 4 - 1 $$
    $$ \text{rg}(f) = 3 $$

3.  **Déduction de la nature de l'image $\text{Im } f$ :**
    Nous avons déterminé que le rang de $f$ est $\text{rg}(f) = 3$.
    Par définition même du rang d'une application linéaire, $\text{rg}(f)$ est la dimension de son image. Donc :
    $$ \dim(\text{Im } f) = 3 $$

    L'image $\text{Im } f$ est un sous-espace vectoriel de l'espace d'arrivée $F = \mathbb{R}^3$.
    Nous savons que la dimension de l'espace d'arrivée est $\dim(\mathbb{R}^3) = 3$.
    Puisque $\text{Im } f$ est un sous-espace vectoriel de $\mathbb{R}^3$ et que sa dimension est égale à celle de $\mathbb{R}^3$ ($\dim(\text{Im } f) = \dim(\mathbb{R}^3) = 3$), il s'ensuit que $\text{Im } f$ est égal à l'espace $\mathbb{R}^3$ tout entier.
    $$ \text{Im } f = \mathbb{R}^3 $$
    Cela signifie que l'application linéaire $f$ est surjective.