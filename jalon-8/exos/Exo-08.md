---
uuid: "jalon-8-exo-08"
title: "Exercice 8 : Propriétés du Noyau et de l'Image d'une Composition d'Applications Linéaires"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 8 : Propriétés du Noyau et de l'Image d'une Composition d'Applications Linéaires (Difficulté : ★★★★☆)

## Énoncé
Soient $E, F, G$ trois $\mathbb{K}$-espaces vectoriels de dimensions finies. Soient $f \in \mathcal{L}(E, F)$ et $g \in \mathcal{L}(F, G)$ deux applications linéaires.
On considère l'application composée $g \circ f : E \to G$.

1.  **Noyau de la composition :**
    a.  Démontrer que $\ker f \subseteq \ker(g \circ f)$. En déduire une inégalité entre les dimensions.
    b.  Démontrer que $\ker(g \circ f) = f^{-1}(\ker g \cap \text{Im } f)$.
    c.  En considérant la restriction de $f$ à un sous-espace vectoriel approprié, ou en utilisant le théorème du rang sur une application bien choisie, établir la relation :
        $$\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\ker g \cap \text{Im } f)$$
    d.  En déduire que $\dim(\ker(g \circ f)) \le \dim(\ker f) + \dim(\ker g)$.

2.  **Image de la composition :**
    a.  Démontrer que $\text{Im}(g \circ f) \subseteq \text{Im } g$. En déduire une inégalité entre les rangs.
    b.  Démontrer que $\text{Im}(g \circ f) = g(\text{Im } f)$.
    c.  En appliquant le théorème du rang à la restriction de $g$ à $\text{Im } f$, établir la relation :
        $$\text{rg}(g \circ f) = \text{rg}(f) - \dim(\ker g \cap \text{Im } f)$$
    d.  En déduire que $\text{rg}(g \circ f) \le \text{rg}(f)$.
    e.  À partir des résultats précédents et du théorème du rang, démontrer l'inégalité de Sylvester :
        $$\text{rg}(g \circ f) \ge \text{rg}(f) + \text{rg}(g) - \dim F$$

## Correction Détaillée

Soient $E, F, G$ trois $\mathbb{K}$-espaces vectoriels de dimensions finies. Soient $f \in \mathcal{L}(E, F)$ et $g \in \mathcal{L}(F, G)$ deux applications linéaires.

