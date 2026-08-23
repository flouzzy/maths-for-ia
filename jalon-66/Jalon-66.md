# Jalon 66 : Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives

## 1. De Riemann à Lebesgue : L'Architecture des Aires par les Niveaux

La théorie de l'intégration développée par Bernhard Riemann au XIXe siècle, bien que d'une élégance fondamentale, rencontre des limites structurelles lorsqu'elle est confrontée à des fonctions fortement discontinues ou à des processus de passage à la limite. L'impasse géométrique originelle se manifeste dans l'approche riemannienne qui consiste à subdiviser le domaine de définition (l'axe des abscisses) en petits intervalles, puis à approximer l'aire sous la courbe par des rectangles verticaux. Cette méthode fonctionne admirablement pour les fonctions continues ou régulières en morceaux. Cependant, si la fonction fluctue sauvagement, comme la célèbre fonction indicatrice des rationnels $\mathbf{1}_{\mathbb{Q}}$, chaque petit intervalle contiendra à la fois des rationnels (valeur 1) et des irrationnels (valeur 0), rendant les sommes de Darboux inférieures et supérieures irrémédiablement distantes.

Henri Lebesgue, au début du XXe siècle, propose un renversement de perspective radical, comparable à une révolution copernicienne en analyse. Plutôt que de découper l'axe des abscisses, Lebesgue suggère de découper l'axe des ordonnées. Géométriquement, cela revient à regrouper les points du domaine qui partagent des valeurs similaires (les ensembles de niveau), mesurés ensuite par une "mesure" abstraite, puis à sommer ces contributions horizontales. C'est la genèse de l'intégrale de Lebesgue. En substituant la notion topologique de longueur d'intervalle par la notion mesurable d'ensembles, Lebesgue permet d'intégrer des espaces infiniment plus complexes et d'établir des théorèmes de convergence d'une puissance inégalée, fondamentaux pour la théorie des probabilités (axiomatisée par Kolmogorov) et l'analyse fonctionnelle (espaces de Sobolev).

## 2. Définitions et Théorèmes Fondamentaux

Nous nous plaçons sur un espace mesurable $(X, \mathcal{A})$ muni d'une mesure positive $\mu$. Soit $\mathcal{M}^+(X, \mathcal{A})$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

### Intégrale d'une fonction étagée positive

**Définition (Intégrale d'une fonction étagée) :**
Soit $s \in \mathcal{M}^+(X, \mathcal{A})$ une fonction étagée positive. Elle s'écrit sous forme canonique :
$$s(x) = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}(x)$$
où $n \in \mathbb{N}^*$, les $\alpha_i \in [0, +\infty[$ sont des réels distincts, et les $A_i \in \mathcal{A}$ forment une partition finie de $X$.
L'intégrale de Lebesgue de $s$ par rapport à la mesure $\mu$ est définie par :
$$\int_X s \, d\mu = \sum_{i=1}^n \alpha_i \mu(A_i)$$
Cette valeur appartient à $[0, +\infty]$ (avec la convention $0 \times (+\infty) = 0$).

**Exemple concret immédiat :**
Considérons l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Soit la fonction étagée $s : \mathbb{R} \to \mathbb{R}$ définie par :
$$s(x) = 2 \cdot \mathbf{1}_{[0, 3]}(x) + 5 \cdot \mathbf{1}_{]3, 4]}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 4]}(x)$$
L'intégrale de $s$ par rapport à $\lambda$ est :
$$\int_{\mathbb{R}} s \, d\lambda = 2 \cdot \lambda([0, 3]) + 5 \cdot \lambda(]3, 4]) + 0 \cdot \lambda(\mathbb{R} \setminus [0, 4])$$
$$\int_{\mathbb{R}} s \, d\lambda = 2 \times 3 + 5 \times 1 + 0 \times (+\infty) = 6 + 5 + 0 = 11$$
L'aire totale sous la "courbe" étagée est exactement 11.

