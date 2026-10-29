# Exercice 10 : Résolution d'une équation intégrale
Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Trouver toutes les densités de probabilité $f$ sur $\mathbb{R}$ telles que :
$f * f = f$
où $*$ désigne le produit de convolution.

**Correction pas à pas :**
1. Soit $X$ et $Y$ deux variables aléatoires indépendantes admettant $f$ pour densité.
   La densité de la somme $X+Y$ est donnée par la convolution $f * f$.
2. L'équation $f * f = f$ signifie que $X+Y$ a la même loi que $X$ (et $Y$).
3. Passons dans le domaine de Fourier, c'est-à-dire appliquons la fonction caractéristique.
   Si $Z = X+Y$, alors $\phi_{X+Y}(t) = \phi_X(t) \phi_Y(t) = (\phi_X(t))^2$.
   Puisque $Z$ a la même loi que $X$, on a $\phi_{X+Y}(t) = \phi_X(t)$.
4. On obtient donc l'équation algébrique pour tout $t \in \mathbb{R}$ :
   $(\phi_X(t))^2 = \phi_X(t) \iff \phi_X(t)(\phi_X(t) - 1) = 0$.
5. Pour chaque $t$, $\phi_X(t)$ ne peut prendre que les valeurs $0$ ou $1$.
6. Or, par le théorème de régularité, la fonction caractéristique est une fonction uniformément **continue** sur $\mathbb{R}$.
   Une fonction continue à valeurs dans $\{0, 1\}$ est nécessairement constante sur un intervalle connexe comme $\mathbb{R}$.
7. De plus, la condition de normalisation impose $\phi_X(0) = 1$.
   Par continuité, il s'ensuit que $\phi_X(t) = 1$ pour tout $t \in \mathbb{R}$.
8. À quelle loi de probabilité correspond la fonction caractéristique constante égale à 1 ?
   C'est la loi de Dirac en 0, notée $\delta_0$ (en effet, $\mathbb{E}[e^{it \cdot 0}] = 1$).
9. Cependant, la mesure de Dirac ne possède **pas** de densité par rapport à la mesure de Lebesgue.
   Par conséquent, dans l'espace des fonctions intégrables (densités), l'équation $f * f = f$ n'admet **aucune solution**.
   L'unique solution est une distribution (mesure singulière), la masse de Dirac.
