# Exercice 04 (2 $\star$) : Analyse de Similarité Sémantique et Transformations Linéaires dans un Espace de Plongement

## Énoncé
Soit $E = \mathbb{R}^3$ l'espace vectoriel euclidien muni du produit scalaire canonique $\langle x, y \rangle = x_1y_1 + x_2y_2 + x_3y_3$ pour $x=(x_1, x_2, x_3)$ et $y=(y_1, y_2, y_3)$. La norme associée est $\|x\| = \sqrt{\langle x, x \rangle}$.
Dans le contexte de l'apprentissage automatique, des vecteurs tels que $u$ et $v$ peuvent représenter des plongements (embeddings) sémantiques de mots ou de concepts.

On considère les vecteurs suivants dans $E$:
$u = (1, 1, 0)$
$v = (1, 0, 1)$

1.  **Calcul de la Similarité Cosinus Initiale:**
    Calculez la similarité cosinus entre les vecteurs $u$ et $v$. Rappelez la formule utilisée.

2.  **Effet d'une Transformation Linéaire (Projection):**
    Considérons une transformation linéaire $L: E \to E$ représentée par la matrice $M$ dans la base canonique de $\mathbb{R}^3$:
    $$M = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
    a. Déterminez les vecteurs transformés $u' = L(u)$ et $v' = L(v)$.
    b. Calculez la similarité cosinus entre $u'$ et $v'$.
    c. Comparez la similarité cosinus obtenue en 2.b avec celle obtenue en 1. Interprétez géométriquement l'effet de $L$ sur les vecteurs et sur leur similarité.

3.  **Exploration des Formes Linéaires (Dualité):**
    L'espace dual $E^*$ de $E$ est l'ensemble des formes linéaires de $E$ dans $\mathbb{R}$. Pour tout vecteur $w \in E$, la fonction $f_w: E \to \mathbb{R}$ définie par $f_w(x) = \langle x, w \rangle$ est une forme linéaire.
    a. Soit $w_1 = (1, 1, 0)$. Calculez $f_{w_1}(u)$ et $f_{w_1}(v)$.
    b. Soit $w_2 = (0, 0, 1)$. Calculez $f_{w_2}(u)$ et $f_{w_2}(v)$.
    c. Interprétez les valeurs $f_{w_1}(u)$, $f_{w_1}(v)$, $f_{w_2}(u)$, $f_{w_2}(v)$ en termes de "caractéristiques sémantiques" si les vecteurs $u, v, w_1, w_2$ représentent des concepts dans un espace de plongement.


### Formulation Rigoureuse de l'Espace Dual
Dans l'étude des requêtes $q$, chaque vecteur peut être identifié à une forme linéaire $\varphi_q \in E^*$ telle que $\varphi_q(x) = \langle q, x \rangle$. La recherche sémantique s'assimile à la maximisation de $\varphi_q$ sur la sphère unité. Le théorème de représentation de Riesz assure l'isomorphisme isométrique entre $E$ et $E^*$, garantissant l'existence et l'unicité de ce prolongement.

## Correction Détaillée
### Analyse et Stratégie
L'exercice vise à évaluer la compréhension des concepts fondamentaux de la géométrie des espaces vectoriels euclidiens, en particulier la similarité cosinus, l'effet des transformations linéaires (projections) sur cette similarité, et l'introduction des formes linéaires via le produit scalaire (dualité).

Pour la première partie, nous appliquerons directement la définition de la similarité cosinus, qui implique le calcul du produit scalaire et des normes des vecteurs.
Pour la deuxième partie, nous effectuerons une multiplication matricielle pour obtenir les vecteurs transformés, puis nous recalculerons la similarité cosinus. L'interprétation géométrique nécessitera de reconnaître la nature de la transformation $L$.
Pour la troisième partie, nous utiliserons la définition de la forme linéaire $f_w(x) = \langle x, w \rangle$ pour calculer les valeurs demandées. L'interprétation finale reliera ces valeurs au concept de "caractéristiques sémantiques" dans un espace de plongement. Toutes les étapes de calcul seront explicitées sans aucune omission.

### Résolution Pas-à-Pas

