# Exercice 6 : Lien avec la classification Multi-Classe

$\bigstar\bigstar\bigstar\star\star$


Dans le cas d'une classification à $K$ classes, l'étiquette réelle d'un échantillon est un vecteur *one-hot* $y \in \{0, 1\}^K$ où exactement une composante vaut 1 (disons $y_c = 1$ pour la classe cible $c$). La prédiction du modèle est un vecteur de probabilités $\hat{y} = (q_1, \dots, q_K)$ tel que $\sum q_k = 1$.

**1.** Réécrire la formule de la Cross-Entropy discrète en fonction de $y$ et $\hat{y}$.
**2.** Simplifier cette expression en utilisant la propriété du vecteur *one-hot*.

**Correction :**

**1.** La vraie distribution pour cet échantillon est empirique et déterministe, donnée par les probabilités $p(k) = y_k$.
Le modèle prédit $q(k) = q_k$.
La formule de l'entropie croisée pour ce point de donnée est :
$$H(y, \hat{y}) = - \sum_{k=1}^K p(k) \ln(q(k)) = - \sum_{k=1}^K y_k \ln(q_k)$$

**2.** Puisque $y$ est un vecteur *one-hot*, $y_c = 1$ et $y_k = 0$ pour tout $k \neq c$.
La somme se réduit à un seul terme non nul :
$$H(y, \hat{y}) = - \ln(q_c)$$
La fonction de perte de la classification multi-classe dépend uniquement du logarithme de la probabilité que le modèle assigne à la bonne classe $c$. Augmenter cette probabilité minimise directement la Cross-Entropy.
