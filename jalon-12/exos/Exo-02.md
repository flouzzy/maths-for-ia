# Exercice 02 (1 $\star$) : Exploration de la Similarité Cosinus et des Formes Duales en $\mathbb{R}^2$

## Énoncé
Soit $E = \mathbb{R}^2$ l'espace vectoriel réel muni du produit scalaire euclidien standard, défini pour tout $x = (x_1, x_2) \in E$ et $y = (y_1, y_2) \in E$ par $\langle x, y \rangle = x_1 y_1 + x_2 y_2$.
On considère les deux vecteurs $u = (3, 4)$ et $v = (5, 12)$ appartenant à $E$.

1.  Calculer la norme euclidienne de $u$ et de $v$.
2.  Calculer le produit scalaire $\langle u, v \rangle$.
3.  En déduire la similarité cosinus entre $u$ et $v$.
4.  Pour chaque vecteur $x \in E$, on associe une forme linéaire $\phi_x \in E^*$ (le dual de $E$) définie par $\phi_x(y) = \langle x, y \rangle$ pour tout $y \in E$.
    a. Déterminer les expressions explicites des formes linéaires $\phi_u$ et $\phi_v$.
    b. Vérifier que $\langle u, v \rangle = \phi_u(v)$ et que $\langle u, v \rangle = \phi_v(u)$.
    c. Exprimer la similarité cosinus entre $u$ et $v$ en utilisant les formes linéaires $\phi_u$, $\phi_v$ et les normes de $u$ et $v$.

## Correction Détaillée
### Analyse et Stratégie
L'objectif de cet exercice est de renforcer la compréhension des concepts fondamentaux liés à la géométrie des espaces vectoriels euclidiens, notamment la norme, le produit scalaire, la similarité cosinus, et la dualité. Étant donné la difficulté de 1 étoile, la résolution s'appuiera sur l'application directe des définitions et des propriétés de base.

La démarche sera la suivante :
Pour les questions 1, 2 et 3, nous appliquerons rigoureusement les définitions de la norme euclidienne, du produit scalaire euclidien standard et de la similarité cosinus.
Pour la question 4.a, nous utiliserons la définition de la forme linéaire $\phi_x$ associée à un vecteur $x$ et les coordonnées des vecteurs $u$ et $v$ pour obtenir leurs expressions explicites.
Pour la question 4.b, nous substituerons les vecteurs et les formes linéaires dans les expressions $\phi_u(v)$ et $\phi_v(u)$ et vérifierons que les résultats sont égaux au produit scalaire $\langle u, v \rangle$ calculé précédemment.
Pour la question 4.c, nous réécrirons la formule de la similarité cosinus en remplaçant le produit scalaire par son expression en termes de formes linéaires, en utilisant les résultats de la question 4.b.

Les hypothèses de régularité (continuité, dérivabilité, intégrabilité) ne sont pas pertinentes dans le cadre de cet exercice. Nous travaillons dans un espace vectoriel de dimension finie ($\mathbb{R}^2$) avec des vecteurs fixes et des opérations algébriques bien définies. Les formes linéaires sont par définition continues et différentiables sur un espace vectoriel normé de dimension finie.

### Résolution Pas-à-Pas

1.  **Calcul des normes euclidiennes de $u$ et de $v$ :**
    La norme euclidienne d'un vecteur $x = (x_1, x_2) \in \mathbb{R}^2$ est définie par $\|x\| = \sqrt{\langle x, x \rangle} = \sqrt{x_1^2 + x_2^2}$.

    Pour le vecteur $u = (3, 4)$ :
    $$ \|u\| = \sqrt{3^2 + 4^2} $$
    $$ \|u\| = \sqrt{9 + 16} $$
    $$ \|u\| = \sqrt{25} $$
    $$ \|u\| = 5 $$

    Pour le vecteur $v = (5, 12)$ :
    $$ \|v\| = \sqrt{5^2 + 12^2} $$
    $$ \|v\| = \sqrt{25 + 144} $$
    $$ \|v\| = \sqrt{169} $$
    $$ \|v\| = 13 $$

2.  **Calcul du produit scalaire $\langle u, v \rangle$ :**
    Le produit scalaire euclidien standard de $u = (u_1, u_2)$ et $v = (v_1, v_2)$ est $\langle u, v \rangle = u_1 v_1 + u_2 v_2$.

    Pour $u = (3, 4)$ et $v = (5, 12)$ :
    $$ \langle u, v \rangle = (3)(5) + (4)(12) $$
    $$ \langle u, v \rangle = 15 + 48 $$
    $$ \langle u, v \rangle = 63 $$

