# Exercice 07 (4 $\star$) : Optimisation de la Similarité Cosinus par Formes Linéaires Duales

## Énoncé
Soit $(V, \langle \cdot, \cdot \rangle)$ un espace vectoriel euclidien de dimension finie $n \ge 2$ sur $\mathbb{R}$. On note $\|\cdot\|$ la norme associée à ce produit scalaire, définie par $\|v\| = \sqrt{\langle v, v \rangle}$ pour tout $v \in V$. Soit $V^*$ son espace dual, c'est-à-dire l'ensemble des formes linéaires de $V$ dans $\mathbb{R}$.

1.  Rappeler la définition de la similarité cosinus entre deux vecteurs non nuls $u, v \in V$.
2.  Démontrer que l'application $\Phi: V \to V^*$ définie par $\Phi(v)(x) = \langle v, x \rangle$ pour tout $v, x \in V$ est un isomorphisme linéaire.
3.  Montrer que l'espace dual $V^*$ peut être muni d'un produit scalaire $\langle \cdot, \cdot \rangle_{V^*}$ tel que pour tout $f, g \in V^*$, si $f = \Phi(u)$ et $g = \Phi(v)$ pour $u, v \in V$, alors $\langle f, g \rangle_{V^*} = \langle u, v \rangle$. En déduire la norme associée $\|\cdot\|_{V^*}$ sur $V^*$.
4.  Soient $q \in V$ et $d \in V$ deux vecteurs non nuls et linéairement indépendants. On considère le problème d'optimisation suivant :
    $$ \text{Maximiser } f(q) \text{ sous les contraintes } f \in V^*, f(d) = 0 \text{ et } \|f\|_{V^*} = 1. $$
    On note $f_0$ une forme linéaire solution de ce problème.
    a.  Justifier l'existence d'une solution $f_0$.
    b.  Déterminer explicitement $f_0$ en fonction de $q$ et $d$.
    c.  Calculer la valeur maximale $f_0(q)$.
    d.  Interpréter géométriquement la forme linéaire $f_0$ et la valeur maximale $f_0(q)$ en relation avec la similarité cosinus.

## Correction Détaillée
### Analyse et Stratégie
L'exercice explore la relation fondamentale entre la géométrie d'un espace euclidien de dimension finie, la notion de similarité cosinus, et la structure de son espace dual. La première partie de l'exercice vise à établir les fondations théoriques nécessaires : la définition de la similarité cosinus, la démonstration rigoureuse du théorème de représentation de Riesz (qui établit un isomorphisme canonique entre $V$ et $V^*$), et la construction du produit scalaire et de la norme induits sur l'espace dual $V^*$. Ces étapes sont cruciales pour poser un cadre mathématique solide pour le problème d'optimisation.

La deuxième partie de l'exercice est un problème d'optimisation sous contraintes. La stratégie principale pour le résoudre consistera à traduire ce problème, initialement formulé dans l'espace dual $V^*$, vers l'espace vectoriel d'origine $V$ grâce à l'isomorphisme de Riesz. La contrainte $f(d)=0$ se transformera en une condition d'orthogonalité dans $V$. La contrainte de normalisation $\|f\|_{V^*}=1$ se traduira par une contrainte de normalisation de la norme dans $V$. Enfin, la fonction objectif $f(q)$ se reformulera comme un produit scalaire dans $V$. Une fois le problème entièrement reformulé dans $V$, il deviendra un problème classique de maximisation d'un produit scalaire sous des contraintes d'orthogonalité et de norme, qui se résout typiquement par l'utilisation de projections orthogonales. L'interprétation géométrique finale permettra de relier la solution obtenue au concept de similarité cosinus et de comprendre sa pertinence dans un contexte de recherche sémantique, où l'on cherche à caractériser des aspects distincts ou pertinents d'une requête par rapport à des documents.

### Résolution Pas-à-Pas

