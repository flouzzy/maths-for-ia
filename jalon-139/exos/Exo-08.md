# Exercice 8 : Stabilité Uniforme des SVM à Noyau (★★★★☆)

## Énoncé
Soit un échantillon $S = ((x_1, y_1), \dots, (x_n, y_n)) \in (\mathcal{X} \times \{-1, 1\})^n$.
On suppose que $\mathcal{X}$ est muni d'un noyau défini positif $K$ associé à un Espace de Hilbert à Noyau Reproduisant (RKHS) $\mathcal{H}_K$. On suppose que pour tout $x \in \mathcal{X}$, $K(x, x) \le \kappa^2$.
L'algorithme SVM à vaste marge (soft margin) apprend une fonction de décision $f_S \in \mathcal{H}_K$ en résolvant :
$$f_S = \arg\min_{f \in \mathcal{H}_K} \left( \frac{1}{n} \sum_{i=1}^n \ell_{\text{hinge}}(f(x_i), y_i) + \lambda \|f\|_K^2 \right)$$
où $\ell_{\text{hinge}}(f(x), y) = \max(0, 1 - y f(x))$ et $\lambda > 0$.
1. Montrer que la fonction de perte charnière $\ell_{\text{hinge}}(a, y) = \max(0, 1 - y a)$ est 1-Lipschitzienne par rapport à sa première variable $a$.
2. En déduire la constante de stabilité uniforme $\beta$ de cet algorithme SVM à noyau.

---

## Correction Détaillée

### 1. Propriété Lipschitzienne de la perte charnière
Soient $a, b \in \mathbb{R}$ et $y \in \{-1, 1\}$. Calculons la différence :
$$|\ell_{\text{hinge}}(a, y) - \ell_{\text{hinge}}(b, y)| = |\max(0, 1 - y a) - \max(0, 1 - y b)|$$

Rappelons la propriété classique du max : pour tous réels $u, v$, $|\max(0, u) - \max(0, v)| \le |u - v|$.
En appliquant cela :
$$|\ell_{\text{hinge}}(a, y) - \ell_{\text{hinge}}(b, y)| \le |(1 - y a) - (1 - y b)| = |-y(a - b)| = |y| |a - b|$$
Puisque $y \in \{-1, 1\}$, sa valeur absolue $|y|$ vaut exactement 1. D'où :
$$|\ell_{\text{hinge}}(a, y) - \ell_{\text{hinge}}(b, y)| \le |a - b|$$
La fonction de perte charnière $\ell_{\text{hinge}}$ est donc 1-Lipschitzienne par rapport à son premier argument.

### 2. Constante de stabilité uniforme du SVM à noyau
La fonctionnelle à minimiser est $G_S(f) = \frac{1}{n}\sum_{i=1}^n \ell_{\text{hinge}}(f(x_i), y_i) + \lambda \|f\|_K^2$.
Puisque le produit scalaire du RKHS est fortement convexe par rapport à sa norme $\|f\|_K$, la fonctionnelle $G_S(f)$ est $2\lambda$-fortement convexe dans $\mathcal{H}_K$.

Soient $S$ et $S^{(i)}$ deux échantillons ne différant que par leur $i$-ème élément. Soient $f_S$ et $f_{S^{(i)}}$ les deux modèles optimaux respectifs.
Par la propriété générale de somme des conditions d'optimalité pour des fonctions fortement convexes (établie à l'Exercice 6) :
$$G_S(f_{S^{(i)}}) + G_{S^{(i)}}(f_S) - G_S(f_S) - G_{S^{(i)}}(f_{S^{(i)}}) \ge 2\lambda \|f_S - f_{S^{(i)}}\|_K^2$$

