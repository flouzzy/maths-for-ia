En tant que Professeur Émérite de Mathématiques, je vous présente l'Exercice 9 pour le Jalon 12. Cet exercice est conçu pour sonder en profondeur les concepts de dualité, de géométrie des espaces vectoriels et d'opérateurs linéaires dans le contexte spécifique des moteurs de recherche sémantique. Il exige une rigueur formelle et une compréhension des structures algébriques avancées, reflétant la difficulté attendue d'un problème de l'École Polytechnique.

---

## Exercice 9 : Géométrie et dualité des espaces d'immersion sémantique pondérée

**Contexte :**
Dans le domaine des moteurs de recherche sémantique, les entités (documents, requêtes, mots) sont couramment représentées comme des vecteurs dans un espace vectoriel réel de haute dimension, appelé **espace d'immersion (embedding space)**. La similarité entre deux entités est quantifiée par le cosinus de l'angle entre leurs vecteurs d'immersion respectifs. Cet exercice explore les fondements théoriques de tels systèmes, en examinant l'interaction complexe entre les opérateurs linéaires, la dualité et la géométrie de ces espaces d'immersion, en particulier lorsque la notion de similarité est elle-même modifiée par une transformation pondérée.

**Hypothèses et définitions formelles :**
1.  Soit $V$ un espace vectoriel réel de dimension finie $n \in \mathbb{N}^*$, i.e., $V \cong \mathbb{R}^n$.
2.  $V$ est muni d'un produit scalaire euclidien $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{R}$, qui induit une norme $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ pour tout $\mathbf{v} \in V$.
3.  La **similarité cosinus standard** entre deux vecteurs non nuls $\mathbf{u}, \mathbf{v} \in V$ est définie par $\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \|\mathbf{v}\|}$.
4.  Un **opérateur de pondération sémantique** est un endomorphisme linéaire $A: V \to V$, i.e., $A \in \mathcal{L}(V)$.
5.  Pour les Parties I, II et III, l'opérateur $A$ est supposé **symétrique (auto-adjoint)** par rapport à $\langle \cdot, \cdot \rangle$, ce qui signifie que $\langle A\mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{u}, A\mathbf{v} \rangle$ pour tous $\mathbf{u}, \mathbf{v} \in V$.
6.  Pour les Parties II et III, l'opérateur $A$ est également supposé **positif défini**, ce qui signifie que $\langle A\mathbf{v}, \mathbf{v} \rangle > 0$ pour tout $\mathbf{v} \in V \setminus \{\mathbf{0}\}$.

---

### Énoncé de l'Exercice 9

#### Partie I : Transformation d'opérateur et dualité

1.  **Rappel et définition des objets duals :**
    *   Soit $V^*$ le dual de $V$, l'espace des formes linéaires sur $V$. Préciser le type d'objet de $V^*$.
    *   Démontrer que l'application $\Phi: V \to V^*$ définie par $\Phi(\mathbf{v})(\mathbf{u}) = \langle \mathbf{v}, \mathbf{u} \rangle$ pour tout $\mathbf{u} \in V$ est un isomorphisme linéaire. Préciser le type d'objet de $\Phi$.
    *   Soit $A \in \mathcal{L}(V)$ un endomorphisme linéaire. Définir son application duale $A^T: V^* \to V^*$. Préciser le type d'objet de $A^T$.
    *   Montrer que l'opérateur adjoint $A^* \in \mathcal{L}(V)$ (défini par $\langle A\mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{u}, A^*\mathbf{v} \rangle$ pour tous $\mathbf{u}, \mathbf{v} \in V$) est lié à l'application duale $A^T$ par la relation $A^T = \Phi \circ A^* \circ \Phi^{-1}$.

2.  **Propriétés des opérateurs symétriques :**
    *   Pour un opérateur $A \in \mathcal{L}(V)$ symétrique, montrer que $A = A^*$.
    *   Démontrer que si $A$ est symétrique, alors $A^T = \Phi \circ A \circ \Phi^{-1}$. Interpréter géométriquement cette relation dans le contexte des espaces d'immersion sémantique.

#### Partie II : Géométrie des espaces d'immersion pondérés

On introduit un nouveau produit scalaire $\langle \cdot, \cdot \rangle_A$ sur $V$ défini pour tout $\mathbf{u}, \mathbf{v} \in V$ par $\langle \mathbf{u}, \mathbf{v} \rangle_A = \langle \mathbf{u}, A\mathbf{v} \rangle$.

1.  Vérifier que $\langle \cdot, \cdot \rangle_A$ est bien un produit scalaire sur $V$ sous les hypothèses que $A$ est symétrique et positif défini. Vous détaillerez la vérification de la bilinéarité, de la symétrie et de la positivité définie.

2.  **La similarité cosinus pondérée :**
    *   Démontrer que, sous les hypothèses que $A$ est symétrique et positif défini, il existe un unique opérateur $S \in \mathcal{L}(V)$ qui est également symétrique et positif défini tel que $A = S^2$. Préciser le type d'objet de $S$.
    *   Pour deux vecteurs non nuls $\mathbf{u}, \mathbf{v} \in V$, la **similarité cosinus pondérée** par $A$ est définie par $\text{sim}_A(\mathbf{u}, \mathbf{v}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle_A}{\sqrt{\langle \mathbf{u}, \mathbf{u} \rangle_A \langle \mathbf{v}, \mathbf{v} \rangle_A}}$.
    *   Montrer que $\text{sim}_A(\mathbf{u}, \mathbf{v})$ peut être interprétée comme la similarité cosinus standard entre des vecteurs transformés dans l'espace $(V, \langle \cdot, \cdot \rangle)$. Préciser formellement la transformation et le type des objets impliqués.