1.  **Définition de la similarité cosinus**
    Soient $u, v \in V$ deux vecteurs non nuls. La similarité cosinus entre $u$ et $v$ est définie par le rapport du produit scalaire de $u$ et $v$ à la produit de leurs normes :
    $$ \text{sim}(u,v) = \frac{\langle u, v \rangle}{\|u\| \|v\|} $$
    Cette valeur représente le cosinus de l'angle $\theta$ entre les vecteurs $u$ et $v$, où $\theta \in [0, \pi]$. Par l'inégalité de Cauchy-Schwarz, nous savons que $|\langle u, v \rangle| \le \|u\| \|v\|$, ce qui implique que $-1 \le \text{sim}(u,v) \le 1$.

2.  **Isomorphisme de Riesz**
    Démontrons que l'application $\Phi: V \to V^*$ définie par $\Phi(v)(x) = \langle v, x \rangle$ pour tout $v, x \in V$ est un isomorphisme linéaire.

    *   **Linéarité de $\Phi$ :**
        Pour montrer que $\Phi$ est linéaire, nous devons vérifier deux propriétés :
        a.  $\Phi(v_1 + v_2) = \Phi(v_1) + \Phi(v_2)$ pour tout $v_1, v_2 \in V$.
        b.  $\Phi(\lambda v_1) = \lambda \Phi(v_1)$ pour tout $v_1 \in V$ et $\lambda \in \mathbb{R}$.

        Pour la propriété (a), évaluons $\Phi(v_1 + v_2)$ sur un vecteur arbitraire $x \in V$:
        $$ \Phi(v_1 + v_2)(x) = \langle v_1 + v_2, x \rangle $$
        Par la bilinéarité du produit scalaire, nous avons :
        $$ \langle v_1 + v_2, x \rangle = \langle v_1, x \rangle + \langle v_2, x \rangle $$
        Par la définition de $\Phi$, ceci est égal à :
        $$ \langle v_1, x \rangle + \langle v_2, x \rangle = \Phi(v_1)(x) + \Phi(v_2)(x) $$
        Par la définition de l'addition de formes linéaires, nous avons :
        $$ \Phi(v_1)(x) + \Phi(v_2)(x) = (\Phi(v_1) + \Phi(v_2))(x) $$
        Puisque cette égalité est vraie pour tout $x \in V$, nous avons $\Phi(v_1 + v_2) = \Phi(v_1) + \Phi(v_2)$.

        Pour la propriété (b), évaluons $\Phi(\lambda v_1)$ sur un vecteur arbitraire $x \in V$:
        $$ \Phi(\lambda v_1)(x) = \langle \lambda v_1, x \rangle $$
        Par la bilinéarité du produit scalaire, nous avons :
        $$ \langle \lambda v_1, x \rangle = \lambda \langle v_1, x \rangle $$
        Par la définition de $\Phi$, ceci est égal à :
        $$ \lambda \langle v_1, x \rangle = \lambda \Phi(v_1)(x) $$
        Par la définition de la multiplication d'une forme linéaire par un scalaire, nous avons :
        $$ \lambda \Phi(v_1)(x) = (\lambda \Phi(v_1))(x) $$
        Puisque cette égalité est vraie pour tout $x \in V$, nous avons $\Phi(\lambda v_1) = \lambda \Phi(v_1)$.
        Ainsi, $\Phi$ est une application linéaire.

    *   **Injectivité de $\Phi$ :**
        Pour montrer que $\Phi$ est injective, nous devons montrer que son noyau est réduit au vecteur nul. C'est-à-dire, si $\Phi(v) = 0_{V^*}$ (la forme linéaire nulle), alors $v = 0_V$.
        Si $\Phi(v) = 0_{V^*}$, cela signifie que pour tout $x \in V$, $\Phi(v)(x) = 0$.
        Par la définition de $\Phi$, cela implique que $\langle v, x \rangle = 0$ pour tout $x \in V$.
        En particulier, en choisissant $x = v$, nous obtenons $\langle v, v \rangle = 0$.
        Puisque le produit scalaire est défini positif, $\langle v, v \rangle = 0$ implique que $v = 0_V$.
        Donc, $\text{Ker}(\Phi) = \{0_V\}$, ce qui prouve que $\Phi$ est injective.

    *   **Surjectivité de $\Phi$ :**
        Puisque $V$ est un espace vectoriel de dimension finie $n$, son espace dual $V^*$ a également pour dimension $n$.
        Nous avons $\dim(V) = n$ et $\dim(V^*) = n$.
        Puisque $\Phi: V \to V^*$ est une application linéaire injective entre deux espaces de même dimension finie, elle est nécessairement surjective.
        Pour être exhaustif, le théorème de représentation de Riesz pour les espaces euclidiens affirme que pour toute forme linéaire $f \in V^*$, il existe un unique vecteur $v \in V$ tel que $f(x) = \langle v, x \rangle$ pour tout $x \in V$.
        Pour prouver ce théorème, soit $(e_1, \dots, e_n)$ une base orthonormée de $V$. Pour tout $x \in V$, $x = \sum_{i=1}^n \langle x, e_i \rangle e_i$.
        Alors, pour toute forme linéaire $f \in V^*$, $f(x) = f\left(\sum_{i=1}^n \langle x, e_i \rangle e_i\right)$.
        Par linéarité de $f$, $f(x) = \sum_{i=1}^n \langle x, e_i \rangle f(e_i)$.
        Soit $v = \sum_{i=1}^n f(e_i) e_i$. Alors, en utilisant la bilinéarité du produit scalaire et l'orthonormalité de la base :
        $$ \langle v, x \rangle = \left\langle \sum_{i=1}^n f(e_i) e_i, x \right\rangle = \sum_{i=1}^n f(e_i) \langle e_i, x \rangle $$
        Puisque $\langle e_i, x \rangle = \langle x, e_i \rangle$ (symétrie du produit scalaire), nous avons :
        $$ \langle v, x \rangle = \sum_{i=1}^n f(e_i) \langle x, e_i \rangle = f(x) $$
        Ainsi, pour tout $f \in V^*$, il existe un $v \in V$ tel que $f = \Phi(v)$, ce qui prouve la surjectivité.

    En conclusion, $\Phi$ est un isomorphisme linéaire.

