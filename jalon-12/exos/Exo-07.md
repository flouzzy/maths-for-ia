Cher Étudiant,

Nous voici au Jalon 12 de notre parcours, où la théorie des espaces de plongement et la dualité rencontrent l'ingénierie des moteurs de recherche sémantiques. L'exercice qui suit est conçu pour consolider votre compréhension de la géométrie vectorielle sous-jacente à la notion de similarité, et pour vous confronter à un problème d'algèbre linéaire de haut niveau, tel qu'il pourrait être posé aux Grandes Écoles.

Préparons-nous à explorer les subtilités des métriques non euclidiennes et leur impact sur la projection orthogonale et la structure duale d'un espace.

---

## Exercice 7 : Géométrie Sémantique, Projection et Dualité dans les Espaces de Plongement

**Contexte :**
Dans le domaine des moteurs de recherche sémantiques et du traitement du langage naturel, les entités (mots, phrases, documents) sont souvent représentées par des vecteurs dans des "espaces de plongement" (embedding spaces). La similarité entre ces entités est mesurée par la similarité cosinus. Habituellement, on utilise le produit scalaire euclidien standard. Cependant, il est parfois souhaitable d'introduire une métrique plus complexe, "sémantiquement informée", qui pondère différemment les dimensions de l'espace de plongement. Cette métrique peut être encodée par une matrice définie positive, modifiant ainsi la géométrie de l'espace.

Cet exercice explore les propriétés d'un tel espace vectoriel muni d'un produit scalaire généralisé, la projection orthogonale sémantique sur un sous-espace, et les concepts de dualité associés.

**Hypothèses Fondamentales :**
*   Soit $V$ un espace vectoriel réel de dimension finie $n \in \mathbb{N}^*$.
*   Soit $B_E = (e_1, \ldots, e_n)$ une base orthonormée de $V$ pour le produit scalaire euclidien standard, noté $\langle \cdot, \cdot \rangle_E$. Pour tout $u = \sum_{i=1}^n u_i e_i$ et $v = \sum_{i=1}^n v_i e_i$ dans $V$, $\langle u, v \rangle_E = \sum_{i=1}^n u_i v_i$.
*   Pour tout $v \in V$, $v$ peut être représenté par son vecteur de coordonnées $X_v = (v_1, \ldots, v_n)^T \in \mathbb{R}^n$ dans la base $B_E$. Ainsi, $\langle u, v \rangle_E = X_u^T X_v$.
*   Soit $S \in \mathcal{M}_n(\mathbb{R})$ une matrice symétrique et définie positive.

---

### Énoncé

**Partie I : Introduction du Produit Scalaire Sémantique**

Nous définissons une nouvelle forme bilinéaire $\langle \cdot, \cdot \rangle_S: V \times V \to \mathbb{R}$ pour tout $u, v \in V$ par :
$$ \langle u, v \rangle_S = X_u^T S X_v $$
où $X_u$ et $X_v$ sont les vecteurs de coordonnées de $u$ et $v$ dans la base $B_E$.

1.  Démontrer que $\langle \cdot, \cdot \rangle_S$ est un produit scalaire sur $V$.
2.  Nous définissons la norme sémantique associée $\|\cdot\|_S$ et la similarité cosinus sémantique $C_S(u,v)$ pour $u, v \in V \setminus \{0_V\}$.
    Expliciter les définitions de $\|u\|_S$ et $C_S(u,v)$ en fonction de $X_u$, $X_v$ et $S$.

**Partie II : Projection Orthogonale Sémantique**

Soit $W$ un sous-espace vectoriel de $V$ de dimension $k \in \{1, \ldots, n-1\}$. Soit $B_W = (w_1, \ldots, w_k)$ une base de $W$.

1.  Définir l'orthogonal sémantique $W^{\perp_S}$ de $W$ par rapport au produit scalaire $\langle \cdot, \cdot \rangle_S$.
2.  Démontrer que $W^{\perp_S}$ est un sous-espace vectoriel de $V$.
3.  Démontrer que $V = W \oplus W^{\perp_S}$, c'est-à-dire que $W \cap W^{\perp_S} = \{0_V\}$ et $\dim(W) + \dim(W^{\perp_S}) = \dim(V)$.
4.  Pour tout $v \in V$, il existe une unique décomposition $v = p + r$ où $p \in W$ et $r \in W^{\perp_S}$. $p$ est appelé la projection orthogonale sémantique de $v$ sur $W$, notée $P_S(v)$.
    Soit $X_{w_j} \in \mathbb{R}^n$ le vecteur de coordonnées de $w_j$ pour $j=1, \ldots, k$. Soit $M_W \in \mathcal{M}_{n,k}(\mathbb{R})$ la matrice dont les colonnes sont les vecteurs $X_{w_1}, \ldots, X_{w_k}$.
    Expliciter la matrice de Gram sémantique $G_S \in \mathcal{M}_k(\mathbb{R})$ associée à la base $B_W$ et au produit scalaire $\langle \cdot, \cdot \rangle_S$.
    Démontrer que $G_S$ est inversible.
