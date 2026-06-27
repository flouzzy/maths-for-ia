Bonjour à toutes et à tous, et bienvenue dans ce nouvel exercice de notre Jalon 12. En tant que Professeur Émérite de Mathématiques, je tiens à insister sur la rigueur et la précision de votre démarche. La compréhension fondamentale des concepts est la pierre angulaire de toute construction théorique solide.

Le présent exercice vise à consolider votre appréhension des notions de base qui sous-tendent la similarité cosinus, un élément central de la conception d'un moteur de recherche sémantique. Nous allons explorer les propriétés géométriques élémentaires des vecteurs dans un espace euclidien, en nous concentrant sur les calculs précis de normes et de produits scalaires.

---

### Exercice 2 : Géométrie euclidienne et similarité cosinus (Difficulté : $\star$)

**Contexte :**
Dans le cadre de la modélisation de concepts par des plongements vectoriels (embeddings) dans un espace euclidien, la similarité cosinus est une mesure fondamentale pour quantifier la proximité sémantique entre deux concepts. Cet exercice aborde les calculs de base nécessaires à la détermination de cette mesure.

**Hypothèses Fondamentales :**
1.  L'espace vectoriel sous-jacent est l'espace euclidien réel tridimensionnel $\mathbb{R}^3$.
2.  $\mathbb{R}^3$ est muni de son produit scalaire euclidien standard, noté $\cdot$, et de la norme euclidienne associée, notée $\left\| \cdot \right\|$.
3.  Tous les vecteurs considérés sont des éléments de $\mathbb{R}^3$ et sont non nuls.

**Énoncé :**

Soient deux vecteurs, $\vec{u}$ et $\vec{v}$, définis par leurs coordonnées dans la base canonique de $\mathbb{R}^3$ :
$$ \vec{u} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \quad \text{et} \quad \vec{v} = \begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix} $$

1.  **Calcul des normes euclidiennes :** Calculer la norme euclidienne de chaque vecteur, $\left\| \vec{u} \right\|$ et $\left\| \vec{v} \right\|$.
2.  **Calcul du produit scalaire euclidien :** Calculer le produit scalaire euclidien des deux vecteurs, $\vec{u} \cdot \vec{v}$.
3.  **Calcul de la similarité cosinus :** En utilisant les résultats des questions précédentes, déterminer la similarité cosinus $S_C(\vec{u}, \vec{v})$ entre $\vec{u}$ et $\vec{v}$.
4.  **Interprétation géométrique :** Interpréter la valeur obtenue pour la similarité cosinus en termes d'angle géométrique entre les vecteurs. Que cela signifie-t-il pour les concepts sémantiques qu'ils pourraient représenter ?

---

### Correction de l'Exercice 2

**Rappel des Hypothèses :**
Nous opérons dans l'espace euclidien $\mathbb{R}^3$ muni du produit scalaire euclidien standard et de la norme euclidienne associée. Les vecteurs $\vec{u}$ et $\vec{v}$ sont des éléments de $\mathbb{R}^3$ et sont non nuls, garantissant la validité des calculs de normes et de similarité cosinus.

**1. Calcul des normes euclidiennes :**

La norme euclidienne d'un vecteur $\vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \in \mathbb{R}^3$ est définie par la formule :
$$ \left\| \vec{x} \right\| = \sqrt{x_1^2 + x_2^2 + x_3^2} $$
Chaque norme $\left\| \vec{x} \right\|$ est un scalaire de type $\mathbb{R}_{\ge 0}$.

*   **Calcul de $\left\| \vec{u} \right\|$ :**
    Le vecteur $\vec{u}$ est donné par $\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$.
    $$ \left\| \vec{u} \right\| = \sqrt{(1)^2 + (2)^2 + (2)^2} $$
    $$ \left\| \vec{u} \right\| = \sqrt{1 + 4 + 4} $$
    $$ \left\| \vec{u} \right\| = \sqrt{9} $$
    $$ \left\| \vec{u} \right\| = 3 $$
    Donc, la norme euclidienne du vecteur $\vec{u}$ est $3$.

