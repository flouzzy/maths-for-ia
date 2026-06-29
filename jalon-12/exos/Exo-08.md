Cher collègue et chers étudiants,

Je vous propose aujourd'hui un exercice fondamental qui, je l'espère, éclairera les liens profonds entre l'algèbre linéaire classique et les fondements théoriques de l'intelligence artificielle moderne, en particulier la conception de moteurs de recherche sémantiques. Nous explorerons la dualité inhérente aux espaces d'intégration (embedding spaces) et la géométrie qui en découle, en mettant en lumière comment une approche rigoureuse peut enrichir notre compréhension des mécanismes de similarité.

---

### Exercice 8 (Difficulté : $\star \star \star \star$)

**Titre : DUALITÉ ET ORTHOGONALITÉ DANS LES ESPACES D'INTÉGRATION SÉMANTIQUE**

**Contexte :**
Dans la conception de moteurs de recherche sémantiques, les documents et les requêtes sont couramment représentés comme des vecteurs dans un espace euclidien de grande dimension, souvent appelé "espace d'intégration" (embedding space). La similarité cosinus est une métrique standard pour quantifier la pertinence sémantique entre un vecteur de requête et un vecteur de document. Cependant, une perspective plus abstraite peut considérer les requêtes non pas comme des vecteurs, mais comme des fonctionnelles linéaires qui attribuent un score aux documents. Cet exercice explore la dualité entre ces deux représentations et ses implications géométriques.

**Hypothèses Fondamentales :**
Nous formulons les hypothèses suivantes pour cet exercice :
1.  $V$ est un espace vectoriel réel de dimension finie $n$, avec $n \ge 1$.
2.  $V$ est muni d'un produit scalaire $\langle \cdot, \cdot \rangle$, ce qui en fait un espace euclidien.
3.  La norme induite par ce produit scalaire sur $V$ est notée $\|\cdot\|_V$.
4.  Tous les vecteurs et fonctionnelles considérés sont bien définis dans leurs espaces respectifs.
5.  Les vecteurs nuls sont notés $0_V$ pour l'espace $V$ et $0_{V^*}$ pour l'espace $V^*$.

**Partie I : Dualité et l'Isomorphisme de Riesz**

1.  Définissez l'espace dual $V^*$ de $V$. Énoncez explicitement la nature de ses éléments et leurs propriétés fondamentales.
2.  Énoncez le Théorème de Riesz de représentation pour les espaces euclidiens de dimension finie. Prouvez que l'application $R: V^* \to V$ qui à chaque $\phi \in V^*$ associe l'unique vecteur $v_\phi \in V$ tel que $\phi(x) = \langle v_\phi, x \rangle$ pour tout $x \in V$, est un isomorphisme d'espaces vectoriels.
3.  En utilisant l'isomorphisme $R$, définissez un produit scalaire $\langle \cdot, \cdot \rangle_{V^*}$ sur $V^*$ tel que $V^*$ devienne également un espace euclidien. Vérifiez que cette définition satisfait les axiomes d'un produit scalaire.
4.  Dérivez une expression pour la norme $\|\phi\|_{V^*}$ d'une fonctionnelle $\phi \in V^*$ en termes de $\phi$ elle-même, sans référence explicite à son représentant de Riesz $v_\phi$.

**Partie II : Similarité Cosinus dans les Espaces Duaux**

1.  Pour un vecteur de document $d \in V \setminus \{0_V\}$ et une fonctionnelle de requête $\Phi \in V^* \setminus \{0_{V^*}\}$, définissez la "similarité cosinus" $\text{cos\_sim}(\Phi, d)$ en utilisant l'isomorphisme de Riesz. Fournissez une formule complètement explicite n'utilisant que $\Phi$, $d$, le produit scalaire sur $V$, et les normes $\|\cdot\|_V$ et $\|\cdot\|_{V^*}$.
2.  Soient $d_1, d_2 \in V \setminus \{0_V\}$ deux vecteurs de document. Montrez que la similarité cosinus standard entre ces deux vecteurs, $\text{cos\_sim}(d_1, d_2)$, peut être exprimée en utilisant une fonctionnelle : $\text{cos\_sim}(d_1, d_2) = \text{cos\_sim}(R^{-1}(d_1), d_2)$. Cette démonstration établit un pont entre l'approche "requête-vecteur" et l'approche "requête-fonctionnelle".

