Voici l'Exercice 4, conçu avec la rigueur et la profondeur attendues par le jury d'un concours exigeant comme celui de l'École Polytechnique.

---

# Exercice 4 : Robustesse Sémantique et Dualité dans les Espaces de Plongement

**Contexte pour la Conception Théorique d'un Moteur de Recherche Sémantique :**
Dans le domaine des moteurs de recherche sémantiques, les entités (requêtes, documents, concepts) sont représentées par des vecteurs dans des espaces de plongement (embedding spaces). La similarité cosinus est une mesure fondamentale pour évaluer la pertinence. Cependant, ces espaces peuvent contenir des dimensions représentant du "bruit" ou des caractéristiques sémantiques indésirables ou non pertinentes pour une tâche donnée. L'objectif est de développer une mesure de similarité plus robuste en projetant les vecteurs sur un sous-espace de "caractéristiques sémantiques pertinentes". Cet exercice explore les propriétés algébriques et géométriques de cette approche, en mettant en lumière le rôle de la dualité.

---

## Énoncé de l'Exercice

Soit $E$ un espace vectoriel euclidien de dimension finie $n \ge 2$ sur le corps des nombres réels $\mathbb{R}$. Nous notons $\langle \cdot, \cdot \rangle: E \times E \to \mathbb{R}$ le produit scalaire sur $E$, et $\| \cdot \|: E \to \mathbb{R}_+$ la norme euclidienne associée, définie par $\| \mathbf{u} \| = \sqrt{\langle \mathbf{u}, \mathbf{u} \rangle}$ pour tout $\mathbf{u} \in E$.

**Hypothèses Fondamentales :**
1.  L'espace $E$ est le *précis* "espace de plongement" où sont représentées les entités sémantiques.
2.  Nous identifions un sous-espace $V$ de $E$ comme le "sous-espace des caractéristiques sémantiques pertinentes". Nous supposons que $V$ est un sous-espace propre de $E$, c'est-à-dire $V \ne \{ \mathbf{0}_E \}$ et $V \ne E$. Sa dimension est notée $k = \text{dim}(V)$, avec $1 \le k < n$.
3.  Le complément orthogonal de $V$ dans $E$ est noté $V^\perp = \{ \mathbf{w} \in E \mid \forall \mathbf{v} \in V, \langle \mathbf{w}, \mathbf{v} \rangle = 0 \}$. Nous savons que $E = V \oplus V^\perp$.
4.  L'opérateur de projection orthogonale sur $V$ est noté $P_V: E \to V$. Pour tout $\mathbf{x} \in E$, $\mathbf{x}$ se décompose de manière unique en $\mathbf{x} = \mathbf{x}_V + \mathbf{x}_{V^\perp}$ où $\mathbf{x}_V \in V$ et $\mathbf{x}_{V^\perp} \in V^\perp$. Par définition, $P_V(\mathbf{x}) = \mathbf{x}_V$.

Pour une requête $\mathbf{q} \in E$ et un document $\mathbf{d} \in E$, la similarité cosinus standard est définie par :
$$ \text{sim}(\mathbf{q}, \mathbf{d}) = \frac{\langle \mathbf{q}, \mathbf{d} \rangle}{\| \mathbf{q} \| \| \mathbf{d} \|} $$
pour tout $\mathbf{q}, \mathbf{d} \in E \setminus \{ \mathbf{0}_E \}$.

Pour introduire une *robustesse sémantique*, nous définissons le *vecteur de requête robuste* comme $\mathbf{q}_V = P_V(\mathbf{q})$ et le *vecteur de document robuste* comme $\mathbf{d}_V = P_V(\mathbf{d})$.
La *similarité cosinus robuste* est alors définie par :
$$ \text{sim}_V(\mathbf{q}, \mathbf{d}) = \frac{\langle \mathbf{q}_V, \mathbf{d}_V \rangle}{\| \mathbf{q}_V \| \| \mathbf{d}_V \|} $$
pour tout $\mathbf{q}, \mathbf{d} \in E$ tels que $\mathbf{q}_V \ne \mathbf{0}_E$ et $\mathbf{d}_V \ne \mathbf{0}_E$.

Soit $E^*$ l'espace dual de $E$, c'est-à-dire l'espace des formes linéaires sur $E$. On rappelle que pour tout $f \in E^*$, il existe un unique vecteur $\mathbf{u}_f \in E$ tel que $f(\mathbf{v}) = \langle \mathbf{u}_f, \mathbf{v} \rangle$ pour tout $\mathbf{v} \in E$. L'application $\Phi: E \to E^*$ définie par $\Phi(\mathbf{u}) = f_{\mathbf{u}}$, où $f_{\mathbf{u}}(\mathbf{v}) = \langle \mathbf{u}, \mathbf{v} \rangle$, est un isomorphisme isométrique d'espaces vectoriels euclidiens.

---

**Questions :**

