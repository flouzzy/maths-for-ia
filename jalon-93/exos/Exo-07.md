# Exercice 07 : Mélange de lois (Mixture Models)
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire. On lance une pièce équilibrée. Si elle tombe sur Pile, $X$ suit une loi Normale $\mathcal{N}(\mu_1, \sigma_1^2)$. Si elle tombe sur Face, $X$ suit une loi Normale $\mathcal{N}(\mu_2, \sigma_2^2)$.
Déterminer la fonction caractéristique de $X$. $X$ est-elle une somme de deux variables gaussiennes indépendantes ?

**Correction pas à pas :**
1. Modélisons l'expérience avec une variable de Bernoulli $B$ (valant 1 pour Pile avec $P=1/2$, 0 pour Face avec $P=1/2$).
   On a $X = B Y_1 + (1-B) Y_2$ avec $Y_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ et $Y_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$.
2. Par le théorème de l'espérance totale en conditionnant par $B$ :
   $\phi_X(t) = \mathbb{E}[e^{itX}] = \mathbb{E}[e^{itX} | B=1] P(B=1) + \mathbb{E}[e^{itX} | B=0] P(B=0)$.
3. Si $B=1$, $X = Y_1$, donc $\mathbb{E}[e^{itX} | B=1] = \mathbb{E}[e^{itY_1}] = e^{it\mu_1 - \frac{1}{2}\sigma_1^2 t^2}$.
   Si $B=0$, $X = Y_2$, donc $\mathbb{E}[e^{itX} | B=0] = \mathbb{E}[e^{itY_2}] = e^{it\mu_2 - \frac{1}{2}\sigma_2^2 t^2}$.
4. Ainsi, $\phi_X(t) = \frac{1}{2} e^{it\mu_1 - \frac{1}{2}\sigma_1^2 t^2} + \frac{1}{2} e^{it\mu_2 - \frac{1}{2}\sigma_2^2 t^2}$.
5. C'est une combinaison linéaire (un mélange convexe) de deux fonctions caractéristiques. Ce n'est **pas** le produit !
   Si $X$ était la somme de deux variables indépendantes, sa fonction caractéristique serait le produit des deux exponentielles, c'est-à-dire une autre loi normale (l'exposant total étant quadratique en $t$).
   Ici, c'est une somme de termes exponentiels, ce qui ne donne pas une expression du type $e^{\text{quadratique}}$. La distribution de $X$ (un mélange gaussien) est souvent bimodale et très différente d'une seule Gaussienne.
