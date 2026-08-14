# Approximation de la fonction carré

### Énoncé $\quad \bigstar\star\star\star\star$

Montrer rigoureusement que la classe de fonctions définies par des combinaisons linéaires d'une fonction d'activation sigmoïdale permet d'approcher la fonction $f(x) = x^2$ sur le segment $[-1, 1]$ avec une erreur maximale $\epsilon > 0$. Construisez explicitement l'approximation en utilisant des fonctions indicatrices approchées par des sigmoïdes.

### Démonstration Détaillée

Soit $f(x) = x^2$. Puisque $f$ est uniformément continue sur le compact $[-1, 1]$, on partitionne ce segment en $N$ sous-intervalles de largeur $\delta = 2/N$. Pour un choix adéquat de $N$, l'oscillation de $f$ sur chaque intervalle est bornée par $\epsilon/2$. On approche l'indicatrice de chaque sous-intervalle par la différence de deux sigmoïdes de très grande pente. La somme pondérée par la valeur de $f$ aux centres des sous-intervalles fournit l'approximation désirée à $\epsilon$ près par inégalité triangulaire.
