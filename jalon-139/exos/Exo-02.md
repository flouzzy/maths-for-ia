# Exercice 2 : Stabilité en Moyenne vs Stabilité Uniforme (★☆☆☆☆)

## Énoncé
Soit $A$ un algorithme d'apprentissage et $\ell$ une fonction de perte.
On définit la **stabilité en moyenne** (on-average stability) $\beta_{\text{moy}}$ par :
$$\beta_{\text{moy}} = \mathbb{E}_{S, Z'} \left[ \frac{1}{n} \sum_{i=1}^n \big| \ell(A(S), Z') - \ell(A(S^{(i)}), Z') \big| \right]$$
où $Z' \sim \mathcal{D}$ est une variable aléatoire indépendante de $S$.
1. Démontrer que si $A$ est $\beta$-uniformément stable, alors la stabilité en moyenne vérifie $\beta_{\text{moy}} \le \beta$.
2. Donner la différence fondamentale entre la stabilité en moyenne et la stabilité empirique moyenne de l'Exercice 1.

---

## Correction Détaillée

### 1. Preuve de la majoration $\beta_{\text{moy}} \le \beta$
Supposons que l'algorithme $A$ soit $\beta$-uniformément stable. Par définition de la stabilité uniforme, pour tout échantillon $S \in \mathcal{Z}^n$, pour tout $i \in \{1, \dots, n\}$, et pour tout point d'observation $z \in \mathcal{Z}$ :
$$\big| \ell(A(S), z) - \ell(A(S^{(i)}), z) \big| \le \beta$$
Puisque cette inégalité est vraie pour tout $z \in \mathcal{Z}$ de manière déterministe, elle reste vraie pour toute variable aléatoire $Z'$ à valeurs dans $\mathcal{Z}$, presque sûrement :
$$\big| \ell(A(S), Z') - \ell(A(S^{(i)}), Z') \big| \le \beta \quad \text{presque sûrement.}$$

En faisant la moyenne sur les $n$ indices de l'échantillon :
$$\frac{1}{n} \sum_{i=1}^n \big| \ell(A(S), Z') - \ell(A(S^{(i)}), Z') \big| \le \beta \quad \text{presque sûrement.}$$

En prenant l'espérance par rapport au tirage conjoint de $S$ et $Z'$ :
$$\beta_{\text{moy}} = \mathbb{E}_{S, Z'} \left[ \frac{1}{n} \sum_{i=1}^n \big| \ell(A(S), Z') - \ell(A(S^{(i)}), Z') \big| \right] \le \mathbb{E}_{S, Z'}[\beta] = \beta$$
On a donc bien démontré que :
$$\beta_{\text{moy}} \le \beta$$

### 2. Différence fondamentale
- Dans la **stabilité empirique moyenne** ($\beta_{\text{emp}}$), le point sur lequel on teste le modèle perturbé est $Z_i$, qui est précisément le point d'entraînement qui a été **retiré** ou modifié pour obtenir $S^{(i)}$. On mesure donc la sensibilité de l'algorithme sur le point même de la perturbation.
- Dans la **stabilité en moyenne** ($\beta_{\text{moy}}$), le point de test est $Z'$, qui est un point "hors échantillon" (out-of-sample) indépendant, représentant une nouvelle donnée test typique tirée selon la loi de probabilité globale $\mathcal{D}$.