1.  **Propriétés des Opérateurs de Projection :**
    *   a) Démontrer que $P_V$ est un opérateur linéaire. Montrer que $P_V^2 = P_V$. En déduire que $I - P_V$ est également un opérateur de projection orthogonale, et spécifier le sous-espace sur lequel il projette. (Ici, $I$ désigne l'opérateur identité sur $E$.)
    *   b) Pour tout $\mathbf{u}, \mathbf{v} \in E$, établir la relation $\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle$. Quelle propriété de l'opérateur $P_V$ en déduit-on concernant son adjoint ?

2.  **Robustesse Sémantique et Dualité :**
    *   a) Soit $f \in E^*$. Nous définissons l'opérateur $P_V^*: E^* \to E^*$ par la relation $(P_V^*(f))(\mathbf{v}) = f(P_V(\mathbf{v}))$ pour tout $\mathbf{v} \in E$. Démontrer que $P_V^*$ est un opérateur linéaire.
    *   b) Démontrer que pour tout $\mathbf{u} \in E$, l'égalité $\Phi(P_V(\mathbf{u})) = P_V^*(\Phi(\mathbf{u}))$ est vérifiée. Interpréter la signification de cette relation en termes de l'isomorphisme de Riesz.
    *   c) Exprimer le produit scalaire $\langle \mathbf{q}_V, \mathbf{d}_V \rangle$ en fonction de la forme linéaire $f_{\mathbf{q}} = \Phi(\mathbf{q})$ et de $P_V(\mathbf{d})$. En déduire une expression en termes de la forme linéaire $P_V^*(f_{\mathbf{q}})$.
    *   d) Soit la forme linéaire $f_{\mathbf{q},V}: E \to \mathbb{R}$ définie par $f_{\mathbf{q},V}(\mathbf{d}) = \langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle$. Montrer que $f_{\mathbf{q},V}$ appartient à l'image de $P_V^*$. Caractériser le noyau de $f_{\mathbf{q},V}$ en fonction de $V$ et du vecteur $\mathbf{q}$.

3.  **Interprétation Géométrique et Application à la Recherche Sémantique :**
    *   a) Supposons $\mathbf{q}_V \ne \mathbf{0}_E$. Démontrer que maximiser $\text{sim}_V(\mathbf{q}, \mathbf{d})$ sur un ensemble de documents $\mathbf{d}$ pour lesquels $\| \mathbf{d}_V \|$ est constant (et non nul) est équivalent à maximiser $\langle \frac{\mathbf{q}_V}{\| \mathbf{q}_V \|}, \mathbf{d}_V \rangle$. Expliquer pourquoi ceci est une approche standard dans la recherche par similarité.
    *   b) Soit $(\mathbf{e}_1, \dots, \mathbf{e}_k)$ une base orthonormée de $V$. Exprimer $P_V(\mathbf{x})$ pour un vecteur quelconque $\mathbf{x} \in E$ à l'aide de cette base.
    *   c) Étude de cas concret : Soit $E = \mathbb{R}^3$ muni du produit scalaire euclidien canonique. On choisit $V$ comme le plan $xy$, c'est-à-dire $V = \{ (x,y,0) \in \mathbb{R}^3 \mid x, y \in \mathbb{R} \}$.
        Considérons la requête $\mathbf{q} = (1, 1, 1)$ et deux documents $\mathbf{d}_1 = (1, 0, 0)$ et $\mathbf{d}_2 = (0, 0, 1)$.
        Calculer les quatre valeurs suivantes : $\text{sim}(\mathbf{q}, \mathbf{d}_1)$, $\text{sim}(\mathbf{q}, \mathbf{d}_2)$, $\text{sim}_V(\mathbf{q}, \mathbf{d}_1)$, et $\text{sim}_V(\mathbf{q}, \mathbf{d}_2)$.
        Discuter des implications de ces résultats pour la conception d'un moteur de recherche sémantique, en particulier en ce qui concerne la gestion du "bruit sémantique".

---

## Correction de l'Exercice

### Rappels Préliminaires
Soit $E$ un espace vectoriel euclidien de dimension $n$. Pour tout $\mathbf{x} \in E$, il existe une décomposition unique $\mathbf{x} = \mathbf{x}_V + \mathbf{x}_{V^\perp}$ où $\mathbf{x}_V \in V$ et $\mathbf{x}_{V^\perp} \in V^\perp$. L'opérateur de projection orthogonale $P_V$ est défini par $P_V(\mathbf{x}) = \mathbf{x}_V$. De même, l'opérateur de projection orthogonale sur $V^\perp$ est $P_{V^\perp}(\mathbf{x}) = \mathbf{x}_{V^\perp}$. Il est important de noter que $\mathbf{x}_{V^\perp} = \mathbf{x} - P_V(\mathbf{x}) = (I - P_V)(\mathbf{x})$.

### 1. Propriétés des Opérateurs de Projection :