3.  **Analyse spectrale et directions sémantiques :**
    *   Étant donné que $A$ est un opérateur symétrique positif défini, il est diagonalisable dans une base orthonormée de $V$. Soient $\lambda_1, \dots, \lambda_n \in \mathbb{R}^+$ ses valeurs propres (toutes strictement positives) et $\mathbf{e}_1, \dots, \mathbf{e}_n$ une base orthonormée de $V$ constituée de vecteurs propres associés.
    *   Interpréter la signification des valeurs propres $\lambda_i$ et des vecteurs propres $\mathbf{e}_i$ en termes de "directions sémantiques" et de "poids sémantiques" dans le contexte de la similarité pondérée $\text{sim}_A$.
    *   Pour un vecteur $\mathbf{v} = \sum_{i=1}^n c_i \mathbf{e}_i \in V$ avec $c_i \in \mathbb{R}$, exprimer l'énergie quadratique pondérée $\langle A\mathbf{v}, \mathbf{v} \rangle$ en fonction des coefficients $c_i$ et des valeurs propres $\lambda_i$.
    *   Démontrer que l'ellipsoïde $\{\mathbf{v} \in V \mid \langle A\mathbf{v}, \mathbf{v} \rangle = 1\}$ est une surface d'iso-norme pour la norme $\|\cdot\|_A$ induite par $\langle \cdot, \cdot \rangle_A$. Décrire ses axes principaux et leurs longueurs en relation avec les $\lambda_i$.

#### Partie III : Opérateurs de projecteurs sémantiques et dualité avancée

On considère un ensemble de "concepts sémantiques" orthogonaux représentés par une famille de sous-espaces vectoriels mutuellement orthogonaux $W_1, \dots, W_k$ de $V$, tels que $V = W_1 \oplus \dots \oplus W_k$.
Soit $P_j: V \to W_j$ l'opérateur de projection orthogonale sur $W_j$ pour $j \in \{1, \dots, k\}$. On a $\sum_{j=1}^k P_j = \text{Id}_V$.

1.  **Construction d'un opérateur de pondération sémantique :**
    *   Soient $\alpha_1, \dots, \alpha_k \in \mathbb{R}$ des scalaires strictement positifs.
    *   Définir l'opérateur $A \in \mathcal{L}(V)$ par $A = \sum_{j=1}^k \alpha_j P_j$.
    *   Montrer que $A$ est symétrique et positif défini.

2.  **Dualité des projections et cônes de pertinence :**
    *   Pour tout $j \in \{1, \dots, k\}$, soit $W_j^* = \Phi(W_j)$ le "dual sémantique" de $W_j$ dans $V^*$.
    *   Décrire l'opérateur dual $P_j^T: V^* \to V^*$ de $P_j$. Plus précisément, montrer que $P_j^T$ est la projection orthogonale (au sens d'un produit scalaire induit sur $V^*$) sur le sous-espace $W_j^*$. Vous préciserez le produit scalaire sur $V^*$ et les propriétés de $P_j^T$.
    *   Considérons un vecteur requête $\mathbf{q} \in V$ et la similarité cosinus pondérée $\text{sim}_A(\mathbf{q}, \mathbf{d})$ avec un document $\mathbf{d} \in V$. La "pertinence non normalisée" d'un document $\mathbf{d}$ par rapport à la requête $\mathbf{q}$ est donnée par la valeur $\langle \mathbf{q}, A\mathbf{d} \rangle$.
    *   On définit le **vecteur de pertinence dual** $\phi_{\mathbf{q}, A} = \Phi(A\mathbf{q}) \in V^*$.
    *   Montrer que la fonction de pertinence $\mathbf{d} \mapsto \langle \mathbf{q}, A\mathbf{d} \rangle$ peut être exprimée comme l'évaluation de $\phi_{\mathbf{q}, A}$ sur $\mathbf{d}$, c'est-à-dire $\langle \mathbf{q}, A\mathbf{d} \rangle = \phi_{\mathbf{q}, A}(\mathbf{d})$. Discuter de l'intérêt et des implications de manipuler ce "vecteur de pertinence dual" $\phi_{\mathbf{q}, A}$ plutôt que le vecteur transformé $A\mathbf{q}$ pour optimiser les performances d'un moteur de recherche sémantique, notamment en termes de calcul et de flexibilité conceptuelle.

---

### Correction de l'Exercice 9

#### Partie I : Transformation d'opérateur et dualité