3.  **Produit scalaire et norme sur $V^*$**
    Nous voulons munir $V^*$ d'un produit scalaire $\langle \cdot, \cdot \rangle_{V^*}$ tel que pour tout $f, g \in V^*$, si $f = \Phi(u)$ et $g = \Phi(v)$ pour $u, v \in V$, alors $\langle f, g \rangle_{V^*} = \langle u, v \rangle$.

    Puisque $\Phi$ est un isomorphisme, pour tout $f \in V^*$, il existe un unique $u \in V$ tel que $f = \Phi(u)$, ce qui signifie $u = \Phi^{-1}(f)$. De même pour $g \in V^*$, il existe un unique $v \in V$ tel que $g = \Phi(v)$, ce qui signifie $v = \Phi^{-1}(g)$.
    Nous pouvons donc définir l'application $\langle \cdot, \cdot \rangle_{V^*}: V^* \times V^* \to \mathbb{R}$ par :
    $$ \langle f, g \rangle_{V^*} = \langle \Phi^{-1}(f), \Phi^{-1}(g) \rangle $$
    Vérifions que cette application est bien un produit scalaire sur $V^*$.

    *   **Symétrie :**
        Pour tout $f, g \in V^*$,
        $$ \langle f, g \rangle_{V^*} = \langle \Phi^{-1}(f), \Phi^{-1}(g) \rangle $$
        Puisque $\langle \cdot, \cdot \rangle$ est symétrique sur $V$, nous avons $\langle \Phi^{-1}(f), \Phi^{-1}(g) \rangle = \langle \Phi^{-1}(g), \Phi^{-1}(f) \rangle$.
        Donc, $\langle f, g \rangle_{V^*} = \langle g, f \rangle_{V^*}$.

    *   **Linéarité par rapport à la première variable :**
        Soient $f_1, f_2, g \in V^*$ et $\lambda \in \mathbb{R}$.
        $$ \langle f_1 + f_2, g \rangle_{V^*} = \langle \Phi^{-1}(f_1 + f_2), \Phi^{-1}(g) \rangle $$
        Puisque $\Phi$ est linéaire, son inverse $\Phi^{-1}$ est également linéaire. Donc $\Phi^{-1}(f_1 + f_2) = \Phi^{-1}(f_1) + \Phi^{-1}(f_2)$.
        Ainsi,
        $$ \langle f_1 + f_2, g \rangle_{V^*} = \langle \Phi^{-1}(f_1) + \Phi^{-1}(f_2), \Phi^{-1}(g) \rangle $$
        Par la linéarité du produit scalaire sur $V$ par rapport à la première variable :
        $$ \langle \Phi^{-1}(f_1) + \Phi^{-1}(f_2), \Phi^{-1}(g) \rangle = \langle \Phi^{-1}(f_1), \Phi^{-1}(g) \rangle + \langle \Phi^{-1}(f_2), \Phi^{-1}(g) \rangle $$
        Par la définition de $\langle \cdot, \cdot \rangle_{V^*}$, ceci est égal à $\langle f_1, g \rangle_{V^*} + \langle f_2, g \rangle_{V^*}$.
        De même,
        $$ \langle \lambda f_1, g \rangle_{V^*} = \langle \Phi^{-1}(\lambda f_1), \Phi^{-1}(g) \rangle = \langle \lambda \Phi^{-1}(f_1), \Phi^{-1}(g) \rangle = \lambda \langle \Phi^{-1}(f_1), \Phi^{-1}(g) \rangle = \lambda \langle f_1, g \rangle_{V^*} $$
        Donc, $\langle \cdot, \cdot \rangle_{V^*}$ est linéaire par rapport à la première variable.

    *   **Définition positive :**
        Pour tout $f \in V^*$,
        $$ \langle f, f \rangle_{V^*} = \langle \Phi^{-1}(f), \Phi^{-1}(f) \rangle $$
        Puisque $\langle \cdot, \cdot \rangle$ est défini positif sur $V$, $\langle \Phi^{-1}(f), \Phi^{-1}(f) \rangle \ge 0$.
        De plus, $\langle f, f \rangle_{V^*} = 0$ si et seulement si $\langle \Phi^{-1}(f), \Phi^{-1}(f) \rangle = 0$.
        Ceci implique $\Phi^{-1}(f) = 0_V$ (par la propriété de définition positive du produit scalaire sur $V$).
        Puisque $\Phi^{-1}$ est un isomorphisme, $\Phi^{-1}(f) = 0_V$ si et seulement si $f = \Phi(0_V) = 0_{V^*}$.
        Donc, $\langle \cdot, \cdot \rangle_{V^*}$ est défini positif.

    Ainsi, $\langle \cdot, \cdot \rangle_{V^*}$ est bien un produit scalaire sur $V^*$.

    La norme associée $\|\cdot\|_{V^*}$ sur $V^*$ est définie par $\|f\|_{V^*} = \sqrt{\langle f, f \rangle_{V^*}}$.
    En utilisant la définition du produit scalaire sur $V^*$:
    $$ \|f\|_{V^*} = \sqrt{\langle \Phi^{-1}(f), \Phi^{-1}(f) \rangle} = \|\Phi^{-1}(f)\| $$
    Si $f = \Phi(u)$, alors $\Phi^{-1}(f) = u$. Donc, $\|f\|_{V^*} = \|u\|$.
    Cette norme est également appelée la norme d'opérateur pour les formes linéaires, car pour $f \in V^*$, $\|f\|_{V^*} = \sup_{x \in V, x \neq 0} \frac{|f(x)|}{\|x\|}$.
    Pour le prouver, soit $f = \Phi(u)$. Alors $f(x) = \langle u, x \rangle$.
    Par l'inégalité de Cauchy-Schwarz, $|f(x)| = |\langle u, x \rangle| \le \|u\| \|x\|$.
    Donc, pour $x \neq 0$, $\frac{|f(x)|}{\|x\|} \le \|u\|$.
    Cette borne supérieure est atteinte lorsque $x$ est colinéaire à $u$. En prenant $x = u$ (si $u \neq 0$), on a $\frac{|f(u)|}{\|u\|} = \frac{|\langle u, u \rangle|}{\|u\|} = \frac{\|u\|^2}{\|u\|} = \|u\|$.
    Donc, $\|f\|_{V^*} = \|u\| = \|\Phi^{-1}(f)\|$.