1.  **Calcul de la Similarité Cosinus Initiale:**
    La similarité cosinus entre deux vecteurs non nuls $x$ et $y$ dans un espace euclidien est définie par la formule:
    $$ \text{sim}(x, y) = \frac{\langle x, y \rangle}{\|x\| \|y\|} $$
    où $\langle x, y \rangle$ est le produit scalaire et $\|x\|$ est la norme euclidienne de $x$.

    Nous avons les vecteurs $u = (1, 1, 0)$ et $v = (1, 0, 1)$.
    Calculons d'abord le produit scalaire $\langle u, v \rangle$:
    $$ \langle u, v \rangle = (1)(1) + (1)(0) + (0)(1) = 1 + 0 + 0 = 1 $$

    Ensuite, calculons les normes $\|u\|$ et $\|v\|$:
    $$ \|u\| = \sqrt{\langle u, u \rangle} = \sqrt{(1)^2 + (1)^2 + (0)^2} = \sqrt{1 + 1 + 0} = \sqrt{2} $$
    $$ \|v\| = \sqrt{\langle v, v \rangle} = \sqrt{(1)^2 + (0)^2 + (1)^2} = \sqrt{1 + 0 + 1} = \sqrt{2} $$

    Maintenant, nous pouvons calculer la similarité cosinus entre $u$ et $v$:
    $$ \text{sim}(u, v) = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2} $$
    La similarité cosinus initiale entre $u$ et $v$ est $\frac{1}{2}$.

