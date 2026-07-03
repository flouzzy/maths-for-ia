---
uuid: "exo-11-06"
title: "Exercice 6: Théorème d'interpolation de Lagrange vu par la dualité"
---
# Exercice 6: Théorème d'interpolation de Lagrange vu par la dualité (Difficulté $\star \star \star \star$)

## Énoncé
Soit $E = \mathbb{R}_{n-1}[X]$. Soient $x_1, \dots, x_n$ des nombres réels deux à deux distincts. On définit les formes linéaires d'évaluation $\phi_i : P \mapsto P(x_i)$ pour $i \in \{1, \dots, n\}$. Démontrer que la famille $(\phi_1, \dots, \phi_n)$ est une base de l'espace dual $E^*$.

## Correction détaillée

1. **Dimension de l'espace de travail :**
   L'espace $E = \mathbb{R}_{n-1}[X]$ est l'espace des polynômes de degré strictement inférieur à $n$. Sa dimension canonique est $n$.
   Son dual $E^*$ est par conséquent de dimension $n$.
   La famille de formes $(\phi_1, \dots, \phi_n)$ possède $n$ éléments. Pour prouver qu'il s'agit d'une base, il est suffisant et nécessaire de démontrer que la famille est libre.

2. **Démonstration de la liberté de la famille de formes :**
   Soient $\lambda_1, \dots, \lambda_n \in \mathbb{R}$ tels que la combinaison linéaire des formes s'annule :
   $$\sum_{i=1}^n \lambda_i \phi_i = 0_{E^*}$$
   Cette relation stipule que l'application combinée renvoie zéro pour *tout* polynôme de $E$. Soit pour tout $P \in \mathbb{R}_{n-1}[X]$ :
   $$\sum_{i=1}^n \lambda_i P(x_i) = 0$$

3. **Utilisation des polynômes de Lagrange comme "fonctions test" :**
   Pour démontrer que chaque scalaire $\lambda_k$ est nul, nous devons trouver un polynôme qui isole l'évaluation $x_k$ et annule toutes les autres. C'est l'essence des polynômes de Lagrange.
   Pour un indice $k$ fixé, construisons le polynôme $L_k \in \mathbb{R}_{n-1}[X]$ :
   $$L_k(X) = \prod_{\substack{j=1 \\ j \neq k}}^n \frac{X - x_j}{x_k - x_j}$$
   Le degré de $L_k$ est exactement $n-1$, il appartient donc bien à l'espace primal $E$.
   Ses propriétés d'évaluation sont par construction :
   - $L_k(x_k) = 1$
   - $L_k(x_j) = 0$ pour tout $j \neq k$.

4. **Évaluation de l'identité duale :**
   Appliquons la relation d'annulation sur le polynôme $L_k$ :
   $$\sum_{i=1}^n \lambda_i L_k(x_i) = 0$$
   Par la propriété d'annulation des points distincts, seul le terme d'indice $k$ survit dans la somme :
   $$\lambda_k L_k(x_k) = 0$$
   $$\lambda_k \times 1 = 0 \implies \lambda_k = 0$$
   Ce raisonnement étant symétriquement valide pour tout $k \in \{1, \dots, n\}$, nous déduisons que tous les coefficients $\lambda_i$ sont nuls.

**Conclusion :**
La famille $(\phi_1, \dots, \phi_n)$ est formellement libre de cardinal égal à la dimension de l'espace. Elle constitue la base duale associée à la base primale des polynômes de Lagrange $(L_1, \dots, L_n)$.
