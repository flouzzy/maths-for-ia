# Exercice 10 : Inégalité de Bienaymé-Chebyshev
$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(\Omega, \mathcal{A}, \mathbb{P})$ un espace de probabilité. Soit $X : \Omega \to \mathbb{R}$ une variable aléatoire mesurable.
On définit son espérance $m = \int_\Omega X \, d\mathbb{P}$ et sa variance $\sigma^2 = \int_\Omega (X - m)^2 \, d\mathbb{P}$ (supposées finies).
En utilisant la construction de l'intégrale de Lebesgue, démontrer rigoureusement l'inégalité de Chebyshev :
Pour tout $\epsilon > 0$, $\mathbb{P}(\{\omega \in \Omega \mid |X(\omega) - m| \ge \epsilon\}) \le \frac{\sigma^2}{\epsilon^2}$.

**Correction :**
1. Posons l'ensemble d'intérêt $A_\epsilon = \{\omega \in \Omega \mid |X(\omega) - m| \ge \epsilon\}$. Cet ensemble est mesurable.
2. Écrivons la variance par définition comme une intégrale de Lebesgue d'une fonction positive $f(\omega) = (X(\omega) - m)^2$ :
   $$\sigma^2 = \int_\Omega (X - m)^2 \, d\mathbb{P}$$
3. L'intégrande est partout positif ou nul : $(X - m)^2 \ge 0$.
   Nous pouvons donc décomposer le domaine d'intégration entre $A_\epsilon$ et son complémentaire $A_\epsilon^c$.
   Par la règle d'additivité (sur les fonctions positives) :
   $$\sigma^2 = \int_{A_\epsilon} (X - m)^2 \, d\mathbb{P} + \int_{A_\epsilon^c} (X - m)^2 \, d\mathbb{P}$$
4. Comme l'intégrale d'une fonction positive sur n'importe quel ensemble est $\ge 0$, on peut minorer :
   $$\sigma^2 \ge \int_{A_\epsilon} (X - m)^2 \, d\mathbb{P} = \int_\Omega (X - m)^2 \mathbf{1}_{A_\epsilon} \, d\mathbb{P}$$
5. Étudions la fonction intégrande sur $A_\epsilon$.
   Par définition de l'ensemble $A_\epsilon$, si $\omega \in A_\epsilon$, on a $|X(\omega) - m| \ge \epsilon$, ce qui implique $(X(\omega) - m)^2 \ge \epsilon^2$.
   Donc pour tout $\omega \in \Omega$, on a l'inégalité point par point :
   $$(X(\omega) - m)^2 \mathbf{1}_{A_\epsilon}(\omega) \ge \epsilon^2 \mathbf{1}_{A_\epsilon}(\omega)$$
6. En appliquant la croissance de l'intégrale de Lebesgue :
   $$\int_\Omega (X - m)^2 \mathbf{1}_{A_\epsilon} \, d\mathbb{P} \ge \int_\Omega \epsilon^2 \mathbf{1}_{A_\epsilon} \, d\mathbb{P}$$
7. L'intégrale du membre de droite concerne une fonction étagée $\epsilon^2 \mathbf{1}_{A_\epsilon}$. Sa valeur est $\epsilon^2 \mathbb{P}(A_\epsilon)$.
8. En combinant les inégalités (étape 4 et étape 7) :
   $$\sigma^2 \ge \epsilon^2 \mathbb{P}(A_\epsilon)$$
9. Puisque $\epsilon > 0$, nous divisons par $\epsilon^2$ :
   $$\mathbb{P}(A_\epsilon) \le \frac{\sigma^2}{\epsilon^2}$$
   La démonstration algébrique est irréprochable et s'appuie fondamentalement sur la positivité et la croissance de l'intégrale de Lebesgue.
