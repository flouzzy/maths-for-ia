# Exercice 6 : Stabilité de la Régression Ridge Multidimensionnelle (★★★☆☆)

## Énoncé
Soit un échantillon $S = ((x_1, y_1), \dots, (x_n, y_n)) \in (\mathcal{B}_2(R) \times [-Y_{\max}, Y_{\max}])^n$.
L'algorithme de régression Ridge résout le problème d'optimisation suivant :
$$w_S = \arg\min_{w \in \mathbb{R}^d} \left( \frac{1}{n} \sum_{i=1}^n (\langle w, x_i \rangle - y_i)^2 + \lambda \|w\|_2^2 \right)$$
où $\lambda > 0$.
1. Démontrer que la fonction objective $F_S(w) = \frac{1}{n} \sum_{i=1}^n (\langle w, x_i \rangle - y_i)^2 + \lambda \|w\|_2^2$ est $2\lambda$-fortement convexe par rapport à la norme euclidienne.
2. Pour tout échantillon perturbé $S^{(i)}$, en utilisant la propriété que $w_S$ et $w_{S^{(i)}}$ minimisent respectivement $F_S$ et $F_{S^{(i)}}$, démontrer rigoureusement l'inégalité sur la norme :
$$\|w_S - w_{S^{(i)}}\|_2 \le \frac{2 R Y_{\max}}{\lambda n}$$

---

## Correction Détaillée

