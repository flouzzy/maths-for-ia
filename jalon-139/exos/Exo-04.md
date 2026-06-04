# Exercice 4 : Instabilité de la Régression Linéaire Sans Régularisation (★★☆☆☆)

## Énoncé
Soit un échantillon $S = ((x_1, y_1), \dots, (x_n, y_n)) \in (\mathbb{R}^d \times \mathbb{R})^n$.
On note $X \in \mathbb{R}^{n \times d}$ la matrice de conception (design matrix) dont la $i$-ème ligne est $x_i^T$, et $Y \in \mathbb{R}^n$ le vecteur des cibles.
L'algorithme des moindres carrés ordinaires (MCO) cherche à minimiser le risque empirique non régularisé :
$$w_S = \arg\min_{w \in \mathbb{R}^d} \frac{1}{n} \|X w - Y\|_2^2$$
On suppose que la matrice de Gram $X^T X$ est inversible.
1. Exprimer la solution $w_S$ sous forme matricielle.
2. Démontrer que si la plus petite valeur propre de la matrice de Gram $X^T X$ est arbitrairement proche de 0 (cas de quasi-colinéarité), une modification infinitésimale d'une cible $y_i$ peut entraîner une modification arbitrairement grande du vecteur de poids optimal $w_S$. 
3. En déduire que la régression linéaire sans régularisation n'est pas uniformément stable au sens de Bousquet-Elisseeff.

---

## Correction Détaillée

### 1. Solution des moindres carrés ordinaires (MCO)
La fonction objective à minimiser est $g(w) = \frac{1}{n} (X w - Y)^T (X w - Y)$.
En calculant le gradient par rapport à $w$ :
$$\nabla g(w) = \frac{2}{n} X^T (X w - Y) = \frac{2}{n} (X^T X w - X^T Y)$$
Puisque $X^T X$ est supposée inversible, le gradient s'annule en un point unique qui est le minimum global :
$$\nabla g(w_S) = 0 \implies X^T X w_S = X^T Y \implies w_S = (X^T X)^{-1} X^T Y$$

### 2. Sensibilité sous perturbation (cas de quasi-colinéarité)
Soit $S^{(i)}$ l'échantillon où la cible $y_i$ est perturbée d'une quantité $\epsilon \in \mathbb{R}$, devenant $y'_i = y_i + \epsilon$.
Le vecteur des cibles perturbé est $Y^{(i)} = Y + \epsilon e_i$, où $e_i = (0, \dots, 1, \dots, 0)^T$ est le $i$-ème vecteur de la base canonique de $\mathbb{R}^n$.
Le vecteur de poids optimal perturbé associé est :
$$w_{S^{(i)}} = (X^T X)^{-1} X^T Y^{(i)} = (X^T X)^{-1} X^T (Y + \epsilon e_i) = w_S + \epsilon (X^T X)^{-1} X^T e_i$$

Calculons la norme de la différence $\|w_S - w_{S^{(i)}}\|_2$ :
$$\|w_S - w_{S^{(i)}}\|_2 = |\epsilon| \|(X^T X)^{-1} x_i\|_2$$
puisque la $i$-ème colonne de $X^T$ est le vecteur de caractéristiques $x_i$.

Par les propriétés des normes de matrices, si nous notons $\sigma_{\min}(X^T X)$ la plus petite valeur propre de la matrice symétrique réelle $X^T X$ :
$$\|(X^T X)^{-1} x_i\|_2 \ge \frac{\|x_i\|_2}{\sigma_{\max}(X^T X)} \quad \text{et dans le pire cas} \quad \|(X^T X)^{-1} x_i\|_2 \sim \frac{\|x_i\|_2}{\sigma_{\min}(X^T X)}$$

Si les caractéristiques présentent une quasi-colinéarité, la plus petite valeur propre de la matrice de Gram s'approche de 0 :
$$\sigma_{\min}(X^T X) \to 0 \implies \|(X^T X)^{-1} x_i\|_2 \to \infty$$
Ainsi, même pour une perturbation $\epsilon$ très petite, le terme $\|\Delta w\|_2 = \|w_S - w_{S^{(i)}}\|_2$ peut être rendu arbitrairement grand.

### 3. Conclusion sur la stabilité uniforme
La perte quadratique est $\ell(w, (x, y)) = (\langle w, x \rangle - y)^2$. La différence de perte sur un point de test $z = (x, y)$ est :
$$|\ell(w_S, z) - \ell(w_{S^{(i)}}, z)| = |(\langle w_S, x \rangle - y)^2 - (\langle w_{S^{(i)}}, x \rangle - y)^2|$$
$$= |\langle w_S - w_{S^{(i)}}, x \rangle| \times |\langle w_S + w_{S^{(i)}}, x \rangle - 2y|$$

Puisque $\|w_S - w_{S^{(i)}}\|_2$ peut être arbitrairement grand en raison de la quasi-colinéarité, le supremum sur l'espace de test de cette différence de perte est infini. 
Ainsi, l'algorithme des moindres carrés ordinaires sans régularisation n'est pas uniformément stable : sa constante de stabilité uniforme $\beta$ est infinie dans le cas général. La régularisation (comme dans Ridge) est indispensable pour forcer la stabilité.
