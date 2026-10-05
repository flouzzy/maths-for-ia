# Exercice 9 : Multiplication par une fonction lisse

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Montrer que si $T \in \mathcal{D}'(\mathbb{R})$ et $\alpha \in \mathcal{C}^\infty(\mathbb{R})$, alors on peut définir le produit $\alpha T$ comme une distribution par : $\langle \alpha T, \phi \rangle = \langle T, \alpha \phi \rangle$.
Calculer ensuite $x \delta_0$.

**Correction Détaillée :**
1. **Légitimité de la définition :**
   Si $\phi \in \mathcal{D}(\mathbb{R})$, son support est compact. La fonction $\alpha \phi$ est le produit de deux fonctions indéfiniment dérivables, donc elle l'est aussi. Son support est inclus dans celui de $\phi$, donc compact.
   Ainsi, $\alpha \phi \in \mathcal{D}(\mathbb{R})$. L'évaluation $\langle T, \alpha \phi \rangle$ a bien un sens.
2. **Vérification de la continuité :**
   La linéarité de l'application $\phi \mapsto \langle T, \alpha \phi \rangle$ est évidente.
   Si $\phi_n \to 0$ dans $\mathcal{D}(\mathbb{R})$, tous les supports sont inclus dans un même compact $K$.
   Les dérivées de $\alpha \phi_n$ se calculent par la formule de Leibniz. Sur $K$, $\alpha$ et ses dérivées sont bornées.
   On peut déduire que la convergence uniforme de toutes les dérivées de $\phi_n$ vers 0 entraîne celle de toutes les dérivées de $\alpha \phi_n$.
   Ainsi, $\alpha \phi_n \to 0$ dans $\mathcal{D}(\mathbb{R})$, ce qui donne par continuité de $T$ : $\langle T, \alpha \phi_n \rangle \to 0$. $\alpha T$ est bien une distribution.
3. **Calcul de $x \delta_0$ :**
   Posons $\alpha(x) = x$.
   $\langle x \delta_0, \phi \rangle = \langle \delta_0, x \mapsto x\phi(x) \rangle = 0 \cdot \phi(0) = 0$.
   Donc $x \delta_0 = 0$ (la distribution nulle).
