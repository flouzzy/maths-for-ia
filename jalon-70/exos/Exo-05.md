## Exercice 5 : Indépendance et Produit de probabilités \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires réelles. Leur loi jointe $P_{(X,Y)}$ est une probabilité sur $(\mathbb{R}^2, \mathcal{B}(\mathbb{R}^2))$.
Montrer que si $P_{(X,Y)} = P_X \otimes P_Y$, alors $P(X \in A, Y \in B) = P(X \in A)P(Y \in B)$ pour tous boréliens $A$ et $B$.

**Correction :**
1. L'événement $\{X \in A, Y \in B\}$ correspond formellement à $(X, Y) \in A \times B$.
2. La probabilité de cet événement est $P_{(X,Y)}(A \times B)$.
3. Par hypothèse, $P_{(X,Y)}$ est la mesure produit de $P_X$ et $P_Y$.
4. Par définition de la mesure produit sur un rectangle mesurable :
   $P_X \otimes P_Y(A \times B) = P_X(A) \cdot P_Y(B)$.
5. Or, par définition des lois marginales, $P_X(A) = P(X \in A)$ et $P_Y(B) = P(Y \in B)$.
6. D'où le résultat : $P(X \in A, Y \in B) = P(X \in A)P(Y \in B)$.