#### 1.a) Linéarité et Idempotence de $P_V$
Pour démontrer la linéarité de $P_V$, nous devons montrer que pour tout $\mathbf{x}, \mathbf{y} \in E$ et tout scalaire $\lambda \in \mathbb{R}$, $P_V(\mathbf{x} + \mathbf{y}) = P_V(\mathbf{x}) + P_V(\mathbf{y})$ et $P_V(\lambda \mathbf{x}) = \lambda P_V(\mathbf{x})$.

Soient $\mathbf{x}, \mathbf{y} \in E$. Leurs décompositions uniques sont $\mathbf{x} = \mathbf{x}_V + \mathbf{x}_{V^\perp}$ et $\mathbf{y} = \mathbf{y}_V + \mathbf{y}_{V^\perp}$.
Par définition, $P_V(\mathbf{x}) = \mathbf{x}_V$ et $P_V(\mathbf{y}) = \mathbf{y}_V$.

Considérons la somme $\mathbf{x} + \mathbf{y}$:
$\mathbf{x} + \mathbf{y} = (\mathbf{x}_V + \mathbf{x}_{V^\perp}) + (\mathbf{y}_V + \mathbf{y}_{V^\perp}) = (\mathbf{x}_V + \mathbf{y}_V) + (\mathbf{x}_{V^\perp} + \mathbf{y}_{V^\perp})$.
Puisque $V$ est un sous-espace vectoriel, $\mathbf{x}_V + \mathbf{y}_V \in V$.
Puisque $V^\perp$ est un sous-espace vectoriel, $\mathbf{x}_{V^\perp} + \mathbf{y}_{V^\perp} \in V^\perp$.
La décomposition de $\mathbf{x} + \mathbf{y}$ est unique. Donc, $P_V(\mathbf{x} + \mathbf{y}) = \mathbf{x}_V + \mathbf{y}_V$.
Par substitution, $P_V(\mathbf{x} + \mathbf{y}) = P_V(\mathbf{x}) + P_V(\mathbf{y})$.

Considérons le produit par un scalaire $\lambda \in \mathbb{R}$:
$\lambda \mathbf{x} = \lambda (\mathbf{x}_V + \mathbf{x}_{V^\perp}) = \lambda \mathbf{x}_V + \lambda \mathbf{x}_{V^\perp}$.
Puisque $V$ est un sous-espace vectoriel, $\lambda \mathbf{x}_V \in V$.
Puisque $V^\perp$ est un sous-espace vectoriel, $\lambda \mathbf{x}_{V^\perp} \in V^\perp$.
La décomposition de $\lambda \mathbf{x}$ est unique. Donc, $P_V(\lambda \mathbf{x}) = \lambda \mathbf{x}_V$.
Par substitution, $P_V(\lambda \mathbf{x}) = \lambda P_V(\mathbf{x})$.
Ainsi, $P_V$ est un opérateur linéaire.

Pour démontrer que $P_V^2 = P_V$:
Pour tout $\mathbf{x} \in E$, $P_V(\mathbf{x}) = \mathbf{x}_V$. Par définition, $\mathbf{x}_V \in V$.
Lorsque nous appliquons $P_V$ à un vecteur qui est déjà dans $V$, le vecteur est projeté sur lui-même. C'est-à-dire, si $\mathbf{v} \in V$, alors sa décomposition est $\mathbf{v} = \mathbf{v} + \mathbf{0}_{V^\perp}$, donc $P_V(\mathbf{v}) = \mathbf{v}$.
Par conséquent, $P_V(P_V(\mathbf{x})) = P_V(\mathbf{x}_V) = \mathbf{x}_V = P_V(\mathbf{x})$.
Donc, $P_V^2 = P_V$. Un tel opérateur est dit idempotent.

Déduction pour $I - P_V$:
Soit $Q = I - P_V$.
Linéarité : Puisque $I$ et $P_V$ sont linéaires, leur différence est également linéaire.
Idempotence :
$Q^2 = (I - P_V)(I - P_V) = I^2 - I P_V - P_V I + P_V^2 = I - P_V - P_V + P_V = I - P_V = Q$.
Donc $I - P_V$ est également un opérateur idempotent.
Pour tout $\mathbf{x} \in E$, $(I - P_V)(\mathbf{x}) = \mathbf{x} - P_V(\mathbf{x}) = \mathbf{x} - \mathbf{x}_V = \mathbf{x}_{V^\perp}$.
Puisque $\mathbf{x}_{V^\perp} \in V^\perp$, l'opérateur $I - P_V$ projette sur le sous-espace $V^\perp$. Il s'agit donc de l'opérateur de projection orthogonale sur $V^\perp$, noté $P_{V^\perp}$.

#### 1.b) Relation sur le produit scalaire et l'adjoint de $P_V$
Soient $\mathbf{u}, \mathbf{v} \in E$. Nous utilisons les décompositions uniques:
$\mathbf{u} = P_V(\mathbf{u}) + P_{V^\perp}(\mathbf{u})$
$\mathbf{v} = P_V(\mathbf{v}) + P_{V^\perp}(\mathbf{v})$

