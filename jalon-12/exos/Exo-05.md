En tant que Professeur Émérite de Mathématiques, je vous présente l'exercice 5, d'une difficulté de 3 étoiles, s'inscrivant dans le Jalon 12. Cet exercice explore la dualité et la géométrie des espaces de plongement, concepts fondamentaux pour la conception théorique de moteurs de recherche sémantique par similarité cosinus, et propose une résolution rigoureuse dans le style des problèmes d'algèbre de l'École Polytechnique.

---

### Exercice 5 : Analyse d'un Moteur de Recherche Sémantique par Projections et Dualité

**Contexte :**
Dans le cadre de la conception d'un moteur de recherche sémantique, des documents et des requêtes sont représentés par des vecteurs dans des espaces de grande dimension, souvent appelés "espaces de plongement" (embedding spaces). La similarité entre une requête et un document est fréquemment mesurée par la similarité cosinus. Cet exercice propose une formalisation mathématique de certains aspects de cette approche en explorant les liens entre les espaces vectoriels euclidiens, leurs espaces duaux, le théorème de Riesz, et les projections orthogonales.

**Hypothèses et Définitions :**
Soit $E$ un $\mathbb{R}$-espace vectoriel de dimension finie $n \in \mathbb{N}^*$.
On munit $E$ d'un produit scalaire $\langle \cdot, \cdot \rangle_E: E \times E \to \mathbb{R}$, ce qui en fait un espace euclidien.
La norme associée est notée $\|x\|_E = \sqrt{\langle x, x \rangle_E}$ pour tout $x \in E$.
On note $E^*$ l'espace dual de $E$, qui est l'espace des formes linéaires continues de $E$ dans $\mathbb{R}$. Pour un espace de dimension finie, toutes les formes linéaires sont continues.
Pour une forme linéaire $\varphi \in E^*$, sa norme est définie par $\|\varphi\|_{E^*} = \sup_{x \in E, \|x\|_E \le 1} |\varphi(x)|$.
Soit $F$ un sous-espace vectoriel de $E$, de dimension $k \in \{1, \dots, n\}$.
On munit $F$ du produit scalaire induit par $E$, noté $\langle \cdot, \cdot \rangle_F$, et de la norme associée $\|\cdot\|_F$. On note $F^*$ l'espace dual de $F$.

**Énoncé :**

**Partie I : Représentation vectorielle d'une requête sémantique**

1.  **L'isomorphisme de Riesz :**
    a.  On définit l'application $\Phi: E \to E^*$ par :
        Pour tout $v \in E$, $\Phi(v)$ est la forme linéaire sur $E$ telle que pour tout $x \in E$, $\Phi(v)(x) = \langle x, v \rangle_E$.
        Démontrez que $\Phi$ est un isomorphisme d'espaces vectoriels.
    b.  Pour toute forme linéaire $\varphi \in E^*$, on définit son "vecteur de représentation" $v_\varphi \in E$ comme l'unique vecteur tel que $\varphi = \Phi(v_\varphi)$. En d'autres termes, $v_\varphi = \Phi^{-1}(\varphi)$.
        Justifiez l'existence et l'unicité de $v_\varphi$.
    c.  Démontrez que pour toute $\varphi \in E^*$, $\|\varphi\|_{E^*} = \|v_\varphi\|_E$.

**Partie II : Mesure de pertinence et projection**

Dans cette partie, on considère que les documents potentiellement pertinents pour une requête sont représentés par des vecteurs appartenant à un sous-espace $F$ de $E$.
Une requête est toujours représentée par une forme linéaire $\varphi \in E^*$, et son vecteur de représentation $v_\varphi \in E$.