5.  Pour un vecteur $v \in V$ donné, $P_S(v)$ peut s'écrire $P_S(v) = \sum_{i=1}^k \alpha_i w_i$ pour des coefficients $\alpha_i \in \mathbb{R}$.
    Dériver une expression explicite pour le vecteur colonne des coefficients $\alpha = (\alpha_1, \ldots, \alpha_k)^T$ en fonction de $M_W$, $S$, et $X_v$.
    En déduire une expression pour $P_S(v)$ dans la base $B_E$.

**Partie III : Dualité et Annihilateur Sémantique**

Soit $V^*$ le dual de $V$, c'est-à-dire l'espace des formes linéaires sur $V$.

1.  Pour chaque $u \in V$, nous définissons une forme linéaire $\phi_u \in V^*$ par $\phi_u(v) = \langle u, v \rangle_S$ pour tout $v \in V$.
    Démontrer que l'application $\Phi_S: V \to V^*$ définie par $\Phi_S(u) = \phi_u$ est un isomorphisme linéaire.
2.  Soit $W^{\circ_S}$ l'annihilateur sémantique de $W$ dans $V^*$, défini comme $W^{\circ_S} = \{ f \in V^* \mid f(w) = 0 \text{ pour tout } w \in W \}$.
    Démontrer que $W^{\circ_S}$ est un sous-espace vectoriel de $V^*$.
    Déterminer la dimension de $W^{\circ_S}$.
3.  Établir une relation précise entre $W^{\perp_S}$ et $W^{\circ_S}$ en utilisant l'isomorphisme $\Phi_S$. Démontrer cette relation.

---

### Correction

**Typage Strict des Objets :**
*   $V$: Espace vectoriel réel de dimension finie $n$.
*   $n$: Entier naturel non nul, $\dim(V)$.
*   $B_E = (e_1, \ldots, e_n)$: Base orthonormée de $V$ pour le produit scalaire euclidien.
*   $\langle \cdot, \cdot \rangle_E$: Produit scalaire euclidien sur $V$.
*   $u, v$: Vecteurs de $V$.
*   $X_u, X_v$: Vecteurs colonnes de coordonnées dans $\mathbb{R}^n$ pour $u$ et $v$ respectivement. $X_u \in \mathbb{R}^n$, $X_v \in \mathbb{R}^n$.
*   $S$: Matrice carrée de taille $n \times n$, $S \in \mathcal{M}_n(\mathbb{R})$. $S$ est symétrique ($S^T = S$) et définie positive ($X^T S X > 0$ pour tout $X \in \mathbb{R}^n \setminus \{0\}$).
*   $\langle \cdot, \cdot \rangle_S$: Forme bilinéaire sur $V \times V$, qui sera démontrée être un produit scalaire.
*   $\|\cdot\|_S$: Norme associée au produit scalaire $\langle \cdot, \cdot \rangle_S$.
*   $C_S(\cdot, \cdot)$: Similarité cosinus associée au produit scalaire $\langle \cdot, \cdot \rangle_S$.
*   $W$: Sous-espace vectoriel de $V$.
*   $k$: Entier naturel, $\dim(W)$, $1 \le k \le n-1$.
*   $B_W = (w_1, \ldots, w_k)$: Base de $W$. $w_j \in W \subset V$.
*   $X_{w_j}$: Vecteur colonne de coordonnées de $w_j$ dans $B_E$, $X_{w_j} \in \mathbb{R}^n$.
*   $M_W$: Matrice $n \times k$ dont les colonnes sont $X_{w_1}, \ldots, X_{w_k}$. $M_W \in \mathcal{M}_{n,k}(\mathbb{R})$.
*   $G_S$: Matrice de Gram sémantique, $G_S \in \mathcal{M}_k(\mathbb{R})$.
*   $P_S(v)$: Projection orthogonale sémantique de $v$ sur $W$. $P_S(v) \in W \subset V$.
*   $p$: Vecteur de $W$.
*   $r$: Vecteur de $W^{\perp_S}$.
*   $\alpha = (\alpha_1, \ldots, \alpha_k)^T$: Vecteur colonne de coefficients dans $\mathbb{R}^k$.
*   $V^*$: Espace dual de $V$, l'ensemble des formes linéaires $f: V \to \mathbb{R}$.
*   $\phi_u$: Forme linéaire associée à $u \in V$. $\phi_u \in V^*$.
*   $\Phi_S$: Application linéaire $V \to V^*$.
*   $W^{\circ_S}$: Annihilateur sémantique de $W$ dans $V^*$. $W^{\circ_S} \subset V^*$.