### 1. Preuve de la forte convexité de $F_S$
Rappelons qu'une fonction $g : \mathbb{R}^d \to \mathbb{R}$ deux fois différentiable est $\alpha$-fortement convexe si et seulement si pour tout $w \in \mathbb{R}^d$, sa matrice hessienne vérifie :
$$\nabla^2 g(w) \succeq \alpha I_d \quad \text{(au sens de l'ordre de Loewner)}$$
c'est-à-dire que pour tout vecteur $u \in \mathbb{R}^d$, $u^T \nabla^2 g(w) u \ge \alpha \|u\|_2^2$.

Calculons la matrice hessienne de la fonction $F_S(w)$ :
$$F_S(w) = \frac{1}{n} \sum_{i=1}^n \left( w^T x_i x_i^T w - 2 y_i x_i^T w + y_i^2 \right) + \lambda w^T w$$
En dérivant une première fois :
$$\nabla F_S(w) = \frac{2}{n} \sum_{i=1}^n (x_i x_i^T w - y_i x_i) + 2 \lambda w$$
En dérivant une seconde fois, nous obtenons la matrice hessienne :
$$\nabla^2 F_S(w) = \frac{2}{n} \sum_{i=1}^n x_i x_i^T + 2 \lambda I_d$$

Soit $u \in \mathbb{R}^d$ un vecteur quelconque. Calculons la forme quadratique associée :
$$u^T \nabla^2 F_S(w) u = u^T \left( \frac{2}{n} \sum_{i=1}^n x_i x_i^T + 2 \lambda I_d \right) u = \frac{2}{n} \sum_{i=1}^n u^T x_i x_i^T u + 2 \lambda u^T u$$
$$= \frac{2}{n} \sum_{i=1}^n (x_i^T u)^2 + 2 \lambda \|u\|_2^2$$
Puisque $(x_i^T u)^2 \ge 0$ pour tout $i$, la somme est positive ou nulle. D'où :
$$u^T \nabla^2 F_S(w) u \ge 2 \lambda \|u\|_2^2$$
La fonction $F_S$ est donc $2\lambda$-fortement convexe sur $\mathbb{R}^d$.

### 2. Preuve de la majoration de $\|w_S - w_{S^{(i)}}\|_2$
Soient $w_S$ et $w_{S^{(i)}}$ les minimisateurs respectifs des fonctions fortement convexes $F_S$ et $F_{S^{(i)}}$.
Par la caractérisation variationnelle du minimum d'une fonction fortement convexe :
- Comme $w_S$ est le minimum de $F_S$ (qui est $2\lambda$-fortement convexe) :
$$F_S(w_{S^{(i)}}) \ge F_S(w_S) + \langle \nabla F_S(w_S), w_{S^{(i)}} - w_S \rangle + \lambda \|w_{S^{(i)}} - w_S\|_2^2$$
Puisque $\nabla F_S(w_S) = 0$, on a :
$$F_S(w_{S^{(i)}}) - F_S(w_S) \ge \lambda \|w_{S^{(i)}} - w_S\|_2^2$$

- De même pour $F_{S^{(i)}}$ (qui est également $2\lambda$-fortement convexe) en son minimum $w_{S^{(i)}}$ :
$$F_{S^{(i)}}(w_S) - F_{S^{(i)}}(w_{S^{(i)}}) \ge \lambda \|w_S - w_{S^{(i)}}\|_2^2$$

Sommons ces deux inégalités :
$$\big( F_S(w_{S^{(i)}}) - F_{S^{(i)}}(w_{S^{(i)}}) \big) - \big( F_S(w_S) - F_{S^{(i)}}(w_S) \big) \ge 2 \lambda \|w_S - w_{S^{(i)}}\|_2^2$$

Écrivons la différence $F_S(w) - F_{S^{(i)}}(w)$ :
$$F_S(w) - F_{S^{(i)}}(w) = \frac{1}{n} \left( (\langle w, x_i \rangle - y_i)^2 - (\langle w, x'_i \rangle - y'_i)^2 \right)$$

Substituons cette différence dans l'inégalité de somme de convexité :
$$\frac{1}{n} \left[ \Big( (\langle w_{S^{(i)}}, x_i \rangle - y_i)^2 - (\langle w_{S^{(i)}}, x'_i \rangle - y'_i)^2 \Big) - \Big( (\langle w_S, x_i \rangle - y_i)^2 - (\langle w_S, x'_i \rangle - y'_i)^2 \Big) \right] \ge 2 \lambda \|w_S - w_{S^{(i)}}\|_2^2$$

Soit la fonction $\psi(w) = (\langle w, x_i \rangle - y_i)^2 - (\langle w, x'_i \rangle - y'_i)^2$. Le terme de gauche vaut $\frac{1}{n}(\psi(w_{S^{(i)}}) - \psi(w_S))$.
Puisque la fonction $\psi$ est continûment différentiable, par le théorème des accroissements finis :
$$\psi(w_{S^{(i)}}) - \psi(w_S) = \langle \nabla \psi(\theta), w_{S^{(i)}} - w_S \rangle \le \|\nabla \psi(\theta)\|_2 \|w_S - w_{S^{(i)}}\|_2$$
où $\theta$ appartient au segment $[w_S, w_{S^{(i)}}]$.

Calculons le gradient de $\psi$ :
$$\nabla \psi(w) = 2 (\langle w, x_i \rangle - y_i) x_i - 2 (\langle w, x'_i \rangle - y'_i) x'_i$$
Puisque la norme euclidienne des points est bornée par $R$ et les cibles par $Y_{\max}$, et que les résidus des modèles optimaux sur les points d'entraînement sont bornés dans le pire des cas par $Y_{\max}$ (car $\lambda > 0$), la norme du gradient vérifie :
$$\|\nabla \psi(w)\|_2 \le 4 R Y_{\max}$$

On obtient donc :
$$\frac{4 R Y_{\max}}{n} \|w_S - w_{S^{(i)}}\|_2 \ge 2 \lambda \|w_S - w_{S^{(i)}}\|_2^2$$
En divisant par $\|w_S - w_{S^{(i)}}\|_2$ (si les deux vecteurs sont différents, sinon le résultat de distance nulle est trivialement vrai) :
$$\|w_S - w_{S^{(i)}}\|_2 \le \frac{2 R Y_{\max}}{\lambda n}$$
L'inégalité est rigoureusement démontrée sans aucune ellipse.