4.  **Problème d'optimisation**
    Soient $q \in V$ et $d \in V$ deux vecteurs non nuls et linéairement indépendants.
    On cherche à maximiser $f(q)$ sous les contraintes $f \in V^*$, $f(d) = 0$ et $\|f\|_{V^*} = 1$.

    a.  **Justification de l'existence d'une solution $f_0$**
        L'ensemble des formes linéaires $f \in V^*$ telles que $\|f\|_{V^*} = 1$ est la sphère unité de $V^*$, notée $S_{V^*} = \{f \in V^* \mid \|f\|_{V^*} = 1\}$.
        Puisque $V^*$ est un espace vectoriel de dimension finie, $S_{V^*}$ est un ensemble fermé et borné, donc compact dans $V^*$.
        La contrainte $f(d) = 0$ définit un sous-espace vectoriel de $V^*$, appelé l'annihilateur de $d$, noté $(\text{span}\{d\})^\perp$. C'est un sous-espace fermé de $V^*$.
        L'ensemble des contraintes est donc l'intersection de la sphère unité $S_{V^*}$ et du sous-espace fermé $(\text{span}\{d\})^\perp$. Cette intersection est un ensemble fermé et borné, donc compact.
        Puisque $d \neq 0$, $\text{span}\{d\}$ est un sous-espace de dimension 1. Son annihilateur $(\text{span}\{d\})^\perp$ est un sous-espace de $V^*$ de dimension $\dim(V^*) - \dim(\text{span}\{d\}) = n-1$. Puisque $n \ge 2$, $n-1 \ge 1$, donc $(\text{span}\{d\})^\perp$ est non vide et contient des vecteurs non nuls. Par conséquent, l'intersection $S_{V^*} \cap (\text{span}\{d\})^\perp$ est non vide.
        La fonction objectif $J(f) = f(q)$ est une application linéaire de $V^*$ dans $\mathbb{R}$. Toute application linéaire sur un espace de dimension finie est continue.
        Puisque nous maximisons une fonction continue sur un ensemble compact non vide, le théorème des valeurs extrêmes (théorème de Weierstrass) garantit l'existence d'une solution $f_0$.

    b.  **Détermination explicite de $f_0$}**
        Nous allons traduire le problème dans l'espace $V$ via l'isomorphisme $\Phi$.
        Soit $f \in V^*$. Il existe un unique $v \in V$ tel que $f = \Phi(v)$.
        Les contraintes se traduisent comme suit :
        *   $f(d) = 0 \implies \Phi(v)(d) = 0 \implies \langle v, d \rangle = 0$. Cela signifie que le vecteur $v$ doit appartenir à l'orthogonal de $d$, noté $d^\perp = \{x \in V \mid \langle x, d \rangle = 0\}$.
        *   $\|f\|_{V^*} = 1 \implies \|\Phi(v)\|_{V^*} = 1$. D'après la question 3, cela implique $\|v\| = 1$.
        L'objectif $f(q)$ se traduit par :
        *   $f(q) = \Phi(v)(q) = \langle v, q \rangle$.

        Le problème d'optimisation devient donc :
        $$ \text{Maximiser } \langle v, q \rangle \text{ sous les contraintes } v \in V, v \in d^\perp \text{ et } \|v\| = 1. $$
        Nous cherchons un vecteur unitaire $v_0 \in d^\perp$ qui maximise $\langle v, q \rangle$.
        Soit $P_{d^\perp}$ l'opérateur de projection orthogonale sur le sous-espace $d^\perp$.
        Pour tout $v \in d^\perp$, nous avons $\langle v, q \rangle = \langle v, P_{d^\perp}(q) \rangle$. En effet, $q = P_{d^\perp}(q) + P_{\text{span}\{d\}}(q)$, et puisque $v \in d^\perp$, $\langle v, P_{\text{span}\{d\}}(q) \rangle = 0$.
        Par l'inégalité de Cauchy-Schwarz, $|\langle v, P_{d^\perp}(q) \rangle| \le \|v\| \|P_{d^\perp}(q)\|$.
        Puisque $\|v\|=1$, nous avons $|\langle v, q \rangle| \le \|P_{d^\perp}(q)\|$.
        L'égalité est atteinte lorsque $v$ est colinéaire à $P_{d^\perp}(q)$ et dans la même direction.
        Donc, le vecteur $v_0$ qui maximise $\langle v, q \rangle$ doit être :
        $$ v_0 = \frac{P_{d^\perp}(q)}{\|P_{d^\perp}(q)\|} $$
        Il est nécessaire de s'assurer que $P_{d^\perp}(q) \neq 0_V$.
        Le sous-espace $d^\perp$ est l'orthogonal de la droite vectorielle engendrée par $d$.
        La projection orthogonale de $q$ sur $d^\perp$ est donnée par $P_{d^\perp}(q) = q - P_{\text{span}\{d\}}(q)$.
        La projection orthogonale de $q$ sur $\text{span}\{d\}$ est $P_{\text{span}\{d\}}(q) = \frac{\langle q, d \rangle}{\langle d, d \rangle} d = \frac{\langle q, d \rangle}{\|d\|^2} d$.
        Donc, $P_{d^\perp}(q) = q - \frac{\langle q, d \rangle}{\|d\|^2} d$.
        Si $P_{d^\perp}(q) = 0_V$, alors $q = \frac{\langle q, d \rangle}{\|d\|^2} d$. Cela signifie que $q$ est colinéaire à $d$.
        Cependant, l'énoncé stipule que $q$ et $d$ sont linéairement indépendants. Par conséquent, $P_{d^\perp}(q) \neq 0_V$.
        Ainsi, le vecteur $v_0$ est bien défini.

        La forme linéaire $f_0$ est alors $\Phi(v_0)$.
        $$ f_0 = \Phi\left(\frac{q - \frac{\langle q, d \rangle}{\|d\|^2} d}{\left\|q - \frac{\langle q, d \rangle}{\|d\|^2} d\right\|}\right) $$
        Pour tout $x \in V$, $f_0(x) = \left\langle \frac{q - \frac{\langle q, d \rangle}{\|d\|^2} d}{\left\|q - \frac{\langle q, d \rangle}{\|d\|^2} d\right\|}, x \right\rangle$.

    c.  **Calcul de la valeur maximale $f_0(q)$**
        La valeur maximale de $f(q)$ est $\langle v_0, q \rangle$.
        $$ \langle v_0, q \rangle = \left\langle \frac{P_{d^\perp}(q)}{\|P_{d^\perp}(q)\|}, q \right\rangle $$
        Puisque $P_{d^\perp}(q) \in d^\perp$, nous avons $\langle P_{d^\perp}(q), d \rangle = 0$.
        De plus, nous pouvons décomposer $q$ en ses composantes orthogonales par rapport à $d^\perp$ et $\text{span}\{d\}$ : $q = P_{d^\perp}(q) + P_{\text{span}\{d\}}(q)$.
        Donc,
        $$ \langle v_0, q \rangle = \frac{1}{\|P_{d^\perp}(q)\|} \langle P_{d^\perp}(q), P_{d^\perp}(q) + P_{\text{span}\{d\}}(q) \rangle $$
        Par l'orthogonalité de $P_{d^\perp}(q)$ et $P_{\text{span}\{d\}}(q)$, nous avons $\langle P_{d^\perp}(q), P_{\text{span}\{d\}}(q) \rangle = 0$.
        Ainsi,
        $$ \langle v_0, q \rangle = \frac{1}{\|P_{d^\perp}(q)\|} \langle P_{d^\perp}(q), P_{d^\perp}(q) \rangle = \frac{\|P_{d^\perp}(q)\|^2}{\|P_{d^\perp}(q)\|} = \|P_{d^\perp}(q)\| $$
        Calculons $\|P_{d^\perp}(q)\|$:
        $$ \|P_{d^\perp}(q)\|^2 = \left\|q - \frac{\langle q, d \rangle}{\|d\|^2} d\right\|^2 $$
        En développant la norme au carré :
        $$ \|P_{d^\perp}(q)\|^2 = \left\langle q - \frac{\langle q, d \rangle}{\|d\|^2} d, q - \frac{\langle q, d \rangle}{\|d\|^2} d \right\rangle $$
        $$ = \langle q, q \rangle - 2 \left\langle q, \frac{\langle q, d \rangle}{\|d\|^2} d \right\rangle + \left\langle \frac{\langle q, d \rangle}{\|d\|^2} d, \frac{\langle q, d \rangle}{\|d\|^2} d \right\rangle $$
        $$ = \|q\|^2 - 2 \frac{\langle q, d \rangle}{\|d\|^2} \langle q, d \rangle + \left(\frac{\langle q, d \rangle}{\|d\|^2}\right)^2 \langle d, d \rangle $$
        $$ = \|q\|^2 - 2 \frac{(\langle q, d \rangle)^2}{\|d\|^2} + \frac{(\langle q, d \rangle)^2}{\|d\|^4} \|d\|^2 $$
        $$ = \|q\|^2 - 2 \frac{(\langle q, d \rangle)^2}{\|d\|^2} + \frac{(\langle q, d \rangle)^2}{\|d\|^2} $$
        $$ = \|q\|^2 - \frac{(\langle q, d \rangle)^2}{\|d\|^2} $$
        Nous savons que la similarité cosinus entre $q$ et $d$ est $\text{sim}(q,d) = \frac{\langle q, d \rangle}{\|q\| \|d\|}$.
        Donc, $\langle q, d \rangle = \|q\| \|d\| \text{sim}(q,d)$. Substituons cette expression :
        $$ \|P_{d^\perp}(q)\|^2 = \|q\|^2 - \frac{(\|q\| \|d\| \text{sim}(q,d))^2}{\|d\|^2} $$
        $$ = \|q\|^2 - \frac{\|q\|^2 \|d\|^2 (\text{sim}(q,d))^2}{\|d\|^2} $$
        $$ = \|q\|^2 - \|q\|^2 (\text{sim}(q,d))^2 $$
        $$ = \|q\|^2 (1 - (\text{sim}(q,d))^2) $$
        Soit $\theta$ l'angle entre $q$ et $d$. Alors $\text{sim}(q,d) = \cos(\theta)$.
        $$ \|P_{d^\perp}(q)\|^2 = \|q\|^2 (1 - \cos^2(\theta)) = \|q\|^2 \sin^2(\theta) $$
        Puisque $q$ et $d$ sont linéairement indépendants, $\theta \neq 0$ et $\theta \neq \pi$. Par conséquent, $\sin(\theta) \neq 0$.
        De plus, pour $\theta \in [0, \pi]$, $\sin(\theta) \ge 0$.
        Donc, $\|P_{d^\perp}(q)\| = \sqrt{\|q\|^2 \sin^2(\theta)} = \|q\| \sin(\theta)$.

        La valeur maximale $f_0(q)$ est donc $\|q\| \sin(\theta)$, où $\theta$ est l'angle entre $q$ et $d$.

    d.  **Interprétation géométrique et relation avec la similarité cosinus**
        La forme linéaire $f_0 = \Phi(v_0)$ est associée au vecteur $v_0 = \frac{P_{d^\perp}(q)}{\|P_{d^\perp}(q)\|}$.
        Ce vecteur $v_0$ est le vecteur unitaire dans $V$ qui est orthogonal à $d$ (car $v_0 \in d^\perp$) et qui est le plus "aligné" avec $q$ parmi tous les vecteurs unitaires orthogonaux à $d$.
        Géométriquement, $P_{d^\perp}(q)$ est la composante de $q$ qui est orthogonale à $d$. C'est le vecteur qui reste de $q$ une fois que toute sa composante colinéaire à $d$ a été retirée.
        La contrainte $f_0(d) = 0$ signifie que la forme linéaire $f_0$ "ignore" complètement le document $d$. Dans le contexte d'un moteur de recherche sémantique, cela pourrait signifier que $f_0$ représente une "caractéristique sémantique" ou un "concept" qui n'est pas présent ou n'est pas pertinent pour le document $d$.
        La valeur maximale $f_0(q)$ est $\|P_{d^\perp}(q)\| = \|q\| \sin(\theta)$.
        Nous avons établi que $\text{sim}(q,d) = \cos(\theta)$.
        La valeur maximale $f_0(q)$ peut donc s'écrire $\|q\| \sqrt{1 - (\text{sim}(q,d))^2}$.
        Cette valeur représente la "force" ou la "magnitude" de la composante de $q$ qui est orthogonalement distincte de $d$. C'est une mesure de la "nouveauté" ou de l'"information non redondante" de $q$ par rapport à $d$, vue à travers le prisme de l'espace dual.
        *   Si $q$ et $d$ sont très similaires (c'est-à-dire $\text{sim}(q,d)$ est proche de 1, ce qui signifie que $\theta$ est proche de 0), alors $\sin(\theta)$ est proche de 0, et $f_0(q)$ est proche de 0. Cela indique qu'il est difficile de trouver une forme linéaire qui distingue $q$ de $d$ tout en étant orthogonale à $d$, car $q$ est presque colinéaire à $d$.
        *   Si $q$ et $d$ sont orthogonaux (c'est-à-dire $\text{sim}(q,d) = 0$, ce qui signifie $\theta = \pi/2$), alors $\sin(\theta) = 1$, et $f_0(q) = \|q\|$. Dans ce cas, $P_{d^\perp}(q) = q$, et $v_0 = q/\|q\|$. La forme linéaire $f_0$ est alors $\Phi(q/\|q\|)$, et $f_0(q) = \langle q/\|q\|, q \rangle = \|q\|$. Cela signifie que la forme linéaire qui maximise $f(q)$ tout en étant orthogonale à $d$ est simplement la forme linéaire associée à la direction de $q$ lui-même, car $q$ est déjà orthogonal à $d$.

        En résumé, $f_0$ est la forme linéaire duale du vecteur unitaire qui représente la composante de $q$ la plus "distincte" de $d$ en termes d'orthogonalité. La valeur maximale $f_0(q)$ quantifie cette "distinctivité" de $q$ par rapport à $d$ dans la direction orthogonale à $d$. Ce concept est pertinent pour la conception de moteurs de recherche sémantiques, où l'on pourrait vouloir identifier des aspects d'une requête qui sont uniques par rapport à des documents déjà connus ou jugés non pertinents, permettant ainsi une exploration plus fine de l'espace sémantique.

### Conclusion
Nous avons démontré que l'espace dual $V^*$ d'un espace euclidien $V$ est lui-même un espace euclidien, isomorphe à $V$ via l'isomorphisme de Riesz $\Phi$. Ce cadre a permis de reformuler un problème d'optimisation dans $V^*$ en un problème équivalent dans $V$.

Le problème d'optimisation consistant à maximiser $f(q)$ sous les contraintes $f(d)=0$ et $\|f\|_{V^*}=1$ a été résolu. La forme linéaire $f_0$ solution est donnée par :
$$ f_0 = \Phi\left(\frac{q - \frac{\langle q, d \rangle}{\|d\|^2} d}{\left\|q - \frac{\langle q, d \rangle}{\|d\|^2} d\right\|}\right) $$
La valeur maximale $f_0(q)$ est :
$$ f_0(q) = \left\|q - \frac{\langle q, d \rangle}{\|d\|^2} d\right\| = \|q\| \sqrt{1 - \left(\frac{\langle q, d \rangle}{\|q\| \|d\|}\right)^2} = \|q\| \sin(\theta) $$
où $\theta$ est l'angle entre les vecteurs $q$ et $d$.

Géométriquement, $f_0$ est la forme linéaire associée au vecteur unitaire $v_0$ qui représente la direction de la projection orthogonale de $q$ sur l'orthogonal de $d$. La valeur maximale $f_0(q)$ est la norme de cette projection. Ce résultat quantifie la "partie" de la requête $q$ qui est sémantiquement distincte du document $d$, mesurée dans une direction orthogonale à $d$. Plus $q$ est orthogonal à $d$, plus cette "distinctivité" est grande, et plus $f_0(q)$ est élevé. Inversement, plus $q$ est similaire à $d$, plus $f_0(q)$ est faible, indiquant une faible "distinctivité" dans la direction orthogonale à $d$. Cette analyse est cruciale pour la conception de moteurs de recherche sémantiques, où l'on pourrait vouloir identifier des aspects d'une requête qui sont uniques par rapport à des documents déjà connus ou jugés non pertinents, permettant ainsi une exploration plus fine de l'espace sémantique.