Développons le membre de gauche de cette inégalité :
$$\Big( G_S(f_{S^{(i)}}) - G_{S^{(i)}}(f_{S^{(i)}}) \Big) - \Big( G_S(f_S) - G_{S^{(i)}}(f_S) \Big) \ge 2\lambda \|f_S - f_{S^{(i)}}\|_K^2$$
La différence $G_S(f) - G_{S^{(i)}}(f)$ ne dépend que de l'élément modifié en position $i$ :
$$G_S(f) - G_{S^{(i)}}(f) = \frac{1}{n} \Big( \ell_{\text{hinge}}(f(x_i), y_i) - \ell_{\text{hinge}}(f(x'_i), y'_i) \Big)$$
Substituons cette expression dans l'inégalité de convexité :
$$\frac{1}{n} \Big[ \Big( \ell_{\text{hinge}}(f_{S^{(i)}}(x_i), y_i) - \ell_{\text{hinge}}(f_{S^{(i)}}(x'_i), y'_i) \Big) - \Big( \ell_{\text{hinge}}(f_S(x_i), y_i) - \ell_{\text{hinge}}(f_S(x'_i), y'_i) \Big) \Big] \ge 2\lambda \|f_S - f_{S^{(i)}}\|_K^2$$

Regroupons les termes de manière astucieuse :
$$\frac{1}{n} \Big[ \Big( \ell_{\text{hinge}}(f_{S^{(i)}}(x_i), y_i) - \ell_{\text{hinge}}(f_S(x_i), y_i) \Big) + \Big( \ell_{\text{hinge}}(f_S(x'_i), y'_i) - \ell_{\text{hinge}}(f_{S^{(i)}}(x'_i), y'_i) \Big) \Big] \ge 2\lambda \|f_S - f_{S^{(i)}}\|_K^2$$

Puisque la perte charnière est 1-Lipschitzienne :
- $\ell_{\text{hinge}}(f_{S^{(i)}}(x_i), y_i) - \ell_{\text{hinge}}(f_S(x_i), y_i) \le |f_{S^{(i)}}(x_i) - f_S(x_i)|$
- $\ell_{\text{hinge}}(f_S(x'_i), y'_i) - \ell_{\text{hinge}}(f_{S^{(i)}}(x'_i), y'_i) \le |f_S(x'_i) - f_{S^{(i)}}(x'_i)|$

L'inégalité se simplifie en :
$$\frac{1}{n} \Big( |f_S(x_i) - f_{S^{(i)}}(x_i)| + |f_S(x'_i) - f_{S^{(i)}}(x'_i)| \Big) \ge 2\lambda \|f_S - f_{S^{(i)}}\|_K^2$$

Exploitons la propriété de reproduction fondamentale des RKHS : pour toute fonction $g \in \mathcal{H}_K$ et tout point $x \in \mathcal{X}$, $g(x) = \langle g, K(x, \cdot) \rangle_K$.
Par l'inégalité de Cauchy-Schwarz dans $\mathcal{H}_K$ et l'hypothèse de borne sur le noyau :
$$|g(x)| \le \|g\|_K \sqrt{K(x, x)} \le \kappa \|g\|_K$$
Appliquons cette relation à la fonction différence $g = f_S - f_{S^{(i)}}$ aux points $x_i$ et $x'_i$ :
- $|f_S(x_i) - f_{S^{(i)}}(x_i)| \le \kappa \|f_S - f_{S^{(i)}}\|_K$
- $|f_S(x'_i) - f_{S^{(i)}}(x'_i)| \le \kappa \|f_S - f_{S^{(i)}}\|_K$

En réinjectant ces bornes dans l'inégalité :
$$\frac{2\kappa}{n} \|f_S - f_{S^{(i)}}\|_K \ge 2\lambda \|f_S - f_{S^{(i)}}\|_K^2 \implies \|f_S - f_{S^{(i)}}\|_K \le \frac{\kappa}{\lambda n}$$

Calculons maintenant la stabilité de la perte pour tout point de test $z = (x, y) \in \mathcal{Z}$ :
$$|\ell_{\text{hinge}}(f_S(x), y) - \ell_{\text{hinge}}(f_{S^{(i)}}(x), y)| \le |f_S(x) - f_{S^{(i)}}(x)| \le \kappa \|f_S - f_{S^{(i)}}\|_K$$
En substituant par notre majoration de la norme :
$$\sup_z |\ell_{\text{hinge}}(f_S(x), y) - \ell_{\text{hinge}}(f_{S^{(i)}}(x), y)| \le \kappa \left( \frac{\kappa}{\lambda n} \right) = \frac{\kappa^2}{\lambda n}$$

La constante de stabilité uniforme du SVM à noyau est donc :
$$\beta = \frac{\kappa^2}{\lambda n}$$
Cette borne décroît en $\mathcal{O}(1/n)$ lorsque $n \to \infty$, démontrant la très forte stabilité géométrique des classifieurs à vaste marge régularisés.
