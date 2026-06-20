# Exercice 10 : Noyau et Image d'une Composée d'Applications Linéaires (Difficulté : *****)

**Énoncé**

Soient $\mathbb{K}$ un corps commutatif et $E, F, G$ des $\mathbb{K}$-espaces vectoriels.
Soient $f \in \mathcal{L}(E, F)$ et $g \in \mathcal{L}(F, G)$ deux applications linéaires.
On note $\ker(\cdot)$ le noyau et $\text{Im}(\cdot)$ l'image d'une application linéaire.

1.  Démontrer que $\ker(g \circ f) = f^{-1}(\ker g \cap \text{Im } f)$.
    (Rappel : $f^{-1}(A) = \{x \in E \mid f(x) \in A\}$ pour un sous-ensemble $A \subseteq F$).

2.  Prouver que l'application $\hat{f}: \ker(g \circ f) \to \ker g \cap \text{Im } f$ définie par $\hat{f}(x) = f(x)$ est une application linéaire surjective dont le noyau est $\ker f$. En déduire l'isomorphisme de $\mathbb{K}$-espaces vectoriels : $\ker(g \circ f) / \ker f \cong \ker g \cap \text{Im } f$.

3.  Prouver que l'application $\bar{g}: \text{Im } f / (\ker g \cap \text{Im } f) \to \text{Im}(g \circ f)$ définie par $\bar{g}(y + (\ker g \cap \text{Im } f)) = g(y)$ pour tout $y \in \text{Im } f$ est un isomorphisme de $\mathbb{K}$-espaces vectoriels.
    (On vérifiera d'abord que le sous-espace $\ker g \cap \text{Im } f$ est bien un sous-espace de $\text{Im } f$ et que $\bar{g}$ est bien définie, linéaire et injective/surjective).

4.  On suppose désormais que $E, F, G$ sont des $\mathbb{K}$-espaces vectoriels de dimensions finies. On note $\dim(V)$ la dimension de $V$ et $\text{rang}(h) = \dim(\text{Im } h)$ le rang d'une application linéaire $h$.
    À partir des résultats des questions 2 et 3, établir les égalités suivantes :
    a) $\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\ker g \cap \text{Im } f)$.
    b) $\text{rang}(g \circ f) = \text{rang}(f) - \dim(\ker g \cap \text{Im } f)$.

5.  Utiliser les résultats précédents et le théorème du rang pour $f$ et $g$ pour démontrer l'inégalité de Sylvester :
    $\text{rang}(f) + \text{rang}(g) - \dim(F) \le \text{rang}(g \circ f) \le \min(\text{rang } f, \text{rang } g)$.

## Correction détaillée

1.  **Démonstration de $\ker(g \circ f) = f^{-1}(\ker g \cap \text{Im } f)$**

    Pour prouver l'égalité de deux ensembles, nous allons démontrer l'inclusion dans les deux sens.

    *   **Inclusion $\ker(g \circ f) \subseteq f^{-1}(\ker g \cap \text{Im } f)$** :
        Soit $x \in \ker(g \circ f)$. Par définition du noyau, cela signifie que $(g \circ f)(x) = 0_G$.
        Par définition de la composition, $g(f(x)) = 0_G$.
        Cela implique que $f(x) \in \ker g$.
        Par ailleurs, par définition de l'image, $f(x)$ est un élément de $\text{Im } f$.
        Donc, $f(x)$ appartient à l'intersection $\ker g \cap \text{Im } f$.
        Par définition de l'image réciproque, $x \in f^{-1}(\ker g \cap \text{Im } f)$.
        L'inclusion est démontrée.

    *   **Inclusion $f^{-1}(\ker g \cap \text{Im } f) \subseteq \ker(g \circ f)$** :
        Soit $x \in f^{-1}(\ker g \cap \text{Im } f)$. Par définition de l'image réciproque, cela signifie que $f(x) \in \ker g \cap \text{Im } f$.
        Puisque $f(x) \in \ker g$, par définition du noyau, nous avons $g(f(x)) = 0_G$.
        Par définition de la composition, $(g \circ f)(x) = 0_G$.
        Cela signifie que $x \in \ker(g \circ f)$.
        L'inclusion est démontrée.

    Ayant démontré les deux inclusions, nous concluons que $\ker(g \circ f) = f^{-1}(\ker g \cap \text{Im } f)$.

