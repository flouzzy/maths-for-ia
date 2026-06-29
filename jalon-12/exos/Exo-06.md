En tant que Professeur Émérite de Mathématiques, je vous propose une incursion dans les fondements rigoureux de la conception d'un moteur de recherche sémantique. Cet exercice, de difficulté notable, vous confrontera à des concepts d'algèbre linéaire avancée, souvent rencontrés dans les concours les plus prestigieux. Il s'agit d'un jalon essentiel pour la compréhension des espaces de plongement et de la géométrie qui sous-tend la notion de similarité.

---

### Exercice 6 (Difficulté : ★★★)

**Titre :** Géométrie des Espaces de Plongement Sémantique et Projections A-Orthogonales

**Préambule :**
La révolution de l'intelligence artificielle a mis en lumière l'importance des espaces de plongement (embedding spaces) pour représenter des entités complexes (mots, documents, images) sous forme de vecteurs numériques. Ces représentations vectorielles permettent ensuite d'effectuer des opérations de recherche et de classification basées sur des notions de distance et de similarité géométrique. Nous allons explorer les fondements théoriques de ces concepts, en particulier la similarité cosinus, la dualité entre espaces et une généralisation des projections orthogonales, un domaine central en algèbre linéaire avancée.

**Hypothèses et Conventions :**
*   L'espace vectoriel $\mathcal{V}$ est un espace vectoriel réel de dimension finie $d \in \mathbb{N}^*$, que nous identifions canoniquement à $\mathbb{R}^d$.
*   Les vecteurs sont représentés par des matrices colonnes $x \in \mathcal{M}_{d,1}(\mathbb{R})$.
*   Le produit scalaire canonique (Euclidien) sur $\mathbb{R}^d$ est noté $\langle u, v \rangle = u^T v$. La norme associée est $\|u\| = \sqrt{\langle u, u \rangle}$.
*   Une matrice $M \in \mathcal{M}_{d,d}(\mathbb{R})$ est dite symétrique si $M^T = M$.
*   Une matrice symétrique $M$ est dite positive (ou semi-définie positive) si pour tout $x \in \mathbb{R}^d$, $x^T M x \ge 0$. Elle est dite définie positive si $x^T M x > 0$ pour tout $x \in \mathbb{R}^d \setminus \{0\}$.

---

**Énoncé :**

**Partie I : Dualité et Géométrie Standard dans les Espaces de Plongement**

Dans un moteur de recherche sémantique, les documents et les requêtes sont transformés en vecteurs (embeddings) dans un espace de grande dimension $\mathcal{V} = \mathbb{R}^d$. La similarité entre une requête $q \in \mathbb{R}^d$ et un document $v \in \mathbb{R}^d$ est souvent mesurée par la similarité cosinus.

1.  **Définition et Normalisation :**
    a.  Rappelez la définition de la similarité cosinus entre deux vecteurs non nuls $q, v \in \mathbb{R}^d$.
    b.  Expliquez pourquoi la normalisation des vecteurs (les ramener sur la sphère unité $\mathcal{S}^{d-1} = \{x \in \mathbb{R}^d \mid \|x\|=1\}$) est une pratique courante dans ce contexte et quelle est son interprétation géométrique.

2.  **Dictionnaire de Vecteurs et Espace Dual :**
    a.  Soit $\mathcal{V}^*$ l'espace dual de $\mathcal{V}$, c'est-à-dire l'espace des formes linéaires sur $\mathcal{V}$. Pour tout $q \in \mathcal{V}$, on définit l'application $\phi_q: \mathcal{V} \to \mathbb{R}$ par $\phi_q(v) = \langle q, v \rangle$. Montrez que $\phi_q$ est une forme linéaire.
    b.  Montrez que l'application $\Psi: \mathcal{V} \to \mathcal{V}^*$ définie par $\Psi(q) = \phi_q$ est un isomorphisme d'espaces vectoriels. (Vous pouvez admettre que $\mathcal{V}$ et $\mathcal{V}^*$ ont la même dimension $d$).
    c.  Discutez brièvement de l'implication de cet isomorphisme pour la notion de "dualité" entre les requêtes (vues comme formes linéaires) et les documents (vus comme vecteurs) dans le contexte d'un moteur de recherche.

---

**Partie II : Projections A-Orthogonales et Similarité Sémantique Généralisée**

