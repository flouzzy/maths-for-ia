# Exercice 8 : Mesure image et changement de variable
$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $(Y, \mathcal{B})$ un espace mesurable.
Soit $\phi : X \to Y$ une application mesurable (i.e. $\forall B \in \mathcal{B}, \phi^{-1}(B) \in \mathcal{A}$).
On définit la mesure image $\nu$ sur $Y$ par $\nu(B) = \mu(\phi^{-1}(B))$ pour tout $B \in \mathcal{B}$.
Soit $f : Y \to \mathbb{R}_+$ une fonction étagée positive.
Montrer que $\int_Y f \, d\nu = \int_X (f \circ \phi) \, d\mu$.

**Correction :**
1. La fonction $f$ étant étagée sur $Y$, écrivons sa forme canonique :
   $$f = \sum_{i=1}^k a_i \mathbf{1}_{B_i}$$
   où les $B_i \in \mathcal{B}$ forment une partition de $Y$, et $a_i \ge 0$.
2. Évaluons l'intégrale de $f$ par rapport à la mesure $\nu$ sur l'espace $Y$ :
   $$\int_Y f \, d\nu = \sum_{i=1}^k a_i \nu(B_i)$$
3. Utilisons la définition de la mesure image $\nu(B_i) = \mu(\phi^{-1}(B_i))$ :
   $$\int_Y f \, d\nu = \sum_{i=1}^k a_i \mu(\phi^{-1}(B_i))$$
4. D'un autre côté, considérons la fonction composée $g = f \circ \phi$ sur l'espace $X$.
   Quel est le comportement de $g$ sur $X$ ?
   Pour $x \in X$, $g(x) = f(\phi(x))$.
   Si $\phi(x) \in B_i$, alors $f(\phi(x)) = a_i$. La condition $\phi(x) \in B_i$ est exactement $x \in \phi^{-1}(B_i)$.
   Donc, $g(x) = a_i$ si $x \in \phi^{-1}(B_i)$.
5. Nous pouvons réécrire $g$ comme une combinaison d'indicatrices sur $X$ :
   $$g = \sum_{i=1}^k a_i \mathbf{1}_{\phi^{-1}(B_i)}$$
6. La fonction $g$ est étagée (elle ne prend que les valeurs $a_i$) et les ensembles $A_i = \phi^{-1}(B_i)$ sont mesurables car $\phi$ est mesurable. De plus, comme les $B_i$ sont disjoints, les préimages $\phi^{-1}(B_i)$ sont disjointes.
   L'intégrale de $g$ par rapport à $\mu$ est :
   $$\int_X g \, d\mu = \sum_{i=1}^k a_i \mu(\phi^{-1}(B_i))$$
7. En comparant l'étape 3 et l'étape 6, nous avons bien l'égalité :
   $$\int_Y f \, d\nu = \int_X (f \circ \phi) \, d\mu$$
   *Ce résultat fondamental, prouvé ici pour les étagées, s'étendra par passage au supremum à toute fonction mesurable positive (formule de transfert).*