**Partie III : Recherche par Sous-espaces de Requête (Problème de l'X)**

Considérons un scénario où les requêtes ne sont pas de simples fonctionnelles individuelles, mais sont plutôt caractérisées par un *sous-espace* de "types de requêtes pertinents".
Soit $W^* \subseteq V^*$ un sous-espace vectoriel de fonctionnelles de dimension $k$, où $1 \le k < n$. Ce sous-espace $W^*$ représente un "domaine de requête" ou un "filtre sémantique" spécifique.

1.  Définissez l'annihilateur $W^\perp_A \subseteq V$ du sous-espace $W^*$. Prouvez que $W^\perp_A$ est un sous-espace vectoriel de $V$ et déterminez sa dimension.
2.  Supposons qu'un vecteur de document $d \in V$ soit donné. Nous voulons trouver la fonctionnelle $\Phi_d \in W^*$ qui "s'aligne" le mieux avec $d$ au sens de maximiser la similarité cosinus $\text{cos\_sim}(\Phi, d)$ pour toutes les fonctionnelles $\Phi \in W^* \setminus \{0_{V^*}\}$. Montrez qu'une telle fonctionnelle $\Phi_d$ existe et est unique à un facteur scalaire non nul près.
    *Indice :* Considérez les représentants de Riesz.
3.  Soit $R(W^*) \subseteq V$ l'image du sous-espace $W^*$ par l'isomorphisme de Riesz $R$. Soit $P_{R(W^*)}: V \to R(W^*)$ le projecteur orthogonal de $V$ sur le sous-espace $R(W^*)$. Montrez que l'ensemble des fonctionnelles qui maximisent $\text{cos\_sim}(\Phi, d)$ est précisément $\{\alpha R^{-1}(P_{R(W^*)}(d)) \mid \alpha \in \mathbb{R} \setminus \{0\}\}$.
4.  Interprétez la signification géométrique de $W^\perp_A$ dans le contexte d'un moteur de recherche sémantique. Si un document $d \in W^\perp_A$, qu'est-ce que cela implique quant à sa pertinence par rapport à toute requête appartenant au sous-espace $W^*$ ?

---

### Correction de l'Exercice 8

**Partie I : Dualité et l'Isomorphisme de Riesz**

1.  **Définition de l'espace dual $V^*$ :**
    L'espace dual $V^*$ de l'espace vectoriel $V$ est l'ensemble de toutes les applications linéaires de $V$ vers le corps des scalaires $\mathbb{R}$.
    Les éléments de $V^*$ sont appelés des **fonctionnelles linéaires**.
    Formellement, $V^* = \{ \phi : V \to \mathbb{R} \mid \phi \text{ est linéaire} \}$.
    Les propriétés fondamentales des éléments de $V^*$ sont :
    *   **Linéarité :** Pour tout $\phi \in V^*$, pour tous $x_1, x_2 \in V$ et tous $\alpha_1, \alpha_2 \in \mathbb{R}$, nous avons $\phi(\alpha_1 x_1 + \alpha_2 x_2) = \alpha_1 \phi(x_1) + \alpha_2 \phi(x_2)$.
    *   **Structure d'espace vectoriel :** $V^*$ est lui-même un espace vectoriel sur $\mathbb{R}$. L'addition de fonctionnelles est définie par $(\phi_1 + \phi_2)(x) = \phi_1(x) + \phi_2(x)$ pour tous $\phi_1, \phi_2 \in V^*$ et $x \in V$. La multiplication par un scalaire est définie par $(\alpha \phi)(x) = \alpha \phi(x)$ pour tout $\alpha \in \mathbb{R}$, $\phi \in V^*$ et $x \in V$.
    *   **Dimension :** Puisque $V$ est un espace vectoriel de dimension finie $n$, son espace dual $V^*$ est également de dimension finie $n$.

2.  **Théorème de Riesz de représentation et preuve de l'isomorphisme $R$ :**
    Le **Théorème de Riesz de représentation** pour les espaces euclidiens de dimension finie stipule que :
    Pour toute fonctionnelle linéaire $\phi \in V^*$, il existe un unique vecteur $v_\phi \in V$ tel que $\phi(x) = \langle v_\phi, x \rangle$ pour tout $x \in V$.

    Prouvons que l'application $R: V^* \to V$, définie par $R(\phi) = v_\phi$, est un isomorphisme d'espaces vectoriels.
    Nous devons montrer que $R$ est linéaire, injective et surjective.

    *   **Linéarité de $R$ :**
        Soient $\phi_1, \phi_2 \in V^*$ et $\alpha_1, \alpha_2 \in \mathbb{R}$. Nous voulons montrer que $R(\alpha_1 \phi_1 + \alpha_2 \phi_2) = \alpha_1 R(\phi_1) + \alpha_2 R(\phi_2)$.
        Par la définition de $R$, le vecteur $R(\alpha_1 \phi_1 + \alpha_2 \phi_2)$ est l'unique vecteur dans $V$ qui, pour tout $x \in V$, satisfait :
        $$ (\alpha_1 \phi_1 + \alpha_2 \phi_2)(x) = \langle R(\alpha_1 \phi_1 + \alpha_2 \phi_2), x \rangle $$
        Par la linéarité des fonctionnelles et les propriétés du produit scalaire, nous avons aussi :
        $$ (\alpha_1 \phi_1 + \alpha_2 \phi_2)(x) = \alpha_1 \phi_1(x) + \alpha_2 \phi_2(x) $$
        $$ = \alpha_1 \langle R(\phi_1), x \rangle + \alpha_2 \langle R(\phi_2), x \rangle $$
        $$ = \langle \alpha_1 R(\phi_1), x \rangle + \langle \alpha_2 R(\phi_2), x \rangle $$
        $$ = \langle \alpha_1 R(\phi_1) + \alpha_2 R(\phi_2), x \rangle $$
        Ainsi, pour tout $x \in V$, nous avons $\langle R(\alpha_1 \phi_1 + \alpha_2 \phi_2), x \rangle = \langle \alpha_1 R(\phi_1) + \alpha_2 R(\phi_2), x \rangle$.
        Cela signifie que $\langle R(\alpha_1 \phi_1 + \alpha_2 \phi_2) - (\alpha_1 R(\phi_1) + \alpha_2 R(\phi_2)), x \rangle = 0$ pour tout $x \in V$.
        En particulier, en prenant $x = R(\alpha_1 \phi_1 + \alpha_2 \phi_2) - (\alpha_1 R(\phi_1) + \alpha_2 R(\phi_2))$, nous obtenons que la norme de ce vecteur est nulle, ce qui implique que le vecteur lui-même est le vecteur nul.
        Donc, $R(\alpha_1 \phi_1 + \alpha_2 \phi_2) = \alpha_1 R(\phi_1) + \alpha_2 R(\phi_2)$. $R$ est linéaire.

    *   **Injectivité de $R$ :**
        Supposons $R(\phi) = 0_V$ pour une fonctionnelle $\phi \in V^*$.
        Par définition de $R$, cela signifie que $v_\phi = 0_V$.
        Alors, pour tout $x \in V$, $\phi(x) = \langle v_\phi, x \rangle = \langle 0_V, x \rangle = 0$.
        Donc, $\phi$ est la fonctionnelle nulle $0_{V^*}$.
        Par conséquent, le noyau de $R$ est $\ker(R) = \{0_{V^*}\}$, ce qui prouve que $R$ est injective.

    *   **Surjectivité de $R$ :**
        Puisque $V$ est de dimension finie $n$, nous savons que $V^*$ est également de dimension $n$.
        $R$ est une application linéaire de $V^*$ vers $V$.
        De l'injectivité de $R$, il découle que $\text{dim}(\ker(R)) = 0$.
        Par le théorème du rang, $\text{dim}(V^*) = \text{dim}(\ker(R)) + \text{dim}(\text{Im}(R))$.
        Donc, $n = 0 + \text{dim}(\text{Im}(R))$, ce qui implique $\text{dim}(\text{Im}(R)) = n$.
        Puisque $\text{Im}(R)$ est un sous-espace vectoriel de $V$ et $\text{dim}(\text{Im}(R)) = \text{dim}(V) = n$, nous concluons que $\text{Im}(R) = V$.
        Par conséquent, $R$ est surjective.

    Puisque $R$ est linéaire, injective et surjective, c'est un isomorphisme d'espaces vectoriels.

3.  **Définition d'un produit scalaire sur $V^*$ :**
    Nous définissons le produit scalaire $\langle \cdot, \cdot \rangle_{V^*}$ sur $V^*$ pour $\phi_1, \phi_2 \in V^*$ comme suit :
    $$ \langle \phi_1, \phi_2 \rangle_{V^*} = \langle R(\phi_1), R(\phi_2) \rangle $$
    Vérifions les axiomes d'un produit scalaire :

    *   **Linéarité par rapport à la première variable :**
        Soient $\phi_1, \phi_2, \phi_3 \in V^*$ et $\alpha, \beta \in \mathbb{R}$.
        $$ \langle \alpha \phi_1 + \beta \phi_2, \phi_3 \rangle_{V^*} = \langle R(\alpha \phi_1 + \beta \phi_2), R(\phi_3) \rangle $$
        Par la linéarité de $R$, $R(\alpha \phi_1 + \beta \phi_2) = \alpha R(\phi_1) + \beta R(\phi_2)$.
        $$ = \langle \alpha R(\phi_1) + \beta R(\phi_2), R(\phi_3) \rangle $$
        Par la linéarité du produit scalaire sur $V$ par rapport à la première variable :
        $$ = \alpha \langle R(\phi_1), R(\phi_3) \rangle + \beta \langle R(\phi_2), R(\phi_3) \rangle $$
        Par la définition du produit scalaire sur $V^*$ :
        $$ = \alpha \langle \phi_1, \phi_3 \rangle_{V^*} + \beta \langle \phi_2, \phi_3 \rangle_{V^*} $$
        Donc, la linéarité est satisfaite.

    *   **Symétrie :**
        Soient $\phi_1, \phi_2 \in V^*$.
        $$ \langle \phi_1, \phi_2 \rangle_{V^*} = \langle R(\phi_1), R(\phi_2) \rangle $$
        Par la symétrie du produit scalaire sur $V$ :
        $$ = \langle R(\phi_2), R(\phi_1) \rangle $$
        Par la définition du produit scalaire sur $V^*$ :
        $$ = \langle \phi_2, \phi_1 \rangle_{V^*} $$
        Donc, la symétrie est satisfaite.

    *   **Définition positive :**
        Soit $\phi \in V^*$.
        $$ \langle \phi, \phi \rangle_{V^*} = \langle R(\phi), R(\phi) \rangle $$
        Par la définition positive du produit scalaire sur $V$, $\langle R(\phi), R(\phi) \rangle \ge 0$.
        De plus, $\langle \phi, \phi \rangle_{V^*} = 0$ si et seulement si $\langle R(\phi), R(\phi) \rangle = 0$.
        Cela implique $R(\phi) = 0_V$.
        Comme $R$ est un isomorphisme, $R(\phi) = 0_V$ si et seulement si $\phi = 0_{V^*}$.
        Donc, $\langle \phi, \phi \rangle_{V^*} = 0$ si et seulement si $\phi = 0_{V^*}$.
        La définition positive est satisfaite.

    Puisque toutes les propriétés sont vérifiées, $\langle \cdot, \cdot \rangle_{V^*}$ est bien un produit scalaire sur $V^*$, et $V^*$ est donc un espace euclidien.

4.  **Expression de la norme $\|\phi\|_{V^*}$ :**
    La norme $\|\phi\|_{V^*}$ est induite par le produit scalaire sur $V^*$.
    $$ \|\phi\|_{V^*} = \sqrt{\langle \phi, \phi \rangle_{V^*}} $$
    En utilisant la définition du produit scalaire sur $V^*$ :
    $$ \|\phi\|_{V^*} = \sqrt{\langle R(\phi), R(\phi) \rangle} $$
    Par la définition de la norme sur $V$ :
    $$ \|\phi\|_{V^*} = \|R(\phi)\|_V $$
    Maintenant, nous voulons exprimer cette norme en termes de $\phi$ elle-même, sans $R(\phi)$.
    Nous savons que $\phi(x) = \langle R(\phi), x \rangle$ pour tout $x \in V$.
    Prenons $x = R(\phi)$. Alors :
    $$ \phi(R(\phi)) = \langle R(\phi), R(\phi) \rangle $$
    $$ \phi(R(\phi)) = \|R(\phi)\|_V^2 $$
    Donc, $\|R(\phi)\|_V = \sqrt{\phi(R(\phi))}$.
    Substituant cela dans l'expression de $\|\phi\|_{V^*}$ :
    $$ \|\phi\|_{V^*} = \sqrt{\phi(R(\phi))} $$
    Ceci est une expression de la norme $\|\phi\|_{V^*}$ en termes de $\phi$ et de son représentant de Riesz. Pour éviter toute référence explicite à $R(\phi)$ dans l'expression *finale*, nous devons reconnaître que $R(\phi)$ est le vecteur $v_\phi$ tel que $\phi(v_\phi) = \|v_\phi\|_V^2$.
    Donc, $R(\phi)$ est précisément le vecteur unique dans $V$ pour lequel $\phi$ prend une valeur égale au carré de sa norme. Si nous souhaitons une expression purement en termes de $\phi$ et de l'opérateur $\phi$ lui-même, la forme $\sqrt{\phi(v_\phi)}$ est la plus appropriée, sachant que $v_\phi$ est défini par le théorème de Riesz. Une forme alternative qui peut être utile est $\sup_{x \in V, x \neq 0_V} \frac{|\phi(x)|}{\|x\|_V}$, qui est la norme d'opérateur de $\phi$. Par le théorème de Riesz, cette norme d'opérateur est égale à $\|v_\phi\|_V$.
    Donc, $\|\phi\|_{V^*} = \sup_{x \in V \setminus \{0_V\}} \frac{|\phi(x)|}{\|x\|_V}$.

**Partie II : Similarité Cosinus dans les Espaces Duaux**

1.  **Définition de $\text{cos\_sim}(\Phi, d)$ :**
    La similarité cosinus entre deux vecteurs $u, v \in V \setminus \{0_V\}$ est définie comme $\text{cos\_sim}(u, v) = \frac{\langle u, v \rangle}{\|u\|_V \|v\|_V}$.
    Pour un vecteur de document $d \in V \setminus \{0_V\}$ et une fonctionnelle de requête $\Phi \in V^* \setminus \{0_{V^*}\}$, nous utilisons l'isomorphisme de Riesz pour associer $\Phi$ à son représentant vectoriel $R(\Phi) \in V$.
    Alors, la similarité cosinus entre $\Phi$ et $d$ est définie comme la similarité cosinus entre leurs représentants vectoriels respectifs dans $V$ (où $\Phi$ est représentée par $R(\Phi)$ et $d$ est déjà un vecteur).
    $$ \text{cos\_sim}(\Phi, d) = \text{cos\_sim}(R(\Phi), d) $$
    $$ = \frac{\langle R(\Phi), d \rangle}{\|R(\Phi)\|_V \|d\|_V} $$
    Nous savons, par la définition de $R$, que $\Phi(d) = \langle R(\Phi), d \rangle$.
    Nous avons également dérivé, en Partie I.4, que $\|R(\Phi)\|_V = \|\Phi\|_{V^*}$.
    En substituant ces expressions dans la formule :
    $$ \text{cos\_sim}(\Phi, d) = \frac{\Phi(d)}{\|\Phi\|_{V^*} \|d\|_V} $$
    C'est la formule explicite demandée.

2.  **Lien entre $\text{cos\_sim}(d_1, d_2)$ et $\text{cos\_sim}(R^{-1}(d_1), d_2)$ :**
    Soient $d_1, d_2 \in V \setminus \{0_V\}$ deux vecteurs de document.
    La similarité cosinus standard entre $d_1$ et $d_2$ est :
    $$ \text{cos\_sim}(d_1, d_2) = \frac{\langle d_1, d_2 \rangle}{\|d_1\|_V \|d_2\|_V} $$
    Considérons maintenant $\text{cos\_sim}(R^{-1}(d_1), d_2)$.
    Ici, $R^{-1}(d_1)$ est la fonctionnelle $\Phi_1 \in V^*$ telle que $R(\Phi_1) = d_1$.
    Par la formule dérivée en Partie II.1 :
    $$ \text{cos\_sim}(R^{-1}(d_1), d_2) = \frac{(R^{-1}(d_1))(d_2)}{\|R^{-1}(d_1)\|_{V^*} \|d_2\|_V} $$
    Nous savons que $R^{-1}(d_1)$ est la fonctionnelle $\Phi_1$ pour laquelle $R(\Phi_1) = d_1$.
    Par la définition de $R$, $(R^{-1}(d_1))(d_2) = \langle R(R^{-1}(d_1)), d_2 \rangle = \langle d_1, d_2 \rangle$.
    De plus, par la Partie I.4, $\|R^{-1}(d_1)\|_{V^*} = \|R(R^{-1}(d_1))\|_V = \|d_1\|_V$.
    En substituant ces deux expressions :
    $$ \text{cos\_sim}(R^{-1}(d_1), d_2) = \frac{\langle d_1, d_2 \rangle}{\|d_1\|_V \|d_2\|_V} $$
    Nous voyons que :
    $$ \text{cos\_sim}(d_1, d_2) = \text{cos\_sim}(R^{-1}(d_1), d_2) $$
    Cette égalité démontre que considérer une requête comme un vecteur $d_1$ ou comme la fonctionnelle $R^{-1}(d_1)$ conduit à la même mesure de similarité cosinus avec un document $d_2$. Cela valide l'interchangeabilité de ces perspectives dans un espace euclidien, via l'isomorphisme de Riesz.

**Partie III : Recherche par Sous-espaces de Requête (Problème de l'X)**

1.  **Définition et dimension de l'annihilateur $W^\perp_A$ :**
    L'annihilateur $W^\perp_A$ du sous-espace $W^* \subseteq V^*$ est défini comme l'ensemble des vecteurs de $V$ qui sont nuls pour toutes les fonctionnelles de $W^*$.
    $$ W^\perp_A = \{ d \in V \mid \forall \Phi \in W^*, \Phi(d) = 0 \} $$
    Prouvons que $W^\perp_A$ est un sous-espace vectoriel de $V$.
    *   **$W^\perp_A$ contient le vecteur nul :** Pour toute $\Phi \in W^*$, $\Phi(0_V) = 0$ par linéarité. Donc $0_V \in W^\perp_A$. $W^\perp_A$ est non vide.
    *   **Stabilité par combinaison linéaire :** Soient $d_1, d_2 \in W^\perp_A$ et $\alpha_1, \alpha_2 \in \mathbb{R}$.
        Pour toute $\Phi \in W^*$, nous avons $\Phi(d_1) = 0$ et $\Phi(d_2) = 0$.
        Alors, par la linéarité de $\Phi$ :
        $$ \Phi(\alpha_1 d_1 + \alpha_2 d_2) = \alpha_1 \Phi(d_1) + \alpha_2 \Phi(d_2) = \alpha_1 \cdot 0 + \alpha_2 \cdot 0 = 0 $$
        Ainsi, $\alpha_1 d_1 + \alpha_2 d_2 \in W^\perp_A$.
    $W^\perp_A$ est un sous-espace vectoriel de $V$.

    Déterminons sa dimension.
    Nous avons l'isomorphisme de Riesz $R: V^* \to V$.
    Soit $R(W^*) = \{ R(\Phi) \mid \Phi \in W^* \}$ l'image de $W^*$ dans $V$ par $R$.
    Puisque $R$ est un isomorphisme, $R(W^*)$ est un sous-espace vectoriel de $V$, et $\text{dim}(R(W^*)) = \text{dim}(W^*) = k$.
    Considérons un vecteur $d \in W^\perp_A$. Cela signifie que pour tout $\Phi \in W^*$, $\Phi(d) = 0$.
    Par la définition de $R$, $\Phi(d) = \langle R(\Phi), d \rangle$.
    Donc, $d \in W^\perp_A$ si et seulement si pour tout $\Phi \in W^*$, $\langle R(\Phi), d \rangle = 0$.
    Cela signifie que $d$ est orthogonal à tous les vecteurs de $R(W^*)$.
    Par conséquent, $W^\perp_A$ est le complément orthogonal de $R(W^*)$ dans $V$, que nous notons $R(W^*)^\perp$.
    $$ W^\perp_A = R(W^*)^\perp $$
    Puisque $V$ est un espace euclidien de dimension finie $n$, et $R(W^*)$ est un sous-espace de dimension $k$, la dimension de son complément orthogonal est :
    $$ \text{dim}(W^\perp_A) = \text{dim}(R(W^*)^\perp) = \text{dim}(V) - \text{dim}(R(W^*)) = n - k $$

2.  **Existence et unicité (à un scalaire près) de $\Phi_d$ :**
    Nous cherchons $\Phi_d \in W^* \setminus \{0_{V^*}\}$ qui maximise $\text{cos\_sim}(\Phi, d)$ pour un $d \in V \setminus \{0_V\}$ donné.
    La similarité cosinus est donnée par $\text{cos\_sim}(\Phi, d) = \frac{\Phi(d)}{\|\Phi\|_{V^*} \|d\|_V}$.
    Puisque $\|d\|_V$ est une constante positive, maximiser $\text{cos\_sim}(\Phi, d)$ revient à maximiser $\frac{\Phi(d)}{\|\Phi\|_{V^*}}$.
    Soit $v_\Phi = R(\Phi)$. Alors $\Phi(d) = \langle v_\Phi, d \rangle$ et $\|\Phi\|_{V^*} = \|v_\Phi\|_V$.
    Le problème devient : trouver $v_{\Phi_d} \in R(W^*) \setminus \{0_V\}$ qui maximise $\frac{\langle v, d \rangle}{\|v\|_V}$.
    Ceci est la maximisation de la similarité cosinus entre $d$ et un vecteur $v$ dans le sous-espace $R(W^*)$.
    Par l'inégalité de Cauchy-Schwarz, $|\langle v, d \rangle| \le \|v\|_V \|d\|_V$.
    Donc, $\frac{|\langle v, d \rangle|}{\|v\|_V \|d\|_V} \le 1$.
    L'égalité est atteinte lorsque $v$ est colinéaire à $d$. Cependant, $v$ doit appartenir à $R(W^*)$.
    Pour maximiser $\frac{\langle v, d \rangle}{\|v\|_V}$, nous voulons maximiser $\langle v, d \rangle$ tout en gardant $\|v\|_V$ constant, ou maximiser la projection de $d$ sur la droite engendrée par $v$.
    Le vecteur $v \in R(W^*)$ qui maximise cette quantité est la projection orthogonale de $d$ sur $R(W^*)$, que nous notons $P_{R(W^*)}(d)$.
    Plus précisément, pour $v \in R(W^*) \setminus \{0_V\}$, on peut écrire $d = P_{R(W^*)}(d) + d^\perp$, où $d^\perp \in R(W^*)^\perp$.
    Alors $\langle v, d \rangle = \langle v, P_{R(W^*)}(d) + d^\perp \rangle = \langle v, P_{R(W^*)}(d) \rangle + \langle v, d^\perp \rangle$.
    Puisque $v \in R(W^*)$ et $d^\perp \in R(W^*)^\perp$, $\langle v, d^\perp \rangle = 0$.
    Donc $\langle v, d \rangle = \langle v, P_{R(W^*)}(d) \rangle$.
    La quantité à maximiser est $\frac{\langle v, P_{R(W^*)}(d) \rangle}{\|v\|_V}$.
    Par Cauchy-Schwarz appliqué à $v$ et $P_{R(W^*)}(d)$, nous avons $\langle v, P_{R(W^*)}(d) \rangle \le \|v\|_V \|P_{R(W^*)}(d)\|_V$.
    Le maximum est atteint quand $v$ est colinéaire à $P_{R(W^*)}(d)$.
    Si $P_{R(W^*)}(d) = 0_V$, alors $\langle v, P_{R(W^*)}(d) \rangle = 0$ pour tout $v$, donc la similarité cosinus est 0 pour tous les $\Phi$. Dans ce cas, n'importe quelle $\Phi \in W^*$ (non nulle) donne la même valeur 0, donc il n'y a pas de fonctionnelle unique maximisante au sens strict (car elles sont toutes "également nulles" pour $d$). Cependant, la question suppose $\Phi \in W^* \setminus \{0_{V^*}\}$.
    Si $P_{R(W^*)}(d) \neq 0_V$, alors le maximum est atteint lorsque $v = \alpha P_{R(W^*)}(d)$ pour un scalaire $\alpha > 0$.
    Ainsi, le représentant de Riesz $v_{\Phi_d}$ de la fonctionnelle maximisante $\Phi_d$ doit être colinéaire à $P_{R(W^*)}(d)$.
    Donc $v_{\Phi_d} = \alpha P_{R(W^*)}(d)$ pour un $\alpha \in \mathbb{R} \setminus \{0\}$.
    Puisque $\Phi_d = R^{-1}(v_{\Phi_d})$, il existe une telle fonctionnelle $\Phi_d$, et elle est unique à un facteur scalaire non nul près (puisque $R^{-1}$ est un isomorphisme).
    La fonctionnelle $\Phi_d$ qui maximise $\text{cos\_sim}(\Phi, d)$ est $R^{-1}(P_{R(W^*)}(d))$.

3.  **Lien avec le projecteur orthogonal $P_{R(W^*)}$ :**
    D'après la question précédente, la maximisation de $\text{cos\_sim}(\Phi, d)$ pour $\Phi \in W^* \setminus \{0_{V^*}\}$ se produit lorsque le représentant de Riesz $v_\Phi = R(\Phi)$ est colinéaire au vecteur $P_{R(W^*)}(d)$.
    Soit $v^* = P_{R(W^*)}(d)$. Si $v^* = 0_V$, alors toute $\Phi \in W^* \setminus \{0_{V^*}\}$ donne $\Phi(d) = \langle R(\Phi), d \rangle = \langle R(\Phi), P_{R(W^*)}(d) \rangle = \langle R(\Phi), 0_V \rangle = 0$, donc $\text{cos\_sim}(\Phi, d)=0$.
    Si $v^* \neq 0_V$, alors le maximum est atteint pour $v_\Phi = \alpha v^*$ pour $\alpha > 0$.
    La fonctionnelle correspondante est $\Phi = R^{-1}(v_\Phi) = R^{-1}(\alpha P_{R(W^*)}(d))$.
    L'ensemble des fonctionnelles qui maximisent $\text{cos\_sim}(\Phi, d)$ est donc l'ensemble de toutes les fonctionnelles dont le représentant de Riesz est un multiple scalaire non nul de $P_{R(W^*)}(d)$.
    $$ \{ \alpha R^{-1}(P_{R(W^*)}(d)) \mid \alpha \in \mathbb{R} \setminus \{0\} \} $$
    Cela signifie que la "meilleure" fonctionnelle de requête (dans le sous-espace $W^*$) pour un document $d$ est celle dont le représentant de Riesz est la projection orthogonale de $d$ sur $R(W^*)$.

4.  **Interprétation géométrique de $W^\perp_A$ :**
    Nous avons établi que $W^\perp_A = R(W^*)^\perp$.
    Si un document $d \in W^\perp_A$, cela signifie que $d$ est orthogonal à tous les vecteurs dans le sous-espace $R(W^*)$.
    Puisque $R(W^*)$ est l'image des fonctionnelles de requête de $W^*$ sous l'isomorphisme de Riesz, cela signifie que $d$ est orthogonal aux représentants de Riesz de *toutes* les fonctionnelles de requête valides dans notre domaine $W^*$.
    Pour tout $\Phi \in W^*$, nous avons $\Phi(d) = \langle R(\Phi), d \rangle$.
    Si $d \in W^\perp_A$, alors $\langle R(\Phi), d \rangle = 0$ pour tout $R(\Phi) \in R(W^*)$.
    Ainsi, $\Phi(d) = 0$ pour tout $\Phi \in W^*$.
    La similarité cosinus $\text{cos\_sim}(\Phi, d) = \frac{\Phi(d)}{\|\Phi\|_{V^*} \|d\|_V}$ sera donc toujours nulle si $d \neq 0_V$ et $\Phi \neq 0_{V^*}$.
    Dans le contexte d'un moteur de recherche sémantique, si un document $d$ appartient à l'annihilateur $W^\perp_A$, cela implique que $d$ n'a *aucune* pertinence sémantique (au sens de la similarité cosinus) pour *aucune* des requêtes définies dans le sous-espace $W^*$. Géométriquement, le vecteur de document $d$ est complètement orthogonal à l'ensemble de "concepts" ou "caractéristiques" représenté par le sous-espace de requête $R(W^*)$. Il se situe dans un espace sémantique complètement distinct et non pertinent par rapport au domaine de requête défini par $W^*$. C'est un document qui "échappe" entièrement à ce filtre sémantique spécifique.

---
J'espère que cet exercice a su stimuler votre réflexion et approfondir votre compréhension de la structure mathématique sous-jacente aux systèmes d'IA. La beauté de ces approches réside souvent dans leur capacité à relier des concepts apparemment disparates, révélant une élégance unificatrice.

Cordialement,

Professeur Émérite de Mathématiques.