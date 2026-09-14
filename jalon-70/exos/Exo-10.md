## Exercice 10 : Mesure de Dirac produit \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $a \in X_1$ et $b \in X_2$. Soit $\delta_a$ la mesure de Dirac en $a$ sur $(X_1, \mathcal{F}_1)$ et $\delta_b$ la mesure de Dirac en $b$ sur $(X_2, \mathcal{F}_2)$.
Montrer que $\delta_a \otimes \delta_b = \delta_{(a,b)}$ où $\delta_{(a,b)}$ est la mesure de Dirac au point $(a,b)$ sur l'espace produit.

**Correction :**
1. Soit un rectangle mesurable $A_1 \times A_2$.
2. Par définition de la mesure produit :
   $(\delta_a \otimes \delta_b)(A_1 \times A_2) = \delta_a(A_1) \cdot \delta_b(A_2)$.
3. Calculons le membre de droite :
   - Si $a \in A_1$ et $b \in A_2$, alors $\delta_a(A_1) = 1$ et $\delta_b(A_2) = 1$. Le produit vaut 1.
   - Sinon, l'un des deux (ou les deux) vaut 0. Le produit vaut 0.
4. Or, $a \in A_1$ et $b \in A_2$ est exactement équivalent à $(a,b) \in A_1 \times A_2$.
5. Donc la mesure du rectangle vaut 1 si $(a,b)$ appartient au rectangle, et 0 sinon.
6. C'est exactement la définition de la mesure de Dirac en $(a,b)$, notée $\delta_{(a,b)}$.
7. Par unicité de l'extension de la mesure produit (les mesures étant trivialement $\sigma$-finies car finies), l'égalité $\delta_a \otimes \delta_b = \delta_{(a,b)}$ est vraie sur toute la tribu produit.