2.  **Projection orthogonale et optimalité de la pertinence :**
    a.  Soit $P_F: E \to F$ l'opérateur de projection orthogonale sur le sous-espace $F$.
        Rappelez la propriété caractéristique de $P_F(x)$ pour tout $x \in E$, en utilisant la décomposition orthogonale de $E$.
    b.  Soit $(e_1, \dots, e_k)$ une base orthonormée de $F$.
        Exprimez $P_F(x)$ en fonction de $x$ et des vecteurs de cette base.
    c.  On définit la "pertinence sémantique" d'un document $d \in F$ par rapport à la requête $\varphi$ comme le score $S(\varphi, d) = \varphi(d)$.
        Nous cherchons à trouver le "document" $d^* \in F$ qui maximise ce score $S(\varphi, d)$ sous la contrainte que $\|d\|_F = 1$.
        Plus précisément, si $P_F(v_\varphi) = 0_E$, quel est le score maximal atteint et quel est le choix de $d^*$ ?
        Si $P_F(v_\varphi) \ne 0_E$, montrez que le vecteur $d^* = \frac{P_F(v_\varphi)}{\|P_F(v_\varphi)\|_E}$ est le vecteur de $F$ de norme 1 qui maximise $S(\varphi, d)$, et donnez la valeur du score maximal.

**Partie III : Dualité de la projection**

Dans cette partie, nous explorons le lien entre la projection du vecteur de représentation de la requête et la représentation duale de la requête restreinte au sous-espace des documents.

3.  **La requête projetée et son vecteur de Riesz :**
    a.  On définit la forme linéaire $\psi_F: F \to \mathbb{R}$ comme la restriction de $\varphi$ à $F$, c'est-à-dire, pour tout $x \in F$, $\psi_F(x) = \varphi(x)$.
        Justifiez que $\psi_F \in F^*$.
    b.  L'espace $F$ étant aussi un espace euclidien, le théorème de Riesz s'applique à $F$. Soit $\Phi_F: F \to F^*$ l'isomorphisme de Riesz pour $F$.
        D'après la Partie I, il existe un unique vecteur $v_{\psi_F} \in F$ tel que pour tout $x \in F$, $\psi_F(x) = \langle x, v_{\psi_F} \rangle_F$.
        Déterminez ce vecteur $v_{\psi_F}$ en fonction de $v_\varphi$ et $P_F$.
    c.  Interprétez le résultat obtenu en termes de géométrie des espaces de plongement et de dualité.

---

### Correction de l'Exercice 5

**Partie I : Représentation vectorielle d'une requête sémantique**