2.  **Effet d'une Transformation Linéaire (Projection):**
    La transformation linéaire $L$ est représentée par la matrice $M = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.

    a. **Détermination des vecteurs transformés $u'$ et $v'$:**
    Pour un vecteur $x = (x_1, x_2, x_3)$, $L(x) = M x$.
    Pour $u = (1, 1, 0)$:
    $$ u' = L(u) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} (1)(1) + (0)(1) + (0)(0) \\ (0)(1) + (1)(1) + (0)(0) \\ (0)(1) + (0)(1) + (0)(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} $$
    Donc, $u' = (1, 1, 0)$.

    Pour $v = (1, 0, 1)$:
    $$ v' = L(v) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} (1)(1) + (0)(0) + (0)(1) \\ (0)(1) + (1)(0) + (0)(1) \\ (0)(1) + (0)(0) + (0)(1) \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} $$
    Donc, $v' = (1, 0, 0)$.

    b. **Calcul de la similarité cosinus entre $u'$ et $v'$:**
    Nous avons $u' = (1, 1, 0)$ et $v' = (1, 0, 0)$.
    Calculons le produit scalaire $\langle u', v' \rangle$:
    $$ \langle u', v' \rangle = (1)(1) + (1)(0) + (0)(0) = 1 + 0 + 0 = 1 $$

    Calculons les normes $\|u'\|$ et $\|v'\|$:
    $$ \|u'\| = \sqrt{(1)^2 + (1)^2 + (0)^2} = \sqrt{1 + 1 + 0} = \sqrt{2} $$
    $$ \|v'\| = \sqrt{(1)^2 + (0)^2 + (0)^2} = \sqrt{1 + 0 + 0} = \sqrt{1} = 1 $$

    Calculons la similarité cosinus entre $u'$ et $v'$:
    $$ \text{sim}(u', v') = \frac{\langle u', v' \rangle}{\|u'\| \|v'\|} = \frac{1}{\sqrt{2} \cdot 1} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} $$
    La similarité cosinus entre $u'$ et $v'$ est $\frac{\sqrt{2}}{2}$.

    c. **Comparaison et interprétation:**
    La similarité cosinus initiale était $\text{sim}(u, v) = \frac{1}{2}$.
    La similarité cosinus après transformation est $\text{sim}(u', v') = \frac{\sqrt{2}}{2}$.
    Puisque $\frac{\sqrt{2}}{2} \approx 0.707$ et $\frac{1}{2} = 0.5$, la similarité cosinus a augmenté après la transformation $L$.

    Géométriquement, la matrice $M$ correspond à une projection orthogonale sur le plan $xy$ (le plan d'équation $z=0$). En effet, elle conserve les composantes $x$ et $y$ et annule la composante $z$.
    Le vecteur $u = (1, 1, 0)$ est déjà dans le plan $xy$, donc $L(u) = u$.
    Le vecteur $v = (1, 0, 1)$ a une composante $z$ non nulle. Sa projection $L(v) = (1, 0, 0)$ est le vecteur $v$ "aplati" sur le plan $xy$.
    L'angle entre $u$ et $v$ était $\arccos(1/2) = 60^\circ$.
    L'angle entre $u'$ et $v'$ est $\arccos(\sqrt{2}/2) = 45^\circ$.
    La projection a rapproché les vecteurs en termes d'angle, car la composante $z$ de $v$ qui l'éloignait de $u$ a été supprimée. Dans le contexte des plongements sémantiques, cela signifie que si la dimension $z$ représentait une caractéristique non pertinente ou du "bruit" pour la similarité entre $u$ et $v$, sa suppression a rendu les concepts $u$ et $v$ plus similaires dans l'espace de caractéristiques réduit.

3.  **Exploration des Formes Linéaires (Dualité):**
    Pour tout vecteur $w \in E$, la forme linéaire $f_w: E \to \mathbb{R}$ est définie par $f_w(x) = \langle x, w \rangle$.

    a. **Calcul de $f_{w_1}(u)$ et $f_{w_1}(v)$ pour $w_1 = (1, 1, 0)$:**
    $$ f_{w_1}(u) = \langle u, w_1 \rangle = \langle (1, 1, 0), (1, 1, 0) \rangle = (1)(1) + (1)(1) + (0)(0) = 1 + 1 + 0 = 2 $$
    $$ f_{w_1}(v) = \langle v, w_1 \rangle = \langle (1, 0, 1), (1, 1, 0) \rangle = (1)(1) + (0)(1) + (1)(0) = 1 + 0 + 0 = 1 $$

    b. **Calcul de $f_{w_2}(u)$ et $f_{w_2}(v)$ pour $w_2 = (0, 0, 1)$:**
    $$ f_{w_2}(u) = \langle u, w_2 \rangle = \langle (1, 1, 0), (0, 0, 1) \rangle = (1)(0) + (1)(0) + (0)(1) = 0 + 0 + 0 = 0 $$
    $$ f_{w_2}(v) = \langle v, w_2 \rangle = \langle (1, 0, 1), (0, 0, 1) \rangle = (1)(0) + (0)(0) + (1)(1) = 0 + 0 + 1 = 1 $$

    c. **Interprétation en termes de "caractéristiques sémantiques":**
    Dans un espace de plongement sémantique, chaque dimension ou direction vectorielle peut correspondre à une caractéristique sémantique latente. Un vecteur $w$ peut être vu comme représentant une "caractéristique" ou un "concept" spécifique. La valeur $f_w(x) = \langle x, w \rangle$ mesure la projection de $x$ sur $w$, ou plus généralement, l'alignement de $x$ avec $w$. Une valeur élevée (positive) indique que $x$ possède fortement la caractéristique représentée par $w$, tandis qu'une valeur faible ou nulle indique une faible présence ou une orthogonalité.

    *   $f_{w_1}(u) = 2$: Le vecteur $u$ est fortement aligné avec la caractéristique $w_1$. En fait, $u$ est colinéaire à $w_1$, ce qui signifie que $u$ incarne pleinement la caractéristique $w_1$.
    *   $f_{w_1}(v) = 1$: Le vecteur $v$ est également aligné avec la caractéristique $w_1$, mais à un degré moindre que $u$.
    *   $f_{w_2}(u) = 0$: Le vecteur $u$ est orthogonal à la caractéristique $w_2$. Cela signifie que $u$ ne possède pas du tout la caractéristique $w_2$ (ou que cette caractéristique est indépendante de $u$).
    *   $f_{w_2}(v) = 1$: Le vecteur $v$ est aligné avec la caractéristique $w_2$. Il possède cette caractéristique à un certain degré.

    Si, par exemple, $u$ représente le mot "chien", $v$ le mot "chat", $w_1$ la caractéristique "animalité" et $w_2$ la caractéristique "indépendance", alors:
    *   "chien" ($u$) a un score élevé pour "animalité" ($w_1$).
    *   "chat" ($v$) a un score pour "animalité" ($w_1$) mais légèrement inférieur à "chien".
    *   "chien" ($u$) a un score nul pour "indépendance" ($w_2$), suggérant qu'il n'est pas indépendant (ou que cette caractéristique n'est pas pertinente pour lui).
    *   "chat" ($v$) a un score pour "indépendance" ($w_2$), suggérant qu'il possède cette caractéristique.

    Ces valeurs quantifient la pertinence ou la force d'une caractéristique sémantique donnée pour un concept représenté par un vecteur de plongement.

### Conclusion
Cet exercice a permis d'explorer la notion de similarité cosinus, un outil fondamental dans l'analyse des espaces de plongement sémantiques. Nous avons observé comment une transformation linéaire, en l'occurrence une projection, peut modifier la similarité entre des vecteurs en altérant leur géométrie dans l'espace. La similarité entre $u$ et $v$ est passée de $1/2$ à $\sqrt{2}/2$ après projection sur le plan $z=0$, illustrant que la pertinence des dimensions peut influencer la perception de la similarité. Enfin, l'introduction des formes linéaires a permis de quantifier la présence de "caractéristiques sémantiques" spécifiques (représentées par les vecteurs $w_1$ et $w_2$) au sein des concepts $u$ et $v$, offrant une perspective sur la dualité et l'interprétabilité des dimensions dans ces espaces.
