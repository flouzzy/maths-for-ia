Mes chers étudiants,

Nous poursuivons notre exploration des fondements mathématiques cruciaux pour la conception de systèmes d'intelligence artificielle, en particulier les moteurs de recherche sémantique. Le Jalon 12 nous invite à une réflexion approfondie sur la dualité et la géométrie des espaces de plongement, des concepts absolument centraux pour comprendre comment les vecteurs peuvent représenter des entités sémantiques et comment leurs relations sont mesurées.

Aujourd'hui, nous allons aborder la dualité dans les espaces euclidiens et l'impact des transformations linéaires sur la notion de similarité, en lien direct avec l'isomorphisme de Riesz. Préparez-vous à une exploration rigoureuse.

---

## Exercice 3 : Dualité, Isomorphisme de Riesz et Transformation Linéaire en Espaces de Plongement Sémantique

**Niveau de difficulté :** $\star \star \text{ (Intermédiaire)}$

### Contexte

Dans le domaine du traitement du langage naturel et de la recherche sémantique, les entités (mots, phrases, documents) sont souvent représentées comme des vecteurs dans des espaces de grande dimension, appelés *espaces de plongement* (embedding spaces). La similarité entre ces entités est fréquemment mesurée par la similarité cosinus entre leurs vecteurs représentatifs. Ce concept repose sur la géométrie euclidienne de l'espace vectoriel. Cependant, les requêtes ou les "filtres" peuvent être naturellement modélisés comme des *fonctionnelles linéaires* qui évaluent les documents. La dualité entre les vecteurs et les fonctionnelles linéaires, médiatisée par l'isomorphisme de Riesz, est fondamentale pour relier ces deux perspectives. De plus, des transformations linéaires sont souvent appliquées aux plongements pour affiner leur sémantique, réduire leur dimensionnalité ou les adapter à des tâches spécifiques.

### Hypothèses

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace vectoriel euclidien réel de dimension finie $n \in \mathbb{N}^*$.
Nous noterons $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ la norme euclidienne associée au produit scalaire pour tout $\mathbf{v} \in E$.
Soit $E^*$ l'espace dual de $E$, c'est-à-dire l'ensemble de toutes les formes linéaires de $E$ vers $\mathbb{R}$. Un élément $f \in E^*$ est une application linéaire $f: E \to \mathbb{R}$.
Soit $L: E \to E$ une application linéaire.

### Énoncé

1.  **L'Isomorphisme de Riesz : Définition et Propriétés Fondamentales**
    Pour tout $f \in E^*$, démontrez qu'il existe un unique vecteur $\mathbf{u}_f \in E$ tel que pour tout $\mathbf{v} \in E$, $f(\mathbf{v}) = \langle \mathbf{u}_f, \mathbf{v} \rangle$.
    Nous définissons l'application $\mathcal{R}: E^* \to E$ par $\mathcal{R}(f) = \mathbf{u}_f$.
    Prouvez que $\mathcal{R}$ est un isomorphisme d'espaces vectoriels. Détaillez la preuve de sa linéarité, injectivité et surjectivité.

2.  **Définition de la Similarité Cosinus dans l'Espace Dual**
    Étant donné deux fonctionnelles linéaires non nulles $f_1, f_2 \in E^*$, proposez une définition rigoureuse de leur "similarité cosinus" en vous basant sur l'isomorphisme de Riesz. Justifiez cette définition par une interprétation géométrique.

3.  **Action d'une Transformation Linéaire sur les Fonctionnelles**
    Soit $L: E \to E$ une application linéaire et $f \in E^*$. Nous définissons la composition $f \circ L: E \to \mathbb{R}$ par $(f \circ L)(\mathbf{v}) = f(L(\mathbf{v}))$ pour tout $\mathbf{v} \in E$.
    Prouvez que $f \circ L$ est une fonctionnelle linéaire, i.e., $f \circ L \in E^*$.
    Exprimez le représentant de Riesz de $f \circ L$, c'est-à-dire $\mathcal{R}(f \circ L)$, en fonction de $\mathcal{R}(f)$ et de l'opérateur adjoint de $L$.