1.  **L'isomorphisme de Riesz :**
    a.  Démontrons que $\Phi: E \to E^*$ est un isomorphisme.
        *   **Linéarité de $\Phi$ :**
            Soient $v_1, v_2 \in E$ et $\lambda \in \mathbb{R}$. Nous devons montrer que $\Phi(v_1 + \lambda v_2) = \Phi(v_1) + \lambda \Phi(v_2)$.
            Par définition, $\Phi(v_1 + \lambda v_2)$ est la forme linéaire telle que pour tout $x \in E$ :
            $$ \Phi(v_1 + \lambda v_2)(x) = \langle x, v_1 + \lambda v_2 \rangle_E $$
            Par la linéarité du produit scalaire par rapport à la deuxième composante :
            $$ \Phi(v_1 + \lambda v_2)(x) = \langle x, v_1 \rangle_E + \lambda \langle x, v_2 \rangle_E $$
            Par définition de $\Phi(v_1)$ et $\Phi(v_2)$ :
            $$ \Phi(v_1 + \lambda v_2)(x) = \Phi(v_1)(x) + \lambda \Phi(v_2)(x) $$
            Donc, $\Phi(v_1 + \lambda v_2) = \Phi(v_1) + \lambda \Phi(v_2)$. L'application $\Phi$ est linéaire.

        *   **Injectivité de $\Phi$ :**
            Soit $v \in E$ tel que $\Phi(v) = 0_{E^*}$, où $0_{E^*}$ est la forme linéaire nulle.
            Cela signifie que pour tout $x \in E$, $\Phi(v)(x) = 0$.
            Par définition de $\Phi(v)$, cela implique que pour tout $x \in E$, $\langle x, v \rangle_E = 0$.
            En particulier, en choisissant $x = v$, nous obtenons $\langle v, v \rangle_E = 0$.
            Par la propriété de définie positivité du produit scalaire, $\|v\|_E^2 = 0$ implique $v = 0_E$.
            Donc, $\ker(\Phi) = \{0_E\}$, ce qui signifie que $\Phi$ est injective.

        *   **Surjectivité de $\Phi$ :**
            Puisque $E$ est un espace vectoriel de dimension finie $n$, son espace dual $E^*$ a également pour dimension $n$.
            $$ \dim(E^*) = \dim(E) = n $$
            Comme $\Phi: E \to E^*$ est une application linéaire injective entre deux espaces vectoriels de même dimension finie, elle est nécessairement surjective.
            (Alternativement, on peut invoquer le théorème de représentation de Riesz qui garantit l'existence de $v$ pour toute $\varphi$).

        Puisque $\Phi$ est linéaire, injective et surjective, c'est un isomorphisme d'espaces vectoriels.

    b.  L'existence et l'unicité de $v_\varphi$ pour toute $\varphi \in E^*$ découlent directement du fait que $\Phi$ est un isomorphisme.
        *   **Existence :** Puisque $\Phi$ est surjective, pour toute $\varphi \in E^*$, il existe au moins un $v \in E$ tel que $\Phi(v) = \varphi$. Ce $v$ est $v_\varphi$.
        *   **Unicité :** Puisque $\Phi$ est injective, si $\Phi(v_1) = \varphi$ et $\Phi(v_2) = \varphi$, alors $\Phi(v_1) = \Phi(v_2)$, ce qui implique $v_1 = v_2$. Donc $v_\varphi$ est unique.

    c.  Démontrons que pour toute $\varphi \in E^*$, $\|\varphi\|_{E^*} = \|v_\varphi\|_E$.
        Par définition, $\|\varphi\|_{E^*} = \sup_{x \in E, \|x\|_E \le 1} |\varphi(x)|$.
        En utilisant la définition de $v_\varphi$, nous avons $\varphi(x) = \langle x, v_\varphi \rangle_E$.
        Donc, $\|\varphi\|_{E^*} = \sup_{x \in E, \|x\|_E \le 1} |\langle x, v_\varphi \rangle_E|$.
        D'après l'inégalité de Cauchy-Schwarz, pour tout $x \in E$:
        $$ |\langle x, v_\varphi \rangle_E| \le \|x\|_E \|v_\varphi\|_E $$
        Si $\|x\|_E \le 1$, alors $|\langle x, v_\varphi \rangle_E| \le \|v_\varphi\|_E$.
        Ceci implique que $\|\varphi\|_{E^*} \le \|v_\varphi\|_E$.

        Pour montrer l'égalité, nous devons trouver un $x_0 \in E$ avec $\|x_0\|_E \le 1$ tel que $|\varphi(x_0)| = \|v_\varphi\|_E$.
        *   Si $v_\varphi = 0_E$, alors $\varphi$ est la forme linéaire nulle, et $\|\varphi\|_{E^*} = 0$. Dans ce cas, $\|v_\varphi\|_E = 0$, donc l'égalité est triviale : $0 = 0$.
        *   Si $v_\varphi \ne 0_E$, choisissons $x_0 = \frac{v_\varphi}{\|v_\varphi\|_E}$. Alors $\|x_0\|_E = 1$.
            Calculons $\varphi(x_0)$:
            $$ \varphi(x_0) = \langle x_0, v_\varphi \rangle_E = \left\langle \frac{v_\varphi}{\|v_\varphi\|_E}, v_\varphi \right\rangle_E = \frac{1}{\|v_\varphi\|_E} \langle v_\varphi, v_\varphi \rangle_E = \frac{1}{\|v_\varphi\|_E} \|v_\varphi\|_E^2 = \|v_\varphi\|_E $$
            Puisque $\varphi(x_0) = \|v_\varphi\|_E$, et que nous avons déjà montré que $|\varphi(x)| \le \|v_\varphi\|_E$ pour tout $x$ de norme 1, la valeur maximale est atteinte.
            Par conséquent, $\|\varphi\|_{E^*} = \|v_\varphi\|_E$.

**Partie II : Mesure de pertinence et projection**

2.  **Projection orthogonale et optimalité de la pertinence :**
    a.  La propriété caractéristique de $P_F(x)$ est que pour tout $x \in E$, $P_F(x)$ est l'unique vecteur dans $F$ tel que $x - P_F(x)$ soit orthogonal à $F$.
        Ceci signifie que $x - P_F(x) \in F^\perp$, où $F^\perp = \{y \in E \mid \forall z \in F, \langle y, z \rangle_E = 0\}$.
        L'espace $E$ admet alors la décomposition orthogonale directe $E = F \oplus F^\perp$.

    b.  Soit $(e_1, \dots, e_k)$ une base orthonormée de $F$.
        Tout $x \in E$ peut être écrit comme $x = y + z$ où $y \in F$ et $z \in F^\perp$. $P_F(x) = y$.
        Puisque $(e_1, \dots, e_k)$ est une base orthonormée de $F$, nous pouvons écrire $y$ comme une combinaison linéaire de ces vecteurs.
        Pour tout $x \in E$, $P_F(x)$ est donné par la formule :
        $$ P_F(x) = \sum_{i=1}^k \langle x, e_i \rangle_E e_i $$
        Pour justifier cette formule, nous vérifions que ce vecteur satisfait la propriété caractéristique.
        1.  Le vecteur $\sum_{i=1}^k \langle x, e_i \rangle_E e_i$ est clairement un élément de $F$.
        2.  Considérons le vecteur $x - \sum_{i=1}^k \langle x, e_i \rangle_E e_i$. Nous devons montrer qu'il est orthogonal à $F$. Il suffit de montrer qu'il est orthogonal à chaque vecteur de base $e_j$ pour $j \in \{1, \dots, k\}$.
            $$ \left\langle x - \sum_{i=1}^k \langle x, e_i \rangle_E e_i, e_j \right\rangle_E = \langle x, e_j \rangle_E - \left\langle \sum_{i=1}^k \langle x, e_i \rangle_E e_i, e_j \right\rangle_E $$
            Par linéarité du produit scalaire :
            $$ = \langle x, e_j \rangle_E - \sum_{i=1}^k \langle x, e_i \rangle_E \langle e_i, e_j \rangle_E $$
            Puisque la base est orthonormée, $\langle e_i, e_j \rangle_E = \delta_{ij}$ (symbole de Kronecker). La somme ne contient qu'un seul terme non nul, lorsque $i=j$.
            $$ = \langle x, e_j \rangle_E - \langle x, e_j \rangle_E = 0 $$
            Le vecteur $x - P_F(x)$ est orthogonal à chaque $e_j$, et donc à $F$. Ainsi, la formule est correcte.

    c.  Nous cherchons à maximiser $S(\varphi, d) = \varphi(d)$ pour $d \in F$ avec $\|d\|_F = 1$.
        Nous savons que $\varphi(d) = \langle d, v_\varphi \rangle_E$.
        Soit $d \in F$. Nous utilisons la décomposition $v_\varphi = P_F(v_\varphi) + (v_\varphi - P_F(v_\varphi))$.
        Nous savons que $P_F(v_\varphi) \in F$ et $(v_\varphi - P_F(v_\varphi)) \in F^\perp$.
        Alors :
        $$ \varphi(d) = \langle d, v_\varphi \rangle_E = \langle d, P_F(v_\varphi) + (v_\varphi - P_F(v_\varphi)) \rangle_E $$
        Par linéarité du produit scalaire :
        $$ \varphi(d) = \langle d, P_F(v_\varphi) \rangle_E + \langle d, v_\varphi - P_F(v_\varphi) \rangle_E $$
        Puisque $d \in F$ et $(v_\varphi - P_F(v_\varphi)) \in F^\perp$, le deuxième terme est nul : $\langle d, v_\varphi - P_F(v_\varphi) \rangle_E = 0$.
        Donc, pour tout $d \in F$ :
        $$ S(\varphi, d) = \varphi(d) = \langle d, P_F(v_\varphi) \rangle_E $$

        *   **Cas 1 : $P_F(v_\varphi) = 0_E$.**
            Si $P_F(v_\varphi) = 0_E$, alors $S(\varphi, d) = \langle d, 0_E \rangle_E = 0$ pour tout $d \in F$.
            Le score maximal atteint est $0$.
            Tout vecteur $d^* \in F$ tel que $\|d^*\|_F = 1$ est un maximiseur (par exemple, n'importe quel vecteur de base de $F$, si $F$ n'est pas trivial).

        *   **Cas 2 : $P_F(v_\varphi) \ne 0_E$.**
            Nous voulons maximiser $\langle d, P_F(v_\varphi) \rangle_E$ sous la contrainte $\|d\|_F = 1$.
            En appliquant l'inégalité de Cauchy-Schwarz aux vecteurs $d \in F$ et $P_F(v_\varphi) \in F$:
            $$ |\langle d, P_F(v_\varphi) \rangle_E| \le \|d\|_E \|P_F(v_\varphi)\|_E $$
            Puisque $d \in F$, $\|d\|_E = \|d\|_F$. Avec la contrainte $\|d\|_F = 1$:
            $$ |\langle d, P_F(v_\varphi) \rangle_E| \le 1 \cdot \|P_F(v_\varphi)\|_E = \|P_F(v_\varphi)\|_E $$
            L'égalité est atteinte si et seulement si $d$ est colinéaire à $P_F(v_\varphi)$, et orienté dans la même direction.
            Le maximum est donc $\|P_F(v_\varphi)\|_E$.
            Le vecteur $d^* \in F$ de norme 1 qui réalise ce maximum est :
            $$ d^* = \frac{P_F(v_\varphi)}{\|P_F(v_\varphi)\|_E} $$
            La valeur du score maximal est $S(\varphi, d^*) = \varphi(d^*) = \left\langle \frac{P_F(v_\varphi)}{\|P_F(v_\varphi)\|_E}, P_F(v_\varphi) \right\rangle_E = \frac{1}{\|P_F(v_\varphi)\|_E} \|P_F(v_\varphi)\|_E^2 = \|P_F(v_\varphi)\|_E$.
            Ce vecteur $d^*$ est unique car la direction est unique (sauf si $P_F(v_\varphi)=0$).

**Partie III : Dualité de la projection**

3.  **La requête projetée et son vecteur de Riesz :**
    a.  La forme linéaire $\psi_F: F \to \mathbb{R}$ est définie comme la restriction de $\varphi$ à $F$.
        Pour justifier que $\psi_F \in F^*$, nous devons montrer qu'elle est une forme linéaire sur $F$.
        Soient $x_1, x_2 \in F$ et $\lambda \in \mathbb{R}$.
        $$ \psi_F(x_1 + \lambda x_2) = \varphi(x_1 + \lambda x_2) $$
        Puisque $\varphi \in E^*$ est une forme linéaire sur $E$, et que $F \subseteq E$:
        $$ \varphi(x_1 + \lambda x_2) = \varphi(x_1) + \lambda \varphi(x_2) $$
        Par définition de $\psi_F$:
        $$ \varphi(x_1) + \lambda \varphi(x_2) = \psi_F(x_1) + \lambda \psi_F(x_2) $$
        Donc $\psi_F(x_1 + \lambda x_2) = \psi_F(x_1) + \lambda \psi_F(x_2)$. $\psi_F$ est bien une forme linéaire sur $F$, d'où $\psi_F \in F^*$.

    b.  Nous cherchons $v_{\psi_F} \in F$ tel que pour tout $x \in F$, $\psi_F(x) = \langle x, v_{\psi_F} \rangle_F$.
        Nous savons, par définition de $\psi_F$, que pour tout $x \in F$, $\psi_F(x) = \varphi(x)$.
        Nous savons aussi, par définition de $v_\varphi$, que pour tout $x \in E$, $\varphi(x) = \langle x, v_\varphi \rangle_E$.
        Donc, pour tout $x \in F$:
        $$ \psi_F(x) = \langle x, v_\varphi \rangle_E $$
        Considérons maintenant $P_F(v_\varphi)$, qui est un vecteur de $F$.
        Pour tout $x \in F$:
        $$ \langle x, P_F(v_\varphi) \rangle_F = \langle x, P_F(v_\varphi) \rangle_E $$
        D'après la propriété de la projection orthogonale (Partie II, question 2.a), nous savons que $v_\varphi - P_F(v_\varphi) \in F^\perp$.
        Cela implique que pour tout $x \in F$:
        $$ \langle x, v_\varphi - P_F(v_\varphi) \rangle_E = 0 $$
        Ainsi :
        $$ \langle x, v_\varphi \rangle_E = \langle x, P_F(v_\varphi) + (v_\varphi - P_F(v_\varphi)) \rangle_E = \langle x, P_F(v_\varphi) \rangle_E + \langle x, v_\varphi - P_F(v_\varphi) \rangle_E = \langle x, P_F(v_\varphi) \rangle_E $$
        En combinant ces résultats, pour tout $x \in F$:
        $$ \psi_F(x) = \langle x, v_\varphi \rangle_E = \langle x, P_F(v_\varphi) \rangle_E = \langle x, P_F(v_\varphi) \rangle_F $$
        Nous avons donc trouvé un vecteur $w = P_F(v_\varphi) \in F$ tel que pour tout $x \in F$, $\psi_F(x) = \langle x, w \rangle_F$.
        Par l'unicité du vecteur de Riesz pour $F$ (garantie par la Partie I, question 1.b appliquée à $F$), nous pouvons conclure que :
        $$ v_{\psi_F} = P_F(v_\varphi) $$

    c.  **Interprétation :**
        Ce résultat établit une connexion profonde et élégante entre la dualité et la géométrie des espaces de plongement dans le contexte de la recherche sémantique.
        *   Initialement, une requête est représentée par une forme linéaire $\varphi \in E^*$. Grâce à l'isomorphisme de Riesz, cette forme linéaire peut être associée de manière unique à un vecteur $v_\varphi \in E$, le "vecteur de représentation" de la requête dans l'espace de plongement $E$.
        *   Lorsque nous nous intéressons à la pertinence d'une requête par rapport à des documents *limités à un sous-espace $F$* (ce qui peut modéliser, par exemple, une catégorie spécifique de documents, ou un sous-espace d'intérêt sémantique), nous pouvons considérer la "requête projetée" $\psi_F$, qui est la restriction de $\varphi$ à ce sous-espace $F$. Cette requête projetée est elle-même une forme linéaire sur $F$.
        *   Le résultat clé $v_{\psi_F} = P_F(v_\varphi)$ signifie que le vecteur de représentation de cette "requête projetée" (c'est-à-dire le vecteur qui, via le produit scalaire dans $F$, évalue la pertinence des documents de $F$ selon $\psi_F$) est précisément la **projection orthogonale** du vecteur de représentation original de la requête $v_\varphi$ sur le sous-espace $F$.

        En d'autres termes, pour évaluer la pertinence d'une requête dans un sous-espace sémantique $F$:
        1.  On peut d'abord transformer la requête linéaire $\varphi$ en son vecteur de représentation $v_\varphi$.
        2.  Puis, on projette ce vecteur $v_\varphi$ orthogonalement sur le sous-espace $F$. Le vecteur obtenu, $P_F(v_\varphi)$, est le vecteur optimal dans $F$ pour mesurer la similarité par rapport à la requête originale.

        Ceci justifie le fait que la projection orthogonale est l'opération géométrique naturelle pour adapter une requête (ou un "concept") à un sous-domaine d'intérêt. La recherche du document le plus pertinent dans $F$ revient à trouver le vecteur de $F$ qui est le plus proche, en termes de direction (similarité cosinus), de la projection de la requête sur $F$. Le résultat de la Partie II.c corrobore cela : le document optimal $d^*$ est la version normalisée de $P_F(v_\varphi)$. La dualité fournit ici une fondation théorique rigoureuse pour cette intuition géométrique.