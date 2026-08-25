## Exercice 8 : Inégalité de Markov (Cas des fonctions simples) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :** Soit $s \in \mathcal{S}_+$ une fonction simple positive, et $\alpha > 0$. Montrer que $\mu(\{x \in X \mid s(x) \ge \alpha\}) \le \frac{1}{\alpha} \int_X s d\mu$.

**Correction Détaillée :**
1. Posons $A = \{x \in X \mid s(x) \ge \alpha\}$.
2. Considérons la fonction simple $\alpha \cdot \mathbf{1}_A$.
3. Pour tout $x \in X$, on a l'inégalité $s(x) \ge \alpha \cdot \mathbf{1}_A(x)$.
   En effet, si $x \in A$, $s(x) \ge \alpha = \alpha \cdot 1$. Si $x \notin A$, $s(x) \ge 0 = \alpha \cdot 0$.
4. Par monotonie de l'intégrale des fonctions simples :
   $$\int_X s d\mu \ge \int_X \alpha \cdot \mathbf{1}_A d\mu$$
5. Par définition de l'intégrale d'une fonction indicatrice, on a :
   $$\int_X \alpha \cdot \mathbf{1}_A d\mu = \alpha \mu(A)$$
6. En combinant ces inégalités, on obtient :
   $$\int_X s d\mu \ge \alpha \mu(A)$$
7. Puisque $\alpha > 0$, on peut diviser par $\alpha$ pour obtenir :
   $$\mu(A) \le \frac{1}{\alpha} \int_X s d\mu$$
   Ce qui démontre l'inégalité de Markov pour une fonction simple.