---

### Correction Détaillée

**Partie I : Introduction du Produit Scalaire Sémantique**

1.  **Démonstration que $\langle \cdot, \cdot \rangle_S$ est un produit scalaire sur $V$.**
    Pour que $\langle \cdot, \cdot \rangle_S$ soit un produit scalaire, il doit satisfaire les propriétés suivantes :
    a.  **Bilinéarité :** Pour tous $u, v, w \in V$ et tout $\lambda \in \mathbb{R}$ :
        *   **Linéarité par rapport à la première variable :**
            $\langle u + \lambda v, w \rangle_S = X_{u+\lambda v}^T S X_w$.
            Par la linéarité des coordonnées, $X_{u+\lambda v} = X_u + \lambda X_v$.
            Donc, $\langle u + \lambda v, w \rangle_S = (X_u + \lambda X_v)^T S X_w$.
            Par la distributivité de la transposition et du produit matriciel, $(X_u + \lambda X_v)^T = X_u^T + \lambda X_v^T$.
            Ainsi, $\langle u + \lambda v, w \rangle_S = (X_u^T + \lambda X_v^T) S X_w$.
            Par la distributivité du produit matriciel, $(X_u^T + \lambda X_v^T) S X_w = X_u^T S X_w + \lambda X_v^T S X_w$.
            Ceci est égal à $\langle u, w \rangle_S + \lambda \langle v, w \rangle_S$.
            La linéarité par rapport à la première variable est démontrée.
        *   **Linéarité par rapport à la deuxième variable :**
            $\langle u, v + \lambda w \rangle_S = X_u^T S X_{v+\lambda w}$.
            Par la linéarité des coordonnées, $X_{v+\lambda w} = X_v + \lambda X_w$.
            Donc, $\langle u, v + \lambda w \rangle_S = X_u^T S (X_v + \lambda X_w)$.
            Par la distributivité du produit matriciel, $X_u^T S (X_v + \lambda X_w) = X_u^T S X_v + \lambda X_u^T S X_w$.
            Ceci est égal à $\langle u, v \rangle_S + \lambda \langle u, w \rangle_S$.
            La bilinéarité est démontrée.

    b.  **Symétrie :** Pour tous $u, v \in V$ :
        $\langle u, v \rangle_S = X_u^T S X_v$.
        Puisque le résultat est un scalaire (un réel), il est égal à sa propre transposée :
        $\langle u, v \rangle_S = (X_u^T S X_v)^T$.
        Par la propriété $(AB)^T = B^T A^T$ appliquée aux matrices $X_u^T$, $S$, $X_v$ (considérées comme des matrices de tailles $1 \times n$, $n \times n$, $n \times 1$ respectivement) :
        $(X_u^T S X_v)^T = X_v^T S^T (X_u^T)^T$.
        Comme $S$ est symétrique, $S^T = S$. Et $(X_u^T)^T = X_u$.
        Donc, $(X_u^T S X_v)^T = X_v^T S X_u$.
        Ceci est la définition de $\langle v, u \rangle_S$.
        Ainsi, $\langle u, v \rangle_S = \langle v, u \rangle_S$. La symétrie est démontrée.

    c.  **Définie-positivité :** Pour tout $u \in V$ :
        $\langle u, u \rangle_S = X_u^T S X_u$.
        Puisque $S$ est une matrice définie positive, par définition, pour tout vecteur colonne $X \in \mathbb{R}^n \setminus \{0\}$, $X^T S X > 0$.
        Si $u \neq 0_V$, alors son vecteur de coordonnées $X_u \neq 0_{\mathbb{R}^n}$.
        Donc, $X_u^T S X_u > 0$, ce qui signifie $\langle u, u \rangle_S > 0$.
        Si $u = 0_V$, alors $X_u = 0_{\mathbb{R}^n}$. Donc $\langle 0_V, 0_V \rangle_S = X_{0_V}^T S X_{0_V} = 0^T S 0 = 0$.
        La définie-positivité est démontrée.

    Ayant satisfait les trois propriétés, $\langle \cdot, \cdot \rangle_S$ est bien un produit scalaire sur $V$.