**Cas limite :**
Si $X = \mathbb{R}$, $\mu = \lambda$, et $s(x) = 1 \cdot \mathbf{1}_{\mathbb{R}}(x)$, alors $\int_{\mathbb{R}} s \, d\lambda = 1 \cdot \lambda(\mathbb{R}) = +\infty$. L'intégrale peut diverger.

### Intégrale d'une fonction mesurable positive quelconque

**Définition (Intégrale d'une fonction mesurable positive) :**
Soit $f \in \mathcal{M}^+(X, \mathcal{A})$. L'intégrale de $f$ par rapport à $\mu$ est définie comme le supremum des intégrales des fonctions étagées positives qui minorant $f$ :
$$\int_X f \, d\mu = \sup \left\{ \int_X s \, d\mu \mid s \text{ est étagée positive et } \forall x \in X, \, 0 \leq s(x) \leq f(x) \right\}$$

**Exemple concret immédiat :**
Soit l'espace $([0, 1], \mathcal{B}([0,1]))$ avec la mesure de Lebesgue $\lambda$. Prenons la fonction indicatrice des rationnels, ou fonction de Dirichlet $f = \mathbf{1}_{\mathbb{Q} \cap [0, 1]}$.
Cherchons les fonctions étagées positives $s$ telles que $0 \leq s(x) \leq f(x)$ pour tout $x$.
Puisque $f(x)=0$ pour $x \notin \mathbb{Q}$, toute telle fonction $s$ doit satisfaire $s(x) \leq 0$ sur les irrationnels. Puisque $s$ est positive, $s(x) = 0$ sur $(\mathbb{R} \setminus \mathbb{Q}) \cap [0, 1]$.
L'ensemble des rationnels est de mesure nulle : $\lambda(\mathbb{Q} \cap [0,1]) = 0$.
Ainsi, pour toute fonction étagée $s$ minorant $f$, ses valeurs strictement positives ne peuvent être atteintes que sur des sous-ensembles de $\mathbb{Q}$, donc de mesure nulle.
Conséquemment, $\int s \, d\lambda = \sum \alpha_i \lambda(A_i) = 0$ (car $\lambda(A_i)=0$ pour $\alpha_i > 0$).
Le supremum est donc $0$. L'intégrale de Lebesgue de la fonction de Dirichlet est $0$, bien qu'elle ne soit pas Riemann-intégrable.

### Propriétés Fondamentales : Linéarité et Croissance

**Théorème (Croissance de l'intégrale) :**
Soient $f, g \in \mathcal{M}^+(X, \mathcal{A})$. Si pour tout $x \in X, f(x) \leq g(x)$, alors :
$$\int_X f \, d\mu \leq \int_X g \, d\mu$$

**Théorème (Linéarité positive) :**
Pour tous $f, g \in \mathcal{M}^+(X, \mathcal{A})$ et pour tous $\alpha, \beta \in \mathbb{R}^+$,
$$\int_X (\alpha f + \beta g) \, d\mu = \alpha \int_X f \, d\mu + \beta \int_X g \, d\mu$$

## 3. Démonstrations

**Démonstration de la croissance de l'intégrale :**
Soient $f, g \in \mathcal{M}^+(X, \mathcal{A})$ telles que $f \leq g$ sur $X$.
Considérons l'ensemble $\mathcal{S}_f = \{s \text{ étagée positive } \mid s \leq f\}$.
Soit $s \in \mathcal{S}_f$. Puisque $s(x) \leq f(x)$ pour tout $x$, et que par hypothèse $f(x) \leq g(x)$ pour tout $x$, nous avons par transitivité :
$$s(x) \leq g(x)$$
Ainsi, toute fonction étagée $s$ qui minore $f$ minore également $g$. Autrement dit, $\mathcal{S}_f \subset \mathcal{S}_g$, où $\mathcal{S}_g = \{s \text{ étagée positive } \mid s \leq g\}$.
Le supremum sur un sous-ensemble étant inférieur ou égal au supremum sur l'ensemble entier, on obtient :
$$\sup_{s \in \mathcal{S}_f} \int_X s \, d\mu \leq \sup_{s \in \mathcal{S}_g} \int_X s \, d\mu$$
Ce qui est exactement la définition de :
$$\int_X f \, d\mu \leq \int_X g \, d\mu$$
$\blacksquare$

**Démonstration partielle de la linéarité positive (cas de l'homogénéité $\alpha f$) :**
Soit $f \in \mathcal{M}^+(X, \mathcal{A})$ et $\alpha > 0$. Montrons que $\int_X \alpha f \, d\mu = \alpha \int_X f \, d\mu$.
Soit $s$ une fonction étagée positive telle que $s \leq f$. Alors $\alpha s$ est une fonction étagée positive telle que $\alpha s \leq \alpha f$.
De plus, si $s = \sum_{i=1}^n c_i \mathbf{1}_{A_i}$, alors $\alpha s = \sum_{i=1}^n (\alpha c_i) \mathbf{1}_{A_i}$.
Par définition de l'intégrale d'une fonction étagée :
$$\int_X (\alpha s) \, d\mu = \sum_{i=1}^n (\alpha c_i) \mu(A_i) = \alpha \sum_{i=1}^n c_i \mu(A_i) = \alpha \int_X s \, d\mu$$
Prenons le supremum sur l'ensemble des $s \leq f$ :
$$\int_X \alpha f \, d\mu = \sup_{s' \leq \alpha f} \int_X s' \, d\mu = \sup_{s \leq f} \int_X \alpha s \, d\mu = \sup_{s \leq f} \left( \alpha \int_X s \, d\mu \right)$$
Comme $\alpha > 0$, l'opération de multiplication commute avec le supremum :
$$= \alpha \sup_{s \leq f} \int_X s \, d\mu = \alpha \int_X f \, d\mu$$
Pour le cas $\alpha = 0$, la fonction $0 \cdot f$ est la fonction nulle, dont l'intégrale est 0, ce qui concorde avec $0 \cdot \int_X f \, d\mu = 0$. $\blacksquare$

## 4. Applications en Physique, Logique & Intelligence Artificielle

L'intégrale de Lebesgue est la clé de voûte mathématique sur laquelle repose la formalisation moderne des probabilités et, par extension, l'Intelligence Artificielle et la Physique Quantique.

- **Théorie de l'Apprentissage Statistique (Machine Learning) :** Le risque espéré dans l'apprentissage automatique est défini comme une intégrale de Lebesgue par rapport à une mesure de probabilité inconnue $\mathbb{P}$ sur l'espace des données $X \times Y$. L'intégrale de Lebesgue permet d'intégrer des fonctions de perte complexes, continues ou discontinues, garantissant l'existence du risque attendu même sur des variétés de grande dimension où la mesure de Riemann échouerait.
- **Physique Théorique Quantique :** L'espace de Hilbert des fonctions d'onde $L^2(\mathbb{R}^d)$ est l'ensemble des fonctions mesurables dont le carré du module est Lebesgue-intégrable. Sans la complétude conférée par l'intégrale de Lebesgue, la mécanique quantique serait mathématiquement inconsistante, car des suites de fonctions d'onde convergentes pourraient converger vers un objet en dehors de l'espace.
- **Théorie de l'Information (Divergence de Kullback-Leibler) :** En IA générative (comme dans la fonction de coût des VAE ou des Modèles de Diffusion), la mesure des distances entre distributions de probabilités complexes repose sur l'intégration par rapport à une mesure de référence (souvent la mesure de Lebesgue). Cette abstraction autorise l'intégration même pour des densités avec des singularités, rendant les algorithmes d'optimisation mathématiquement robustes.