Dans certains cas, la structure sémantique de l'espace de plongement peut être mieux capturée par une métrique différente du produit scalaire euclidien standard. Soit $A \in \mathcal{M}_{d,d}(\mathbb{R})$ une matrice symétrique définie positive. Nous définissons un nouveau produit scalaire sur $\mathbb{R}^d$ par $\langle u, v \rangle_A = u^T A v$ pour tous $u, v \in \mathbb{R}^d$. La norme associée est $\|u\|_A = \sqrt{\langle u, u \rangle_A}$.

1.  **Propriétés du Produit Scalaire Généralisé :**
    Démontrez que $\langle \cdot, \cdot \rangle_A$ satisfait les axiomes d'un produit scalaire sur $\mathbb{R}^d$:
    a.  Linéarité par rapport au premier argument : $\langle \alpha u + \beta w, v \rangle_A = \alpha \langle u, v \rangle_A + \beta \langle w, v \rangle_A$ pour tous $\alpha, \beta \in \mathbb{R}$ et $u, w, v \in \mathbb{R}^d$.
    b.  Symétrie : $\langle u, v \rangle_A = \langle v, u \rangle_A$ pour tous $u, v \in \mathbb{R}^d$.
    c.  Définition positive : $\langle u, u \rangle_A \ge 0$ pour tout $u \in \mathbb{R}^d$, et $\langle u, u \rangle_A = 0 \iff u = 0$.

2.  **Projections A-Orthogonales :**
    Soit $\mathcal{S}$ un sous-espace vectoriel de $\mathbb{R}^d$ de dimension $k$, avec $1 \le k < d$. Soit $(e_1, \ldots, e_k)$ une base de $\mathcal{S}$. On forme la matrice $E \in \mathcal{M}_{d,k}(\mathbb{R})$ dont les colonnes sont les vecteurs $e_1, \ldots, e_k$.
    a.  Définissez le sous-espace $A$-orthogonal $\mathcal{S}^{\perp_A}$ de $\mathcal{S}$ par rapport au produit scalaire $\langle \cdot, \cdot \rangle_A$. Montrez que $\mathbb{R}^d = \mathcal{S} \oplus \mathcal{S}^{\perp_A}$ (somme directe $A$-orthogonale).
        *Indications : Pour la somme directe, montrez que $\mathcal{S} \cap \mathcal{S}^{\perp_A} = \{0\}$ et utilisez des arguments de dimension. Pour le fait que tout vecteur de $\mathbb{R}^d$ peut être décomposé, considérez l'existence de $P_A(v)$ et $v - P_A(v)$.*
    b.  La projection $A$-orthogonale $P_A(v)$ d'un vecteur $v \in \mathbb{R}^d$ sur $\mathcal{S}$ est l'unique vecteur $s_0 \in \mathcal{S}$ tel que $v - s_0 \in \mathcal{S}^{\perp_A}$.
        Démontrez que la matrice de projection $P_A$ (qui, appliquée à $v$, donne $P_A(v)$) est donnée par $P_A = E (E^T A E)^{-1} E^T A$.
        *Hypothèse :* La matrice $E^T A E$ est inversible. Prouvez cette hypothèse.

3.  **Similarité Sémantique A-Généralisée :**
    Dans ce cadre généralisé, la similarité entre une requête $q \in \mathbb{R}^d$ et un document $v \in \mathbb{R}^d$ peut être évaluée par leur similarité dans le sous-espace sémantique $\mathcal{S}$, en utilisant le produit scalaire $A$.
    a.  Définissons la "similarité sémantique $A$-généralisée" comme $S_{\mathcal{S},A}(q,v) = \langle P_A(q), P_A(v) \rangle_A$.
        Montrez que $S_{\mathcal{S},A}(q,v)$ peut s'écrire sous la forme $q^T M_A v$ pour une matrice $M_A \in \mathcal{M}_{d,d}(\mathbb{R})$. Déterminez $M_A$.
    b.  Prouvez que $M_A$ est une matrice symétrique et positive (semi-définie positive). Quel est son rang ?
    c.  Montrez que $P_A^T A P_A = M_A$.
    d.  La "similarité cosinus $A$-généralisée" entre $u, w \in \mathbb{R}^d$ est définie par $\cos_A(\theta_{u,w}) = \frac{\langle u, w \rangle_A}{\|u\|_A \|w\|_A}$.
        Exprimez $S_{\mathcal{S},A}(q,v)$ en fonction des normes $A$-généralisées des projections de $q$ et $v$ sur $\mathcal{S}$ et de la similarité cosinus $A$-généralisée entre ces projections. Quelle est la valeur de cette similarité cosinus ?

---

### Correction de l'Exercice 6

**Partie I : Dualité et Géométrie Standard dans les Espaces de Plongement**

