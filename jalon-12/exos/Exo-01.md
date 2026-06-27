# Jalon 12 : Livrable IA T1 - Exercice 1 (Difficulté : $\star$)

Chers étudiants,

Nous abordons aujourd'hui les fondations mathématiques indispensables à la compréhension des moteurs de recherche sémantiques. Le premier jalon de cette exploration concerne la notion de similarité cosinus, pierre angulaire de la quantification de la ressemblance entre des objets représentés dans un espace vectoriel. Il est impératif de maîtriser ces concepts fondamentaux avec la plus grande rigueur.

---

## Énoncé de l'Exercice 1 : Introduction à la Similarité Cosinus dans les Espaces Vectoriels Réels Euclidiens

### Contexte et Hypothèses Fondamentales

Soit $V$ un espace vectoriel réel, de dimension finie, et muni d'un produit scalaire. Nous le nommerons un **espace vectoriel euclidien**. Dans le cadre de cet exercice, nous considérerons spécifiquement l'espace $\mathbb{R}^n$, où $n \in \mathbb{N}^*$ est un entier strictement positif, muni de son produit scalaire euclidien canonique.

Le **produit scalaire euclidien canonique** de deux vecteurs $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \in \mathbb{R}^n$ et $\mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix} \in \mathbb{R}^n$ est la fonction bilinéaire symétrique $\langle \cdot, \cdot \rangle : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ définie par :
$$ \langle \mathbf{x}, \mathbf{y} \rangle = \sum_{i=1}^{n} x_i y_i = x_1 y_1 + x_2 y_2 + \dots + x_n y_n $$

La **norme euclidienne** (ou norme $L_2$) d'un vecteur $\mathbf{x} \in \mathbb{R}^n$, induite par ce produit scalaire, est la fonction $\| \cdot \| : \mathbb{R}^n \to \mathbb{R}_{\ge 0}$ définie par :
$$ \| \mathbf{x} \| = \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle} = \sqrt{\sum_{i=1}^{n} x_i^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2} $$

La **similarité cosinus** entre deux vecteurs non nuls $\mathbf{u} \in \mathbb{R}^n \setminus \{ \mathbf{0} \}$ et $\mathbf{v} \in \mathbb{R}^n \setminus \{ \mathbf{0} \}$ est définie comme le cosinus de l'angle $\theta$ entre ces deux vecteurs. Elle est calculée par la formule :
$$ \text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\| \mathbf{u} \| \| \mathbf{v} \|} $$
Nous postulons que les vecteurs $\mathbf{u}$ et $\mathbf{v}$ sont non nuls, condition nécessaire à la validité de la définition de la similarité cosinus, car elle implique une division par la norme des vecteurs, lesquelles doivent être strictement positives.

### Question

Considérons l'espace vectoriel euclidien $\mathbb{R}^3$. Soient deux vecteurs $\mathbf{u}$ et $\mathbf{v}$ définis comme suit :
*   $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \in \mathbb{R}^3$
*   $\mathbf{v} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix} \in \mathbb{R}^3$

1.  Déterminez la norme euclidienne du vecteur $\mathbf{u}$.
2.  Déterminez la norme euclidienne du vecteur $\mathbf{v}$.
3.  Calculez le produit scalaire euclidien de $\mathbf{u}$ et $\mathbf{v}$.
4.  Déduisez-en la similarité cosinus entre $\mathbf{u}$ et $\mathbf{v}$.
5.  Interprétez qualitativement le signe de la similarité cosinus obtenue.

---

## Correction de l'Exercice 1

### Rappel des Données

Nous avons les vecteurs :
*   $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \in \mathbb{R}^3$
*   $\mathbf{v} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix} \in \mathbb{R}^3$

### 1. Détermination de la norme euclidienne de $\mathbf{u}$

La norme euclidienne d'un vecteur $\mathbf{u} = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \in \mathbb{R}^3$ est donnée par la formule $\| \mathbf{u} \| = \sqrt{u_1^2 + u_2^2 + u_3^2}$.

Appliquons cette formule au vecteur $\mathbf{u}$:
$$ \| \mathbf{u} \| = \sqrt{1^2 + 2^2 + 1^2} $$
$$ \| \mathbf{u} \| = \sqrt{(1 \times 1) + (2 \times 2) + (1 \times 1)} $$
$$ \| \mathbf{u} \| = \sqrt{1 + 4 + 1} $$
$$ \| \mathbf{u} \| = \sqrt{6} $$
Ainsi, la norme euclidienne du vecteur $\mathbf{u}$ est $\sqrt{6} \in \mathbb{R}_{>0}$.

### 2. Détermination de la norme euclidienne de $\mathbf{v}$

La norme euclidienne d'un vecteur $\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} \in \mathbb{R}^3$ est donnée par la formule $\| \mathbf{v} \| = \sqrt{v_1^2 + v_2^2 + v_3^2}$.