Calculons $\langle \mathbf{u}, P_V(\mathbf{v}) \rangle$:
$\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}) + P_{V^\perp}(\mathbf{u}), P_V(\mathbf{v}) \rangle$.
Par linéarité du produit scalaire :
$\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle + \langle P_{V^\perp}(\mathbf{u}), P_V(\mathbf{v}) \rangle$.
Puisque $P_V(\mathbf{u}) \in V$, $P_V(\mathbf{v}) \in V$, et $P_{V^\perp}(\mathbf{u}) \in V^\perp$, par définition de l'orthogonalité des sous-espaces $V$ et $V^\perp$, tout vecteur de $V^\perp$ est orthogonal à tout vecteur de $V$.
Ainsi, $\langle P_{V^\perp}(\mathbf{u}), P_V(\mathbf{v}) \rangle = 0$.
Par conséquent, nous obtenons :
$$ \langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle $$
Cette relation démontre que $P_V$ est un opérateur auto-adjoint (ou symétrique). En effet, par définition, l'adjoint $P_V^*$ de $P_V$ est l'opérateur tel que $\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V^*(\mathbf{u}), \mathbf{v} \rangle$ pour tout $\mathbf{u}, \mathbf{v} \in E$.
La relation que nous venons d'établir est $\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle$.
Par la relation $\langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) + P_{V^\perp}(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), \mathbf{v} \rangle$ (car $P_V(\mathbf{u}) \in V$ est orthogonal à $P_{V^\perp}(\mathbf{v}) \in V^\perp$).
Donc, nous avons $\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), \mathbf{v} \rangle$.
Par unicité de l'adjoint, cela signifie que $P_V^* = P_V$. L'opérateur de projection orthogonale est donc auto-adjoint.

### 2. Robustesse Sémantique et Dualité :

#### 2.a) Linéarité de l'opérateur $P_V^*$
L'opérateur $P_V^*: E^* \to E^*$ est défini par $(P_V^*(f))(\mathbf{v}) = f(P_V(\mathbf{v}))$ pour tout $f \in E^*$ et $\mathbf{v} \in E$.
Pour démontrer la linéarité, nous devons montrer que pour tout $f_1, f_2 \in E^*$ et tout scalaire $\lambda \in \mathbb{R}$, $P_V^*(f_1 + f_2) = P_V^*(f_1) + P_V^*(f_2)$ et $P_V^*(\lambda f_1) = \lambda P_V^*(f_1)$.

Considérons la somme de formes linéaires $f_1 + f_2$:
Pour tout $\mathbf{v} \in E$:
$(P_V^*(f_1 + f_2))(\mathbf{v}) = (f_1 + f_2)(P_V(\mathbf{v}))$.
Par définition de la somme de formes linéaires :
$(f_1 + f_2)(P_V(\mathbf{v})) = f_1(P_V(\mathbf{v})) + f_2(P_V(\mathbf{v}))$.
Par définition de $P_V^*$:
$f_1(P_V(\mathbf{v})) + f_2(P_V(\mathbf{v})) = (P_V^*(f_1))(\mathbf{v}) + (P_V^*(f_2))(\mathbf{v})$.
Par définition de la somme de formes linéaires :
$(P_V^*(f_1))(\mathbf{v}) + (P_V^*(f_2))(\mathbf{v}) = (P_V^*(f_1) + P_V^*(f_2))(\mathbf{v})$.
Ainsi, $P_V^*(f_1 + f_2) = P_V^*(f_1) + P_V^*(f_2)$.

Considérons le produit par un scalaire $\lambda \in \mathbb{R}$:
Pour tout $\mathbf{v} \in E$:
$(P_V^*(\lambda f_1))(\mathbf{v}) = (\lambda f_1)(P_V(\mathbf{v}))$.
Par définition du produit scalaire-forme linéaire :
$(\lambda f_1)(P_V(\mathbf{v})) = \lambda (f_1(P_V(\mathbf{v})))$.
Par définition de $P_V^*$:
$\lambda (f_1(P_V(\mathbf{v}))) = \lambda (P_V^*(f_1))(\mathbf{v})$.
Par définition du produit scalaire-forme linéaire :
$\lambda (P_V^*(f_1))(\mathbf{v}) = (\lambda P_V^*(f_1))(\mathbf{v})$.
Ainsi, $P_V^*(\lambda f_1) = \lambda P_V^*(f_1)$.
Donc, $P_V^*$ est un opérateur linéaire.

#### 2.b) Relation $\Phi(P_V(\mathbf{u})) = P_V^*(\Phi(\mathbf{u}))$
Nous devons montrer que pour tout $\mathbf{u} \in E$, les deux formes linéaires $\Phi(P_V(\mathbf{u}))$ et $P_V^*(\Phi(\mathbf{u}))$ sont égales. Deux formes linéaires sont égales si elles prennent les mêmes valeurs sur tous les vecteurs de l'espace.
Soit $\mathbf{v} \in E$.