3.  **Calcul de la similarité cosinus entre $u$ et $v$ :**
    La similarité cosinus entre deux vecteurs non nuls $u$ et $v$ est définie par la formule :
    $$ \text{sim}(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|} $$

    En utilisant les résultats obtenus aux questions 1 et 2 :
    $$ \text{sim}(u, v) = \frac{63}{(5)(13)} $$
    $$ \text{sim}(u, v) = \frac{63}{65} $$

4.  **Exploration des formes linéaires duales :**
    a. **Détermination des expressions explicites des formes linéaires $\phi_u$ et $\phi_v$ :**
    Pour un vecteur $x = (x_1, x_2)$, la forme linéaire $\phi_x$ est définie par $\phi_x(y) = \langle x, y \rangle$ pour tout $y = (y_1, y_2) \in E$.
    En substituant l'expression du produit scalaire euclidien standard, nous obtenons :
    $$ \phi_x(y_1, y_2) = x_1 y_1 + x_2 y_2 $$

    Pour le vecteur $u = (3, 4)$ :
    $$ \phi_u(y_1, y_2) = 3y_1 + 4y_2 $$

    Pour le vecteur $v = (5, 12)$ :
    $$ \phi_v(y_1, y_2) = 5y_1 + 12y_2 $$

    b. **Vérification de $\langle u, v \rangle = \phi_u(v)$ et $\langle u, v \rangle = \phi_v(u)$ :**
    Calculons $\phi_u(v)$ en substituant les coordonnées de $v = (5, 12)$ dans l'expression de $\phi_u$ :
    $$ \phi_u(v) = \phi_u(5, 12) = 3(5) + 4(12) $$
    $$ \phi_u(v) = 15 + 48 $$
    $$ \phi_u(v) = 63 $$
    Nous constatons que $\phi_u(v)$ est égal au produit scalaire $\langle u, v \rangle$ calculé à la question 2.

    Calculons $\phi_v(u)$ en substituant les coordonnées de $u = (3, 4)$ dans l'expression de $\phi_v$ :
    $$ \phi_v(u) = \phi_v(3, 4) = 5(3) + 12(4) $$
    $$ \phi_v(u) = 15 + 48 $$
    $$ \phi_v(u) = 63 $$
    Nous constatons également que $\phi_v(u)$ est égal au produit scalaire $\langle u, v \rangle$.
    Ces vérifications illustrent la relation d'isomorphisme entre l'espace vectoriel $E$ et son dual $E^*$ dans le cas d'un espace euclidien de dimension finie, et confirment la propriété de symétrie du produit scalaire, $\langle u, v \rangle = \langle v, u \rangle$.

    c. **Expression de la similarité cosinus en utilisant les formes linéaires :**
    La formule générale de la similarité cosinus est $\text{sim}(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|}$.
    En utilisant les résultats de la question 4.b, nous pouvons remplacer le produit scalaire $\langle u, v \rangle$ par $\phi_u(v)$ ou par $\phi_v(u)$.

    Ainsi, la similarité cosinus peut être exprimée de deux manières équivalentes en utilisant les formes linéaires duales :
    $$ \text{sim}(u, v) = \frac{\phi_u(v)}{\|u\| \|v\|} $$
    ou
    $$ \text{sim}(u, v) = \frac{\phi_v(u)}{\|u\| \|v\|} $$

### Conclusion
Nous avons effectué une analyse complète des vecteurs $u = (3, 4)$ et $v = (5, 12)$ dans l'espace euclidien $\mathbb{R}^2$. Les normes euclidiennes ont été calculées comme $\|u\| = 5$ et $\|v\| = 13$. Le produit scalaire $\langle u, v \rangle$ a été déterminé à $63$. En conséquence, la similarité cosinus entre ces deux vecteurs est $\frac{63}{65}$.

Par la suite, nous avons exploré la dualité en déterminant les formes linéaires associées à ces vecteurs : $\phi_u(y_1, y_2) = 3y_1 + 4y_2$ et $\phi_v(y_1, y_2) = 5y_1 + 12y_2$. Nous avons vérifié que le produit scalaire $\langle u, v \rangle$ peut être exprimé comme l'évaluation de la forme linéaire associée à un vecteur sur l'autre vecteur, c'est-à-dire $\phi_u(v) = 63$ et $\phi_v(u) = 63$.

Enfin, nous avons reformulé la similarité cosinus en utilisant ces formes linéaires duales :
$$ \text{sim}(u, v) = \frac{\phi_u(v)}{\|u\| \|v\|} = \frac{\phi_v(u)}{\|u\| \|v\|} $$
Cet exercice démontre la connexion intrinsèque entre les concepts géométriques (norme, produit scalaire, similarité cosinus) et la structure algébrique de dualité dans les espaces euclidiens de dimension finie, un principe fondamental pour la compréhension des espaces de plongement en apprentissage automatique.
