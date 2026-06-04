# Exercice 3 : Stabilité d'un Algorithme à Décision Constante (★★☆☆☆)

## Énoncé
Soit $A_0$ un algorithme d'apprentissage "trivial" qui associe à tout échantillon $S$ la fonction constante nulle :
$$f_S(x) = 0 \quad \forall x \in \mathcal{X}$$
On suppose que la fonction de perte $\ell$ est de la forme $\ell(f, (x, y)) = \phi(f(x), y)$ où $\phi$ est une fonction mesurable quelconque.
1. Calculer la constante de stabilité uniforme $\beta$ de cet algorithme $A_0$.
2. En utilisant le Théorème de Bousquet-Elisseeff, donner la borne de généralisation associée à ce modèle pour un risque empirique pénalisé et commenter ce résultat.

---

## Correction Détaillée

### 1. Calcul de la stabilité uniforme de $A_0$
Par définition de l'algorithme $A_0$ :
$$A_0(S) = f_S = 0 \quad \text{et} \quad A_0(S^{(i)}) = f_{S^{(i)}} = 0$$
pour tout échantillon $S$, pour tout indice de perturbation $i$ et pour toute modification.

Calculons la différence de perte pour tout point de test $z = (x, y) \in \mathcal{Z}$ :
$$\big| \ell(A_0(S), z) - \ell(A_0(S^{(i)}), z) \big| = \big| \ell(0, z) - \ell(0, z) \big| = | \phi(0, y) - \phi(0, y) | = 0$$

Comme cette différence est identiquement nulle pour tous les choix possibles d'échantillons, de perturbations et d'observations :
$$\beta = \sup_{S, i, Z'_i} \sup_{z} \big| \ell(A_0(S), z) - \ell(A_0(S^{(i)}), z) \big| = 0$$
L'algorithme $A_0$ possède une constante de stabilité uniforme $\beta = 0$ (stabilité parfaite).

### 2. Borne de généralisation et commentaire
Supposons que la perte $\phi(0, y)$ soit bornée par $M > 0$.
Puisque $\beta = 0$, la borne de généralisation de Bousquet-Elisseeff s'écrit pour tout $\delta \in (0, 1)$ avec probabilité d'au moins $1 - \delta$ :
$$R(0) \le R_n(0) + 2(0) + (4n(0) + M) \sqrt{\frac{\ln(1/\delta)}{2n}} = R_n(0) + M \sqrt{\frac{\ln(1/\delta)}{2n}}$$

#### Commentaire :
Ce résultat montre que pour un modèle constant, l'erreur de généralisation converge très proprement vers l'erreur empirique à la vitesse $\mathcal{O}(1/\sqrt{n})$. C'est parfaitement logique : un modèle constant n'apprend rien à partir des données $S$, il n'y a donc aucun risque de sur-apprentissage (overfitting). La différence entre sa performance sur l'échantillon d'entraînement et sa performance sur de nouvelles données provient uniquement de la fluctuation statistique naturelle de l'échantillon, contrôlée par la vitesse classique de la loi des grands nombres et de l'inégalité de Hoeffding.