2.  **Définitions de la norme sémantique $\|\cdot\|_S$ et de la similarité cosinus sémantique $C_S(u,v)$.**
    *   La norme associée à un produit scalaire $\langle \cdot, \cdot \rangle_S$ est définie par $\|u\|_S = \sqrt{\langle u, u \rangle_S}$.
        En utilisant l'expression du produit scalaire sémantique :
        $$ \|u\|_S = \sqrt{X_u^T S X_u} $$
    *   La similarité cosinus entre deux vecteurs non nuls $u, v \in V \setminus \{0_V\}$ est définie par $C_S(u,v) = \frac{\langle u, v \rangle_S}{\|u\|_S \|v\|_S}$.
        En utilisant les expressions du produit scalaire et de la norme sémantiques :
        $$ C_S(u,v) = \frac{X_u^T S X_v}{\sqrt{X_u^T S X_u} \sqrt{X_v^T S X_v}} $$

**Partie II : Projection Orthogonale Sémantique**

1.  **Définition de l'orthogonal sémantique $W^{\perp_S}$.**
    L'orthogonal sémantique de $W$ est l'ensemble des vecteurs de $V$ qui sont orthogonaux à tous les vecteurs de $W$ selon le produit scalaire $\langle \cdot, \cdot \rangle_S$.
    $$ W^{\perp_S} = \{ v \in V \mid \langle v, w \rangle_S = 0 \text{ pour tout } w \in W \} $$

2.  **Démonstration que $W^{\perp_S}$ est un sous-espace vectoriel de $V$.**
    Pour montrer que $W^{\perp_S}$ est un sous-espace vectoriel, il faut vérifier trois points :
    a.  **$W^{\perp_S}$ n'est pas vide :** Le vecteur nul $0_V \in V$ appartient à $W^{\perp_S}$. En effet, pour tout $w \in W$, $\langle 0_V, w \rangle_S = X_{0_V}^T S X_w = 0^T S X_w = 0$. Donc $0_V \in W^{\perp_S}$.
    b.  **Stabilité par addition :** Soient $v_1, v_2 \in W^{\perp_S}$. Cela signifie que pour tout $w \in W$, $\langle v_1, w \rangle_S = 0$ et $\langle v_2, w \rangle_S = 0$.
        Considérons $v_1 + v_2$. Pour tout $w \in W$, par la linéarité du produit scalaire par rapport à la première variable :
        $\langle v_1 + v_2, w \rangle_S = \langle v_1, w \rangle_S + \langle v_2, w \rangle_S = 0 + 0 = 0$.
        Donc $v_1 + v_2 \in W^{\perp_S}$.
    c.  **Stabilité par multiplication scalaire :** Soient $v \in W^{\perp_S}$ et $\lambda \in \mathbb{R}$. Cela signifie que pour tout $w \in W$, $\langle v, w \rangle_S = 0$.
        Considérons $\lambda v$. Pour tout $w \in W$, par la linéarité du produit scalaire par rapport à la première variable :
        $\langle \lambda v, w \rangle_S = \lambda \langle v, w \rangle_S = \lambda \cdot 0 = 0$.
        Donc $\lambda v \in W^{\perp_S}$.
    Ces trois points prouvent que $W^{\perp_S}$ est un sous-espace vectoriel de $V$.