1.  **Rappel et définition des objets duals :**
    *   $V^*$ est l'espace vectoriel des formes linéaires de $V$ vers $\mathbb{R}$. Il est également de dimension finie, et $\dim(V^*) = \dim(V) = n$. Ses éléments sont des applications linéaires $\psi: V \to \mathbb{R}$.
    *   L'application $\Phi: V \to V^*$ est définie par $\Phi(\mathbf{v})(\mathbf{u}) = \langle \mathbf{v}, \mathbf{u} \rangle$ pour tout $\mathbf{u} \in V$.
        *   **Linéarité de $\Phi$ :** Soient $\mathbf{v}_1, \mathbf{v}_2 \in V$ et $\alpha \in \mathbb{R}$. Pour tout $\mathbf{u} \in V$:
            $\Phi(\mathbf{v}_1 + \alpha \mathbf{v}_2)(\mathbf{u}) = \langle \mathbf{v}_1 + \alpha \mathbf{v}_2, \mathbf{u} \rangle$
            Par bilinéarité du produit scalaire : $= \langle \mathbf{v}_1, \mathbf{u} \rangle + \alpha \langle \mathbf{v}_2, \mathbf{u} \rangle$
            $= \Phi(\mathbf{v}_1)(\mathbf{u}) + \alpha \Phi(\mathbf{v}_2)(\mathbf{u})$
            $= (\Phi(\mathbf{v}_1) + \alpha \Phi(\mathbf{v}_2))(\mathbf{u})$.
            Donc, $\Phi(\mathbf{v}_1 + \alpha \mathbf{v}_2) = \Phi(\mathbf{v}_1) + \alpha \Phi(\mathbf{v}_2)$. $\Phi$ est une application linéaire.
        *   **Injectivité de $\Phi$ :** Soit $\mathbf{v} \in \text{Ker}(\Phi)$. Alors $\Phi(\mathbf{v}) = \mathbf{0}_{V^*}$, ce qui signifie que $\Phi(\mathbf{v})(\mathbf{u}) = 0$ pour tout $\mathbf{u} \in V$.
            Ainsi, $\langle \mathbf{v}, \mathbf{u} \rangle = 0$ pour tout $\mathbf{u} \in V$.
            En particulier, en prenant $\mathbf{u} = \mathbf{v}$, on obtient $\langle \mathbf{v}, \mathbf{v} \rangle = 0$.
            Par la propriété de positivité définie du produit scalaire, cela implique que $\mathbf{v} = \mathbf{0}_V$.
            Donc $\text{Ker}(\Phi) = \{\mathbf{0}_V\}$, ce qui prouve que $\Phi$ est injective.
        *   **Isomorphisme :** Puisque $\Phi$ est linéaire, injective et que $\dim(V) = \dim(V^*) = n$, $\Phi$ est un isomorphisme linéaire. Son type d'objet est un isomorphisme d'espaces vectoriels.

    *   L'application duale $A^T: V^* \to V^*$ de $A \in \mathcal{L}(V)$ est définie pour toute forme linéaire $\psi \in V^*$ et tout vecteur $\mathbf{u} \in V$ par $(A^T \psi)(\mathbf{u}) = \psi(A\mathbf{u})$.
        *   **Linéarité de $A^T$ :** Soient $\psi_1, \psi_2 \in V^*$ et $\beta \in \mathbb{R}$. Pour tout $\mathbf{u} \in V$:
            $(A^T(\psi_1 + \beta \psi_2))(\mathbf{u}) = (\psi_1 + \beta \psi_2)(A\mathbf{u})$
            $= \psi_1(A\mathbf{u}) + \beta \psi_2(A\mathbf{u})$ (par linéarité des formes linéaires)
            $= (A^T \psi_1)(\mathbf{u}) + \beta (A^T \psi_2)(\mathbf{u})$
            $= (A^T \psi_1 + \beta A^T \psi_2)(\mathbf{u})$.
            Donc $A^T(\psi_1 + \beta \psi_2) = A^T \psi_1 + \beta A^T \psi_2$. $A^T$ est un endomorphisme linéaire sur $V^*$, donc $A^T \in \mathcal{L}(V^*)$.

    *   **Relation entre $A^T$ et $A^*$ :**
        Nous voulons montrer que $A^T = \Phi \circ A^* \circ \Phi^{-1}$.
        Soit $\psi \in V^*$. Alors $\Phi^{-1}(\psi) \in V$. Soit $\mathbf{v} = \Phi^{-1}(\psi)$. Cela signifie que $\psi = \Phi(\mathbf{v})$, donc $\psi(\mathbf{u}) = \langle \mathbf{v}, \mathbf{u} \rangle$ pour tout $\mathbf{u} \in V$.
        Calculons $(\Phi \circ A^* \circ \Phi^{-1})(\psi)$.
        $(\Phi \circ A^* \circ \Phi^{-1})(\psi) = \Phi(A^*(\Phi^{-1}(\psi))) = \Phi(A^*\mathbf{v})$.
        L'application $\Phi(A^*\mathbf{v})$ est une forme linéaire sur $V$. Pour tout $\mathbf{u} \in V$:
        $(\Phi(A^*\mathbf{v}))(\mathbf{u}) = \langle A^*\mathbf{v}, \mathbf{u} \rangle$.
        Par définition de l'opérateur adjoint $A^*$, $\langle A^*\mathbf{v}, \mathbf{u} \rangle = \langle \mathbf{v}, A\mathbf{u} \rangle$.
        Rappelons que $\psi(\mathbf{x}) = \langle \mathbf{v}, \mathbf{x} \rangle$. Donc $\langle \mathbf{v}, A\mathbf{u} \rangle = \psi(A\mathbf{u})$.
        Par définition de l'application duale $A^T$, $\psi(A\mathbf{u}) = (A^T \psi)(\mathbf{u})$.
        Donc, $(\Phi(A^*\mathbf{v}))(\mathbf{u}) = (A^T \psi)(\mathbf{u})$ pour tout $\mathbf{u} \in V$.
        Ceci implique que $\Phi(A^*\mathbf{v}) = A^T \psi$.
        En substituant $\mathbf{v} = \Phi^{-1}(\psi)$, nous obtenons $A^T \psi = \Phi(A^*(\Phi^{-1}(\psi)))$, ce qui prouve la relation $A^T = \Phi \circ A^* \circ \Phi^{-1}$.

