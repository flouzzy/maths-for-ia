# Exercice 1 : Stabilité Empirique vs Stabilité Uniforme (★☆☆☆☆)

## Énoncé
Soit $A$ un algorithme d'apprentissage et $\ell$ une fonction de perte.
On rappelle qu'un algorithme est $\beta$-uniformément stable si :
$$\sup_{S \in \mathcal{Z}^n, i \in \{1,\dots,n\}, Z'_i \in \mathcal{Z}} \sup_{z \in \mathcal{Z}} \big| \ell(A(S), z) - \ell(A(S^{(i)}), z) \big| \le \beta$$
On définit une notion plus faible, la **stabilité empirique moyenne** $\beta_{\text{emp}}$, par :
$$\beta_{\text{emp}} = \mathbb{E}_S \left[ \frac{1}{n} \sum_{i=1}^n \big| \ell(A(S), Z_i) - \ell(A(S^{(i)}), Z_i) \big| \right]$$
1. Démontrer que si $A$ est $\beta$-uniformément stable, alors la stabilité empirique moyenne vérifie $\beta_{\text{emp}} \le \beta$.
2. Expliquer intuitivement pourquoi la stabilité empirique moyenne est plus facile à satisfaire que la stabilité uniforme.

---

## Correction Détaillée

### 1. Preuve de la majoration $\beta_{\text{emp}} \le \beta$
Supposons que l'algorithme $A$ soit $\beta$-uniformément stable. Par définition, pour tout échantillon $S \in \mathcal{Z}^n$, pour tout indice de perturbation $i \in \{1, \dots, n\}$ et pour tout point d'observation $z \in \mathcal{Z}$ :
$$\big| \ell(A(S), z) - \ell(A(S^{(i)}), z) \big| \le \beta$$

Puisque cette inégalité est vraie pour tout $z \in \mathcal{Z}$, elle est en particulier vraie lorsque le point de test est l'un des points d'entraînement $Z_i$ de l'échantillon $S$ (c'est-à-dire $z = Z_i$). On a donc :
$$\big| \ell(A(S), Z_i) - \ell(A(S^{(i)}), Z_i) \big| \le \beta \quad \text{presque sûrement.}$$

Faisons la moyenne empirique de ces termes sur les $n$ indices de l'échantillon :
$$\frac{1}{n} \sum_{i=1}^n \big| \ell(A(S), Z_i) - \ell(A(S^{(i)}), Z_i) \big| \le \frac{1}{n} \sum_{i=1}^n \beta = \beta \quad \text{presque sûrement.}$$

En prenant l'espérance par rapport au tirage de l'échantillon $S$ :
$$\mathbb{E}_S \left[ \frac{1}{n} \sum_{i=1}^n \big| \ell(A(S), Z_i) - \ell(A(S^{(i)}), Z_i) \big| \right] \le \mathbb{E}_S[\beta] = \beta$$
Par conséquent, on a bien :
$$\beta_{\text{emp}} \le \beta$$

### 2. Discussion intuitive
La stabilité uniforme exige que la modification d'un point d'entraînement n'affecte presque pas la perte du modèle sur **n'importe quel** point de test $z$ de l'espace (supremum sur $\mathcal{Z}$). C'est une contrainte globale et très forte.
La stabilité empirique moyenne, elle, ne regarde que la variation de la perte sur les points d'entraînement de l'échantillon eux-mêmes, moyennée sur les $n$ points et en moyenne sur les échantillons. Elle tolère que le modèle subisse de grandes variations locales sur certaines régions de l'espace de test, pourvu que ces variations n'affectent pas trop les prédictions sur les points d'entraînement en moyenne. C'est pourquoi elle est mathématiquement plus faible et plus facile à satisfaire.
