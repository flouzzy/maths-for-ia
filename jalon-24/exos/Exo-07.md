---
title: "Exercice 7 : Optimisation par Descente de Gradient"
difficulty: ★★★★☆
---
# Énoncé
Au lieu de l'inversion matricielle, on utilise la descente de gradient : $\mathbf{a}^{(t+1)} = \mathbf{a}^{(t)} - \eta \nabla \mathcal{L}(\mathbf{a}^{(t)})$.
Déterminer la condition stricte sur le pas d'apprentissage $\eta$ pour garantir la convergence globale de cet algorithme.

# Correction Détaillée
1. **Expression de la récurrence :**
   Le gradient est $\nabla \mathcal{L}(\mathbf{a}) = 2(\mathbf{X}^\top\mathbf{X}\mathbf{a} - \mathbf{X}^\top\mathbf{y})$.
   Donc $\mathbf{a}^{(t+1)} = \mathbf{a}^{(t)} - 2\eta (\mathbf{X}^\top\mathbf{X}\mathbf{a}^{(t)} - \mathbf{X}^\top\mathbf{y})$.
   $\mathbf{a}^{(t+1)} = (\mathbf{I} - 2\eta \mathbf{X}^\top\mathbf{X})\mathbf{a}^{(t)} + 2\eta\mathbf{X}^\top\mathbf{y}$.

2. **Dynamique de l'erreur :**
   Soit $\mathbf{a}^*$ le point fixe tel que $\mathbf{X}^\top\mathbf{X}\mathbf{a}^* = \mathbf{X}^\top\mathbf{y}$.
   Soustraire $\mathbf{a}^*$ des deux côtés :
   $\mathbf{a}^{(t+1)} - \mathbf{a}^* = (\mathbf{I} - 2\eta \mathbf{X}^\top\mathbf{X})(\mathbf{a}^{(t)} - \mathbf{a}^*)$.
   L'erreur à l'itération $t$ est donc multipliée par la matrice $\mathbf{I} - 2\eta \mathbf{X}^\top\mathbf{X}$.

3. **Condition de convergence :**
   Pour que $\lim_{t \to \infty} \mathbf{a}^{(t)} = \mathbf{a}^*$, il faut et il suffit que le rayon spectral de la matrice d'itération soit strictement inférieur à 1 : $\rho(\mathbf{I} - 2\eta \mathbf{X}^\top\mathbf{X}) < 1$.
   Soient $\lambda_i$ les valeurs propres de $\mathbf{X}^\top\mathbf{X}$. Comme elle est définie positive, $0 < \lambda_{\min} \le \dots \le \lambda_{\max}$.
   Les valeurs propres de la matrice d'itération sont $1 - 2\eta \lambda_i$.
   La condition $|1 - 2\eta \lambda_i| < 1$ pour tout $i$ équivaut à :
   $-1 < 1 - 2\eta \lambda_{\max} \implies 2\eta \lambda_{\max} < 2 \implies \eta < \frac{1}{\lambda_{\max}}$.
   De plus, $\eta > 0$.
   La condition stricte est donc $0 < \eta < \frac{1}{\lambda_{\max}}$, où $\lambda_{\max}$ est la plus grande valeur singulière de $\mathbf{X}$ au carré (la constante de Lipschitz du gradient).