2.  **Propriétés des opérateurs symétriques :**
    *   Un opérateur $A \in \mathcal{L}(V)$ est symétrique si $\langle A\mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{u}, A\mathbf{v} \rangle$ pour tous $\mathbf{u}, \mathbf{v} \in V$.
        Par définition de l'adjoint $A^*$, nous avons $\langle A\mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{u}, A^*\mathbf{v} \rangle$.
        Si $A$ est symétrique, alors $\langle \mathbf{u}, A\mathbf{v} \rangle = \langle \mathbf{u}, A^*\mathbf{v} \rangle$ pour tous $\mathbf{u}, \mathbf{v} \in V$.
        Ceci signifie que $\langle \mathbf{u}, (A - A^*)\mathbf{v} \rangle = 0$ pour tous $\mathbf{u}, \mathbf{v} \in V$.
        En particulier, en prenant $\mathbf{u} = (A - A^*)\mathbf{v}$, nous obtenons $\|(A - A^*)\mathbf{v}\|^2 = 0$, ce qui implique $(A - A^*)\mathbf{v} = \mathbf{0}_V$ pour tout $\mathbf{v} \in V$.
        Donc $A - A^* = \mathbf{0}_{\mathcal{L}(V)}$, ce qui signifie $A = A^*$.

    *   Si $A$ est symétrique, alors $A = A^*$. En utilisant la relation démontrée précédemment ($A^T = \Phi \circ A^* \circ \Phi^{-1}$), nous pouvons substituer $A^*$ par $A$ pour obtenir $A^T = \Phi \circ A \circ \Phi^{-1}$.

        **Interprétation géométrique :**
        L'isomorphisme $\Phi$ peut être pensé comme un "changement de perspective" entre les vecteurs de l'espace d'immersion $V$ (représentant des entités sémantiques) et les formes linéaires de $V^*$ (représentant des "critères de pertinence" ou des "hyperplans de classification").
        Si un vecteur $\mathbf{v} \in V$ est une immersion d'une entité, alors $\Phi(\mathbf{v})$ est la forme linéaire qui "teste" la projection sur $\mathbf{v}$ (multipliée par la norme).
        L'opérateur $A \in \mathcal{L}(V)$ transforme les vecteurs d'immersion, par exemple pour ajuster leur position dans l'espace ou pour mettre l'accent sur certains aspects sémantiques.
        La relation $A^T = \Phi \circ A \circ \Phi^{-1}$ signifie que l'action de $A$ sur les vecteurs d'immersion dans $V$ est "duale" à l'action de $A^T$ sur les formes linéaires de $V^*$. Si $A$ transforme un vecteur $\mathbf{v}$ en $A\mathbf{v}$, alors l'opérateur dual $A^T$ transforme la forme $\Phi(\mathbf{v})$ en $\Phi(A\mathbf{v})$. En d'autres termes, l'opérateur $A$ agit sur l'espace des entités, et simultanément, $A^T$ agit sur l'espace des critères ou fonctions de scoring de manière parfaitement compatible, sans distorsion intrinsèque entre les "objets" et leurs "évaluateurs" (c'est-à-dire que le même opérateur $A$ peut être appliqué directement ou via la dualité). Cela signifie que les transformations sémantiques appliquées aux plongements se reflètent directement et sans modification supplémentaire sur les règles de pertinence induites. C'est essentiel pour la cohérence d'un système où les plongements et les fonctions de scoring peuvent évoluer.

#### Partie II : Géométrie des espaces d'immersion pondérés

1.  **Vérifier que $\langle \cdot, \cdot \rangle_A$ est bien un produit scalaire sur $V$ :**
    Nous devons vérifier trois propriétés : bilinéarité, symétrie et positivité définie.

    *   **Bilinéarité :**
        Pour la première composante : Soient $\mathbf{u}_1, \mathbf{u}_2, \mathbf{v} \in V$ et $\alpha \in \mathbb{R}$.
        $\langle \mathbf{u}_1 + \alpha \mathbf{u}_2, \mathbf{v} \rangle_A = \langle \mathbf{u}_1 + \alpha \mathbf{u}_2, A\mathbf{v} \rangle$
        Par bilinéarité du produit scalaire $\langle \cdot, \cdot \rangle$: $= \langle \mathbf{u}_1, A\mathbf{v} \rangle + \alpha \langle \mathbf{u}_2, A\mathbf{v} \rangle$
        Par définition de $\langle \cdot, \cdot \rangle_A$: $= \langle \mathbf{u}_1, \mathbf{v} \rangle_A + \alpha \langle \mathbf{u}_2, \mathbf{v} \rangle_A$.
        Pour la seconde composante : Soient $\mathbf{u}, \mathbf{v}_1, \mathbf{v}_2 \in V$ et $\beta \in \mathbb{R}$.
        $\langle \mathbf{u}, \mathbf{v}_1 + \beta \mathbf{v}_2 \rangle_A = \langle \mathbf{u}, A(\mathbf{v}_1 + \beta \mathbf{v}_2) \rangle$
        Par linéarité de $A$: $= \langle \mathbf{u}, A\mathbf{v}_1 + \beta A\mathbf{v}_2 \rangle$
        Par bilinéarité du produit scalaire $\langle \cdot, \cdot \rangle$: $= \langle \mathbf{u}, A\mathbf{v}_1 \rangle + \beta \langle \mathbf{u}, A\mathbf{v}_2 \rangle$
        Par définition de $\langle \cdot, \cdot \rangle_A$: $= \langle \mathbf{u}, \mathbf{v}_1 \rangle_A + \beta \langle \mathbf{u}, \mathbf{v}_2 \rangle_A$.
        Donc $\langle \cdot, \cdot \rangle_A$ est bilinéaire.

    *   **Symétrie :** Soient $\mathbf{u}, \mathbf{v} \in V$.
        $\langle \mathbf{u}, \mathbf{v} \rangle_A = \langle \mathbf{u}, A\mathbf{v} \rangle$.
        Puisque $A$ est symétrique, $\langle \mathbf{u}, A\mathbf{v} \rangle = \langle A\mathbf{u}, \mathbf{v} \rangle$.
        Puisque $\langle \cdot, \cdot \rangle$ est symétrique, $\langle A\mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, A\mathbf{u} \rangle$.
        Par définition de $\langle \cdot, \cdot \rangle_A$: $= \langle \mathbf{v}, \mathbf{u} \rangle_A$.
        Donc $\langle \cdot, \cdot \rangle_A$ est symétrique.

    *   **Positivité définie :** Soit $\mathbf{v} \in V$.
        $\langle \mathbf{v}, \mathbf{v} \rangle_A = \langle \mathbf{v}, A\mathbf{v} \rangle$.
        Par hypothèse, $A$ est positif défini, ce qui signifie que $\langle A\mathbf{v}, \mathbf{v} \rangle > 0$ pour tout $\mathbf{v} \in V \setminus \{\mathbf{0}_V\}$.
        Puisque $A$ est symétrique, $\langle \mathbf{v}, A\mathbf{v} \rangle = \langle A\mathbf{v}, \mathbf{v} \rangle$.
        Donc, $\langle \mathbf{v}, \mathbf{v} \rangle_A > 0$ pour tout $\mathbf{v} \in V \setminus \{\mathbf{0}_V\}$.
        Si $\mathbf{v} = \mathbf{0}_V$, alors $\langle \mathbf{0}_V, A\mathbf{0}_V \rangle = \langle \mathbf{0}_V, \mathbf{0}_V \rangle = 0$.
        Donc $\langle \cdot, \cdot \rangle_A$ est positif défini.

    Ayant vérifié ces trois propriétés, $\langle \cdot, \cdot \rangle_A$ est bien un produit scalaire sur $V$.

2.  **La similarité cosinus pondérée :**
    *   **Existence et unicité de $S$ :**
        Puisque $A$ est un opérateur symétrique positif défini sur un espace vectoriel réel de dimension finie, le théorème spectral garantit que $A$ est diagonalisable dans une base orthonormée, et ses valeurs propres $\lambda_i$ sont strictement positives.
        On peut alors définir l'opérateur $S = \sqrt{A}$. Pour ce faire, si $A\mathbf{e}_i = \lambda_i \mathbf{e}_i$ pour une base orthonormée $\{\mathbf{e}_i\}_{i=1}^n$, alors on définit $S\mathbf{e}_i = \sqrt{\lambda_i} \mathbf{e}_i$.
        $S$ est linéaire, symétrique (car ses vecteurs propres sont ceux de $A$, et il est défini par des multiplicateurs réels sur une base orthonormée, $\sqrt{\lambda_i} \in \mathbb{R}$), et positif défini (car $\sqrt{\lambda_i} > 0$ pour toutes les valeurs propres).
        De plus, $S^2\mathbf{e}_i = S(S\mathbf{e}_i) = S(\sqrt{\lambda_i} \mathbf{e}_i) = \sqrt{\lambda_i} S\mathbf{e}_i = \sqrt{\lambda_i} (\sqrt{\lambda_i} \mathbf{e}_i) = \lambda_i \mathbf{e}_i = A\mathbf{e}_i$.
        Puisque $S^2$ et $A$ agissent de la même manière sur une base de $V$, $S^2 = A$.
        L'unicité de $S$ (étant donné qu'il doit être symétrique et positif défini) découle de l'unicité de la racine carrée positive définie d'une matrice symétrique positive définie.
        Le type d'objet de $S$ est un endomorphisme linéaire de $V$, $S \in \mathcal{L}(V)$, spécifiquement un opérateur symétrique positif défini.

    *   **Interprétation de $\text{sim}_A(\mathbf{u}, \mathbf{v})$ :**
        La similarité cosinus pondérée est donnée par $\text{sim}_A(\mathbf{u}, \mathbf{v}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle_A}{\sqrt{\langle \mathbf{u}, \mathbf{u} \rangle_A \langle \mathbf{v}, \mathbf{v} \rangle_A}}$.
        Utilisons la définition de $\langle \cdot, \cdot \rangle_A$ et le fait que $A = S^2$.
        $\langle \mathbf{u}, \mathbf{v} \rangle_A = \langle \mathbf{u}, A\mathbf{v} \rangle = \langle \mathbf{u}, S^2\mathbf{v} \rangle$.
        Puisque $S$ est symétrique, $\langle \mathbf{u}, S^2\mathbf{v} \rangle = \langle S\mathbf{u}, S\mathbf{v} \rangle$.
        De même, $\langle \mathbf{u}, \mathbf{u} \rangle_A = \langle S\mathbf{u}, S\mathbf{u} \rangle = \|S\mathbf{u}\|^2$.
        Et $\langle \mathbf{v}, \mathbf{v} \rangle_A = \langle S\mathbf{v}, S\mathbf{v} \rangle = \|S\mathbf{v}\|^2$.
        En substituant ces expressions dans la formule de similarité pondérée :
        $\text{sim}_A(\mathbf{u}, \mathbf{v}) = \frac{\langle S\mathbf{u}, S\mathbf{v} \rangle}{\sqrt{\|S\mathbf{u}\|^2 \|S\mathbf{v}\|^2}} = \frac{\langle S\mathbf{u}, S\mathbf{v} \rangle}{\|S\mathbf{u}\| \|S\mathbf{v}\|}$.
        Cette dernière expression est précisément la similarité cosinus standard entre les vecteurs $S\mathbf{u}$ et $S\mathbf{v}$.
        **Interprétation :** La similarité cosinus pondérée par $A$ entre $\mathbf{u}$ et $\mathbf{v}$ est équivalente à la similarité cosinus standard entre les vecteurs transformés $S\mathbf{u}$ et $S\mathbf{v}$. L'opérateur $S \in \mathcal{L}(V)$ agit comme une **transformation d'espace d'immersion**. Il mappe chaque vecteur d'immersion $\mathbf{x} \in V$ à un nouveau vecteur d'immersion $S\mathbf{x} \in V$. Dans ce nouveau système de coordonnées (ou espace d'immersion effectif), les relations angulaires sont mesurées avec la métrique standard. Cela signifie qu'un opérateur de pondération $A$ peut être concrètement réalisé en transformant les embeddings eux-mêmes avant de calculer la similarité standard.