1.  **Noyau de la composition :**

    a.  Démontrons que $\ker f \subseteq \ker(g \circ f)$.
        Soit $x \in \ker f$. Par définition du noyau, $f(x) = 0_F$.
        Alors, par définition de la composition, $(g \circ f)(x) = g(f(x))$.
        En substituant $f(x) = 0_F$, nous obtenons $(g \circ f)(x) = g(0_F)$.
        Puisque $g$ est une application linéaire, elle envoie le vecteur nul de son espace de départ sur le vecteur nul de son espace d'arrivée, c'est-à-dire $g(0_F) = 0_G$.
        Donc, $(g \circ f)(x) = 0_G$, ce qui signifie que $x \in \ker(g \circ f)$.
        Ainsi, tout élément de $\ker f$ est aussi un élément de $\ker(g \circ f)$, ce qui prouve l'inclusion $\ker f \subseteq \ker(g \circ f)$.
        Comme $\ker f$ est un sous-espace vectoriel de $\ker(g \circ f)$, sa dimension est inférieure ou égale à celle de $\ker(g \circ f)$.
        Par conséquent, $\dim(\ker f) \le \dim(\ker(g \circ f))$.

    b.  Démontrons que $\ker(g \circ f) = f^{-1}(\ker g \cap \text{Im } f)$.
        Soit $x \in \ker(g \circ f)$. Par définition, $(g \circ f)(x) = 0_G$, ce qui signifie $g(f(x)) = 0_G$.
        Cette égalité implique que le vecteur $f(x)$ appartient au noyau de $g$, c'est-à-dire $f(x) \in \ker g$.
        De plus, par définition de l'image, $f(x)$ est un élément de l'image de $f$, c'est-à-dire $f(x) \in \text{Im } f$.
        Par conséquent, $f(x)$ appartient à l'intersection de ces deux sous-espaces : $f(x) \in \ker g \cap \text{Im } f$.
        Par définition de l'image réciproque, si $f(x) \in S$ pour un ensemble $S$, alors $x \in f^{-1}(S)$.
        Donc, $x \in f^{-1}(\ker g \cap \text{Im } f)$.
        Ceci prouve l'inclusion $\ker(g \circ f) \subseteq f^{-1}(\ker g \cap \text{Im } f)$.

        Réciproquement, soit $x \in f^{-1}(\ker g \cap \text{Im } f)$.
        Par définition de l'image réciproque, cela signifie que $f(x) \in \ker g \cap \text{Im } f$.
        Puisque $f(x) \in \ker g$, par définition du noyau, nous avons $g(f(x)) = 0_G$.
        Par définition de la composition, $g(f(x)) = (g \circ f)(x)$.
        Donc, $(g \circ f)(x) = 0_G$, ce qui signifie que $x \in \ker(g \circ f)$.
        Ceci prouve l'inclusion $f^{-1}(\ker g \cap \text{Im } f) \subseteq \ker(g \circ f)$.

        Par double inclusion, nous avons établi l'égalité $\ker(g \circ f) = f^{-1}(\ker g \cap \text{Im } f)$.

    c.  Établissons la relation $\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\ker g \cap \text{Im } f)$.
        Considérons l'application linéaire $f$ restreinte à $\ker(g \circ f)$. Notons cette restriction $f' : \ker(g \circ f) \to F$.
        Le domaine de $f'$ est $\ker(g \circ f)$.
        L'image de $f'$ est $\text{Im } f' = \{ f(x) \mid x \in \ker(g \circ f) \}$.
        D'après la question 1.b, nous savons que $f(x) \in \ker g \cap \text{Im } f$ pour tout $x \in \ker(g \circ f)$.
        Réciproquement, si $y \in \ker g \cap \text{Im } f$, alors $y \in \text{Im } f$, donc il existe $x \in E$ tel que $f(x) = y$. De plus, $y \in \ker g$, donc $g(y) = 0_G$. Ainsi $g(f(x)) = 0_G$, ce qui signifie $x \in \ker(g \circ f)$. Donc $y = f(x)$ est dans l'image de $f'$.
        Par conséquent, $\text{Im } f' = \ker g \cap \text{Im } f$.

        Le noyau de $f'$ est $\ker f' = \{ x \in \ker(g \circ f) \mid f(x) = 0_F \}$.
        Par définition, $f(x) = 0_F$ signifie $x \in \ker f$.
        Donc, $\ker f' = \{ x \mid x \in \ker(g \circ f) \text{ et } x \in \ker f \} = \ker(g \circ f) \cap \ker f$.
        D'après la question 1.a, nous avons montré que $\ker f \subseteq \ker(g \circ f)$.
        Par conséquent, l'intersection $\ker(g \circ f) \cap \ker f$ est simplement $\ker f$.
        Ainsi, $\ker f' = \ker f$.

        Appliquons le théorème du rang à l'application linéaire $f' : \ker(g \circ f) \to F$.
        Le théorème du rang stipule que $\dim(\text{domaine}) = \dim(\text{noyau}) + \dim(\text{image})$.
        Donc, $\dim(\ker(g \circ f)) = \dim(\ker f') + \dim(\text{Im } f')$.
        En substituant les expressions que nous avons trouvées pour $\ker f'$ et $\text{Im } f'$ :
        $$\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\ker g \cap \text{Im } f)$$

    d.  Déduisons que $\dim(\ker(g \circ f)) \le \dim(\ker f) + \dim(\ker g)$.
        Nous savons que $\ker g \cap \text{Im } f$ est un sous-espace vectoriel de $\ker g$.
        Par conséquent, la dimension de l'intersection est inférieure ou égale à la dimension de $\ker g$ :
        $$\dim(\ker g \cap \text{Im } f) \le \dim(\ker g)$$
        En utilisant la relation établie en 1.c :
        $$\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\ker g \cap \text{Im } f)$$
        Puisque $\dim(\ker g \cap \text{Im } f) \le \dim(\ker g)$, nous pouvons remplacer $\dim(\ker g \cap \text{Im } f)$ par une valeur plus grande ou égale, ce qui rend le membre de droite plus grand ou égal :
        $$\dim(\ker(g \circ f)) \le \dim(\ker f) + \dim(\ker g)$$

