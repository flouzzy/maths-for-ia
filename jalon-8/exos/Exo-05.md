# Exercice 5 : Noyau, Image et Rang de la composition d'applications linéaires (Difficulté : ***)

**Énoncé du Problème**

Soient $K$ un corps commutatif. Soient $E, F, G$ trois $K$-espaces vectoriels de dimensions finies.
Soient $f: E \to F$ et $g: F \to G$ deux applications linéaires.

1.  Démontrer que $\ker(f) \subseteq \ker(g \circ f)$ et que $\text{Im}(g \circ f) \subseteq \text{Im}(g)$.
2.  On considère l'application linéaire restreinte $g_f: \text{Im}(f) \to G$ définie par $g_f(y) = g(y)$ pour tout $y \in \text{Im}(f)$.
    a) Démontrer que $\ker(g_f) = \text{Im}(f) \cap \ker(g)$.
    b) Démontrer que $\text{Im}(g_f) = \text{Im}(g \circ f)$.
3.  En utilisant le théorème du rang pour l'application $g_f$ et l'application $f$, établir la relation suivante :
    $$ \dim(\ker(g \circ f)) = \dim(\ker(f)) + \dim(\text{Im}(f) \cap \ker(g)) $$
4.  En déduire la relation liant les rangs des applications linéaires :
    $$ \text{rg}(g \circ f) = \text{rg}(f) - \dim(\text{Im}(f) \cap \ker(g)) $$

---

## Correction détaillée

1.  **Démonstration de $\ker(f) \subseteq \ker(g \circ f)$ et $\text{Im}(g \circ f) \subseteq \text{Im}(g)$**

    *   **Pour $\ker(f) \subseteq \ker(g \circ f)$ :**
        Soit $x \in \ker(f)$. Par définition du noyau, cela signifie que $f(x) = 0_F$, où $0_F$ est le vecteur nul de $F$.
        Appliquons l'application $g$ à $f(x)$ :
        $(g \circ f)(x) = g(f(x)) = g(0_F)$.
        Puisque $g$ est une application linéaire, elle envoie le vecteur nul sur le vecteur nul : $g(0_F) = 0_G$.
        Ainsi, $(g \circ f)(x) = 0_G$.
        Par définition du noyau, $x \in \ker(g \circ f)$.
        Donc, tout élément de $\ker(f)$ est aussi un élément de $\ker(g \circ f)$, ce qui prouve $\ker(f) \subseteq \ker(g \circ f)$.

    *   **Pour $\text{Im}(g \circ f) \subseteq \text{Im}(g)$ :**
        Soit $z \in \text{Im}(g \circ f)$. Par définition de l'image, cela signifie qu'il existe un vecteur $x \in E$ tel que $z = (g \circ f)(x)$.
        On peut réécrire $z = g(f(x))$.
        Posons $y = f(x)$. Alors, par définition de l'image de $f$, $y \in \text{Im}(f)$.
        Nous avons $z = g(y)$.
        Puisque $y \in F$ et $z = g(y)$, par définition de l'image de $g$, $z \in \text{Im}(g)$.
        Donc, tout élément de $\text{Im}(g \circ f)$ est aussi un élément de $\text{Im}(g)$, ce qui prouve $\text{Im}(g \circ f) \subseteq \text{Im}(g)$.

2.  **Propriétés de l'application linéaire restreinte $g_f$**

    L'application $g_f: \text{Im}(f) \to G$ est définie par $g_f(y) = g(y)$ pour tout $y \in \text{Im}(f)$.
    Il est important de noter que $\text{Im}(f)$ est un sous-espace vectoriel de $F$, et $g_f$ est la restriction de $g$ à ce sous-espace.

    a) **Démonstration de $\ker(g_f) = \text{Im}(f) \cap \ker(g)$**

        *   **Inclusion $\subseteq$ :**
            Soit $y \in \ker(g_f)$. Par définition du noyau de $g_f$, cela signifie que $y \in \text{Im}(f)$ et $g_f(y) = 0_G$.
            Par définition de $g_f$, on a $g_f(y) = g(y)$. Donc, $g(y) = 0_G$.
            Puisque $g(y) = 0_G$, par définition du noyau de $g$, on a $y \in \ker(g)$.
            Ainsi, $y$ appartient à la fois à $\text{Im}(f)$ et à $\ker(g)$. Donc $y \in \text{Im}(f) \cap \ker(g)$.
            Ceci prouve $\ker(g_f) \subseteq \text{Im}(f) \cap \ker(g)$.

        *   **Inclusion $\supseteq$ :**
            Soit $y \in \text{Im}(f) \cap \ker(g)$. Par définition de l'intersection, cela signifie que $y \in \text{Im}(f)$ et $y \in \ker(g)$.
            Puisque $y \in \text{Im}(f)$, l'application $g_f(y)$ est bien définie.
            Puisque $y \in \ker(g)$, par définition du noyau de $g$, on a $g(y) = 0_G$.
            Par définition de $g_f$, on a $g_f(y) = g(y)$. Donc, $g_f(y) = 0_G$.
            Ainsi, $y \in \ker(g_f)$.
            Ceci prouve $\text{Im}(f) \cap \ker(g) \subseteq \ker(g_f)$.

        Les deux inclusions étant établies, on conclut que $\ker(g_f) = \text{Im}(f) \cap \ker(g)$.

    b) **Démonstration de $\text{Im}(g_f) = \text{Im}(g \circ f)$**

        *   **Inclusion $\subseteq$ :**
            Soit $z \in \text{Im}(g_f)$. Par définition de l'image de $g_f$, cela signifie qu'il existe un vecteur $y \in \text{Im}(f)$ tel que $z = g_f(y)$.
            Par définition de $g_f$, on a $z = g(y)$.
            Puisque $y \in \text{Im}(f)$, par définition de l'image de $f$, il existe un vecteur $x \in E$ tel que $y = f(x)$.
            En substituant $y$, nous obtenons $z = g(f(x))$.
            Par définition de la composition d'applications, $z = (g \circ f)(x)$.
            Puisque $x \in E$ et $z = (g \circ f)(x)$, par définition de l'image de $g \circ f$, on a $z \in \text{Im}(g \circ f)$.
            Ceci prouve $\text{Im}(g_f) \subseteq \text{Im}(g \circ f)$.

        *   **Inclusion $\supseteq$ :**
            Soit $z \in \text{Im}(g \circ f)$. Par définition de l'image de $g \circ f$, cela signifie qu'il existe un vecteur $x \in E$ tel que $z = (g \circ f)(x)$.
            On peut réécrire $z = g(f(x))$.
            Posons $y = f(x)$. Alors, par définition de l'image de $f$, $y \in \text{Im}(f)$.
            Puisque $y \in \text{Im}(f)$, l'application $g_f(y)$ est bien définie, et par définition $g_f(y) = g(y)$.
            Ainsi, $z = g(f(x)) = g(y) = g_f(y)$.
            Puisque $y \in \text{Im}(f)$ et $z = g_f(y)$, par définition de l'image de $g_f$, on a $z \in \text{Im}(g_f)$.
            Ceci prouve $\text{Im}(g \circ f) \subseteq \text{Im}(g_f)$.

        Les deux inclusions étant établies, on conclut que $\text{Im}(g_f) = \text{Im}(g \circ f)$.

