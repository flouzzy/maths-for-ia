# Exercice 1 : Vérification d'une relation d'équivalence sur les nombres réels
**Difficulté :** ⭐

## Énoncé
Soit l'ensemble des nombres réels $\mathbb{R}$. On définit sur $\mathbb{R}$ une relation $\mathcal{R}$ de la manière suivante :
Pour tout $x, y \in \mathbb{R}$, $x \mathcal{R} y$ si et seulement si $|x| = |y|$.

Démontrez que $\mathcal{R}$ est une relation d'équivalence sur $\mathbb{R}$.

## Correction Détaillée
Pour démontrer qu'une relation $\mathcal{R}$ est une relation d'équivalence sur un ensemble $E$, nous devons vérifier qu'elle possède les trois propriétés fondamentales suivantes : la réflexivité, la symétrie et la transitivité.

### 1. Propriété de Réflexivité
Une relation $\mathcal{R}$ est réflexive si, pour tout élément $x$ de l'ensemble $E$, $x \mathcal{R} x$.

*   **Hypothèse :** Considérons un nombre réel arbitraire $x \in \mathbb{R}$.
*   **Objectif :** Nous devons vérifier si l'affirmation $x \mathcal{R} x$ est vraie pour tout $x \in \mathbb{R}$.
*   **Application de la définition de $\mathcal{R}$ :** Conformément à la définition de la relation $\mathcal{R}$, l'expression $x \mathcal{R} x$ signifie que la valeur absolue de $x$ est égale à la valeur absolue de $x$.
    $$ |x| = |x| $$
*   **Justification de l'égalité :** La propriété d'égalité réflexive stipule que toute quantité est égale à elle-même. Par conséquent, l'égalité $|x| = |x|$ est une affirmation intrinsèquement vraie pour tout nombre réel $x$.
*   **Conclusion :** Puisque l'égalité $|x| = |x|$ est toujours vérifiée pour tout $x \in \mathbb{R}$, nous pouvons affirmer que la relation $\mathcal{R}$ est réflexive sur $\mathbb{R}$.
    $$ \forall x \in \mathbb{R}, \quad |x| = |x| \implies x \mathcal{R} x $$

### 2. Propriété de Symétrie
Une relation $\mathcal{R}$ est symétrique si, pour tout couple d'éléments $(x, y)$ de l'ensemble $E$, si $x \mathcal{R} y$ est vraie, alors $y \mathcal{R} x$ doit également être vraie.

*   **Hypothèse :** Soient deux nombres réels arbitraires $x, y \in \mathbb{R}$. Supposons que la relation $x \mathcal{R} y$ est vraie.
*   **Objectif :** Nous devons démontrer que, sous cette hypothèse, la relation $y \mathcal{R} x$ est nécessairement vraie.
*   **Traduction de l'hypothèse selon la définition de $\mathcal{R}$ :** L'hypothèse $x \mathcal{R} y$ signifie, par définition de la relation $\mathcal{R}$, que la valeur absolue de $x$ est égale à la valeur absolue de $y$.
    $$ |x| = |y| $$
*   **Justification de la symétrie de l'égalité :** L'égalité mathématique est une relation symétrique. Cela signifie que si une quantité $A$ est égale à une quantité $B$, alors la quantité $B$ est aussi égale à la quantité $A$. Par conséquent, si nous avons $|x| = |y|$, il s'ensuit logiquement que $|y| = |x|$.
    $$ \text{Si } |x| = |y|, \text{ alors } |y| = |x| $$
*   **Traduction de la conclusion selon la définition de $\mathcal{R}$ :** L'expression $|y| = |x|$ signifie, par définition de la relation $\mathcal{R}$, que $y \mathcal{R} x$.
*   **Conclusion :** Ayant démontré que l'hypothèse $x \mathcal{R} y$ implique la conclusion $y \mathcal{R} x$, nous pouvons affirmer que la relation $\mathcal{R}$ est symétrique sur $\mathbb{R}$.
    $$ \forall x, y \in \mathbb{R}, \quad (x \mathcal{R} y \implies y \mathcal{R} x) $$

### 3. Propriété de Transitivité
Une relation $\mathcal{R}$ est transitive si, pour tout triplet d'éléments $(x, y, z)$ de l'ensemble $E$, si $x \mathcal{R} y$ est vraie ET $y \mathcal{R} z$ est vraie, alors $x \mathcal{R} z$ doit également être vraie.

*   **Hypothèse :** Soient trois nombres réels arbitraires $x, y, z \in \mathbb{R}$. Supposons que la relation $x \mathcal{R} y$ est vraie ET que la relation $y \mathcal{R} z$ est vraie.
*   **Objectif :** Nous devons démontrer que, sous ces hypothèses, la relation $x \mathcal{R} z$ est nécessairement vraie.
*   **Traduction des hypothèses selon la définition de $\mathcal{R}$ :**
    *   L'hypothèse $x \mathcal{R} y$ signifie, par définition de la relation $\mathcal{R}$, que la valeur absolue de $x$ est égale à la valeur absolue de $y$.
        $$ |x| = |y| \quad (1) $$
    *   L'hypothèse $y \mathcal{R} z$ signifie, par définition de la relation $\mathcal{R}$, que la valeur absolue de $y$ est égale à la valeur absolue de $z$.
        $$ |y| = |z| \quad (2) $$
*   **Combinaison des égalités :** À partir des équations (1) et (2), nous avons la suite d'égalités : $|x| = |y|$ et $|y| = |z|$.
*   **Justification de la transitivité de l'égalité :** L'égalité mathématique est une relation transitive. Cela signifie que si une quantité $A$ est égale à une quantité $B$, et que cette quantité $B$ est égale à une quantité $C$, alors la quantité $A$ est aussi égale à la quantité $C$. En appliquant la transitivité de l'égalité à nos expressions, nous déduisons de $|x| = |y|$ et $|y| = |z|$ que $|x| = |z|$.
    $$ \text{Si } |x| = |y| \text{ et } |y| = |z|, \text{ alors } |x| = |z| $$
*   **Traduction de la conclusion selon la définition de $\mathcal{R}$ :** L'expression $|x| = |z|$ signifie, par définition de la relation $\mathcal{R}$, que $x \mathcal{R} z$.
*   **Conclusion :** Ayant démontré que les hypothèses $x \mathcal{R} y$ et $y \mathcal{R} z$ impliquent la conclusion $x \mathcal{R} z$, nous pouvons affirmer que la relation $\mathcal{R}$ est transitive sur $\mathbb{R}$.
    $$ \forall x, y, z \in \mathbb{R}, \quad ((x \mathcal{R} y \land y \mathcal{R} z) \implies x \mathcal{R} z) $$

### Conclusion Générale
La relation $\mathcal{R}$ définie sur l'ensemble des nombres réels $\mathbb{R}$ a été démontrée comme étant réflexive, symétrique et transitive. Puisqu'elle satisfait ces trois propriétés, nous pouvons conclure que $\mathcal{R}$ est une relation d'équivalence sur $\mathbb{R}$.