*   **Calcul de $\left\| \vec{v} \right\|$ :**
    Le vecteur $\vec{v}$ est donné par $\begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}$.
    $$ \left\| \vec{v} \right\| = \sqrt{(2)^2 + (1)^2 + (-2)^2} $$
    $$ \left\| \vec{v} \right\| = \sqrt{4 + 1 + 4} $$
    $$ \left\| \vec{v} \right\| = \sqrt{9} $$
    $$ \left\| \vec{v} \right\| = 3 $$
    Donc, la norme euclidienne du vecteur $\vec{v}$ est $3$.

**2. Calcul du produit scalaire euclidien :**

Le produit scalaire euclidien de deux vecteurs $\vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \in \mathbb{R}^3$ et $\vec{y} = \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} \in \mathbb{R}^3$ est défini par la formule :
$$ \vec{x} \cdot \vec{y} = x_1 y_1 + x_2 y_2 + x_3 y_3 $$
Le produit scalaire $\vec{x} \cdot \vec{y}$ est un scalaire de type $\mathbb{R}$.

*   **Calcul de $\vec{u} \cdot \vec{v}$ :**
    Nous avons $\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$ et $\vec{v} = \begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}$.
    $$ \vec{u} \cdot \vec{v} = (1)(2) + (2)(1) + (2)(-2) $$
    $$ \vec{u} \cdot \vec{v} = 2 + 2 - 4 $$
    $$ \vec{u} \cdot \vec{v} = 0 $$
    Donc, le produit scalaire euclidien des vecteurs $\vec{u}$ et $\vec{v}$ est $0$.

**3. Calcul de la similarité cosinus :**

La similarité cosinus entre deux vecteurs $\vec{u}$ et $\vec{v}$ est définie par la formule :
$$ S_C(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\left\| \vec{u} \right\| \left\| \vec{v} \right\|} $$
La valeur de la similarité cosinus $S_C(\vec{u}, \vec{v})$ est un scalaire de type $\mathbb{R}$ appartenant à l'intervalle $[-1, 1]$.

En utilisant les résultats précédents :
*   $\vec{u} \cdot \vec{v} = 0$
*   $\left\| \vec{u} \right\| = 3$
*   $\left\| \vec{v} \right\| = 3$

Nous substituons ces valeurs dans la formule :
$$ S_C(\vec{u}, \vec{v}) = \frac{0}{3 \cdot 3} $$
$$ S_C(\vec{u}, \vec{v}) = \frac{0}{9} $$
$$ S_C(\vec{u}, \vec{v}) = 0 $$
Donc, la similarité cosinus entre les vecteurs $\vec{u}$ et $\vec{v}$ est $0$.

**4. Interprétation géométrique :**

La similarité cosinus $S_C(\vec{u}, \vec{v})$ est égale au cosinus de l'angle $\theta$ entre les deux vecteurs. Autrement dit, $\cos(\theta) = S_C(\vec{u}, \vec{v})$.

Dans notre cas, nous avons trouvé $S_C(\vec{u}, \vec{v}) = 0$.
$$ \cos(\theta) = 0 $$
L'angle $\theta \in [0, \pi]$ (puisque l'angle entre des vecteurs non nuls est traditionnellement pris dans cet intervalle) dont le cosinus est $0$ est $\theta = \frac{\pi}{2}$ radians, soit $90^\circ$.

**Signification géométrique :** Un angle de $\frac{\pi}{2}$ radians (ou $90^\circ$) signifie que les deux vecteurs $\vec{u}$ et $\vec{v}$ sont **orthogonaux** (ou perpendiculaires). Leur produit scalaire nul est la signature mathématique de cette orthogonalité.

**Interprétation sémantique pour un moteur de recherche :**
Dans le contexte d'un moteur de recherche sémantique où les concepts sont représentés par des vecteurs dans un espace de plongement (embedding space), une similarité cosinus de $0$ indique que les concepts représentés par $\vec{u}$ et $\vec{v}$ sont **complètement indépendants ou non corrélés sémantiquement**. Il n'y a aucune direction commune ou similitude dans leur signification, du moins telle que capturée par cet espace de plongement spécifique. C'est l'opposé d'une similarité forte (proche de 1) qui indiquerait des concepts très similaires, ou d'une similarité négative (proche de -1) qui suggérerait des concepts opposés.