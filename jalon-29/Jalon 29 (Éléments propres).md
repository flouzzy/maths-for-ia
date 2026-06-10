---
uuid: "jalon-29"
title: "Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/reduction-endomorphismes
prev: "[[Jalon 28 (Polynômes d'endomorphismes).md]]"
next: "[[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.).md]]"
---

# Jalon 29 : Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous transformez une image (par exemple en la tournant ou en l'étirant). La plupart des points vont bouger et changer de direction. Mais il existe parfois des vecteurs (des flèches) qui, même après la transformation, restent sur la **même ligne** qu'au départ. Ils ont seulement été étirés ou rétrécis. Ces vecteurs sont les "vecteurs propres". Le facteur par lequel ils ont été étirés est la "valeur propre".
- **Le "Pourquoi on a inventé ça" :** Diagonaliser, c'est trouver une base dans laquelle une transformation complexe devient une simple mise à l'échelle sur chaque axe. C'est le moyen le plus simple possible pour "voir" ce que fait une matrice.
- **Visualisation :** Une rotation tourne tout. Un étirement garde les axes stables : ce sont les vecteurs propres.

## 2. Formalisation
### A. Définitions
1. **Vecteur propre :** $v \neq 0$ tel que $f(v) = \lambda v$. $\lambda$ est la valeur propre.
2. **Sous-espace propre :** $E_\lambda(f) = \ker(f - \lambda Id)$.
3. **Polynôme caractéristique :** $\chi_f(X) = \det(X \cdot Id - f)$.

### B. Théorèmes
> **Critère de Diagonalisabilité :**
> $f$ est diagonalisable $\iff \chi_f$ est scindé ET $\forall \lambda, \dim(E_\lambda) = \text{ordre de multiplicité de } \lambda$.

## 3. Démonstrations
### Démonstration : Familles de vecteurs propres de valeurs propres distinctes sont libres
Soient $\lambda_1, ..., \lambda_k$ des valeurs propres distinctes et $v_1, ..., v_k$ des vecteurs propres associés.
1. **Récurrence :** Pour $k=1$, $\{v_1\}$ est libre car $v_1 \neq 0$.
2. **Hérédité :** Supposons la famille libre jusqu'à $k$. Soit $\sum_{i=1}^{k+1} \alpha_i v_i = 0$.
3. **Calcul :** $f(\sum_{i=1}^{k+1} \alpha_i v_i) = \sum_{i=1}^{k+1} \alpha_i \lambda_i v_i = 0$.
4. **Combinaison :** Soustraire $\lambda_{k+1}$ fois la somme initiale : $\sum_{i=1}^k \alpha_i (\lambda_i - \lambda_{k+1}) v_i = 0$.
5. **Conclusion :** Par hypothèse de récurrence, les $\alpha_i (\lambda_i - \lambda_{k+1}) = 0$. Comme $\lambda_i \neq \lambda_{k+1}$, alors $\alpha_i = 0$. La famille est libre.

## 4. Exercices d'Application
### Exercice 1 : Diagonalisation
$A = \begin{pmatrix} 1 & 1 \ 0 & 2 \end{pmatrix}$. $\chi_A = (X-1)(X-2)$. Valeurs propres 1 et 2. Diagonalisable.

## 5. Ancrage & Application en IA
*   **PCA** cherche les vecteurs propres de la matrice de covariance. Ce sont les "axes" principaux des données.

## 6. Liens Obsidian
- [[Jalon 28 (Polynômes d'endomorphismes).md]], [[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.).md]]