Calculons la valeur de $\Phi(P_V(\mathbf{u}))$ sur $\mathbf{v}$:
Par définition de $\Phi$, $\Phi(P_V(\mathbf{u}))$ est la forme linéaire $f_{P_V(\mathbf{u})}$.
Donc, $(\Phi(P_V(\mathbf{u})))(\mathbf{v}) = f_{P_V(\mathbf{u})}(\mathbf{v}) = \langle P_V(\mathbf{u}), \mathbf{v} \rangle$.

Calculons la valeur de $P_V^*(\Phi(\mathbf{u}))$ sur $\mathbf{v}$:
Par définition de $\Phi$, $\Phi(\mathbf{u})$ est la forme linéaire $f_{\mathbf{u}}$.
Donc, $(P_V^*(\Phi(\mathbf{u})))(\mathbf{v}) = (P_V^*(f_{\mathbf{u}}))(\mathbf{v})$.
Par définition de $P_V^*$:
$(P_V^*(f_{\mathbf{u}}))(\mathbf{v}) = f_{\mathbf{u}}(P_V(\mathbf{v}))$.
Par définition de $f_{\mathbf{u}}$:
$f_{\mathbf{u}}(P_V(\mathbf{v})) = \langle \mathbf{u}, P_V(\mathbf{v}) \rangle$.

En utilisant le résultat de la question 1.b) : $\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle$.
Et aussi, $\langle P_V(\mathbf{u}), \mathbf{v} \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) + P_{V^\perp}(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle + \langle P_V(\mathbf{u}), P_{V^\perp}(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle$, car $P_V(\mathbf{u}) \in V$ est orthogonal à $P_{V^\perp}(\mathbf{v}) \in V^\perp$.
Donc, nous avons $\langle P_V(\mathbf{u}), \mathbf{v} \rangle = \langle \mathbf{u}, P_V(\mathbf{v}) \rangle$.

Finalement, $(\Phi(P_V(\mathbf{u})))(\mathbf{v}) = \langle P_V(\mathbf{u}), \mathbf{v} \rangle$ et $(P_V^*(\Phi(\mathbf{u})))(\mathbf{v}) = \langle \mathbf{u}, P_V(\mathbf{v}) \rangle$.
Comme $\langle P_V(\mathbf{u}), \mathbf{v} \rangle = \langle \mathbf{u}, P_V(\mathbf{v}) \rangle$ (démontré en 1.b, puisque $P_V$ est auto-adjoint), nous avons bien:
$$ (\Phi(P_V(\mathbf{u})))(\mathbf{v}) = (P_V^*(\Phi(\mathbf{u})))(\mathbf{v}) $$
pour tout $\mathbf{v} \in E$. Par conséquent, $\Phi(P_V(\mathbf{u})) = P_V^*(\Phi(\mathbf{u}))$.

**Interprétation :** Cette relation signifie que l'isomorphisme de Riesz $\Phi$ "commute" avec l'opérateur de projection orthogonale $P_V$ et son adjoint dual $P_V^*$. En d'autres termes, appliquer la projection $P_V$ à un vecteur $\mathbf{u}$ dans l'espace $E$, puis le transformer en sa forme linéaire duale via $\Phi$, est équivalent à transformer d'abord $\mathbf{u}$ en sa forme linéaire duale $f_{\mathbf{u}}$ via $\Phi$, puis appliquer l'opérateur de projection dual $P_V^*$ à cette forme linéaire. Cela garantit que les opérations de projection sont cohérentes entre l'espace vectoriel et son dual, préservant la structure euclidienne via l'isomorphisme.

#### 2.c) Expression de $\langle \mathbf{q}_V, \mathbf{d}_V \rangle$
Nous avons $\mathbf{q}_V = P_V(\mathbf{q})$ et $\mathbf{d}_V = P_V(\mathbf{d})$.
Donc, $\langle \mathbf{q}_V, \mathbf{d}_V \rangle = \langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle$.

En utilisant la relation établie en 1.b) $(\langle \mathbf{u}, P_V(\mathbf{v}) \rangle = \langle P_V(\mathbf{u}), P_V(\mathbf{v}) \rangle)$, nous pouvons écrire :
$\langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle = \langle P_V(\mathbf{q}), \mathbf{d} \rangle$.
Par définition de la forme linéaire $f_{P_V(\mathbf{q})}$ :
$$ \langle P_V(\mathbf{q}), \mathbf{d} \rangle = f_{P_V(\mathbf{q})}(\mathbf{d}) $$
Ainsi, $\langle \mathbf{q}_V, \mathbf{d}_V \rangle = f_{P_V(\mathbf{q})}(\mathbf{d})$.

Maintenant, utilisons la relation de la question 2.b) : $\Phi(P_V(\mathbf{q})) = P_V^*(\Phi(\mathbf{q}))$.
Comme $f_{P_V(\mathbf{q})} = \Phi(P_V(\mathbf{q}))$, nous avons $f_{P_V(\mathbf{q})} = P_V^*(\Phi(\mathbf{q}))$.
En substituant cette expression dans la précédente :
$$ \langle \mathbf{q}_V, \mathbf{d}_V \rangle = (P_V^*(\Phi(\mathbf{q})))(\mathbf{d}) $$
Cette dernière expression relie le produit scalaire robuste au projecteur dual agissant sur la forme duale de la requête.