2.  **Image de la composition :**

    a.  Démontrons que $\text{Im}(g \circ f) \subseteq \text{Im } g$.
        Soit $y \in \text{Im}(g \circ f)$. Par définition, il existe un vecteur $x \in E$ tel que $y = (g \circ f)(x)$.
        Par définition de la composition, $y = g(f(x))$.
        Posons $z = f(x)$. Alors $z$ est un vecteur de $F$.
        Nous avons $y = g(z)$, ce qui signifie que $y$ est l'image d'un élément $z \in F$ par l'application $g$.
        Par conséquent, $y \in \text{Im } g$.
        Ainsi, tout élément de $\text{Im}(g \circ f)$ est aussi un élément de $\text{Im } g$, ce qui prouve l'inclusion $\text{Im}(g \circ f) \subseteq \text{Im } g$.
        Comme $\text{Im}(g \circ f)$ est un sous-espace vectoriel de $\text{Im } g$, sa dimension est inférieure ou égale à celle de $\text{Im } g$.
        Par conséquent, $\text{rg}(g \circ f) \le \text{rg}(g)$.

    b.  Démontrons que $\text{Im}(g \circ f) = g(\text{Im } f)$.
        Soit $y \in \text{Im}(g \circ f)$. Il existe $x \in E$ tel que $y = (g \circ f)(x) = g(f(x))$.
        Puisque $f(x)$ est un élément de l'image de $f$, nous pouvons écrire $f(x) \in \text{Im } f$.
        Donc, $y$ est l'image par $g$ d'un élément de $\text{Im } f$. Par définition, $y \in g(\text{Im } f)$.
        Ceci prouve l'inclusion $\text{Im}(g \circ f) \subseteq g(\text{Im } f)$.

        Réciproquement, soit $y \in g(\text{Im } f)$. Par définition, il existe un vecteur $z \in \text{Im } f$ tel que $y = g(z)$.
        Puisque $z \in \text{Im } f$, par définition de l'image, il existe un vecteur $x \in E$ tel que $z = f(x)$.
        En substituant $z$ dans l'expression de $y$, nous obtenons $y = g(f(x))$.
        Par définition de la composition, $y = (g \circ f)(x)$.
        Donc, $y$ est l'image d'un élément $x \in E$ par $g \circ f$. Par conséquent, $y \in \text{Im}(g \circ f)$.
        Ceci prouve l'inclusion $g(\text{Im } f) \subseteq \text{Im}(g \circ f)$.

        Par double inclusion, nous avons établi l'égalité $\text{Im}(g \circ f) = g(\text{Im } f)$.

    c.  Établissons la relation $\text{rg}(g \circ f) = \text{rg}(f) - \dim(\ker g \cap \text{Im } f)$.
        Considérons l'application linéaire $g$ restreinte à $\text{Im } f$. Notons cette restriction $g' : \text{Im } f \to G$.
        Le domaine de $g'$ est $\text{Im } f$. Sa dimension est $\dim(\text{Im } f) = \text{rg}(f)$.
        L'image de $g'$ est $\text{Im } g' = \{ g(z) \mid z \in \text{Im } f \}$.
        D'après la question 2.b, nous avons montré que $\text{Im } g' = g(\text{Im } f) = \text{Im}(g \circ f)$.
        Le noyau de $g'$ est $\ker g' = \{ z \in \text{Im } f \mid g(z) = 0_G \}$.
        Par définition, ceci est exactement l'intersection de $\ker g$ et $\text{Im } f$.
        Ainsi, $\ker g' = \ker g \cap \text{Im } f$.

        Appliquons le théorème du rang à l'application linéaire $g' : \text{Im } f \to G$.
        Le théorème du rang stipule que $\dim(\text{domaine}) = \dim(\text{noyau}) + \dim(\text{image})$.
        Donc, $\dim(\text{Im } f) = \dim(\ker g') + \dim(\text{Im } g')$.
        En substituant les expressions que nous avons trouvées pour $\dim(\text{Im } f)$, $\ker g'$ et $\text{Im } g'$ :
        $$\text{rg}(f) = \dim(\ker g \cap \text{Im } f) + \text{rg}(g \circ f)$$
        En réarrangeant les termes pour isoler $\text{rg}(g \circ f)$, nous obtenons :
        $$\text{rg}(g \circ f) = \text{rg}(f) - \dim(\ker g \cap \text{Im } f)$$

    d.  Déduisons que $\text{rg}(g \circ f) \le \text{rg}(f)$.
        Nous savons que $\dim(\ker g \cap \text{Im } f)$ est une dimension d'un sous-espace vectoriel, donc elle est toujours supérieure ou égale à zéro :
        $$\dim(\ker g \cap \text{Im } f) \ge 0$$
        En utilisant la relation établie en 2.c :
        $$\text{rg}(g \circ f) = \text{rg}(f) - \dim(\ker g \cap \text{Im } f)$$
        Puisque nous soustrayons une quantité non-négative de $\text{rg}(f)$, il s'ensuit que :
        $$\text{rg}(g \circ f) \le \text{rg}(f)$$

    e.  Démontrons l'inégalité de Sylvester : $\text{rg}(g \circ f) \ge \text{rg}(f) + \text{rg}(g) - \dim F$.
        Nous partons de la relation établie à la question 2.c :
        $$\text{rg}(g \circ f) = \text{rg}(f) - \dim(\ker g \cap \text{Im } f) \quad (*)$$
        Nous savons que $\ker g \cap \text{Im } f$ est un sous-espace vectoriel de $\ker g$.
        Par conséquent, sa dimension est inférieure ou égale à la dimension de $\ker g$ :
        $$\dim(\ker g \cap \text{Im } f) \le \dim(\ker g)$$
        Multiplions cette inégalité par $-1$ et inversons le sens de l'inégalité :
        $$-\dim(\ker g \cap \text{Im } f) \ge -\dim(\ker g)$$
        Ajoutons $\text{rg}(f)$ aux deux membres de l'inégalité :
        $$\text{rg}(f) - \dim(\ker g \cap \text{Im } f) \ge \text{rg}(f) - \dim(\ker g)$$
        Le membre de gauche de cette inégalité est précisément $\text{rg}(g \circ f)$ d'après l'équation $(*)$.
        Le membre de droite peut être simplifié en utilisant le théorème du rang pour l'application linéaire $g : F \to G$.
        Le théorème du rang pour $g$ stipule que $\dim F = \dim(\ker g) + \text{rg}(g)$.
        De cette relation, nous pouvons exprimer $\dim(\ker g)$ comme $\dim(\ker g) = \dim F - \text{rg}(g)$.
        Substituons cette expression de $\dim(\ker g)$ dans le membre de droite de notre inégalité :
        $$\text{rg}(f) - \dim(\ker g) = \text{rg}(f) - (\dim F - \text{rg}(g))$$
        $$\text{rg}(f) - \dim(\ker g) = \text{rg}(f) - \dim F + \text{rg}(g)$$
        En combinant toutes ces étapes, nous obtenons l'inégalité de Sylvester :
        $$\text{rg}(g \circ f) \ge \text{rg}(f) + \text{rg}(g) - \dim F$$