1.  **Définition et Normalisation :**
    a.  Soient $q \in \mathbb{R}^d$ et $v \in \mathbb{R}^d$ deux vecteurs non nuls. La similarité cosinus entre $q$ et $v$, notée $\cos(\theta)$, est définie par :
        $$ \cos(\theta) = \frac{\langle q, v \rangle}{\|q\| \|v\|} $$
        où $\langle q, v \rangle = q^T v$ est le produit scalaire euclidien standard, et $\|q\| = \sqrt{q^T q}$ et $\|v\| = \sqrt{v^T v}$ sont les normes euclidiennes associées.

    b.  La normalisation des vecteurs consiste à les diviser par leur norme, c'est-à-dire à remplacer $q$ par $\hat{q} = \frac{q}{\|q\|}$ et $v$ par $\hat{v} = \frac{v}{\|v\|}$. Les vecteurs normalisés $\hat{q}$ et $\hat{v}$ ont une norme égale à 1 et appartiennent donc à la sphère unité $\mathcal{S}^{d-1}$.
        Après normalisation, la similarité cosinus se simplifie en :
        $$ \cos(\theta) = \langle \hat{q}, \hat{v} \rangle = \hat{q}^T \hat{v} $$
        L'interprétation géométrique de la normalisation est que l'on ne s'intéresse plus à l'amplitude des vecteurs (qui pourrait par exemple représenter la longueur d'un document ou la fréquence d'un terme dans un document), mais uniquement à leur direction. La similarité cosinus mesure alors l'angle $\theta$ entre ces directions vectorielles. Des vecteurs pointant dans des directions similaires auront un cosinus proche de 1 (angle faible), tandis que des vecteurs pointant dans des directions opposées auront un cosinus proche de -1 (angle proche de $\pi$). Des vecteurs orthogonaux (sémantiquement indépendants) auront un cosinus de 0 (angle de $\pi/2$). Travailler sur la sphère unité rend les comparaisons angulaires directes et invariantes à l'échelle.

