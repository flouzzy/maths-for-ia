---
uuid: "jalon-122"
title: "Notion de sous-gradient"
year: 3
trimester: 11
tags:
  - math/optimisation
  - ia/fondations
prev: "[[Jalon 121 (Ensembles et Fonctions convexes).md]]"
next: "[[Jalon 123 (Problèmes d'optimisation sous contraintes).md]]"
---

# Jalon 122 : Notion de sous-gradient

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez dans une vallée en forme de "V" (comme la fonction $|x|$).
    - Au fond de la vallée, il y a une pointe. Si vous essayez de poser une plaque de verre (un plan tangent) sur cette pointe, vous pouvez la faire basculer dans plusieurs directions sans qu'elle ne rentre à l'intérieur de la montagne.
    - Chacune de ces positions stables pour la plaque de verre correspond à un **Sous-gradient**.
    - La collection de toutes les pentes possibles de ces plaques s'appelle le **Sous-différentiel**.
    - Si la vallée était arrondie (différentiable), il n'y aurait qu'une seule position possible. Mais comme c'est pointu, il y a tout un choix de pentes.
- **Le "Pourquoi on a inventé ça" :** En IA, on utilise souvent des fonctions qui ont des "cures" ou des angles droits (comme la ReLU ou la norme L1). Le gradient classique (la dérivée) n'existe pas à ces endroits précis. Pour pouvoir quand même faire une descente de gradient, on a dû inventer cette version "élargie" de la pente.
- **Visualisation :** Un point sur une courbe en "V". On peut tracer plusieurs droites qui passent par ce point et qui restent toutes en dessous de la courbe.

## 2. Formalisation & Rigueur Académique

Soit $f : \mathbb{R}^n \to \mathbb{R}$ une fonction convexe.

### A. Définition du Sous-gradient

> **Définition 1 (Sous-gradient) :**
> Un vecteur $g \in \mathbb{R}^n$ est un **sous-gradient** de $f$ au point $x$ si pour tout $y \in \mathbb{R}^n$ :
> $$f(y) \ge f(x) + \langle g, y - x \rangle$$
> L'inégalité dit que la fonction affine $y \mapsto f(x) + \langle g, y - x \rangle$ est une **minorante** de $f$ qui coïncide avec $f$ en $x$.

### B. Le Sous-différentiel

> **Définition 2 (Sous-différentiel) :**
> On appelle **sous-différentiel** de $f$ en $x$, noté $\partial f(x)$, l'ensemble de tous les sous-gradients de $f$ en $x$.

> **Propriétés fondamentales :**
> 1. $\partial f(x)$ est un ensemble **convexe, fermé et non vide** (si $x$ est dans l'intérieur du domaine).
> 2. Si $f$ est différentiable en $x$, alors $\partial f(x) = \{ \nabla f(x) \}$.
> 3. **Condition d'optimalité :** $x^*$ est un minimum global de $f$ si et seulement si le vecteur nul appartient au sous-différentiel :
>    $$x^* = \text{argmin } f(x) \iff 0 \in \partial f(x^*)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Exemple : Sous-différentiel de la valeur absolue $|x|$

Soit $f(x) = |x|$ sur $\mathbb{R}$.

1. **Cas $x > 0$ :** La fonction est dérivable, $f'(x) = 1$. Donc $\partial f(x) = \{1\}$.
2. **Cas $x < 0$ :** La fonction est dérivable, $f'(x) = -1$. Donc $\partial f(x) = \{-1\}$.
3. **Cas $x = 0$ :** On cherche $g$ tel que $\forall y, |y| \ge |0| + g(y-0)$, soit $|y| \ge g y$.
   - Si $y > 0$, alors $y \ge gy \implies g \le 1$.
   - Si $y < 0$, alors $-y \ge gy \implies g \ge -1$.
   Donc $g \in [-1, 1]$.
4. **Conclusion :** $\partial f(0) = [-1, 1]$.
   Remarquons que $0 \in [-1, 1]$, ce qui confirme que 0 est le minimum de la valeur absolue.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Maximum de deux fonctions
**Énoncé :** Soit $f(x) = \max(f_1(x), f_2(x))$ où $f_1, f_2$ sont convexes et différentiables. Quel est le sous-différentiel au point $x$ où $f_1(x) = f_2(x)$ ?
**Correction Détaillée :**
En ce point, les deux fonctions se croisent. Tout vecteur qui est une combinaison convexe des deux gradients convient :
$\partial f(x) = \{ (1-\lambda) \nabla f_1(x) + \lambda \nabla f_2(x) \mid \lambda \in [0, 1] \}$.
C'est le segment reliant les deux gradients.

### Exercice 2 : Niveau Avancé (Norme $L^1$)
**Énoncé :** Déterminer le sous-différentiel de $f(x) = \|x\|_1 = \sum |x_i|$ en un point $x \in \mathbb{R}^n$.
**Correction Détaillée :**
Comme les variables sont séparées, le sous-différentiel est le produit des sous-différentiels de chaque composante :
$\partial f(x) = \partial |x_1| \times \dots \times \partial |x_n|$.
- Si $x_i \neq 0$, la $i$-ème composante du sous-gradient est $\text{sgn}(x_i)$.
- Si $x_i = 0$, la $i$-ème composante peut être n'importe quel nombre dans $[-1, 1]$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les algorithmes de **Descente de Sous-gradient** (Subgradient Descent) remplacent le gradient par n'importe quel élément du sous-différentiel. $\theta_{t+1} = \theta_t - \eta g_t$ avec $g_t \in \partial L(\theta_t)$.
- **Example Concret :**
    - **Optimisation L1 (Lasso) :** On veut minimiser $f(w) = \frac{1}{2}\|Xw-y\|^2 + \lambda \|w\|_1$. La pointe de la norme L1 en 0 force certains poids à devenir exactement nuls. L'analyse du sous-différentiel explique pourquoi le modèle choisit des solutions "éparses" (sparse).
    - **Entraînement de ReLU :** La fonction ReLU n'est pas dérivable en 0. En pratique, les frameworks comme PyTorch posent arbitrairement que la dérivée en 0 est 0 ou 1. Mathématiquement, ils piochent simplement un élément dans le sous-différentiel $[0, 1]$.
    - **SVM (Hinge Loss) :** La fonction de perte des SVM est $L(y) = \max(0, 1-y)$. C'est une fonction "coude" non-lisse. L'utilisation du sous-gradient est ce qui permet de résoudre le problème d'optimisation des SVM de manière robuste.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 121 (Ensembles et Fonctions convexes).md]], [[Jalon 45 (Différentiabilité et Gradient).md]]
- **Concepts Futurs dépendants :** [[Jalon 125 (Opérateurs proximaux).md]], [[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]]