#### 2.d) Propriétés de la forme linéaire $f_{\mathbf{q},V}$
La forme linéaire est définie par $f_{\mathbf{q},V}(\mathbf{d}) = \langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle$.

**Appartenance à l'image de $P_V^*$ :**
D'après la question 2.c), nous avons montré que $\langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle = (P_V^*(\Phi(\mathbf{q})))(\mathbf{d})$.
Cela signifie que $f_{\mathbf{q},V}(\mathbf{d}) = (P_V^*(\Phi(\mathbf{q})))(\mathbf{d})$ pour tout $\mathbf{d} \in E$.
Par conséquent, $f_{\mathbf{q},V} = P_V^*(\Phi(\mathbf{q}))$.
Puisque $\Phi(\mathbf{q}) \in E^*$, $f_{\mathbf{q},V}$ est l'image d'une forme linéaire de $E^*$ par l'opérateur $P_V^*$.
Ainsi, $f_{\mathbf{q},V} \in \text{Im}(P_V^*)$.

**Caractérisation du noyau de $f_{\mathbf{q},V}$ :**
Le noyau de $f_{\mathbf{q},V}$, noté $\text{Ker}(f_{\mathbf{q},V})$, est l'ensemble des vecteurs $\mathbf{d} \in E$ tels que $f_{\mathbf{q},V}(\mathbf{d}) = 0$.
Donc, $\text{Ker}(f_{\mathbf{q},V}) = \{ \mathbf{d} \in E \mid \langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle = 0 \}$.

Deux cas se présentent :
1.  **Si $P_V(\mathbf{q}) = \mathbf{0}_E$ :** Cela signifie que $\mathbf{q}$ est entièrement contenu dans $V^\perp$ (le sous-espace de bruit).
    Dans ce cas, $\langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle = \langle \mathbf{0}_E, P_V(\mathbf{d}) \rangle = 0$ pour tout $\mathbf{d} \in E$.
    Par conséquent, $f_{\mathbf{q},V}(\mathbf{d}) = 0$ pour tout $\mathbf{d} \in E$.
    Le noyau est alors l'espace entier : $\text{Ker}(f_{\mathbf{q},V}) = E$.

2.  **Si $P_V(\mathbf{q}) \ne \mathbf{0}_E$ :**
    La condition $\langle P_V(\mathbf{q}), P_V(\mathbf{d}) \rangle = 0$ signifie que le vecteur projeté de $\mathbf{d}$, à savoir $P_V(\mathbf{d})$, est orthogonal à $P_V(\mathbf{q})$ *dans le sous-espace $V$*.
    Soit $\mathbf{v}_q = P_V(\mathbf{q})$. Alors $\text{Ker}(f_{\mathbf{q},V}) = \{ \mathbf{d} \in E \mid \langle \mathbf{v}_q, P_V(\mathbf{d}) \rangle = 0 \}$.
    Nous savons que $P_V(\mathbf{d}) \in V$. Soit $V_q^\perp$ le complément orthogonal de $\text{span}\{\mathbf{v}_q\}$ *dans $V$*. Autrement dit, $V_q^\perp = \{ \mathbf{v} \in V \mid \langle \mathbf{v}_q, \mathbf{v} \rangle = 0 \}$.
    Alors $\langle \mathbf{v}_q, P_V(\mathbf{d}) \rangle = 0$ si et seulement si $P_V(\mathbf{d}) \in V_q^\perp$.
    Tout vecteur $\mathbf{d} \in E$ peut s'écrire $\mathbf{d} = P_V(\mathbf{d}) + P_{V^\perp}(\mathbf{d})$.
    Donc, $\mathbf{d} \in \text{Ker}(f_{\mathbf{q},V})$ si et seulement si $P_V(\mathbf{d}) \in V_q^\perp$.
    Le noyau est donc l'ensemble des vecteurs dont la projection sur $V$ est orthogonale à $P_V(\mathbf{q})$.
    Formellement, $\text{Ker}(f_{\mathbf{q},V}) = \{ \mathbf{v} + \mathbf{w} \mid \mathbf{v} \in V_q^\perp, \mathbf{w} \in V^\perp \}$.
    Ceci est la somme directe des sous-espaces $V_q^\perp$ et $V^\perp$:
    $\text{Ker}(f_{\mathbf{q},V}) = V_q^\perp \oplus V^\perp$.
    La dimension de $V_q^\perp$ (dans $V$) est $\text{dim}(V) - 1 = k-1$ (puisque $\mathbf{v}_q \ne \mathbf{0}_E$).
    La dimension de $V^\perp$ est $n - k$.
    Donc, la dimension du noyau est $(k-1) + (n-k) = n-1$.