3.  **Démonstration que $V = W \oplus W^{\perp_S}$.**
    Il s'agit de montrer que $W \cap W^{\perp_S} = \{0_V\}$ et que $\dim(W) + \dim(W^{\perp_S}) = \dim(V)$.

    a.  **Démonstration de $W \cap W^{\perp_S} = \{0_V\}$ :**
        Soit $v \in W \cap W^{\perp_S}$.
        Puisque $v \in W^{\perp_S}$, par définition, $\langle v, w \rangle_S = 0$ pour tout $w \in W$.
        Puisque $v \in W$, nous pouvons en particulier prendre $w = v$.
        Donc, $\langle v, v \rangle_S = 0$.
        Par la propriété de définie-positivité du produit scalaire $\langle \cdot, \cdot \rangle_S$ (démontrée en Partie I, question 1.c), $\langle v, v \rangle_S = 0$ implique que $v = 0_V$.
        Ainsi, $W \cap W^{\perp_S} = \{0_V\}$.

    b.  **Démonstration de $\dim(W) + \dim(W^{\perp_S}) = \dim(V)$ :**
        Soit $B_W = (w_1, \ldots, w_k)$ une base de $W$.
        Un vecteur $v \in V$ appartient à $W^{\perp_S}$ si et seulement si $\langle v, w_j \rangle_S = 0$ pour tout $j \in \{1, \ldots, k\}$.
        Chaque condition $\langle v, w_j \rangle_S = 0$ est une équation linéaire homogène pour les coordonnées de $v$.
        Exprimons ceci en termes matriciels. Soit $X_v$ le vecteur de coordonnées de $v$ dans $B_E$.
        Les conditions sont $X_v^T S X_{w_j} = 0$ pour $j=1, \ldots, k$.
        Ceci peut être réécrit comme $X_{w_j}^T S X_v = 0$ (par symétrie du produit scalaire).
        Construisons la matrice $M_W \in \mathcal{M}_{n,k}(\mathbb{R})$ dont les colonnes sont $X_{w_1}, \ldots, X_{w_k}$.
        Alors, l'ensemble des conditions peut s'écrire $M_W^T S X_v = 0_{\mathbb{R}^k}$.
        C'est un système linéaire homogène de $k$ équations à $n$ inconnues ($X_v$).
        L'espace $W^{\perp_S}$ est l'ensemble des vecteurs $v$ dont les coordonnées $X_v$ sont dans le noyau de l'application linéaire représentée par $M_W^T S$.
        Ainsi, $\dim(W^{\perp_S}) = n - \mathrm{rang}(M_W^T S)$.
        Puisque $S$ est une matrice symétrique définie positive, elle est inversible.
        La matrice $M_W^T S$ est de taille $k \times n$.
        Le rang de $M_W^T S$ est égal au rang de $M_W^T$ car $S$ est inversible et le produit par une matrice inversible ne change pas le rang : $\mathrm{rang}(M_W^T S) = \mathrm{rang}(M_W^T)$.
        De plus, $\mathrm{rang}(M_W^T) = \mathrm{rang}(M_W)$.
        Les colonnes de $M_W$ sont les vecteurs de coordonnées d'une base $(w_1, \ldots, w_k)$ de $W$. Puisque ces vecteurs sont linéairement indépendants, le rang de $M_W$ est $k$.
        Donc, $\mathrm{rang}(M_W^T S) = k$.
        Par le théorème du rang, $\dim(W^{\perp_S}) = n - k$.
        Puisque $\dim(W) = k$, nous avons bien $\dim(W) + \dim(W^{\perp_S}) = k + (n-k) = n = \dim(V)$.

    De $W \cap W^{\perp_S} = \{0_V\}$ et $\dim(W) + \dim(W^{\perp_S}) = \dim(V)$, il résulte que $V = W \oplus W^{\perp_S}$.

4.  **Matrice de Gram sémantique $G_S$ et son inversibilité.**
    La matrice de Gram sémantique $G_S \in \mathcal{M}_k(\mathbb{R})$ associée à la base $B_W = (w_1, \ldots, w_k)$ et au produit scalaire $\langle \cdot, \cdot \rangle_S$ a pour éléments $(G_S)_{ij} = \langle w_i, w_j \rangle_S$.
    En utilisant la définition du produit scalaire sémantique :
    $(G_S)_{ij} = X_{w_i}^T S X_{w_j}$.
    La matrice $M_W$ a pour colonnes $X_{w_1}, \ldots, X_{w_k}$. Donc $M_W = (X_{w_1} | \ldots | X_{w_k})$.
    Alors $M_W^T = \begin{pmatrix} X_{w_1}^T \\ \vdots \\ X_{w_k}^T \end{pmatrix}$.
    Le produit matriciel $M_W^T S M_W$ est :
    $$ M_W^T S M_W = \begin{pmatrix} X_{w_1}^T \\ \vdots \\ X_{w_k}^T \end{pmatrix} S (X_{w_1} | \ldots | X_{w_k}) = \begin{pmatrix} X_{w_1}^T S X_{w_1} & \ldots & X_{w_1}^T S X_{w_k} \\ \vdots & \ddots & \vdots \\ X_{w_k}^T S X_{w_1} & \ldots & X_{w_k}^T S X_{w_k} \end{pmatrix} $$
    Ainsi, la matrice de Gram sémantique est $G_S = M_W^T S M_W$.

    **Démonstration que $G_S$ est inversible :**
    La matrice $G_S$ est une matrice de Gram pour le produit scalaire $\langle \cdot, \cdot \rangle_S$ et la base $B_W = (w_1, \ldots, w_k)$.
    Puisque $B_W$ est une base de $W$, ses vecteurs sont linéairement indépendants.
    Nous pouvons démontrer l'inversibilité en montrant que son noyau est trivial. Soit $\alpha = (\alpha_1, \ldots, \alpha_k)^T \in \mathbb{R}^k$ tel que $G_S \alpha = 0_{\mathbb{R}^k}$.
    Cela signifie $\sum_{j=1}^k (G_S)_{ij} \alpha_j = 0$ pour tout $i=1, \ldots, k$.
    C'est-à-dire $\sum_{j=1}^k \langle w_i, w_j \rangle_S \alpha_j = 0$ pour tout $i=1, \ldots, k$.
    Considérons le vecteur $w = \sum_{j=1}^k \alpha_j w_j \in W$.
    Alors pour tout $i \in \{1, \ldots, k\}$, $\langle w_i, w \rangle_S = \langle w_i, \sum_{j=1}^k \alpha_j w_j \rangle_S = \sum_{j=1}^k \alpha_j \langle w_i, w_j \rangle_S = 0$.
    Puisque $w$ est orthogonal à tous les vecteurs de la base $B_W$ de $W$, il est orthogonal à tout vecteur de $W$. C'est-à-dire $w \in W^{\perp_S}$.
    Puisque $w \in W$ par construction, nous avons $w \in W \cap W^{\perp_S}$.
    D'après la question 3.a de cette partie, $W \cap W^{\perp_S} = \{0_V\}$.
    Donc $w = 0_V$.
    $w = \sum_{j=1}^k \alpha_j w_j = 0_V$.
    Comme $B_W = (w_1, \ldots, w_k)$ est une base, les vecteurs $w_j$ sont linéairement indépendants.
    Par conséquent, tous les coefficients $\alpha_j$ doivent être nuls : $\alpha_1 = \ldots = \alpha_k = 0$.
    Le noyau de $G_S$ est donc trivial, ce qui signifie que $G_S$ est inversible.