3.  **Établissement de la relation $\dim(\ker(g \circ f)) = \dim(\ker(f)) + \dim(\text{Im}(f) \cap \ker(g))$**

    Nous allons appliquer le théorème du rang aux applications linéaires $f$ et $g_f$.

    *   **Théorème du rang pour $g_f: \text{Im}(f) \to G$ :**
        Puisque $\text{Im}(f)$ est un sous-espace vectoriel de $F$ et est de dimension finie (car $F$ est de dimension finie), le théorème du rang s'applique à $g_f$.
        $$ \dim(\text{Im}(f)) = \dim(\ker(g_f)) + \dim(\text{Im}(g_f)) $$
        En utilisant les résultats de la question 2a) et 2b) :
        $$ \dim(\text{Im}(f)) = \dim(\text{Im}(f) \cap \ker(g)) + \dim(\text{Im}(g \circ f)) \quad (*)$$

    *   **Théorème du rang pour $f: E \to F$ :**
        $$ \dim(E) = \dim(\ker(f)) + \dim(\text{Im}(f)) $$
        On peut exprimer $\dim(\text{Im}(f))$ comme :
        $$ \dim(\text{Im}(f)) = \dim(E) - \dim(\ker(f)) \quad (**) $$

    *   **Théorème du rang pour $g \circ f: E \to G$ :**
        $$ \dim(E) = \dim(\ker(g \circ f)) + \dim(\text{Im}(g \circ f)) $$
        On peut exprimer $\dim(\text{Im}(g \circ f))$ comme :
        $$ \dim(\text{Im}(g \circ f)) = \dim(E) - \dim(\ker(g \circ f)) \quad (***) $$

    Substituons $(**)$ et $(***)$ dans l'équation $(*)$ :
    $$ (\dim(E) - \dim(\ker(f))) = \dim(\text{Im}(f) \cap \ker(g)) + (\dim(E) - \dim(\ker(g \circ f))) $$
    Simplifions en soustrayant $\dim(E)$ des deux côtés :
    $$ -\dim(\ker(f)) = \dim(\text{Im}(f) \cap \ker(g)) - \dim(\ker(g \circ f)) $$
    Réarrangeons les termes pour isoler $\dim(\ker(g \circ f))$ :
    $$ \dim(\ker(g \circ f)) = \dim(\ker(f)) + \dim(\text{Im}(f) \cap \ker(g)) $$
    Ceci établit la relation demandée.

4.  **Déduction de la relation $\text{rg}(g \circ f) = \text{rg}(f) - \dim(\text{Im}(f) \cap \ker(g))$**

    Par définition, le rang d'une application linéaire est la dimension de son image.
    Donc $\text{rg}(f) = \dim(\text{Im}(f))$ et $\text{rg}(g \circ f) = \dim(\text{Im}(g \circ f))$.

    Reprenons l'équation $(*)$ établie à la question 3 :
    $$ \dim(\text{Im}(f)) = \dim(\text{Im}(f) \cap \ker(g)) + \dim(\text{Im}(g \circ f)) $$
    En substituant les termes par leurs rangs correspondants :
    $$ \text{rg}(f) = \dim(\text{Im}(f) \cap \ker(g)) + \text{rg}(g \circ f) $$
    Pour obtenir la relation souhaitée, il suffit de réarranger les termes :
    $$ \text{rg}(g \circ f) = \text{rg}(f) - \dim(\text{Im}(f) \cap \ker(g)) $$
    Ceci conclut la déduction.