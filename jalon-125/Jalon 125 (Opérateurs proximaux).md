---
uuid: "jalon-125"
title: "Opérateurs proximaux"
year: 3
trimester: 11
tags:
  - math/optimisation
  - ia/fondations
prev: "[[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]]"
next: "[[Jalon 126 (Noyaux définis positifs).md]]"
---

# Jalon 125 : Opérateurs proximaux

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez perdu dans le brouillard sur une montagne (la fonction $f$). Vous voulez descendre, mais vous avez peur de vous égarer trop loin de votre campement actuel (le point $x$).
    - L'**Opérateur Proximal**, c'est comme avoir un guide qui vous propose un compromis : "On va aller vers un point plus bas, mais en restant dans un rayon raisonnable autour du camp".
    - Le guide calcule un score qui mélange deux choses : l'altitude du nouveau point et la distance pour y aller.
    - Ce point de compromis est unique et très stable. Même si la montagne a des crêtes tranchantes (fonctions non-lisses), le guide saura toujours vous proposer un point de chute propre.
- **Le "Pourquoi on a inventé ça" :** La descente de gradient classique échoue sur les fonctions "pointues" (comme la valeur absolue). L'opérateur proximal permet de "lisser" mathématiquement ces pointes pour pouvoir continuer à optimiser sans que l'algorithme ne saute dans tous les sens. C'est le moteur des algorithmes d'IA qui cherchent la simplicité (parcimonie).
- **Visualisation :** On remplace une pointe de "V" par une petite courbe arrondie (enveloppe de Moreau) qui est beaucoup plus facile à descendre.

## 2. Formalisation

Soit $f : \mathbb{R}^n \to \mathbb{R}$ une fonction convexe, propre et inférieurement semi-continue.

### A. Définition de l'opérateur proximal

> **Définition 1 (Opérateur Proximal) :**
> Pour tout $\lambda > 0$, l'opérateur proximal de $f$ est l'application $prox_{\lambda f} : \mathbb{R}^n \to \mathbb{R}^n$ définie par :
> $$prox_{\lambda f}(x) = \text{argmin}_{y \in \mathbb{R}^n} \left\{ f(y) + \frac{1}{2\lambda} \|y - x\|^2 \right\}$$
> Le point $prox_{\lambda f}(x)$ est l'unique point qui réalise le meilleur compromis entre minimiser $f$ et rester proche de $x$.

### B. Propriétés Fondamentales

> **Théorème (Caractérisation) :**
> $p = prox_{\lambda f}(x) \iff x - p \in \lambda \partial f(p)$.
> (Le vecteur reliant $x$ à sa projection proximale est un sous-gradient de $f$ au point $p$).

> **Propriété (Non-expansivité) :**
> L'opérateur proximal est 1-lipschitzien. C'est une application très stable numériquement.

### C. Décomposition de Moreau

> **Théorème :** $x = prox_f(x) + prox_{f^*}(x)$, où $f^*$ est la transformée de Fenchel-Legendre de $f$.

## 3. Démonstrations

### Exemple : Proximal de la valeur absolue (Soft-Thresholding)

Soit $f(x) = |x|$ sur $\mathbb{R}$. Cherchons $p = prox_{\lambda | \cdot |}(x)$.

1. **Objectif :** Minimiser $h(y) = |y| + \frac{1}{2\lambda} (y-x)^2$.
2. **Condition d'optimalité :** $0 \in \partial |p| + \frac{1}{\lambda} (p-x)$, soit $x-p \in \lambda \partial |p|$.
3. **Cas 1 : $p > 0$.** Alors $\partial |p| = \{1\}$.
   $x-p = \lambda \implies p = x-\lambda$. Comme $p > 0$, cela impose $x > \lambda$.
4. **Cas 2 : $p < 0$.** Alors $\partial |p| = \{-1\}$.
   $x-p = -\lambda \implies p = x+\lambda$. Comme $p < 0$, cela impose $x < -\lambda$.
5. **Cas 3 : $p = 0$.** Alors $\partial |p| = [-1, 1]$.
   $x-0 \in \lambda [-1, 1] \implies x \in [-\lambda, \lambda]$.
6. **Conclusion :**
   $$prox_{\lambda | \cdot |}(x) = \begin{cases} x-\lambda & \text{si } x > \lambda \\ 0 & \text{si } |x| \le \lambda \\ x+\lambda & \text{si } x < -\lambda \end{cases} = \text{sgn}(x) \cdot \max(|x|-\lambda, 0)$$
   C'est l'opérateur de **Seuillage Doux** (Soft-thresholding).

## 4. Exercices d'Application

### Exercice 1 : Projection sur un convexe
**Énoncé :** Soit $C$ un ensemble convexe fermé. On définit $f(x) = 0$ si $x \in C$ and $+\infty$ sinon (fonction indicatrice $\iota_C$). Calculer $prox_f(x)$.
**Correction Détaillée :**
$prox_f(x) = \text{argmin}_{y \in C} \{ 0 + \frac{1}{2} \|y-x\|^2 \}$.
C'est exactement la définition de la **Projection orthogonale** sur l'ensemble $C$.
**Résultat :** L'opérateur proximal généralise la notion de projection géométrique.

### Exercice 2 : Niveau Avancé (Algorithme ISTA)
**Énoncé :** Expliquer comment résoudre $\min g(x) + f(x)$ où $g$ est lisse et $f$ est non-lisse (ex: L1).
**Correction Détaillée :**
On utilise l'algorithme de **Gradient Proximal** : $x_{k+1} = prox_{\eta f}(x_k - \eta \nabla g(x_k))$.
On fait un pas de gradient sur la partie lisse, puis on "projette" le résultat via l'opérateur proximal pour gérer la partie pointue. C'est l'algorithme standard pour le Lasso.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Les opérateurs proximaux sont la clé de l'**IA parcimonieuse** (Sparse AI). Ils permettent d'annuler exactement les poids inutiles sans perturber la convergence.
- **Example Concret :**
    - **Apprentissage de dictionnaires :** Pour représenter une image comme une somme de quelques motifs de base, on utilise des opérateurs proximaux (Soft-thresholding) à chaque itération.
    - **ADMM (Alternating Direction Method of Multipliers) :** Cet algorithme, très utilisé pour l'IA distribuée (plusieurs serveurs qui apprennent ensemble), repose sur l'application alternée d'opérateurs proximaux.
    - **Total Variation Denoising :** Pour nettoyer une image tout en gardant les contours nets, on utilise un proximal par rapport à la norme de la dérivée (TV norm). Cela "écrase" le bruit tout en préservant les sauts brusques.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 122 (Notion de sous-gradient).md]], [[Jalon 121 (Ensembles et Fonctions convexes).md]]
- **Concepts Futurs dépendants :** [[Jalon 129 (Optimisation stochastique).md]], [[Jalon 130 (Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.).md]]