3.  **Analyse spectrale et directions sémantiques :**
    *   **Interprétation des valeurs propres et vecteurs propres :**
        Les vecteurs propres $\mathbf{e}_i$ de $A$ sont les **directions sémantiques principales** ou **axes sémantiques** de l'espace pondéré. Ce sont des directions dans $V$ qui ne sont pas "tournées" par l'opérateur $A$, seulement étirées ou compressées.
        Les valeurs propres $\lambda_i$ sont les **poids sémantiques** ou **facteurs d'importance** associés à ces directions. Une grande valeur propre $\lambda_i$ indique que la direction sémantique $\mathbf{e}_i$ est fortement pondérée par l'opérateur $A$. Les différences d'angle entre les vecteurs sont amplifiées dans cette direction. Inversement, une petite valeur propre signifie une faible pondération, et la direction correspondante a moins d'impact sur la similarité pondérée.
        En d'autres termes, $A$ déforme la géométrie de l'espace $V$ en étirant les distances et les angles différemment selon ces directions privilégiées. Une requête ou un document fortement aligné avec une direction $\mathbf{e}_i$ associée à une grande $\lambda_i$ aura une influence sémantique accrue.

    *   **Expression de $\langle A\mathbf{v}, \mathbf{v} \rangle$ :**
        Soit $\mathbf{v} = \sum_{i=1}^n c_i \mathbf{e}_i \in V$, où $c_i = \langle \mathbf{v}, \mathbf{e}_i \rangle$ (car la base est orthonormée).
        Alors $A\mathbf{v} = A\left(\sum_{i=1}^n c_i \mathbf{e}_i\right) = \sum_{i=1}^n c_i A\mathbf{e}_i$ (par linéarité de $A$).
        Puisque $\mathbf{e}_i$ sont des vecteurs propres de $A$ avec valeurs propres $\lambda_i$, $A\mathbf{e}_i = \lambda_i \mathbf{e}_i$.
        Donc $A\mathbf{v} = \sum_{i=1}^n c_i \lambda_i \mathbf{e}_i$.
        Maintenant, calculons $\langle A\mathbf{v}, \mathbf{v} \rangle$:
        $\langle A\mathbf{v}, \mathbf{v} \rangle = \left\langle \sum_{i=1}^n c_i \lambda_i \mathbf{e}_i, \sum_{j=1}^n c_j \mathbf{e}_j \right\rangle$.
        Par bilinéarité du produit scalaire : $= \sum_{i=1}^n \sum_{j=1}^n c_i \lambda_i c_j \langle \mathbf{e}_i, \mathbf{e}_j \rangle$.
        Puisque $\{\mathbf{e}_i\}_{i=1}^n$ est une base orthonormée, $\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij}$ (symbole de Kronecker).
        $= \sum_{i=1}^n c_i \lambda_i c_i = \sum_{i=1}^n \lambda_i c_i^2$.
        Donc $\langle A\mathbf{v}, \mathbf{v} \rangle = \sum_{i=1}^n \lambda_i c_i^2$.

    *   **Description de l'ellipsoïde d'iso-norme :**
        La norme induite par $\langle \cdot, \cdot \rangle_A$ est $\|\mathbf{v}\|_A = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle_A} = \sqrt{\langle A\mathbf{v}, \mathbf{v} \rangle}$.
        L'ellipsoïde $\{\mathbf{v} \in V \mid \langle A\mathbf{v}, \mathbf{v} \rangle = 1\}$ est donc l'ensemble des vecteurs dont la norme pondérée est $1$, i.e., $\|\mathbf{v}\|_A = 1$. C'est une surface d'iso-norme.
        En utilisant l'expression précédente, l'équation de cette ellipsoïde est $\sum_{i=1}^n \lambda_i c_i^2 = 1$.
        Dans le système de coordonnées défini par la base orthonormée de vecteurs propres $\{\mathbf{e}_i\}_{i=1}^n$, les coordonnées de $\mathbf{v}$ sont $(c_1, \dots, c_n)$.
        L'équation peut être réécrite comme $\sum_{i=1}^n \frac{c_i^2}{1/\lambda_i} = 1$.
        Ceci est l'équation canonique d'un ellipsoïde.
        *   Les **axes principaux** de cet ellipsoïde sont alignés avec les vecteurs propres $\mathbf{e}_i$.
        *   Les **longueurs des demi-axes** le long de chaque direction $\mathbf{e}_i$ sont $1/\sqrt{\lambda_i}$.
        **Interprétation :** Les directions sémantiques associées aux grandes valeurs propres $\lambda_i$ (qui sont fortement pondérées) correspondent à des demi-axes courts ($1/\sqrt{\lambda_i}$ petit). Inversement, les directions associées aux petites valeurs propres $\lambda_i$ (faiblement pondérées) correspondent à des demi-axes longs ($1/\sqrt{\lambda_i}$ grand). Géométriquement, l'opérateur $A$ "compresse" l'espace dans les directions importantes et "étire" dans les directions moins importantes, de sorte que l'ensemble des vecteurs ayant une norme pondérée unitaire forme une ellipsoïde plus "aplatie" le long des directions les plus pertinentes.

