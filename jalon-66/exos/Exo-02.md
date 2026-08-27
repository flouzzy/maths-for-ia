## Exercice 2 : Indicatrice d'un ensemble mesurable \quad $$\bigstar\bigstar$$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $A \in \mathcal{F}$.
Calculer $\int_X \mathbf{1}_A \, d\mu$.

**Correction :**
1. La fonction $f = \mathbf{1}_A$ ne prend que les valeurs 0 et 1 sur des ensembles mesurables ($A$ et $A^c$).
2. Elle est donc, par définition, une fonction étagée, $f \in \mathcal{E}_+$.
3. Son écriture canonique (si $A \neq X$ et $A \neq \emptyset$) est : $f = 1 \cdot \mathbf{1}_A + 0 \cdot \mathbf{1}_{A^c}$.
4. Son intégrale en tant que fonction étagée est : $\int_X f \, d\mu = 1 \cdot \mu(A) + 0 \cdot \mu(A^c) = \mu(A)$.
5. Par définition de l'intégrale de Lebesgue pour les fonctions positives (qui coïncide avec l'intégrale pour les fonctions étagées lorsque $f \in \mathcal{E}_+$) :
   $$\int_X \mathbf{1}_A \, d\mu = \mu(A)$$