### 3. Interprétation Géométrique et Application à la Recherche Sémantique :

#### 3.a) Maximisation de $\text{sim}_V(\mathbf{q}, \mathbf{d})$
Nous avons $\text{sim}_V(\mathbf{q}, \mathbf{d}) = \frac{\langle \mathbf{q}_V, \mathbf{d}_V \rangle}{\| \mathbf{q}_V \| \| \mathbf{d}_V \|}$.
Soit $\mathbf{q}_{\text{unit}} = \frac{\mathbf{q}_V}{\| \mathbf{q}_V \|}$. C'est le vecteur de requête robuste normalisé. Par hypothèse, $\mathbf{q}_V \ne \mathbf{0}_E$.
Alors, $\text{sim}_V(\mathbf{q}, \mathbf{d}) = \frac{\langle \| \mathbf{q}_V \| \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle}{\| \mathbf{q}_V \| \| \mathbf{d}_V \|} = \frac{\| \mathbf{q}_V \| \langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle}{\| \mathbf{q}_V \| \| \mathbf{d}_V \|} = \frac{\langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle}{\| \mathbf{d}_V \|}$.

L'objectif est de maximiser $\text{sim}_V(\mathbf{q}, \mathbf{d})$ pour un ensemble de documents. Si nous considérons des documents $\mathbf{d}$ pour lesquels la norme de leur projection robuste $\| \mathbf{d}_V \|$ est constante (et non nulle), alors maximiser $\frac{\langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle}{\| \mathbf{d}_V \|}$ est équivalent à maximiser directement $\langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle$, puisque $\| \mathbf{d}_V \|$ est une constante positive.
$$ \max_{\mathbf{d}} \left( \frac{\langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle}{\| \mathbf{d}_V \|} \right) \quad \text{est équivalent à} \quad \max_{\mathbf{d}} \left( \langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle \right) \text{ si } \| \mathbf{d}_V \| \text{ est constant.} $$
Cette approche est standard dans la recherche par similarité car elle se base sur le principe que pour une requête donnée (représentée par $\mathbf{q}_{\text{unit}}$), les documents les plus pertinents sont ceux dont la composante significative ($\mathbf{d}_V$) est la plus alignée avec la requête. Le produit scalaire $\langle \mathbf{q}_{\text{unit}}, \mathbf{d}_V \rangle$ mesure cette "projection" ou "contribution" de $\mathbf{d}_V$ le long de la direction de $\mathbf{q}_{\text{unit}}$. Un produit scalaire plus élevé signifie un alignement plus fort et donc une pertinence sémantique plus grande dans le sous-espace des caractéristiques pertinentes $V$.

#### 3.b) $P_V(\mathbf{x})$ avec une base orthonormée
Soit $(\mathbf{e}_1, \dots, \mathbf{e}_k)$ une base orthonormée de $V$.
Pour tout vecteur $\mathbf{x} \in E$, sa projection orthogonale sur $V$, $P_V(\mathbf{x})$, est le vecteur de $V$ qui minimise la distance à $\mathbf{x}$. $P_V(\mathbf{x})$ est donné par la formule classique de projection:
$$ P_V(\mathbf{x}) = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{e}_i \rangle \mathbf{e}_i $$
Cette formule exprime $P_V(\mathbf{x})$ comme une combinaison linéaire des vecteurs de base de $V$, où les coefficients sont les projections de $\mathbf{x}$ sur chacun de ces vecteurs de base.

#### 3.c) Étude de cas concret
Soit $E = \mathbb{R}^3$ avec le produit scalaire euclidien canonique.
Le sous-espace $V$ est le plan $xy$, donc $V = \text{span}\{(1,0,0), (0,1,0)\}$.
Le complément orthogonal $V^\perp$ est l'axe $z$, donc $V^\perp = \text{span}\{(0,0,1)\}$.
L'opérateur de projection orthogonale $P_V: \mathbb{R}^3 \to V$ est défini par $P_V(x,y,z) = (x,y,0)$.

Vecteurs donnés :
Requête : $\mathbf{q} = (1, 1, 1)$.
Documents : $\mathbf{d}_1 = (1, 0, 0)$, $\mathbf{d}_2 = (0, 0, 1)$.

**Calcul des similarités cosinus standard :**
Normes :
$\| \mathbf{q} \| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$.
$\| \mathbf{d}_1 \| = \sqrt{1^2 + 0^2 + 0^2} = 1$.
$\| \mathbf{d}_2 \| = \sqrt{0^2 + 0^2 + 1^2} = 1$.

Produits scalaires :
$\langle \mathbf{q}, \mathbf{d}_1 \rangle = (1)(1) + (1)(0) + (1)(0) = 1$.
$\langle \mathbf{q}, \mathbf{d}_2 \rangle = (1)(0) + (1)(0) + (1)(1) = 1$.