2.  **Analyse de l'application $\hat{f}$ et isomorphisme de quotient**

    Considérons l'application $\hat{f}: \ker(g \circ f) \to \ker g \cap \text{Im } f$ définie par $\hat{f}(x) = f(x)$.

    *   **$\hat{f}$ est bien définie et linéaire** :
        Le domaine de $\hat{f}$ est $\ker(g \circ f)$, qui est un sous-espace vectoriel de $E$.
        Pour tout $x \in \ker(g \circ f)$, nous avons montré à la question 1 que $f(x) \in \ker g \cap \text{Im } f$. Donc le codomaine est correct.
        L'application $f$ est linéaire, et $\hat{f}$ est simplement la restriction de $f$ à un sous-espace vectoriel, avec un codomaine restreint. Par conséquent, $\hat{f}$ est linéaire.

    *   **$\hat{f}$ est surjective** :
        Soit $y \in \ker g \cap \text{Im } f$. Puisque $y \in \text{Im } f$, il existe un $x \in E$ tel que $f(x) = y$.
        Puisque $y \in \ker g$, nous avons $g(y) = 0_G$.
        Donc, $g(f(x)) = 0_G$, ce qui signifie $(g \circ f)(x) = 0_G$.
        Par conséquent, $x \in \ker(g \circ f)$.
        Nous avons trouvé un élément $x$ dans le domaine de $\hat{f}$ tel que $\hat{f}(x) = f(x) = y$.
        Donc, $\hat{f}$ est surjective sur son codomaine $\ker g \cap \text{Im } f$.

    *   **Détermination du noyau de $\hat{f}$** :
        Par définition, $\ker \hat{f} = \{x \in \ker(g \circ f) \mid \hat{f}(x) = 0_F\}$.
        Cela signifie $\ker \hat{f} = \{x \in \ker(g \circ f) \mid f(x) = 0_F\}$.
        L'ensemble $\{x \in E \mid f(x) = 0_F\}$ est $\ker f$.
        Donc, $\ker \hat{f} = \ker(g \circ f) \cap \ker f$.
        Nous savons que si $x \in \ker f$, alors $f(x) = 0_F$. Par suite, $g(f(x)) = g(0_F) = 0_G$, ce qui implique $x \in \ker(g \circ f)$.
        Ainsi, $\ker f \subseteq \ker(g \circ f)$.
        Par conséquent, l'intersection $\ker(g \circ f) \cap \ker f$ se réduit à $\ker f$.
        Donc, $\ker \hat{f} = \ker f$.

    *   **Application du premier théorème d'isomorphisme** :
        Puisque $\hat{f}: \ker(g \circ f) \to \ker g \cap \text{Im } f$ est une application linéaire surjective de noyau $\ker f$, le premier théorème d'isomorphisme établit que
        $\ker(g \circ f) / \ker f \cong \text{Im}(\hat{f})$.
        Comme $\hat{f}$ est surjective sur son codomaine, $\text{Im}(\hat{f}) = \ker g \cap \text{Im } f$.
        Nous en déduisons l'isomorphisme : $\ker(g \circ f) / \ker f \cong \ker g \cap \text{Im } f$.