4.  **Impact d'une Transformation sur la Similarité des Fonctionnelles**
    Soient $f_1, f_2 \in E^*$ deux fonctionnelles linéaires non nulles.
    Comparez la similarité cosinus de $f_1, f_2$ avec celle de $f_1 \circ L, f_2 \circ L$.
    Considérez le cas particulier où $L$ est un projecteur orthogonal sur un sous-espace vectoriel $W \subset E$. Analysez dans quelles conditions la similarité est préservée ou modifiée.

5.  **Relation entre l'Adjoint et l'Isomorphisme de Riesz**
    Rappelez la définition de l'opérateur adjoint $L^T: E \to E$ de $L$.
    Démontrez formellement la relation suivante : $\mathcal{R}(f \circ L) = L^T(\mathcal{R}(f))$ pour tout $f \in E^*$.

---

### Correction Détaillée

1.  **L'Isomorphisme de Riesz : Définition et Propriétés Fondamentales**

    *   **Existence et Unicité du Vecteur $\mathbf{u}_f$ :**
        Soit $f \in E^*$.
        *   **Existence :** Si $f$ est la fonctionnelle nulle (i.e., $f(\mathbf{v}) = 0$ pour tout $\mathbf{v} \in E$), alors le vecteur $\mathbf{u}_f = \mathbf{0}_E$ (vecteur nul de $E$) satisfait $f(\mathbf{v}) = \langle \mathbf{0}_E, \mathbf{v} \rangle = 0$.
        *   Si $f$ n'est pas la fonctionnelle nulle, alors $\text{ker}(f) = \{\mathbf{v} \in E \mid f(\mathbf{v}) = 0\}$ est un sous-espace vectoriel de $E$ de dimension $n-1$ (un hyperplan). Il existe donc un vecteur non nul $\mathbf{w} \in E$ tel que $\mathbf{w} \notin \text{ker}(f)$. L'orthogonal de $\text{ker}(f)$, noté $(\text{ker}(f))^{\perp}$, est une droite vectorielle de dimension 1. Soit $\mathbf{u}_0$ un vecteur unitaire qui engendre cette droite. Pour tout $\mathbf{v} \in E$, $\mathbf{v}$ peut s'écrire de manière unique comme $\mathbf{v} = \mathbf{v}_k + \alpha \mathbf{u}_0$ avec $\mathbf{v}_k \in \text{ker}(f)$ et $\alpha \in \mathbb{R}$.
        Alors $f(\mathbf{v}) = f(\mathbf{v}_k + \alpha \mathbf{u}_0) = f(\mathbf{v}_k) + \alpha f(\mathbf{u}_0) = 0 + \alpha f(\mathbf{u}_0) = \alpha f(\mathbf{u}_0)$.
        Par ailleurs, $\langle \mathbf{u}_0, \mathbf{v} \rangle = \langle \mathbf{u}_0, \mathbf{v}_k + \alpha \mathbf{u}_0 \rangle = \langle \mathbf{u}_0, \mathbf{v}_k \rangle + \alpha \langle \mathbf{u}_0, \mathbf{u}_0 \rangle = 0 + \alpha \|\mathbf{u}_0\|^2 = \alpha$.
        Ainsi, $f(\mathbf{v}) = f(\mathbf{u}_0) \langle \mathbf{u}_0, \mathbf{v} \rangle = \langle f(\mathbf{u}_0) \mathbf{u}_0, \mathbf{v} \rangle$.
        Nous posons $\mathbf{u}_f = f(\mathbf{u}_0) \mathbf{u}_0$. Ce vecteur satisfait la condition d'existence.
        *   **Unicité :** Supposons qu'il existe deux vecteurs $\mathbf{u}_f$ et $\mathbf{u}'_f$ tels que pour tout $\mathbf{v} \in E$, $f(\mathbf{v}) = \langle \mathbf{u}_f, \mathbf{v} \rangle$ et $f(\mathbf{v}) = \langle \mathbf{u}'_f, \mathbf{v} \rangle$.
        Alors pour tout $\mathbf{v} \in E$, $\langle \mathbf{u}_f, \mathbf{v} \rangle = \langle \mathbf{u}'_f, \mathbf{v} \rangle$.
        Ceci implique $\langle \mathbf{u}_f - \mathbf{u}'_f, \mathbf{v} \rangle = 0$ pour tout $\mathbf{v} \in E$.
        En prenant $\mathbf{v} = \mathbf{u}_f - \mathbf{u}'_f$, nous obtenons $\langle \mathbf{u}_f - \mathbf{u}'_f, \mathbf{u}_f - \mathbf{u}'_f \rangle = 0$, ce qui signifie $\|\mathbf{u}_f - \mathbf{u}'_f\|^2 = 0$.
        Par conséquent, $\mathbf{u}_f - \mathbf{u}'_f = \mathbf{0}_E$, d'où $\mathbf{u}_f = \mathbf{u}'_f$. L'unicité est prouvée.

    *   **Preuve que $\mathcal{R}$ est un isomorphisme :**
        L'application $\mathcal{R}: E^* \to E$ est définie par $\mathcal{R}(f) = \mathbf{u}_f$.

        *   **Linéarité :** Soient $f_1, f_2 \in E^*$ et $\alpha, \beta \in \mathbb{R}$.
            Nous voulons montrer que $\mathcal{R}(\alpha f_1 + \beta f_2) = \alpha \mathcal{R}(f_1) + \beta \mathcal{R}(f_2)$.
            Par définition de $\mathcal{R}$, pour tout $\mathbf{v} \in E$:
            $(\alpha f_1 + \beta f_2)(\mathbf{v}) = \langle \mathcal{R}(\alpha f_1 + \beta f_2), \mathbf{v} \rangle$.
            Par ailleurs, par linéarité des fonctionnelles et du produit scalaire :
            $(\alpha f_1 + \beta f_2)(\mathbf{v}) = \alpha f_1(\mathbf{v}) + \beta f_2(\mathbf{v})$
            $= \alpha \langle \mathcal{R}(f_1), \mathbf{v} \rangle + \beta \langle \mathcal{R}(f_2), \mathbf{v} \rangle$
            $= \langle \alpha \mathcal{R}(f_1), \mathbf{v} \rangle + \langle \beta \mathcal{R}(f_2), \mathbf{v} \rangle$
            $= \langle \alpha \mathcal{R}(f_1) + \beta \mathcal{R}(f_2), \mathbf{v} \rangle$.
            En égalant les deux expressions pour $(\alpha f_1 + \beta f_2)(\mathbf{v})$ :
            $\langle \mathcal{R}(\alpha f_1 + \beta f_2), \mathbf{v} \rangle = \langle \alpha \mathcal{R}(f_1) + \beta \mathcal{R}(f_2), \mathbf{v} \rangle$ pour tout $\mathbf{v} \in E$.
            Par l'unicité du vecteur de Riesz (démontrée ci-dessus), nous en déduisons :
            $\mathcal{R}(\alpha f_1 + \beta f_2) = \alpha \mathcal{R}(f_1) + \beta \mathcal{R}(f_2)$.
            L'application $\mathcal{R}$ est linéaire.

        *   **Injectivité :** Nous devons montrer que si $\mathcal{R}(f) = \mathbf{0}_E$, alors $f$ est la fonctionnelle nulle.
            Si $\mathcal{R}(f) = \mathbf{0}_E$, alors par définition de $\mathcal{R}$, le vecteur $\mathbf{u}_f$ associé à $f$ est $\mathbf{0}_E$.
            Ainsi, pour tout $\mathbf{v} \in E$, $f(\mathbf{v}) = \langle \mathbf{u}_f, \mathbf{v} \rangle = \langle \mathbf{0}_E, \mathbf{v} \rangle = 0$.
            Ceci signifie que $f$ est la fonctionnelle nulle.
            Par conséquent, $\text{ker}(\mathcal{R}) = \{f_0\}$, où $f_0$ est la fonctionnelle nulle. L'application $\mathcal{R}$ est injective.

        *   **Surjectivité :** Nous devons montrer que pour tout $\mathbf{u} \in E$, il existe une fonctionnelle $f \in E^*$ telle que $\mathcal{R}(f) = \mathbf{u}$.
            Soit $\mathbf{u} \in E$. Définissons une application $f_{\mathbf{u}}: E \to \mathbb{R}$ par $f_{\mathbf{u}}(\mathbf{v}) = \langle \mathbf{u}, \mathbf{v} \rangle$ pour tout $\mathbf{v} \in E$.
            *   $f_{\mathbf{u}}$ est linéaire : Pour $\mathbf{v}_1, \mathbf{v}_2 \in E$ et $\alpha, \beta \in \mathbb{R}$,
                $f_{\mathbf{u}}(\alpha \mathbf{v}_1 + \beta \mathbf{v}_2) = \langle \mathbf{u}, \alpha \mathbf{v}_1 + \beta \mathbf{v}_2 \rangle = \alpha \langle \mathbf{u}, \mathbf{v}_1 \rangle + \beta \langle \mathbf{u}, \mathbf{v}_2 \rangle = \alpha f_{\mathbf{u}}(\mathbf{v}_1) + \beta f_{\mathbf{u}}(\mathbf{v}_2)$.
                Donc $f_{\mathbf{u}} \in E^*$.
            *   Par la définition de $\mathcal{R}$, le vecteur de Riesz associé à $f_{\mathbf{u}}$ est $\mathbf{u}$ lui-même. C'est-à-dire $\mathcal{R}(f_{\mathbf{u}}) = \mathbf{u}$.
            Ainsi, chaque vecteur de $E$ est l'image d'au moins une fonctionnelle de $E^*$. L'application $\mathcal{R}$ est surjective.

        Puisque $\mathcal{R}$ est linéaire, injective et surjective, c'est un isomorphisme d'espaces vectoriels.

