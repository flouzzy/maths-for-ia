---
uuid: "exo-11-10"
title: "Exercice 10: Forme linéaire et hyperplan osculateur (Approche IA)"
---
# Exercice 10: Séparabilité de classes par un hyperplan (Difficulté $\star \star \star \star \star$)

## Énoncé
Dans $E = \mathbb{R}^n$, soient $A$ et $B$ deux ensembles convexes compacts disjoints non vides. Un théorème de séparation stricte garantit l'existence d'une forme linéaire $\phi \in E^*$ et d'un scalaire $\alpha \in \mathbb{R}$ tels que pour tout $a \in A, \phi(a) < \alpha$ et pour tout $b \in B, \phi(b) > \alpha$.
Montrer que l'hyperplan vectoriel $H = \ker \phi$ permet de définir géométriquement deux demi-espaces stricts séparant les ensembles.

## Correction détaillée

1. **Le rôle fondamental de l'hyperplan affine :**
   L'équation de séparation $\phi(x) = \alpha$ définit un sous-espace affine.
   Puisque $\phi$ est une forme linéaire sur $\mathbb{R}^n$, elle s'écrit $\phi(x) = \langle w, x \rangle$ par le théorème de Riesz (produit scalaire). Le vecteur $w$ est le vecteur normal à l'hyperplan.
   L'hyperplan affine séparateur est $H_\alpha = \{ x \in E \mid \phi(x) = \alpha \}$.
   L'hyperplan vectoriel directeur est $H = \ker \phi = \{ x \in E \mid \phi(x) = 0 \}$.

2. **Création des zones de classification (le perceptron) :**
   L'espace $E$ est partitionné par $H_\alpha$ en trois parties disjointes :
   - $H_\alpha$ lui-même.
   - $E^- = \{ x \in E \mid \phi(x) < \alpha \}$ (le demi-espace ouvert inférieur).
   - $E^+ = \{ x \in E \mid \phi(x) > \alpha \}$ (le demi-espace ouvert supérieur).
   L'hypothèse du théorème stipule exactement que l'ensemble compact $A$ est entièrement inclus dans $E^-$, et l'ensemble $B$ est entièrement inclus dans $E^+$.

3. **Caractère topologique strict :**
   Parce que les inégalités sont strictes, la frontière de décision $H_\alpha$ (le séparateur de marge) ne touche ni l'ensemble $A$ ni l'ensemble $B$.
   La distance (la marge) de $H_\alpha$ à $A$ et $B$ est strictement positive en raison de la compacité des ensembles (la forme continue $\phi$ atteint ses bornes sur un compact).

**Conclusion :**
C'est la formalisation mathématique absolue de la capacité d'un neurone artificiel (perceptron) à discriminer linéairement deux clusters de données distincts dans un espace latent.