5.  **Dérivation de l'expression des coefficients $\alpha$ pour $P_S(v)$.**
    Nous savons que $v = P_S(v) + r$, où $P_S(v) \in W$ et $r \in W^{\perp_S}$.
    Soit $P_S(v) = p$. Puisque $p \in W$ et $B_W = (w_1, \ldots, w_k)$ est une base de $W$, $p$ s'écrit de manière unique comme $p = \sum_{i=1}^k \alpha_i w_i$ pour des coefficients $\alpha_i \in \mathbb{R}$.
    Le fait que $r \in W^{\perp_S}$ signifie que $v - p \in W^{\perp_S}$.
    Par définition de $W^{\perp_S}$, cela implique que $\langle v - p, w_j \rangle_S = 0$ pour tout $j \in \{1, \ldots, k\}$.
    En substituant $p = \sum_{i=1}^k \alpha_i w_i$, nous obtenons :
    $\langle v - \sum_{i=1}^k \alpha_i w_i, w_j \rangle_S = 0$ pour tout $j \in \{1, \ldots, k\}$.
    Par linéarité du produit scalaire :
    $\langle v, w_j \rangle_S - \langle \sum_{i=1}^k \alpha_i w_i, w_j \rangle_S = 0$.
    $\langle v, w_j \rangle_S - \sum_{i=1}^k \alpha_i \langle w_i, w_j \rangle_S = 0$.
    Ceci peut être réécrit comme :
    $\sum_{i=1}^k \alpha_i \langle w_i, w_j \rangle_S = \langle v, w_j \rangle_S$ pour tout $j \in \{1, \ldots, k\}$.

    Ceci est un système de $k$ équations linéaires pour les $k$ inconnues $\alpha_1, \ldots, \alpha_k$.
    Identifions les composantes de ce système matriciel :
    *   La matrice des coefficients est la matrice de Gram sémantique $G_S$, où $(G_S)_{ji} = \langle w_j, w_i \rangle_S$. (Notez l'ordre des indices pour correspondre à $G_S \alpha = b$).
    *   Le vecteur des inconnues est $\alpha = (\alpha_1, \ldots, \alpha_k)^T$.
    *   Le vecteur du second membre $b = (b_1, \ldots, b_k)^T$ est défini par $b_j = \langle v, w_j \rangle_S$.

    En écriture matricielle, le système est :
    $$ G_S \alpha = b $$
    où $G_S = M_W^T S M_W$ (comme vu en question 4).
    Le vecteur $b$ peut être écrit comme :
    $b_j = \langle v, w_j \rangle_S = X_v^T S X_{w_j}$.
    Donc $b = \begin{pmatrix} X_v^T S X_{w_1} \\ \vdots \\ X_v^T S X_{w_k} \end{pmatrix}$.
    Ceci est équivalent à $b = \begin{pmatrix} X_{w_1}^T S X_v \\ \vdots \\ X_{w_k}^T S X_v \end{pmatrix} = M_W^T S X_v$.

    Puisque nous avons démontré que $G_S$ est inversible (question 4), nous pouvons résoudre pour $\alpha$:
    $$ \alpha = G_S^{-1} b $$
    En substituant les expressions pour $G_S$ et $b$:
    $$ \alpha = (M_W^T S M_W)^{-1} (M_W^T S X_v) $$
    Cette expression donne le vecteur colonne des coefficients $\alpha_i$.

    **Expression pour $P_S(v)$ dans la base $B_E$ :**
    Nous avons $P_S(v) = \sum_{i=1}^k \alpha_i w_i$.
    Le vecteur de coordonnées de $P_S(v)$ dans la base $B_E$ est $X_{P_S(v)}$.
    Puisque $M_W$ est la matrice dont les colonnes sont les $X_{w_i}$, nous pouvons écrire $X_p = M_W \alpha$.
    Donc, en substituant l'expression de $\alpha$:
    $$ X_{P_S(v)} = M_W (M_W^T S M_W)^{-1} (M_W^T S X_v) $$
    Cette formule fournit le vecteur de coordonnées de la projection orthogonale sémantique de $v$ sur $W$ dans la base $B_E$. Le vecteur $P_S(v)$ lui-même est la combinaison linéaire des $e_i$ avec ces coordonnées.

**Partie III : Dualité et Annihilateur Sémantique**

1.  **Démonstration que $\Phi_S: V \to V^*$ est un isomorphisme linéaire.**
    L'application $\Phi_S(u) = \phi_u$ est définie par $\phi_u(v) = \langle u, v \rangle_S$.

    a.  **Linéarité de $\Phi_S$ :** Pour tous $u_1, u_2 \in V$ et tout $\lambda \in \mathbb{R}$.
        Nous devons montrer que $\Phi_S(u_1 + \lambda u_2) = \Phi_S(u_1) + \lambda \Phi_S(u_2)$.
        Ceci signifie que pour tout $v \in V$, $(\Phi_S(u_1 + \lambda u_2))(v) = (\Phi_S(u_1) + \lambda \Phi_S(u_2))(v)$.
        Le membre de gauche est $\phi_{u_1 + \lambda u_2}(v) = \langle u_1 + \lambda u_2, v \rangle_S$.
        Par la linéarité du produit scalaire par rapport à la première variable :
        $\langle u_1 + \lambda u_2, v \rangle_S = \langle u_1, v \rangle_S + \lambda \langle u_2, v \rangle_S$.
        Le membre de droite est $(\Phi_S(u_1) + \lambda \Phi_S(u_2))(v) = \phi_{u_1}(v) + \lambda \phi_{u_2}(v)$.
        Par définition de $\phi_u$: $\phi_{u_1}(v) + \lambda \phi_{u_2}(v) = \langle u_1, v \rangle_S + \lambda \langle u_2, v \rangle_S$.
        Les deux membres sont égaux. Donc $\Phi_S$ est linéaire.

    b.  **Injectivité de $\Phi_S$ :**
        Soit $u \in V$ tel que $\Phi_S(u) = 0_{V^*}$ (la forme linéaire nulle).
        Cela signifie que pour tout $v \in V$, $\phi_u(v) = 0$.
        Donc, pour tout $v \in V$, $\langle u, v \rangle_S = 0$.
        En particulier, en prenant $v=u$, nous avons $\langle u, u \rangle_S = 0$.
        Par la définie-positivité du produit scalaire $\langle \cdot, \cdot \rangle_S$, ceci implique $u = 0_V$.
        Le noyau de $\Phi_S$ est $\{0_V\}$, donc $\Phi_S$ est injective.

    c.  **Surjectivité de $\Phi_S$ :**
        Nous savons que $V$ est un espace vectoriel réel de dimension finie $n$.
        Son dual $V^*$ est également un espace vectoriel réel de dimension finie.
        Il est un théorème fondamental d'algèbre linéaire que $\dim(V^*) = \dim(V) = n$.
        Puisque $\Phi_S$ est une application linéaire injective entre deux espaces de même dimension finie, elle est nécessairement surjective.
        (Pour une preuve plus directe sans utiliser le théorème de la dimension du dual, on peut utiliser le théorème de représentation de Riesz, qui garantit l'existence d'un unique $u \in V$ pour chaque $f \in V^*$ tel que $f(v) = \langle u, v \rangle_S$ pour tout $v$. Cet $u$ est précisément $\Phi_S^{-1}(f)$).

    Puisque $\Phi_S$ est linéaire, injective et surjective, c'est un isomorphisme linéaire.

2.  **Démonstration que $W^{\circ_S}$ est un sous-espace vectoriel de $V^*$ et détermination de sa dimension.**
    $W^{\circ_S} = \{ f \in V^* \mid f(w) = 0 \text{ pour tout } w \in W \}$.

    a.  **$W^{\circ_S}$ est un sous-espace vectoriel de $V^*$ :**
        *   **Non-vide :** La forme linéaire nulle $0_{V^*}$ est telle que $0_{V^*}(w) = 0$ pour tout $w \in W$. Donc $0_{V^*} \in W^{\circ_S}$.
        *   **Stabilité par addition :** Soient $f_1, f_2 \in W^{\circ_S}$. Pour tout $w \in W$, $f_1(w) = 0$ et $f_2(w) = 0$.
            Alors $(f_1 + f_2)(w) = f_1(w) + f_2(w) = 0 + 0 = 0$. Donc $f_1 + f_2 \in W^{\circ_S}$.
        *   **Stabilité par multiplication scalaire :** Soient $f \in W^{\circ_S}$ et $\lambda \in \mathbb{R}$. Pour tout $w \in W$, $f(w) = 0$.
            Alors $(\lambda f)(w) = \lambda f(w) = \lambda \cdot 0 = 0$. Donc $\lambda f \in W^{\circ_S}$.
        Ces trois points prouvent que $W^{\circ_S}$ est un sous-espace vectoriel de $V^*$.

    b.  **Détermination de la dimension de $W^{\circ_S}$ :**
        Nous savons que pour un sous-espace $W$ d'un espace de dimension finie $V$, la dimension de son annihilateur $W^\circ$ (défini sans référence à un produit scalaire spécifique, i.e., $W^\circ = \{f \in V^* \mid f(w)=0 \text{ pour tout } w \in W\}$) est donnée par $\dim(W^\circ) = \dim(V) - \dim(W)$.
        La définition de $W^{\circ_S}$ que nous avons donnée *est* la définition standard de l'annihilateur d'un sous-espace $W$ dans le dual $V^*$. Le "S" n'indique pas un changement dans la *définition* de l'annihilateur, mais plutôt une connexion future avec le produit scalaire sémantique.
        Ainsi, $\dim(W^{\circ_S}) = \dim(V) - \dim(W) = n - k$.

3.  **Relation précise entre $W^{\perp_S}$ et $W^{\circ_S}$ et démonstration de cette relation.**
    Nous avons montré que $\Phi_S: V \to V^*$ est un isomorphisme linéaire. Nous pouvons l'utiliser pour relier les deux sous-espaces.
    La relation est : $W^{\circ_S} = \Phi_S(W^{\perp_S})$.

    **Démonstration :**
    *   **$\Phi_S(W^{\perp_S}) \subseteq W^{\circ_S}$ :**
        Soit $f \in \Phi_S(W^{\perp_S})$. Par définition, il existe un $u \in W^{\perp_S}$ tel que $f = \Phi_S(u)$.
        Par définition de $\Phi_S$, $f(v) = \phi_u(v) = \langle u, v \rangle_S$ pour tout $v \in V$.
        Puisque $u \in W^{\perp_S}$, par définition de $W^{\perp_S}$, $\langle u, w \rangle_S = 0$ pour tout $w \in W$.
        Donc, pour tout $w \in W$, $f(w) = \langle u, w \rangle_S = 0$.
        Par définition de $W^{\circ_S}$, ceci signifie que $f \in W^{\circ_S}$.
        Par conséquent, $\Phi_S(W^{\perp_S}) \subseteq W^{\circ_S}$.

    *   **$W^{\circ_S} \subseteq \Phi_S(W^{\perp_S})$ :**
        Soit $f \in W^{\circ_S}$. Par définition, $f \in V^*$ et $f(w) = 0$ pour tout $w \in W$.
        Puisque $\Phi_S$ est un isomorphisme (et donc surjectif), il existe un unique $u \in V$ tel que $f = \Phi_S(u)$.
        Cela signifie que pour tout $v \in V$, $f(v) = \langle u, v \rangle_S$.
        Puisque $f \in W^{\circ_S}$, nous savons que $f(w) = 0$ pour tout $w \in W$.
        Donc, $\langle u, w \rangle_S = 0$ pour tout $w \in W$.
        Par définition de $W^{\perp_S}$, ceci signifie que $u \in W^{\perp_S}$.
        Puisque $f = \Phi_S(u)$ et $u \in W^{\perp_S}$, il s'ensuit que $f \in \Phi_S(W^{\perp_S})$.
        Par conséquent, $W^{\circ_S} \subseteq \Phi_S(W^{\perp_S})$.

    De l'inclusion mutuelle des deux ensembles, nous concluons que $W^{\circ_S} = \Phi_S(W^{\perp_S})$.
    Cette relation est fondamentale et montre comment l'orthogonalité (géométrique, définie par le produit scalaire) et l'annihilation (algébrique, définie par les formes linéaires) sont intrinsèquement liées dans un espace de Hilbert de dimension finie via l'isomorphisme de Riesz (ici $\Phi_S$). Elle souligne que les "conditions d'orthogonalité sémantique" sont équivalentes aux "conditions d'annulation sémantique" dans le dual.

---

J'espère que cet exercice vous aura permis d'apprécier la richesse de la géométrie des espaces vectoriels et le rôle crucial de la dualité, même dans des applications modernes comme la conception de moteurs de recherche sémantiques. L'X attend de ses élèves une maîtrise de ces concepts, non seulement dans leur application directe mais aussi dans leur démonstration rigoureuse.