2.  **Définition de la Similarité Cosinus dans l'Espace Dual**

    *   **Définition :** Soient $f_1, f_2 \in E^*$ deux fonctionnelles linéaires non nulles. Leur similarité cosinus, notée $\text{sim}(f_1, f_2)$, est définie par :
        $$ \text{sim}(f_1, f_2) = \frac{\langle \mathcal{R}(f_1), \mathcal{R}(f_2) \rangle}{\|\mathcal{R}(f_1)\| \cdot \|\mathcal{R}(f_2)\|} $$
        où $\mathcal{R}(f_1)$ et $\mathcal{R}(f_2)$ sont les représentants de Riesz de $f_1$ et $f_2$ respectivement. Puisque $f_1$ et $f_2$ sont non nulles, leurs représentants de Riesz $\mathcal{R}(f_1)$ et $\mathcal{R}(f_2)$ sont également non nuls (par injectivité de $\mathcal{R}$), et leurs normes sont donc strictement positives.

    *   **Justification et Interprétation Géométrique :**
        L'isomorphisme de Riesz $\mathcal{R}: E^* \to E$ établit une correspondance bijective et linéaire entre l'espace dual $E^*$ et l'espace euclidien $E$. Cela signifie que $E^*$ "hérite" de la structure euclidienne de $E$ via $\mathcal{R}$. Chaque fonctionnelle $f \in E^*$ peut être identifiée de manière unique à un vecteur $\mathbf{u}_f \in E$.
        Géométriquement, une fonctionnelle linéaire $f$ peut être interprétée comme définissant un hyperplan $H_f = \{\mathbf{v} \in E \mid f(\mathbf{v}) = 0\}$ passant par l'origine. Le vecteur $\mathbf{u}_f = \mathcal{R}(f)$ est un vecteur normal à cet hyperplan (sa direction est orthogonale à l'hyperplan).
        La similarité cosinus entre $f_1$ et $f_2$ est alors équivalente à la similarité cosinus entre leurs vecteurs normaux associés $\mathcal{R}(f_1)$ et $\mathcal{R}(f_2)$. Cette mesure quantifie l'angle entre les directions définies par ces vecteurs normaux, et donc par extension, la "proximité angulaire" des hyperplans qu'elles définissent. Si deux fonctionnelles sont "similaires", cela signifie qu'elles tendent à évaluer les vecteurs de $E$ de manière proportionnellement similaire, et cela se traduit par leurs hyperplans associés ayant des directions normales proches.