#### Partie III : Opérateurs de projecteurs sémantiques et dualité avancée

1.  **Construction d'un opérateur de pondération sémantique :**
    *   L'opérateur est défini par $A = \sum_{j=1}^k \alpha_j P_j$. Les scalaires $\alpha_j \in \mathbb{R}$ sont strictement positifs.

    *   **Symétrie de $A$ :**
        Pour tous $\mathbf{u}, \mathbf{v} \in V$:
        $\langle A\mathbf{u}, \mathbf{v} \rangle = \left\langle \sum_{j=1}^k \alpha_j P_j \mathbf{u}, \mathbf{v} \right\rangle$.
        Par linéarité du produit scalaire : $= \sum_{j=1}^k \alpha_j \langle P_j \mathbf{u}, \mathbf{v} \rangle$.
        Comme $P_j$ est un opérateur de projection orthogonale, il est symétrique (auto-adjoint), c'est-à-dire $\langle P_j \mathbf{x}, \mathbf{y} \rangle = \langle \mathbf{x}, P_j \mathbf{y} \rangle$ pour tous $\mathbf{x}, \mathbf{y} \in V$.
        Donc : $= \sum_{j=1}^k \alpha_j \langle \mathbf{u}, P_j \mathbf{v} \rangle$.
        Par linéarité du produit scalaire : $= \left\langle \mathbf{u}, \sum_{j=1}^k \alpha_j P_j \mathbf{v} \right\rangle$.
        Par définition de $A$: $= \langle \mathbf{u}, A\mathbf{v} \rangle$.
        Donc $A$ est symétrique.

    *   **Positivité définie de $A$ :**
        Pour tout $\mathbf{v} \in V \setminus \{\mathbf{0}_V\}$:
        $\langle A\mathbf{v}, \mathbf{v} \rangle = \left\langle \sum_{j=1}^k \alpha_j P_j \mathbf{v}, \mathbf{v} \right\rangle = \sum_{j=1}^k \alpha_j \langle P_j \mathbf{v}, \mathbf{v} \rangle$.
        Puisque $P_j$ est une projection orthogonale, $P_j = P_j^* = P_j^2$. Donc $\langle P_j \mathbf{v}, \mathbf{v} \rangle = \langle P_j^2 \mathbf{v}, \mathbf{v} \rangle = \langle P_j \mathbf{v}, P_j \mathbf{v} \rangle = \|P_j \mathbf{v}\|^2$.
        Ainsi, $\langle A\mathbf{v}, \mathbf{v} \rangle = \sum_{j=1}^k \alpha_j \|P_j \mathbf{v}\|^2$.
        Puisque tous les $\alpha_j$ sont strictement positifs ($\alpha_j > 0$), et que $\|P_j \mathbf{v}\|^2 \ge 0$, on a $\langle A\mathbf{v}, \mathbf{v} \rangle \ge 0$.
        Pour montrer qu'il est strictement positif, supposons $\langle A\mathbf{v}, \mathbf{v} \rangle = 0$.
        Alors $\sum_{j=1}^k \alpha_j \|P_j \mathbf{v}\|^2 = 0$. Puisque $\alpha_j > 0$ et $\|P_j \mathbf{v}\|^2 \ge 0$, cela implique $\|P_j \mathbf{v}\|^2 = 0$ pour tout $j \in \{1, \dots, k\}$.
        Donc $P_j \mathbf{v} = \mathbf{0}_V$ pour tout $j$.
        Puisque $\sum_{j=1}^k P_j = \text{Id}_V$, nous avons $\mathbf{v} = \text{Id}_V \mathbf{v} = \sum_{j=1}^k P_j \mathbf{v} = \sum_{j=1}^k \mathbf{0}_V = \mathbf{0}_V$.
        Donc, si $\mathbf{v} \ne \mathbf{0}_V$, alors $\langle A\mathbf{v}, \mathbf{v} \rangle > 0$.
        $A$ est donc positif défini.

