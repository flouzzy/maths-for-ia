---
uuid: "exo-11-05"
title: "Exercice 5: Orthogonal d'un hyperplan"
---
# Exercice 5: Orthogonal d'un hyperplan (Difficulté $\star \star \star$)

## Énoncé
Soit $E$ un espace vectoriel sur $\mathbb{K}$ de dimension $n$. Soit $H$ un hyperplan de $E$, et $\phi \in E^*$ une forme linéaire non nulle telle que $H = \ker \phi$. Démontrer que l'orthogonal de $H$ dans le dual, noté $H^\perp$, est la droite vectorielle engendrée par $\phi$, c'est-à-dire $H^\perp = \text{Vect}(\phi)$.

## Correction détaillée

1. **Preuve de l'inclusion $\text{Vect}(\phi) \subseteq H^\perp$ :**
   Soit $\psi \in \text{Vect}(\phi)$. Il existe un scalaire $\lambda \in \mathbb{K}$ tel que $\psi = \lambda \phi$.
   Pour démontrer que $\psi \in H^\perp$, il faut vérifier que $\psi$ annule tout vecteur de $H$.
   Soit $x \in H$. Puisque $H = \ker \phi$, nous savons que $\phi(x) = 0$.
   Évaluons $\psi(x)$ :
   $$\psi(x) = (\lambda \phi)(x) = \lambda \phi(x) = \lambda \times 0 = 0$$
   L'application $\psi$ s'annule sur tout $H$, donc formellement $\psi \in H^\perp$.
   Cette première inclusion est validée.

2. **Évaluation de la dimension par l'isomorphisme canonique :**
   Nous savons, d'après les propriétés fondamentales des orthogonaux en dimension finie, que :
   $$\dim(H) + \dim(H^\perp) = \dim(E)$$
   Puisque $H$ est un hyperplan par hypothèse, le théorème de dimension stipule que $\dim(H) = n - 1$.
   En substituant :
   $$(n - 1) + \dim(H^\perp) = n$$
   D'où $\dim(H^\perp) = 1$.

3. **Conclusion par argument de dimension :**
   Nous avons établi que $\text{Vect}(\phi)$ est un sous-espace inclus dans $H^\perp$.
   De plus, comme $\phi \neq 0_{E^*}$, la droite $\text{Vect}(\phi)$ possède une dimension égale à 1.
   Puisque $\dim(H^\perp) = 1$, l'inclusion d'un sous-espace de dimension 1 dans un espace de dimension 1 implique l'égalité stricte des ensembles.

**Conclusion :**
Nous avons $H^\perp = \text{Vect}(\phi)$. L'espace des formes annihilant un hyperplan est structurellement unidimensionnel, engendré par l'équation même de l'hyperplan.