3.  **Action d'une Transformation Linéaire sur les Fonctionnelles**

    *   **Prouvons que $f \circ L$ est une fonctionnelle linéaire :**
        Soient $\mathbf{v}_1, \mathbf{v}_2 \in E$ et $\alpha, \beta \in \mathbb{R}$.
        $(f \circ L)(\alpha \mathbf{v}_1 + \beta \mathbf{v}_2) = f(L(\alpha \mathbf{v}_1 + \beta \mathbf{v}_2))$
        Par linéarité de $L$:
        $f(L(\alpha \mathbf{v}_1 + \beta \mathbf{v}_2)) = f(\alpha L(\mathbf{v}_1) + \beta L(\mathbf{v}_2))$
        Par linéarité de $f$:
        $f(\alpha L(\mathbf{v}_1) + \beta L(\mathbf{v}_2)) = \alpha f(L(\mathbf{v}_1)) + \beta f(L(\mathbf{v}_2))$
        $= \alpha (f \circ L)(\mathbf{v}_1) + \beta (f \circ L)(\mathbf{v}_2)$.
        Donc $f \circ L$ est bien une fonctionnelle linéaire, et $f \circ L \in E^*$.

    *   **Représentant de Riesz de $f \circ L$ :**
        Soit $\mathbf{u}_f = \mathcal{R}(f)$ le représentant de Riesz de $f$.
        Par définition, pour tout $\mathbf{v} \in E$, $f(\mathbf{v}) = \langle \mathbf{u}_f, \mathbf{v} \rangle$.
        Nous cherchons $\mathcal{R}(f \circ L)$, le vecteur $\mathbf{u}_{f \circ L}$ tel que pour tout $\mathbf{v} \in E$, $(f \circ L)(\mathbf{v}) = \langle \mathbf{u}_{f \circ L}, \mathbf{v} \rangle$.
        Nous avons $(f \circ L)(\mathbf{v}) = f(L(\mathbf{v}))$.
        En utilisant la définition de $\mathbf{u}_f$:
        $f(L(\mathbf{v})) = \langle \mathbf{u}_f, L(\mathbf{v}) \rangle$.
        Par la définition de l'opérateur adjoint $L^T$ (que nous rappelons plus formellement à la question 5), pour tout $\mathbf{x}, \mathbf{y} \in E$, $\langle \mathbf{x}, L(\mathbf{y}) \rangle = \langle L^T(\mathbf{x}), \mathbf{y} \rangle$.
        En appliquant cette propriété avec $\mathbf{x} = \mathbf{u}_f$ et $\mathbf{y} = \mathbf{v}$:
        $\langle \mathbf{u}_f, L(\mathbf{v}) \rangle = \langle L^T(\mathbf{u}_f), \mathbf{v} \rangle$.
        Donc, pour tout $\mathbf{v} \in E$, $(f \circ L)(\mathbf{v}) = \langle L^T(\mathbf{u}_f), \mathbf{v} \rangle$.
        Par l'unicité du représentant de Riesz, nous obtenons :
        $\mathcal{R}(f \circ L) = L^T(\mathbf{u}_f) = L^T(\mathcal{R}(f))$.