2.  **Dictionnaire de Vecteurs et Espace Dual :**
    a.  Soit $\phi_q: \mathcal{V} \to \mathbb{R}$ une application définie pour tout $q \in \mathcal{V}$ par $\phi_q(v) = \langle q, v \rangle$. Pour montrer que $\phi_q$ est une forme linéaire, nous devons vérifier la linéarité, c'est-à-dire que pour tous $\alpha, \beta \in \mathbb{R}$ et tous $v_1, v_2 \in \mathcal{V}$:
        $$ \phi_q(\alpha v_1 + \beta v_2) = \alpha \phi_q(v_1) + \beta \phi_q(v_2) $$
        Calculons le membre de gauche :
        $$ \phi_q(\alpha v_1 + \beta v_2) = \langle q, \alpha v_1 + \beta v_2 \rangle $$
        Par la linéarité du produit scalaire par rapport au second argument :
        $$ \langle q, \alpha v_1 + \beta v_2 \rangle = \alpha \langle q, v_1 \rangle + \beta \langle q, v_2 \rangle $$
        Par la définition de $\phi_q$:
        $$ \alpha \langle q, v_1 \rangle + \beta \langle q, v_2 \rangle = \alpha \phi_q(v_1) + \beta \phi_q(v_2) $$
        Ainsi, $\phi_q$ est bien une forme linéaire, et donc $\phi_q \in \mathcal{V}^*$.

    b.  L'application $\Psi: \mathcal{V} \to \mathcal{V}^*$ est définie par $\Psi(q) = \phi_q$. Pour montrer que $\Psi$ est un isomorphisme, nous devons prouver qu'elle est linéaire et bijective.

        *Linéarité de $\Psi$ :* Pour tous $\alpha, \beta \in \mathbb{R}$ et tous $q_1, q_2 \in \mathcal{V}$, nous devons montrer que $\Psi(\alpha q_1 + \beta q_2) = \alpha \Psi(q_1) + \beta \Psi(q_2)$.
        Cela signifie que pour tout $v \in \mathcal{V}$:
        $$ [\Psi(\alpha q_1 + \beta q_2)](v) = [\alpha \Psi(q_1) + \beta \Psi(q_2)](v) $$
        Calculons le membre de gauche :
        $$ [\Psi(\alpha q_1 + \beta q_2)](v) = \phi_{\alpha q_1 + \beta q_2}(v) = \langle \alpha q_1 + \beta q_2, v \rangle $$
        Par la linéarité du produit scalaire par rapport au premier argument :
        $$ \langle \alpha q_1 + \beta q_2, v \rangle = \alpha \langle q_1, v \rangle + \beta \langle q_2, v \rangle $$
        Par la définition de $\phi_q$:
        $$ \alpha \langle q_1, v \rangle + \beta \langle q_2, v \rangle = \alpha \phi_{q_1}(v) + \beta \phi_{q_2}(v) $$
        Ceci est par définition :
        $$ \alpha \phi_{q_1}(v) + \beta \phi_{q_2}(v) = (\alpha \Psi(q_1) + \beta \Psi(q_2))(v) $$
        Donc $\Psi$ est linéaire.

        *Injectivité de $\Psi$ :* $\Psi$ est injective si son noyau est réduit au vecteur nul. Supposons $q \in \ker(\Psi)$. Alors $\Psi(q) = \phi_q$ est la forme linéaire nulle.
        Ceci signifie que $\phi_q(v) = 0$ pour tout $v \in \mathcal{V}$.
        Donc $\langle q, v \rangle = 0$ pour tout $v \in \mathcal{V}$.
        En particulier, si nous choisissons $v = q$, nous avons $\langle q, q \rangle = 0$.
        Puisque $\langle \cdot, \cdot \rangle$ est un produit scalaire, sa définition positive implique que $\langle q, q \rangle = 0 \iff q = 0$.
        Donc $\ker(\Psi) = \{0\}$, ce qui prouve que $\Psi$ est injective.

        *Bijectivité de $\Psi$ :* Nous savons que $\Psi$ est une application linéaire injective entre deux espaces vectoriels de même dimension ($d$ pour $\mathcal{V}$ et $d$ pour $\mathcal{V}^*$). Une application linéaire injective entre espaces de même dimension est nécessairement surjective, et donc bijective.
        Par conséquent, $\Psi$ est un isomorphisme d'espaces vectoriels.

    c.  L'isomorphisme $\Psi: \mathcal{V} \to \mathcal{V}^*$ établit une équivalence fondamentale entre les vecteurs de l'espace de plongement $\mathcal{V}$ et les formes linéaires de son espace dual $\mathcal{V}^*$.
        Dans le contexte d'un moteur de recherche, cela signifie qu'une requête $q \in \mathcal{V}$ peut être conceptualisée non seulement comme un simple vecteur, mais aussi comme une "sonde" ou un "filtre" ($\phi_q \in \mathcal{V}^*$) qui mesure la pertinence de chaque document $v \in \mathcal{V}$ en lui attribuant un score $\phi_q(v) = \langle q, v \rangle$.
        Cette dualité suggère une symétrie sous-jacente : une requête peut "interroger" des documents, et inversement, un document peut être vu comme une forme linéaire qui évaluerait la pertinence de différentes requêtes. Cette perspective est utile pour comprendre des concepts plus avancés comme les espaces biduels ou des transformations de plongements qui préservent cette relation duale.

---

**Partie II : Projections A-Orthogonales et Similarité Sémantique Généralisée**

1.  **Propriétés du Produit Scalaire Généralisé :**
    Nous devons démontrer que $\langle u, v \rangle_A = u^T A v$ satisfait les trois axiomes d'un produit scalaire sur $\mathbb{R}^d$, étant donné que $A \in \mathcal{M}_{d,d}(\mathbb{R})$ est une matrice symétrique définie positive.

    a.  **Linéarité par rapport au premier argument :** Pour tous $\alpha, \beta \in \mathbb{R}$ et tous $u, w, v \in \mathbb{R}^d$:
        $$ \langle \alpha u + \beta w, v \rangle_A = (\alpha u + \beta w)^T A v $$
        En utilisant la propriété de la transposée $(X+Y)^T = X^T+Y^T$ et $(\alpha X)^T = \alpha X^T$:
        $$ (\alpha u + \beta w)^T A v = (\alpha u^T + \beta w^T) A v $$
        En développant la multiplication matricielle :
        $$ (\alpha u^T + \beta w^T) A v = \alpha u^T A v + \beta w^T A v $$
        Par la définition de notre produit scalaire généralisé :
        $$ \alpha u^T A v + \beta w^T A v = \alpha \langle u, v \rangle_A + \beta \langle w, v \rangle_A $$
        La linéarité par rapport au premier argument est satisfaite.

    b.  **Symétrie :** Pour tous $u, v \in \mathbb{R}^d$:
        $$ \langle u, v \rangle_A = u^T A v $$
        Puisque $u^T A v$ est un scalaire, il est égal à sa propre transposée :
        $$ u^T A v = (u^T A v)^T $$
        En utilisant la propriété de la transposée $(XYZ)^T = Z^T Y^T X^T$:
        $$ (u^T A v)^T = v^T A^T (u^T)^T = v^T A^T u $$
        Puisque $A$ est une matrice symétrique, $A^T = A$. Donc :
        $$ v^T A^T u = v^T A u = \langle v, u \rangle_A $$
        La symétrie est satisfaite.

    c.  **Définition positive :** Pour tout $u \in \mathbb{R}^d$, nous devons montrer que $\langle u, u \rangle_A \ge 0$, et $\langle u, u \rangle_A = 0 \iff u = 0$.
        $$ \langle u, u \rangle_A = u^T A u $$
        Par hypothèse, $A$ est une matrice symétrique définie positive. Par définition d'une matrice définie positive, pour tout $u \in \mathbb{R}^d \setminus \{0\}$, nous avons $u^T A u > 0$. Si $u=0$, alors $0^T A 0 = 0$.
        Donc, $u^T A u \ge 0$ pour tout $u \in \mathbb{R}^d$, et $u^T A u = 0 \iff u = 0$.
        La définition positive est satisfaite.

    Puisque les trois axiomes sont vérifiés, $\langle \cdot, \cdot \rangle_A$ est bien un produit scalaire sur $\mathbb{R}^d$.