Similarités cosinus standard :
$\text{sim}(\mathbf{q}, \mathbf{d}_1) = \frac{1}{\sqrt{3} \cdot 1} = \frac{1}{\sqrt{3}} \approx 0.577$.
$\text{sim}(\mathbf{q}, \mathbf{d}_2) = \frac{1}{\sqrt{3} \cdot 1} = \frac{1}{\sqrt{3}} \approx 0.577$.

**Calcul des similarités cosinus robustes :**
Projections robustes :
$\mathbf{q}_V = P_V(\mathbf{q}) = P_V(1,1,1) = (1,1,0)$.
$\mathbf{d}_{1,V} = P_V(\mathbf{d}_1) = P_V(1,0,0) = (1,0,0)$.
$\mathbf{d}_{2,V} = P_V(\mathbf{d}_2) = P_V(0,0,1) = (0,0,0)$.

Normes robustes :
$\| \mathbf{q}_V \| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$.
$\| \mathbf{d}_{1,V} \| = \sqrt{1^2 + 0^2 + 0^2} = 1$.
$\| \mathbf{d}_{2,V} \| = \sqrt{0^2 + 0^2 + 0^2} = 0$.

Produits scalaires robustes :
$\langle \mathbf{q}_V, \mathbf{d}_{1,V} \rangle = (1)(1) + (1)(0) + (0)(0) = 1$.
$\langle \mathbf{q}_V, \mathbf{d}_{2,V} \rangle = \langle (1,1,0), (0,0,0) \rangle = 0$.

Similarités cosinus robustes :
$\text{sim}_V(\mathbf{q}, \mathbf{d}_1) = \frac{1}{\sqrt{2} \cdot 1} = \frac{1}{\sqrt{2}} \approx 0.707$.
$\text{sim}_V(\mathbf{q}, \mathbf{d}_2)$ est **indéfinie** car $\| \mathbf{d}_{2,V} \| = 0$.

**Discussion des implications pour la recherche sémantique :**

1.  **Limites de la similarité standard :** La similarité cosinus standard attribue la même pertinence à $\mathbf{d}_1$ et $\mathbf{d}_2$ (valeur de $1/\sqrt{3}$). Cependant, la signification de ces documents est très différente par rapport au plan $xy$ (notre sous-espace pertinent $V$).
    *   Le document $\mathbf{d}_1=(1,0,0)$ est entièrement situé dans le sous-espace $V$ (le plan $xy$). Il représente une caractéristique sémantique pertinente.
    *   Le document $\mathbf{d}_2=(0,0,1)$ est entièrement situé dans le sous-espace $V^\perp$ (l'axe $z$). Il représente une caractéristique sémantique purement "bruit" ou non pertinente selon notre définition de $V$.
    La similarité standard échoue à distinguer la pertinence intrinsèque de ces deux documents vis-à-vis du concept de "caractéristiques sémantiques pertinentes". Elle est sensible à toutes les dimensions de l'espace de plongement, y compris celles qui peuvent être du bruit.

2.  **Avantages de la similarité robuste :**
    *   **Filtrage du bruit :** La similarité robuste $\text{sim}_V(\mathbf{q}, \mathbf{d})$ filtre efficacement les informations non pertinentes. Pour $\mathbf{d}_2$, puisque sa projection $P_V(\mathbf{d}_2)$ est le vecteur nul, la similarité robuste est indéfinie (ou peut être conventionnellement définie comme 0), indiquant que $\mathbf{d}_2$ n'a aucune composante sémantiquement pertinente pour la requête dans le sous-espace $V$. Cela reflète correctement le fait que $\mathbf{d}_2$ est "hors sujet" par rapport à ce que $V$ représente.
    *   **Accentuation des caractéristiques pertinentes :** Pour $\mathbf{d}_1$, la similarité robuste est plus élevée ($1/\sqrt{2} \approx 0.707$) que la similarité standard. Cela est dû au fait que la composante "bruit" de la requête $\mathbf{q}$ (sa composante sur l'axe $z$) a été ignorée, ce qui a réduit l'angle entre les vecteurs effectifs dans $V$. La similarité robuste se concentre uniquement sur l'alignement des parties pertinentes de la requête et du document, offrant une mesure de pertinence plus précise et plus élevée lorsque le document est intrinsèquement pertinent dans $V$.
    *   **Meilleur classement :** Dans un moteur de recherche, cette approche permettrait de classer les documents en fonction de leur contenu sémantique *spécifique et pertinent* pour la requête, en ignorant les dimensions parasites. Les documents sans composante pertinente dans $V$ seraient écartés, tandis que ceux ayant des projections significatives seraient mieux classés.

En conclusion, cet exercice démontre comment l'intégration de la dualité et de la géométrie des espaces de plongement, en particulier l'utilisation des projections orthogonales, permet de construire des mesures de similarité cosinus plus sophistiquées et robustes. Ces mesures sont essentielles pour la conception de moteurs de recherche sémantiques capables de faire abstraction du "bruit" et de se concentrer sur les caractéristiques sémantiques les plus pertinentes pour une requête donnée.

---