4.  **Impact d'une Transformation sur la Similarité des Fonctionnelles**

    *   **Comparaison de la similarité :**
        Soient $\mathbf{u}_1 = \mathcal{R}(f_1)$ et $\mathbf{u}_2 = \mathcal{R}(f_2)$ les représentants de Riesz des fonctionnelles $f_1$ et $f_2$.
        La similarité cosinus de $f_1$ et $f_2$ est :
        $$ \text{sim}(f_1, f_2) = \frac{\langle \mathbf{u}_1, \mathbf{u}_2 \rangle}{\|\mathbf{u}_1\| \cdot \|\mathbf{u}_2\|} $$
        Les fonctionnelles transformées sont $f_1 \circ L$ et $f_2 \circ L$. Leurs représentants de Riesz sont, d'après la question 3 :
        $\mathcal{R}(f_1 \circ L) = L^T(\mathbf{u}_1)$ et $\mathcal{R}(f_2 \circ L) = L^T(\mathbf{u}_2)$.
        La similarité cosinus de $f_1 \circ L$ et $f_2 \circ L$ est :
        $$ \text{sim}(f_1 \circ L, f_2 \circ L) = \frac{\langle L^T(\mathbf{u}_1), L^T(\mathbf{u}_2) \rangle}{\|L^T(\mathbf{u}_1)\| \cdot \|L^T(\mathbf{u}_2)\|} $$
        En général, la similarité n'est pas préservée. Le produit scalaire $\langle L^T(\mathbf{u}_1), L^T(\mathbf{u}_2) \rangle$ n'est pas nécessairement égal à $\langle \mathbf{u}_1, \mathbf{u}_2 \rangle$, et de même pour les normes. Une transformation linéaire $L$ (et donc son adjoint $L^T$) peut modifier les angles entre les vecteurs.

    *   **Cas particulier : $L$ est un projecteur orthogonal sur un sous-espace $W \subset E$.**
        Soit $P: E \to E$ un projecteur orthogonal sur $W$. Par définition, pour tout $\mathbf{v} \in E$, $P(\mathbf{v}) \in W$ et $\mathbf{v} - P(\mathbf{v}) \in W^{\perp}$.
        Une propriété clé des projecteurs orthogonaux est qu'ils sont auto-adjoints, c'est-à-dire $P^T = P$.
        Donc, les représentants de Riesz des fonctionnelles transformées sont $\mathcal{R}(f_1 \circ P) = P(\mathbf{u}_1)$ et $\mathcal{R}(f_2 \circ P) = P(\mathbf{u}_2)$.
        La similarité des fonctionnelles transformées devient :
        $$ \text{sim}(f_1 \circ P, f_2 \circ P) = \frac{\langle P(\mathbf{u}_1), P(\mathbf{u}_2) \rangle}{\|P(\mathbf{u}_1)\| \cdot \|P(\mathbf{u}_2)\|} $$
        Analysons les conditions :
        *   **Préservation de la similarité :** Si $\mathbf{u}_1, \mathbf{u}_2 \in W$ (c'est-à-dire si les représentants de Riesz des fonctionnelles appartiennent au sous-espace sur lequel la projection est effectuée), alors $P(\mathbf{u}_1) = \mathbf{u}_1$ et $P(\mathbf{u}_2) = \mathbf{u}_2$. Dans ce cas, la similarité est préservée :
            $\text{sim}(f_1 \circ P, f_2 \circ P) = \frac{\langle \mathbf{u}_1, \mathbf{u}_2 \rangle}{\|\mathbf{u}_1\| \cdot \|\mathbf{u}_2\|} = \text{sim}(f_1, f_2)$.
            Cela signifie que si les requêtes (fonctionnelles) sont naturellement alignées avec le sous-espace $W$, la projection ne modifie pas leur relation sémantique.

        *   **Modification de la similarité :** Si $\mathbf{u}_1$ ou $\mathbf{u}_2$ n'appartiennent pas à $W$, alors $P(\mathbf{u}_1)$ ou $P(\mathbf{u}_2)$ sont des projections de ces vecteurs. L'angle entre $P(\mathbf{u}_1)$ et $P(\mathbf{u}_2)$ peut être très différent de l'angle entre $\mathbf{u}_1$ et $\mathbf{u}_2$.
            *   **Exemple 1 :** Si $\mathbf{u}_1$ et $\mathbf{u}_2$ sont presque orthogonaux mais ont leurs projections $P(\mathbf{u}_1)$ et $P(\mathbf{u}_2)$ presque parallèles (par exemple, si $W$ est une droite et $\mathbf{u}_1, \mathbf{u}_2$ sont des vecteurs qui ont des projections non nulles sur cette droite), la similarité peut augmenter de manière significative.
            *   **Exemple 2 :** Si $P(\mathbf{u}_1) = \mathbf{0}_E$ (c'est-à-dire $\mathbf{u}_1 \in W^{\perp}$), alors $\text{sim}(f_1 \circ P, f_2 \circ P)$ est indéfinie car le dénominateur contient un terme nul. Cela correspond à une fonctionnelle $f_1 \circ P$ qui devient la fonctionnelle nulle (elle donne 0 pour tous les vecteurs de $W$ après projection, et tout vecteur de $E$ est projeté sur $W$).

        En pratique, dans les espaces de plongement sémantique, la projection sur un sous-espace de plus faible dimension (comme dans une analyse en composantes principales) vise souvent à capturer la variance la plus importante ou la sémantique la plus pertinente. Cette opération peut altérer les similarités originales, en renforçant certaines relations (celles qui sont alignées avec les axes de projection principaux) et en diluant d'autres (celles qui sont orthogonales aux axes de projection).

5.  **Relation entre l'Adjoint et l'Isomorphisme de Riesz**

    *   **Définition de l'opérateur adjoint $L^T$ :**
        L'opérateur adjoint $L^T: E \to E$ de $L: E \to E$ est l'unique application linéaire qui satisfait la relation suivante pour tout $\mathbf{x}, \mathbf{y} \in E$:
        $$ \langle L(\mathbf{x}), \mathbf{y} \rangle = \langle \mathbf{x}, L^T(\mathbf{y}) \rangle $$
        L'existence et l'unicité de $L^T$ sont garanties pour un opérateur linéaire sur un espace de Hilbert (et donc sur un espace euclidien de dimension finie).

    *   **Démonstration formelle de $\mathcal{R}(f \circ L) = L^T(\mathcal{R}(f))$ :**
        Soit $f \in E^*$. Soit $\mathbf{u}_f = \mathcal{R}(f)$ son représentant de Riesz.
        Par définition de l'isomorphisme de Riesz, $f(\mathbf{v}) = \langle \mathbf{u}_f, \mathbf{v} \rangle$ pour tout $\mathbf{v} \in E$.
        Nous voulons trouver le représentant de Riesz de la fonctionnelle $f \circ L$. Notons ce représentant $\mathbf{u}_{f \circ L} = \mathcal{R}(f \circ L)$.
        Par définition de $\mathcal{R}$, pour tout $\mathbf{v} \in E$:
        $$ (f \circ L)(\mathbf{v}) = \langle \mathbf{u}_{f \circ L}, \mathbf{v} \rangle $$
        Par ailleurs, par la définition de la composition $f \circ L$:
        $$ (f \circ L)(\mathbf{v}) = f(L(\mathbf{v})) $$
        En substituant l'expression de $f$ en termes de $\mathbf{u}_f$:
        $$ f(L(\mathbf{v})) = \langle \mathbf{u}_f, L(\mathbf{v}) \rangle $$
        Maintenant, nous utilisons la définition de l'opérateur adjoint $L^T$. Pour $\mathbf{x} = \mathbf{u}_f$ et $\mathbf{y} = \mathbf{v}$:
        $$ \langle \mathbf{u}_f, L(\mathbf{v}) \rangle = \langle L^T(\mathbf{u}_f), \mathbf{v} \rangle $$
        En combinant ces égalités, nous obtenons pour tout $\mathbf{v} \in E$:
        $$ \langle \mathbf{u}_{f \circ L}, \mathbf{v} \rangle = \langle L^T(\mathbf{u}_f), \mathbf{v} \rangle $$
        Par l'unicité du représentant de Riesz (démontrée à la question 1), si deux vecteurs produisent le même produit scalaire avec tout autre vecteur de l'espace, alors ces deux vecteurs sont égaux.
        Donc :
        $$ \mathbf{u}_{f \circ L} = L^T(\mathbf{u}_f) $$
        Ce qui se réécrit, en utilisant la notation de l'isomorphisme de Riesz :
        $$ \mathcal{R}(f \circ L) = L^T(\mathcal{R}(f)) $$
        Cette relation est fondamentale. Elle montre que l'action d'une transformation linéaire $L$ sur les vecteurs d'un espace (via $f(L(\mathbf{v}))$) est équivalente à l'action de l'opérateur adjoint $L^T$ sur les représentants de Riesz de ces fonctionnelles. Elle lie ainsi intrinsèquement l'algèbre linéaire des opérateurs à la géométrie de l'espace dual.

---

J'espère que cet exercice vous a permis de solidifier votre compréhension de ces concepts. La dualité et l'action des opérateurs adjoints sont des outils mathématiques puissants qui trouvent de nombreuses applications, notamment dans l'optimisation, les méthodes de Monte Carlo, et bien sûr, la compréhension profonde des espaces de plongement en intelligence artificielle. Maîtriser ces outils est une étape essentielle pour tout ingénieur ou chercheur en IA.