2.  **Projections A-Orthogonales :**
    a.  Le sous-espace $A$-orthogonal $\mathcal{S}^{\perp_A}$ de $\mathcal{S}$ est défini par :
        $$ \mathcal{S}^{\perp_A} = \{x \in \mathbb{R}^d \mid \langle x, s \rangle_A = 0 \text{ pour tout } s \in \mathcal{S}\} $$
        Pour montrer que $\mathbb{R}^d = \mathcal{S} \oplus \mathcal{S}^{\perp_A}$, nous devons prouver que $\mathcal{S} \cap \mathcal{S}^{\perp_A} = \{0\}$ et que $\mathbb{R}^d = \mathcal{S} + \mathcal{S}^{\perp_A}$.

        *Preuve de $\mathcal{S} \cap \mathcal{S}^{\perp_A} = \{0\}$ :*
        Soit $x \in \mathcal{S} \cap \mathcal{S}^{\perp_A}$. Puisque $x \in \mathcal{S}$, et $x \in \mathcal{S}^{\perp_A}$, par la définition de $\mathcal{S}^{\perp_A}$, nous avons $\langle x, x \rangle_A = 0$.
        Or, $\langle \cdot, \cdot \rangle_A$ est un produit scalaire, donc par sa propriété de définition positive, $\langle x, x \rangle_A = 0 \iff x = 0$.
        Par conséquent, $\mathcal{S} \cap \mathcal{S}^{\perp_A} = \{0\}$.

        *Preuve de $\mathbb{R}^d = \mathcal{S} + \mathcal{S}^{\perp_A}$ :*
        Pour tout $v \in \mathbb{R}^d$, nous cherchons une décomposition unique $v = s_0 + z_0$ où $s_0 \in \mathcal{S}$ et $z_0 \in \mathcal{S}^{\perp_A}$. L'existence de $s_0 = P_A(v)$ et $z_0 = v - P_A(v)$ montrera que tout vecteur de $\mathbb{R}^d$ peut être décomposé.
        Nous savons que $\mathcal{S}$ est un sous-espace de dimension $k$.
        L'application $L_A: \mathbb{R}^d \to (\mathbb{R}^d)^*$ définie par $L_A(x)(y) = \langle x, y \rangle_A$ est un isomorphisme de $\mathbb{R}^d$ vers son dual (similaire à la Partie I.2.b).
        L'orthogonal $A$-orthogonal $\mathcal{S}^{\perp_A}$ est le noyau des formes linéaires $\phi_s(x) = \langle s, x \rangle_A$ pour $s \in \mathcal{S}$. Plus formellement, $\mathcal{S}^{\perp_A} = \{x \in \mathbb{R}^d \mid \forall s \in \mathcal{S}, s^T A x = 0\}$.
        Considérons l'application linéaire $f: \mathbb{R}^d \to \mathbb{R}^k$ définie par $f(x) = ( \langle e_1, x \rangle_A, \ldots, \langle e_k, x \rangle_A )^T$. Son noyau est $\ker(f) = \mathcal{S}^{\perp_A}$.
        L'image de $f$ a pour dimension $\text{rank}(f) = \dim(\mathbb{R}^d) - \dim(\ker(f)) = d - \dim(\mathcal{S}^{\perp_A})$.
        Puisque les $e_j$ sont linéairement indépendants et $A$ est définie positive, l'image de $f$ est de dimension $k$. En effet, si $x \in \mathcal{S}^{\perp_A}$, alors $e_j^T A x = 0$ pour tout $j$. Si $x \in \mathcal{S}$, alors $x = \sum \alpha_j e_j$.
        On peut montrer que $\dim(\mathcal{S}^{\perp_A}) = d - k$.
        Alors, $\dim(\mathcal{S} + \mathcal{S}^{\perp_A}) = \dim(\mathcal{S}) + \dim(\mathcal{S}^{\perp_A}) - \dim(\mathcal{S} \cap \mathcal{S}^{\perp_A})$.
        En utilisant $\dim(\mathcal{S} \cap \mathcal{S}^{\perp_A}) = 0$ et $\dim(\mathcal{S}^{\perp_A}) = d-k$:
        $\dim(\mathcal{S} + \mathcal{S}^{\perp_A}) = k + (d-k) - 0 = d$.
        Puisque $\mathcal{S} + \mathcal{S}^{\perp_A}$ est un sous-espace de $\mathbb{R}^d$ et qu'il a la même dimension $d$, il doit être égal à $\mathbb{R}^d$.
        Donc, $\mathbb{R}^d = \mathcal{S} \oplus \mathcal{S}^{\perp_A}$.

    b.  La projection $A$-orthogonale $P_A(v)$ de $v \in \mathbb{R}^d$ sur $\mathcal{S}$ est l'unique vecteur $s_0 \in \mathcal{S}$ tel que $v - s_0 \in \mathcal{S}^{\perp_A}$.
        Puisque $s_0 \in \mathcal{S}$ et $(e_1, \ldots, e_k)$ est une base de $\mathcal{S}$, $s_0$ peut être écrit comme une combinaison linéaire des $e_j$. Il existe donc un vecteur colonne $x \in \mathbb{R}^k$ tel que $s_0 = E x$.
        La condition $v - s_0 \in \mathcal{S}^{\perp_A}$ signifie que $v - s_0$ est $A$-orthogonal à tous les vecteurs de $\mathcal{S}$. Il suffit de vérifier cette condition pour la base $(e_1, \ldots, e_k)$ :
        $$ \langle v - s_0, e_j \rangle_A = 0 \quad \text{pour tout } j = 1, \ldots, k $$
        Ceci peut être réécrit comme :
        $$ \langle v, e_j \rangle_A - \langle s_0, e_j \rangle_A = 0 \quad \text{pour tout } j = 1, \ldots, k $$
        Ou encore :
        $$ \langle s_0, e_j \rangle_A = \langle v, e_j \rangle_A \quad \text{pour tout } j = 1, \ldots, k $$
        Substituons $s_0 = E x$:
        $$ \langle E x, e_j \rangle_A = \langle v, e_j \rangle_A \quad \text{pour tout } j = 1, \ldots, k $$
        En utilisant la définition du produit scalaire $\langle u, v \rangle_A = u^T A v$:
        $$ (E x)^T A e_j = v^T A e_j \quad \text{pour tout } j = 1, \ldots, k $$
        $$ x^T E^T A e_j = v^T A e_j \quad \text{pour tout } j = 1, \ldots, k $$
        Nous pouvons rassembler ces $k$ équations en une seule équation matricielle. Le vecteur $E^T A e_j$ est la $j$-ième colonne de $E^T A E$. Le vecteur $E^T A v$ est un vecteur colonne de $\mathbb{R}^k$.
        $$ (E^T A E) x = E^T A v $$

        *Preuve de l'hypothèse : la matrice $E^T A E$ est inversible.*
        La matrice $E^T A E$ est une matrice carrée de taille $k \times k$. Pour montrer qu'elle est inversible, nous devons montrer que son noyau est trivial, c'est-à-dire que si $(E^T A E) x = 0$ pour un $x \in \mathbb{R}^k$, alors $x=0$.
        Si $(E^T A E) x = 0$, alors en multipliant par $x^T$ à gauche :
        $$ x^T (E^T A E) x = 0 $$
        $$ (E x)^T A (E x) = 0 $$
        Soit $u = E x \in \mathbb{R}^d$. Puisque $x \in \mathbb{R}^k$, $u$ est une combinaison linéaire des colonnes de $E$, donc $u \in \mathcal{S}$.
        L'équation devient $\langle u, u \rangle_A = 0$.
        Puisque $\langle \cdot, \cdot \rangle_A$ est un produit scalaire (partie II.1), sa propriété de définition positive implique que $\langle u, u \rangle_A = 0 \iff u = 0$.
        Donc $u = E x = 0$.
        Par hypothèse, $(e_1, \ldots, e_k)$ est une base de $\mathcal{S}$, ce qui signifie que les colonnes de $E$ sont linéairement indépendantes. Par conséquent, si $E x = 0$, cela implique $x=0$.
        Ainsi, $E^T A E$ est inversible.

        Nous pouvons maintenant résoudre pour $x$:
        $$ x = (E^T A E)^{-1} E^T A v $$
        Enfin, nous substituons $x$ dans l'expression de $s_0$:
        $$ s_0 = P_A(v) = E x = E (E^T A E)^{-1} E^T A v $$
        La matrice de projection $P_A \in \mathcal{M}_{d,d}(\mathbb{R})$ est donc :
        $$ P_A = E (E^T A E)^{-1} E^T A $$