2.  **Dualité des projections et cônes de pertinence :**
    *   **Description de $P_j^T$ :**
        L'opérateur dual $P_j^T$ est défini par $P_j^T = \Phi \circ P_j \circ \Phi^{-1}$.
        Pour montrer que $P_j^T$ est une projection orthogonale sur $W_j^* = \Phi(W_j)$:
        1.  **$P_j^T$ est un projecteur :**
            $(P_j^T)^2 = (\Phi \circ P_j \circ \Phi^{-1}) \circ (\Phi \circ P_j \circ \Phi^{-1})$
            $= \Phi \circ P_j \circ (\Phi^{-1} \circ \Phi) \circ P_j \circ \Phi^{-1}$
            $= \Phi \circ P_j \circ \text{Id}_V \circ P_j \circ \Phi^{-1} = \Phi \circ P_j^2 \circ \Phi^{-1}$.
            Comme $P_j$ est une projection, $P_j^2 = P_j$.
            Donc $(P_j^T)^2 = \Phi \circ P_j \circ \Phi^{-1} = P_j^T$. $P_j^T$ est bien un projecteur.
        2.  **Image de $P_j^T$ :**
            $\text{Im}(P_j^T) = \text{Im}(\Phi \circ P_j \circ \Phi^{-1}) = \Phi(\text{Im}(P_j))$.
            Puisque $\text{Im}(P_j) = W_j$, on a $\text{Im}(P_j^T) = \Phi(W_j) = W_j^*$.
        3.  **Orthogonalité de $P_j^T$ :**
            Pour définir l'orthogonalité dans $V^*$, on munit $V^*$ d'un produit scalaire induit par celui de $V$. Pour $\psi_1, \psi_2 \in V^*$, on définit $\langle \psi_1, \psi_2 \rangle_{V^*} = \langle \Phi^{-1}(\psi_1), \Phi^{-1}(\psi_2) \rangle_V$.
            Nous devons montrer que $P_j^T$ est auto-adjoint par rapport à ce produit scalaire sur $V^*$.
            Pour $\psi_1, \psi_2 \in V^*$:
            $\langle P_j^T \psi_1, \psi_2 \rangle_{V^*} = \langle \Phi^{-1}(P_j^T \psi_1), \Phi^{-1}(\psi_2) \rangle_V$.
            $\Phi^{-1}(P_j^T \psi_1) = \Phi^{-1}(\Phi \circ P_j \circ \Phi^{-1}(\psi_1)) = P_j(\Phi^{-1}(\psi_1))$.
            Donc $\langle P_j^T \psi_1, \psi_2 \rangle_{V^*} = \langle P_j(\Phi^{-1}(\psi_1)), \Phi^{-1}(\psi_2) \rangle_V$.
            Puisque $P_j$ est un projecteur orthogonal, il est auto-adjoint ($P_j = P_j^*$).
            $= \langle \Phi^{-1}(\psi_1), P_j(\Phi^{-1}(\psi_2)) \rangle_V$.
            $= \langle \Phi^{-1}(\psi_1), \Phi^{-1}(P_j^T \psi_2) \rangle_V = \langle \psi_1, P_j^T \psi_2 \rangle_{V^*}$.
            Donc $P_j^T$ est auto-adjoint.
            En résumé, $P_j^T$ est un projecteur auto-adjoint dont l'image est $W_j^*$, il est donc la projection orthogonale sur $W_j^*$.
            L'image de $P_j^T$ est $W_j^* = \Phi(W_j)$, et son noyau est $(W_j^*)^\perp = \Phi(W_j^\perp)$.

    *   **Vecteur de pertinence dual $\phi_{\mathbf{q}, A}$ et discussion :**
        La pertinence non normalisée est $\langle \mathbf{q}, A\mathbf{d} \rangle$.
        On définit $\phi_{\mathbf{q}, A} = \Phi(A\mathbf{q}) \in V^*$.
        Par définition de $\Phi$, la forme linéaire $\phi_{\mathbf{q}, A}$ agit sur un vecteur $\mathbf{d} \in V$ comme suit :
        $\phi_{\mathbf{q}, A}(\mathbf{d}) = \Phi(A\mathbf{q})(\mathbf{d}) = \langle A\mathbf{q}, \mathbf{d} \rangle$.
        Puisque $A$ est symétrique, $\langle A\mathbf{q}, \mathbf{d} \rangle = \langle \mathbf{q}, A\mathbf{d} \rangle$.
        Donc, $\phi_{\mathbf{q}, A}(\mathbf{d}) = \langle \mathbf{q}, A\mathbf{d} \rangle$.
        Ceci démontre que la fonction de pertinence $\mathbf{d} \mapsto \langle \mathbf{q}, A\mathbf{d} \rangle$ peut être exprimée comme l'évaluation de la forme linéaire $\phi_{\mathbf{q}, A}$ sur le vecteur $\mathbf{d}$.

        **Intérêt et implications de manipuler $\phi_{\mathbf{q}, A}$ :**
        1.  **Flexibilité conceptuelle :** Dans un moteur de recherche sémantique, la requête peut être vue comme un "filtre" ou un "critère" qui sélectionne les documents pertinents. Le passage au dual permet de représenter directement ce critère comme une forme linéaire $\phi_{\mathbf{q}, A}$, qui, lorsqu'elle est appliquée à un document $\mathbf{d}$, produit sa pertinence. Cela correspond mieux à l'intuition d'une "requête" comme une "fonction d'évaluation" sur l'espace des documents.
        2.  **Optimisation de calcul :**
            *   **Pré-calcul :** Pour une requête donnée $\mathbf{q}$, le vecteur $A\mathbf{q}$ peut être calculé une seule fois. Ensuite, pour chaque document $\mathbf{d}_i$ dans la base de données, la pertinence $\langle A\mathbf{q}, \mathbf{d}_i \rangle$ peut être calculée comme un simple produit scalaire. Cependant, manipuler $\phi_{\mathbf{q}, A}$ plutôt que $A\mathbf{q}$ n'apporte pas un avantage computationnel direct pour ce simple cas, car $\phi_{\mathbf{q}, A}$ est l'objet dual de $A\mathbf{q}$.
            *   **Contextes plus complexes (e.g., apprentissage) :** L'intérêt devient plus manifeste lorsque l'on considère des scénarios d'apprentissage où les opérateurs $A$ ou les requêtes $\mathbf{q}$ sont eux-mêmes optimisés. Par exemple, si nous cherchons à ajuster $A$ ou $\mathbf{q}$ pour maximiser la pertinence de certains documents et minimiser celle d'autres, travailler dans l'espace dual peut simplifier la formulation des fonctions objectif, surtout si ces fonctions sont naturellement définies sur des formes linéaires (par exemple, des contraintes sur la marge entre des hyperplans de séparation).
            *   **Opérateurs agissant sur le dual :** Si de futurs traitements sémantiques sont formulés directement dans l'espace dual (e.g., des opérateurs $B^T: V^* \to V^*$ qui transforment des critères de pertinence), alors il est naturel d'avoir les requêtes déjà sous forme duale.
            *   **Représentation sparsifiée :** Dans certains contextes de grande dimension, les formes linéaires peuvent être représentées de manière plus sparsifiée ou plus efficace pour certains calculs (e.g., les formes linéaires associées à des classifieurs linéaires).

        En somme, la manipulation du vecteur de pertinence dual $\phi_{\mathbf{q}, A}$ offre une perspective plus abstraite et potentiellement plus puissante pour la modélisation et l'optimisation des interactions entre requêtes et documents, surtout lorsque la complexité des transformations sémantiques et des critères de pertinence augmente. Elle permet de mieux séparer conceptuellement la "requête en tant qu'entité" de la "requête en tant que fonction d'évaluation".

---