---
uuid: "jalon-123"
title: "Problèmes d'optimisation sous contraintes"
year: 3
trimester: 11
tags:
  - math/optimisation
  - ia/fondations
prev: "[[Jalon 122 (Notion de sous-gradient).md]]"
next: "[[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]]"
---

# Jalon 123 : Problèmes d'optimisation sous contraintes

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous deviez construire la maison la plus spacieuse possible, mais vous avez deux règles à respecter :
    1. Vous ne pouvez pas dépasser les limites de votre terrain (une **Contrainte d'inégalité**).
    2. Votre maison doit être exactement à 5 mètres de la route (une **Contrainte d'égalité**).
    - Au lieu de chercher à tâtons, vous introduisez un système de "taxes" : chaque mètre carré construit hors du terrain ou trop proche de la route vous coûte une amende.
    - Le **Lagrangien**, c'est le calcul de votre bonheur total : Espace de la maison - Amendes.
    - Le **Problème Dual**, c'est le point de vue du percepteur des impôts : il cherche à fixer le prix des amendes ($\lambda$ et $\nu$) de manière à ce que, même si vous optimisez parfaitement votre maison, il récolte le maximum d'argent possible.
- **Le "Pourquoi on a inventé ça" :** Dans la vraie vie, on n'est jamais totalement libre. On a un budget limité, un temps limité, ou des lois physiques à respecter. L'optimisation sous contraintes permet de trouver le "meilleur compromis" sous pression.
- **Visualisation :** On cherche le point le plus bas d'un paysage, mais seulement à l'intérieur d'une zone délimitée par des clôtures.

## 2. Formalisation & Rigueur Académique

Soit $f_0 : \mathbb{R}^n \to \mathbb{R}$ la fonction objectif à minimiser.

### A. Forme Standard du Problème (Primal)

On cherche à résoudre :
$$\text{Minimiser } f_0(x)$$
Sous les contraintes :
- $f_i(x) \le 0$ pour $i=1, \dots, m$ (Inégalités)
- $h_j(x) = 0$ pour $j=1, \dots, p$ (Égalités)
L'ensemble des points $x$ vérifiant ces conditions est l'**ensemble admissible** (feasible set).

### B. Le Lagrangien et la Fonction Duale

> **Définition 1 (Lagrangien) :**
> L'application $\mathcal{L} : \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R}$ définie par :
> $$\mathcal{L}(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)$$
> Les $\lambda_i \ge 0$ et $\nu_j \in \mathbb{R}$ sont les **multiplicateurs de Lagrange** (ou variables duales).

> **Définition 2 (Fonction Duale de Lagrange) :**
> C'est la valeur minimale du lagrangien pour des multiplicateurs fixés :
> $$g(\lambda, \nu) = \inf_{x \in \mathbb{R}^n} \mathcal{L}(x, \lambda, \nu)$$
> *Propriété :* $g$ est toujours **concave**, même si le problème original ne l'est pas.

### C. La Dualité

> **Théorème (Dualité Faible) :**
> Pour tous $\lambda \ge 0$ and $\nu$, la valeur $g(\lambda, \nu)$ est une borne inférieure du problème primal :
> $g(\lambda, \nu) \le f_0(x^*)$
> La **Dualité Forte** ($g(\lambda^*, \nu^*) = f_0(x^*)$) est vérifiée sous certaines conditions de convexité (ex: condition de Slater).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Preuve de la Dualité Faible

Soit $x$ un point admissible (vérifiant $f_i(x) \le 0$ et $h_j(x) = 0$). Soit $\lambda \ge 0$ and $\nu \in \mathbb{R}^p$.

1. **Signe des termes du lagrangien :**
   - $\lambda_i f_i(x) \le 0$ (produit d'un positif par un négatif).
   - $\nu_j h_j(x) = 0$ (produit par zéro).
2. **Inégalité sur le lagrangien :**
   $$\mathcal{L}(x, \lambda, \nu) = f_0(x) + \sum \lambda_i f_i(x) + \sum \nu_j h_j(x) \le f_0(x) + 0 + 0 = f_0(x)$$
3. **Passage à l'infimum sur x :**
   Par définition de $g$ :
   $$g(\lambda, \nu) = \inf_{z} \mathcal{L}(z, \lambda, \nu) \le \mathcal{L}(x, \lambda, \nu)$$
4. **Combinaison :**
   $g(\lambda, \nu) \le f_0(x)$ pour tout point admissible $x$.
5. **Conclusion :**
   En prenant le minimum sur $x$ (le résultat du problème primal $p^*$) et le maximum sur $\lambda, \nu$ (le résultat du problème dual $d^*$), on a :
   $$d^* \le p^*$$
   L'écart $p^* - d^*$ est appelé le **saut de dualité** (duality gap).

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Dual d'un problème quadratique simple
**Énoncé :** Minimiser $f(x) = \frac{1}{2} x^2$ sous la contrainte $ax - b = 0$.
**Correction Détaillée :**
1. **Lagrangien :** $\mathcal{L}(x, \nu) = \frac{1}{2} x^2 + \nu(ax - b)$.
2. **Infimum sur x :** On dérive par rapport à $x$ : $x + a\nu = 0 \implies x = -a\nu$.
3. **Fonction duale :** $g(\nu) = \frac{1}{2}(-a\nu)^2 + \nu(a(-a\nu) - b) = \frac{1}{2}a^2\nu^2 - a^2\nu^2 - b\nu = -\frac{1}{2}a^2\nu^2 - b\nu$.
4. **Optimisation duale :** On maximise $g(\nu)$. $g'(\nu) = -a^2\nu - b = 0 \implies \nu^* = -b/a^2$.
5. **Résultat :** $x^* = -a(-b/a^2) = b/a$. (Ce que l'on trouve directement en résolvant $ax-b=0$).

### Exercice 2 : Niveau Avancé (Condition de Slater)
**Énoncé :** Énoncer la condition de Slater pour un problème convexe et expliquer son rôle.
**Correction Détaillée :**
La condition de Slater dit qu'il doit exister au moins un point $x$ strictement admissible (vérifiant $f_i(x) < 0$ pour toutes les inégalités). Si cette condition est remplie, alors le saut de dualité est nul ($d^* = p^*$). C'est la garantie que l'on peut résoudre le problème en passant par le dual.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** L'optimisation duale est la base algorithmique des **SVM** et de l'**Apprentissage par Renforcement** (via les fonctions de valeur).
- **Example Concret :**
    - **SVM à marge souple (Soft Margin) :** On veut séparer les données tout en minimisant les erreurs de classification. Le problème primal est difficile (milliers de variables), mais le **Problème Dual** ne dépend que des produits scalaires entre les points (le Noyau). C'est grâce à la dualité de Lagrange que le "Kernel Trick" est possible.
    - **Maximum Entropy RL (Soft Actor-Critic) :** On veut maximiser la récompense sous la contrainte que la politique reste "exploratrice" (haute entropie). Le multiplicateur de Lagrange $\lambda$ devient la température du modèle qui règle le compromis entre exploration et exploitation.
    - **Differential Privacy :** On minimise l'erreur du modèle sous des contraintes de confidentialité (bornes sur l'influence de chaque donnée). On résout cela en ajoutant des multiplicateurs de Lagrange aux gradients.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 121 (Ensembles et Fonctions convexes).md]], [[Jalon 33 (Formes quadratiques).md]]
- **Concepts Futurs dépendants :** [[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]], [[Jalon 125 (Opérateurs proximaux).md]]