3.  **Similarité Sémantique A-Généralisée :**
    a.  La "similarité sémantique $A$-généralisée" est définie par $S_{\mathcal{S},A}(q,v) = \langle P_A(q), P_A(v) \rangle_A$.
        En utilisant la définition du produit scalaire $\langle u, w \rangle_A = u^T A w$:
        $$ S_{\mathcal{S},A}(q,v) = (P_A q)^T A (P_A v) $$
        Substituons l'expression de $P_A$:
        $$ S_{\mathcal{S},A}(q,v) = \left(E (E^T A E)^{-1} E^T A q\right)^T A \left(E (E^T A E)^{-1} E^T A v\right) $$
        Utilisons $(XY Z)^T = Z^T Y^T X^T$ :
        $$ \left(E (E^T A E)^{-1} E^T A q\right)^T = q^T A^T (E^T)^T ((E^T A E)^{-1})^T E^T $$
        Puisque $A$ est symétrique ($A^T=A$) et $E^T A E$ est symétrique (car $A$ est symétrique, donc $(E^T A E)^T = E^T A^T (E^T)^T = E^T A E$), son inverse est aussi symétrique $((E^T A E)^{-1})^T = (E^T A E)^{-1}$.
        $$ \left(E (E^T A E)^{-1} E^T A q\right)^T = q^T A E (E^T A E)^{-1} E^T $$
        Maintenant, substituons cela dans l'expression de $S_{\mathcal{S},A}(q,v)$:
        $$ S_{\mathcal{S},A}(q,v) = \left(q^T A E (E^T A E)^{-1} E^T\right) A \left(E (E^T A E)^{-1} E^T A v\right) $$
        $$ S_{\mathcal{S},A}(q,v) = q^T A E (E^T A E)^{-1} (E^T A E) (E^T A E)^{-1} E^T A v $$
        Puisque $(E^T A E)^{-1} (E^T A E) = I_k$ (matrice identité $k \times k$):
        $$ S_{\mathcal{S},A}(q,v) = q^T A E (E^T A E)^{-1} E^T A v $$
        Donc, $S_{\mathcal{S},A}(q,v)$ s'écrit bien sous la forme $q^T M_A v$, où $M_A \in \mathcal{M}_{d,d}(\mathbb{R})$ est :
        $$ M_A = A E (E^T A E)^{-1} E^T A $$

    b.  **Symétrie de $M_A$ :**
        $$ M_A^T = (A E (E^T A E)^{-1} E^T A)^T $$
        $$ M_A^T = A^T (E^T)^T ((E^T A E)^{-1})^T E^T A^T $$
        Puisque $A$ est symétrique ($A^T=A$) et $(E^T A E)^{-1}$ est symétrique :
        $$ M_A^T = A E (E^T A E)^{-1} E^T A = M_A $$
        Donc $M_A$ est une matrice symétrique.

        **Définition positive (semi-définie positive) de $M_A$ :**
        Pour tout $x \in \mathbb{R}^d$:
        $$ x^T M_A x = x^T A E (E^T A E)^{-1} E^T A x $$
        Soit $y = E^T A x \in \mathbb{R}^k$.
        $$ x^T M_A x = y^T (E^T A E)^{-1} y $$
        Comme $E^T A E$ est une matrice symétrique définie positive de taille $k \times k$ (prouvé en II.2.b), son inverse $(E^T A E)^{-1}$ est également une matrice symétrique définie positive.
        Par définition d'une matrice définie positive, pour tout $y \in \mathbb{R}^k \setminus \{0\}$, $y^T (E^T A E)^{-1} y > 0$. Si $y = 0$, alors $y^T (E^T A E)^{-1} y = 0$.
        Donc $x^T M_A x \ge 0$ pour tout $x \in \mathbb{R}^d$.
        Par conséquent, $M_A$ est une matrice positive (semi-définie positive).

        **Rang de $M_A$ :**
        La matrice $M_A = A E (E^T A E)^{-1} E^T A$.
        Puisque $A$ est une matrice définie positive, elle est inversible.
        Nous avons la propriété $\text{rank}(XYZ) = \text{rank}(Y)$ si $X$ et $Z$ sont inversibles.
        Ici, $X=A$ est inversible, et $Z=A$ est inversible.
        Donc $\text{rank}(M_A) = \text{rank}(E (E^T A E)^{-1} E^T)$.
        La matrice $(E^T A E)^{-1}$ est aussi inversible.
        Considérons la matrice $P_A = E (E^T A E)^{-1} E^T A$. C'est une matrice de projection.
        Le rang d'une matrice de projection sur un sous-espace de dimension $k$ est $k$.
        $$ \text{rank}(M_A) = \text{rank}(A P_A) $$
        Puisque $A$ est inversible, la multiplication par $A$ à gauche ne change pas le rang de $P_A$.
        $$ \text{rank}(M_A) = \text{rank}(P_A) $$
        La matrice $P_A$ est la matrice de projection $A$-orthogonale sur le sous-espace $\mathcal{S}$ de dimension $k$. Par conséquent :
        $$ \text{rank}(P_A) = k $$
        Donc, le rang de $M_A$ est $k$.

    c.  Nous avons montré à la question II.3.a que $S_{\mathcal{S},A}(q,v) = q^T M_A v$ et que $M_A = A E (E^T A E)^{-1} E^T A$.
        D'autre part, nous avons $P_A = E (E^T A E)^{-1} E^T A$.
        Donc $M_A = A P_A$.
        Calculons $P_A^T A P_A$:
        $$ P_A^T = (E (E^T A E)^{-1} E^T A)^T = A^T (E^T)^T ((E^T A E)^{-1})^T E^T = A E (E^T A E)^{-1} E^T $$
        (En utilisant $A^T=A$ et la symétrie de $(E^T A E)^{-1}$)
        $$ P_A^T A P_A = \left(A E (E^T A E)^{-1} E^T\right) A \left(E (E^T A E)^{-1} E^T A\right) $$
        $$ P_A^T A P_A = A E (E^T A E)^{-1} (E^T A E) (E^T A E)^{-1} E^T A $$
        Puisque $(E^T A E)^{-1} (E^T A E) = I_k$:
        $$ P_A^T A P_A = A E (E^T A E)^{-1} E^T A $$
        Nous voyons bien que $P_A^T A P_A = M_A$.

    d.  La "similarité cosinus $A$-généralisée" entre $u, w \in \mathbb{R}^d$ est définie par $\cos_A(\theta_{u,w}) = \frac{\langle u, w \rangle_A}{\|u\|_A \|w\|_A}$.
        Nous voulons exprimer $S_{\mathcal{S},A}(q,v) = \langle P_A(q), P_A(v) \rangle_A$ en fonction des normes $A$-généralisées des projections et de la similarité cosinus $A$-généralisée entre ces projections.
        Soient $u' = P_A(q)$ et $w' = P_A(v)$. Par la définition de la similarité cosinus $A$-généralisée, nous avons :
        $$ \cos_A(\theta_{u',w'}) = \frac{\langle u', w' \rangle_A}{\|u'\|_A \|w'\|_A} $$
        Donc :
        $$ \langle u', w' \rangle_A = \|u'\|_A \|w'\|_A \cos_A(\theta_{u',w'}) $$
        En remplaçant $u'$ et $w'$ :
        $$ S_{\mathcal{S},A}(q,v) = \|P_A(q)\|_A \|P_A(v)\|_A \cos_A(\theta_{P_A(q), P_A(v)}) $$
        La valeur de cette similarité cosinus, $\cos_A(\theta_{P_A(q), P_A(v)})$, est la mesure de l'angle entre les projections $A$-orthogonales des vecteurs $q$ et $v$ sur le sous-espace sémantique $\mathcal{S}$, calculée en utilisant le produit scalaire généralisé $\langle \cdot, \cdot \rangle_A$. Elle indique à quel point les composantes sémantiques de $q$ et $v$ (représentées par leurs projections sur $\mathcal{S}$) pointent dans la même direction, selon la métrique $A$. Elle serait 1 si les projections étaient $A$-parallèles et 0 si elles étaient $A$-orthogonales.

---