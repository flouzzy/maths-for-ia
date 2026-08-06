# Exercice 5 : Produit de Hadamard et Jacobienne d'activation
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé
L'application d'activation est $a = \sigma(z)$, opérant élément par élément sur le vecteur $z \in \mathbb{R}^n$. Montrer que la multiplication par la Jacobienne de cette transformation se réduit à un produit de Hadamard (terme à terme).

## Correction détaillée
1. On a le vecteur $a = (a_1, a_2, \dots, a_n)^T$ avec $a_i = \sigma(z_i)$.
2. La Jacobienne $J_z(a)$ est de taille $n \times n$. Son coefficient $(i, j)$ est $\frac{\partial a_i}{\partial z_j}$.
3. Puisque $a_i$ ne dépend que de $z_i$, les dérivées croisées sont nulles : $\frac{\partial a_i}{\partial z_j} = 0$ si $i \neq j$.
4. Pour les termes diagonaux ($i = j$), on a $\frac{\partial a_i}{\partial z_i} = \sigma'(z_i)$.
5. La matrice Jacobienne $J_z(a)$ est donc une matrice diagonale : $J_z(a) = \text{diag}(\sigma'(z_1), \dots, \sigma'(z_n))$.
6. Lors de la rétropropagation, on calcule le vecteur $\delta_{in} = J_z(a)^T \delta_{out}$.
7. Multiplier un vecteur $\delta_{out}$ par une matrice diagonale $\text{diag}(v)$ équivaut à multiplier composante par composante le vecteur $v$ et le vecteur $\delta_{out}$.
8. Ainsi, on retrouve la notation du produit de Hadamard : $\delta_{in} = \delta_{out} \odot \sigma'(z)$.
Cette propriété garantit l'efficacité calculatoire de la rétropropagation, évitant une véritable multiplication de matrices pleines.