3.  **Analyse de l'application $\bar{g}$ et isomorphisme de quotient**

    Considérons l'application $\bar{g}: \text{Im } f / (\ker g \cap \text{Im } f) \to \text{Im}(g \circ f)$ définie par $\bar{g}(y + (\ker g \cap \text{Im } f)) = g(y)$.

    *   **$\ker g \cap \text{Im } f$ est un sous-espace de $\text{Im } f$** :
        $\ker g$ est un sous-espace de $F$ car c'est le noyau d'une application linéaire.
        $\text{Im } f$ est un sous-espace de $F$ car c'est l'image d'une application linéaire.
        L'intersection de deux sous-espaces vectoriels est toujours un sous-espace vectoriel.
        Puisque $\ker g \cap \text{Im } f$ est contenu dans $\text{Im } f$, il est bien un sous-espace de $\text{Im } f$.
        Le quotient $\text{Im } f / (\ker g \cap \text{Im } f)$ est donc bien défini.

    *   **$\bar{g}$ est bien définie** :
        Soient $Y_1 = y_1 + (\ker g \cap \text{Im } f)$ et $Y_2 = y_2 + (\ker g \cap \text{Im } f)$ deux représentants de la même classe dans le quotient.
        Cela signifie que $y_1 - y_2 \in \ker g \cap \text{Im } f$.
        Puisque $y_1 - y_2 \in \ker g$, nous avons $g(y_1 - y_2) = 0_G$.
        Par linéarité de $g$, $g(y_1) - g(y_2) = 0_G$, d'où $g(y_1) = g(y_2)$.
        Ainsi, $\bar{g}(Y_1) = g(y_1) = g(y_2) = \bar{g}(Y_2)$. L'application $\bar{g}$ est donc bien définie.

    *   **$\bar{g}$ est linéaire** :
        Soient $Y_1 = y_1 + (\ker g \cap \text{Im } f)$ et $Y_2 = y_2 + (\ker g \cap \text{Im } f)$ deux éléments du quotient, et $\lambda \in \mathbb{K}$.
        $\bar{g}(Y_1 + Y_2) = \bar{g}((y_1+y_2) + (\ker g \cap \text{Im } f)) = g(y_1+y_2)$.
        Par linéarité de $g$, $g(y_1+y_2) = g(y_1) + g(y_2) = \bar{g}(Y_1) + \bar{g}(Y_2)$.
        $\bar{g}(\lambda Y_1) = \bar{g}(\lambda y_1 + (\ker g \cap \text{Im } f)) = g(\lambda y_1)$.
        Par linéarité de $g$, $g(\lambda y_1) = \lambda g(y_1) = \lambda \bar{g}(Y_1)$.
        L'application $\bar{g}$ est donc linéaire.

    *   **$\bar{g}$ est surjective** :
        Soit $z \in \text{Im}(g \circ f)$. Par définition, il existe $x \in E$ tel que $z = (g \circ f)(x)$.
        Cela signifie $z = g(f(x))$.
        Posons $y = f(x)$. Alors $y \in \text{Im } f$.
        L'élément $y + (\ker g \cap \text{Im } f)$ est un élément du domaine de $\bar{g}$.
        Alors $\bar{g}(y + (\ker g \cap \text{Im } f)) = g(y) = g(f(x)) = z$.
        Donc, pour tout $z \in \text{Im}(g \circ f)$, il existe un antécédent dans le domaine de $\bar{g}$.
        L'application $\bar{g}$ est surjective.

    *   **$\bar{g}$ est injective** :
        Soit $Y = y + (\ker g \cap \text{Im } f)$ un élément du noyau de $\bar{g}$.
        Cela signifie $\bar{g}(Y) = 0_G$, c'est-à-dire $g(y) = 0_G$.
        Puisque $g(y) = 0_G$, $y$ appartient à $\ker g$.
        Par ailleurs, par la définition du domaine du quotient, $y$ appartient à $\text{Im } f$.
        Donc, $y \in \ker g \cap \text{Im } f$.
        Par conséquent, la classe $Y = y + (\ker g \cap \text{Im } f)$ est la classe zéro du quotient, i.e., $Y = \ker g \cap \text{Im } f$.
        Le noyau de $\bar{g}$ est réduit à l'élément neutre du quotient.
        L'application $\bar{g}$ est injective.

    *   **Conclusion** :
        Puisque $\bar{g}$ est linéaire, bien définie, surjective et injective, c'est un isomorphisme de $\mathbb{K}$-espaces vectoriels.
        Ainsi, $\text{Im } f / (\ker g \cap \text{Im } f) \cong \text{Im}(g \circ f)$.

4.  **Application aux dimensions finies**

    Nous supposons $E, F, G$ de dimensions finies.

    a) **Égalité pour le noyau** :
        D'après la question 2, nous avons l'isomorphisme $\ker(g \circ f) / \ker f \cong \ker g \cap \text{Im } f$.
        Pour des espaces vectoriels de dimensions finies, si $V_1 \cong V_2$, alors $\dim(V_1) = \dim(V_2)$.
        De plus, pour un quotient $V/W$, $\dim(V/W) = \dim(V) - \dim(W)$.
        Donc, $\dim(\ker(g \circ f) / \ker f) = \dim(\ker(g \circ f)) - \dim(\ker f)$.
        Par conséquent, $\dim(\ker(g \circ f)) - \dim(\ker f) = \dim(\ker g \cap \text{Im } f)$.
        Ce qui donne l'égalité souhaitée :
        $\dim(\ker(g \circ f)) = \dim(\ker f) + \dim(\ker g \cap \text{Im } f)$.

    b) **Égalité pour l'image (rang)** :
        D'après la question 3, nous avons l'isomorphisme $\text{Im } f / (\ker g \cap \text{Im } f) \cong \text{Im}(g \circ f)$.
        En appliquant le même principe des dimensions finies :
        $\dim(\text{Im } f / (\ker g \cap \text{Im } f)) = \dim(\text{Im } f) - \dim(\ker g \cap \text{Im } f)$.
        Et $\dim(\text{Im}(g \circ f)) = \text{rang}(g \circ f)$.
        De plus, $\dim(\text{Im } f) = \text{rang}(f)$.
        Par conséquent, $\text{rang}(g \circ f) = \text{rang}(f) - \dim(\ker g \cap \text{Im } f)$.