Appliquons cette formule au vecteur $\mathbf{v}$:
$$ \| \mathbf{v} \| = \sqrt{2^2 + 1^2 + (-1)^2} $$
$$ \| \mathbf{v} \| = \sqrt{(2 \times 2) + (1 \times 1) + ((-1) \times (-1))} $$
$$ \| \mathbf{v} \| = \sqrt{4 + 1 + 1} $$
$$ \| \mathbf{v} \| = \sqrt{6} $$
Ainsi, la norme euclidienne du vecteur $\mathbf{v}$ est $\sqrt{6} \in \mathbb{R}_{>0}$.

### 3. Calcul du produit scalaire euclidien de $\mathbf{u}$ et $\mathbf{v}$

Le produit scalaire euclidien de deux vecteurs $\mathbf{u} = \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \in \mathbb{R}^3$ et $\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} \in \mathbb{R}^3$ est donné par la formule $\langle \mathbf{u}, \mathbf{v} \rangle = u_1 v_1 + u_2 v_2 + u_3 v_3$.

Appliquons cette formule aux vecteurs $\mathbf{u}$ et $\mathbf{v}$:
$$ \langle \mathbf{u}, \mathbf{v} \rangle = (1 \times 2) + (2 \times 1) + (1 \times (-1)) $$
$$ \langle \mathbf{u}, \mathbf{v} \rangle = 2 + 2 + (-1) $$
$$ \langle \mathbf{u}, \mathbf{v} \rangle = 4 - 1 $$
$$ \langle \mathbf{u}, \mathbf{v} \rangle = 3 $$
Ainsi, le produit scalaire des vecteurs $\mathbf{u}$ et $\mathbf{v}$ est $3 \in \mathbb{R}$.

### 4. Déduction de la similarité cosinus entre $\mathbf{u}$ et $\mathbf{v}$

La similarité cosinus entre $\mathbf{u}$ et $\mathbf{v}$ est donnée par la formule $\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\| \mathbf{u} \| \| \mathbf{v} \|}$.

Substituons les valeurs calculées précédemment :
*   $\langle \mathbf{u}, \mathbf{v} \rangle = 3$
*   $\| \mathbf{u} \| = \sqrt{6}$
*   $\| \mathbf{v} \| = \sqrt{6}$

$$ \text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{3}{\sqrt{6} \times \sqrt{6}} $$
$$ \text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{3}{6} $$
$$ \text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{1}{2} $$
$$ \text{cos\_sim}(\mathbf{u}, \mathbf{v}) = 0.5 $$
Ainsi, la similarité cosinus entre $\mathbf{u}$ et $\mathbf{v}$ est $0.5 \in [-1, 1]$.

### 5. Interprétation qualitative du signe de la similarité cosinus obtenue

Le résultat de la similarité cosinus est $0.5$. Ce nombre est strictement positif.
La similarité cosinus est, par définition, le cosinus de l'angle $\theta$ formé par les deux vecteurs $\mathbf{u}$ et $\mathbf{v}$. Les valeurs de la similarité cosinus se situent dans l'intervalle $[-1, 1]$.

*   Si $\text{cos\_sim}(\mathbf{u}, \mathbf{v}) > 0$, cela implique que $\cos(\theta) > 0$. L'angle $\theta$ entre les vecteurs est alors aigu ($0 \le \theta < \pi/2$ radians, ou $0^\circ \le \theta < 90^\circ$). Cela signifie que les vecteurs pointent généralement dans la même direction. Dans le contexte de la sémantique, cela indique une certaine ressemblance ou corrélation positive entre les entités que représentent les vecteurs.
*   Si $\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = 0$, cela implique que $\cos(\theta) = 0$. L'angle $\theta$ est droit ($\theta = \pi/2$ radians, ou $90^\circ$). Les vecteurs sont orthogonaux (ou perpendiculaires), indiquant une absence de relation linéaire ou une indépendance.
*   Si $\text{cos\_sim}(\mathbf{u}, \mathbf{v}) < 0$, cela implique que $\cos(\theta) < 0$. L'angle $\theta$ est alors obtus ($\pi/2 < \theta \le \pi$ radians, ou $90^\circ < \theta \le 180^\circ$). Les vecteurs pointent dans des directions opposées. Dans le contexte sémantique, cela suggérerait une opposition ou une dissemblance.

Dans notre cas, $\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = 0.5 > 0$. Cela indique que les vecteurs $\mathbf{u}$ et $\mathbf{v}$ ont une orientation générale similaire ; ils forment un angle aigu. Cela suggère qu'ils partagent une certaine ressemblance dans l'espace d'intégration sémantique. L'angle exact $\theta = \arccos(0.5) = \pi/3$ radians, ce qui correspond à $60^\circ$.

---

Ce premier exercice pose les bases formelles de l'approche. Nous progresserons vers des concepts plus abstraits et des applications concrètes dans les jalons suivants.