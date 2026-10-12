# Exercice 07 : Indépendance et variance d'une combinaison linéaire
Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $X_1, X_2, \dots, X_n$ des variables aléatoires deux à deux indépendantes de même variance $\sigma^2$.
Soit $S_n = \sum_{i=1}^n c_i X_i$ où $c_i \in \mathbb{R}$.
Démontrer rigoureusement que $\text{Var}(S_n) = \sigma^2 \sum_{i=1}^n c_i^2$.

**Correction :**
1. On applique la formule de la variance d'une somme finie :
$\text{Var}\left(\sum_{i=1}^n c_i X_i\right) = \sum_{i=1}^n \text{Var}(c_i X_i) + \sum_{1 \leq i \neq j \leq n} \text{Cov}(c_i X_i, c_j X_j)$.
2. Propriétés de la variance et de la covariance :
$\text{Var}(c_i X_i) = c_i^2 \text{Var}(X_i)$.
$\text{Cov}(c_i X_i, c_j X_j) = c_i c_j \text{Cov}(X_i, X_j)$.
3. Les variables sont indépendantes deux à deux, ce qui implique (Théorème 1) que pour $i \neq j$, $X_i$ et $X_j$ sont indépendantes et donc $\text{Cov}(X_i, X_j) = 0$.
4. Le terme de somme double s'annule complètement :
$\text{Var}(S_n) = \sum_{i=1}^n c_i^2 \text{Var}(X_i) + 0$.
5. Puisque par hypothèse $\text{Var}(X_i) = \sigma^2$ pour tout $i$ :
$\text{Var}(S_n) = \sum_{i=1}^n c_i^2 \sigma^2 = \sigma^2 \sum_{i=1}^n c_i^2$.
Cette propriété est fondamentale en statistiques pour évaluer la variance d'un estimateur linéaire.