5.  **Démonstration de l'inégalité de Sylvester**

    L'inégalité de Sylvester est de la forme $\text{rang}(f) + \text{rang}(g) - \dim(F) \le \text{rang}(g \circ f) \le \min(\text{rang } f, \text{rang } g)$.
    Nous allons prouver les deux parties de l'inégalité.

    *   **Borne supérieure : $\text{rang}(g \circ f) \le \min(\text{rang } f, \text{rang } g)$** :
        1.  **$\text{rang}(g \circ f) \le \text{rang}(f)$** :
            D'après la question 4b, $\text{rang}(g \circ f) = \text{rang}(f) - \dim(\ker g \cap \text{Im } f)$.
            Comme $\ker g \cap \text{Im } f$ est un sous-espace vectoriel, sa dimension est non-négative : $\dim(\ker g \cap \text{Im } f) \ge 0$.
            Par conséquent, $\text{rang}(g \circ f) \le \text{rang}(f)$.
            On peut aussi observer que $\text{Im}(g \circ f) = g(\text{Im } f)$. L'image d'un sous-espace par une application linéaire a une dimension inférieure ou égale à la dimension de ce sous-espace. Ainsi, $\dim(g(\text{Im } f)) \le \dim(\text{Im } f)$, ce qui signifie $\text{rang}(g \circ f) \le \text{rang}(f)$.

        2.  **$\text{rang}(g \circ f) \le \text{rang}(g)$** :
            Comme précédemment, $\text{Im}(g \circ f) = g(\text{Im } f)$.
            Puisque $\text{Im } f \subseteq F$, tout vecteur dans $g(\text{Im } f)$ est aussi un vecteur dans $g(F)$, c'est-à-dire dans $\text{Im } g$.
            Donc $\text{Im}(g \circ f)$ est un sous-espace de $\text{Im } g$.
            Par conséquent, $\dim(\text{Im}(g \circ f)) \le \dim(\text{Im } g)$, ce qui signifie $\text{rang}(g \circ f) \le \text{rang}(g)$.

        Ces deux inégalités prouvent que $\text{rang}(g \circ f) \le \min(\text{rang } f, \text{rang } g)$.

    *   **Borne inférieure : $\text{rang}(f) + \text{rang}(g) - \dim(F) \le \text{rang}(g \circ f)$** :
        D'après la question 4b, nous avons $\text{rang}(g \circ f) = \text{rang}(f) - \dim(\ker g \cap \text{Im } f)$.
        Nous devons maintenant borner $\dim(\ker g \cap \text{Im } f)$.
        Le sous-espace $\ker g \cap \text{Im } f$ est un sous-espace de $\ker g$.
        Donc, $\dim(\ker g \cap \text{Im } f) \le \dim(\ker g)$.
        En utilisant cette inégalité dans l'expression de $\text{rang}(g \circ f)$ :
        $\text{rang}(g \circ f) \ge \text{rang}(f) - \dim(\ker g)$.

        Maintenant, nous utilisons le théorème du rang pour l'application linéaire $g: F \to G$.
        Le théorème du rang stipule que $\dim(F) = \dim(\ker g) + \dim(\text{Im } g)$.
        Puisque $\dim(\text{Im } g) = \text{rang}(g)$, nous avons $\dim(F) = \dim(\ker g) + \text{rang}(g)$.
        D'où $\dim(\ker g) = \dim(F) - \text{rang}(g)$.

        Substituons cette expression de $\dim(\ker g)$ dans l'inégalité pour $\text{rang}(g \circ f)$ :
        $\text{rang}(g \circ f) \ge \text{rang}(f) - (\dim(F) - \text{rang}(g))$.
        En réarrangeant les termes, nous obtenons :
        $\text{rang}(g \circ f) \ge \text{rang}(f) + \text{rang}(g) - \dim(F)$.

    Nous avons ainsi démontré les deux parties de l'inégalité de Sylvester.