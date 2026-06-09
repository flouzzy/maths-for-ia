---
uuid: "jalon-98"
title: "Théorème de Hahn-Banach (forme analytique)"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 97 (Espaces de Banach et Opérateurs Linéaires).md]]"
next: "[[Jalon 99 (Théorème de Hahn-Banach).md]]"
---

# Jalon 98 : Théorème de Hahn-Banach (forme analytique)

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un cartographe. Vous avez dessiné une carte très précise d'un petit quartier (un sous-espace $M$). Vous avez une règle qui vous donne l'altitude exacte dans ce quartier.
    - Maintenant, on vous demande de compléter la carte pour tout le pays (l'espace $E$).
    - On vous impose une contrainte : votre nouvelle carte ne doit jamais dépasser l'altitude d'une montagne protectrice qui recouvre tout le pays (une fonction sous-linéaire $p$).
    - Le **Théorème de Hahn-Banach** dit que c'est **toujours possible**. Vous pouvez toujours étendre votre règle locale à tout l'espace sans jamais tricher avec les mesures originales et sans jamais percer le "toit" imposé par la montagne.
- **Le "Pourquoi on a inventé ça" :** En dimension infinie, les espaces sont si vastes qu'on pourrait craindre qu'il n'y ait pas assez de "scanners" (formes linéaires) pour tout voir. Hahn-Banach garantit qu'il y a "suffisamment" de formes linéaires pour distinguer tous les points et pour supporter toutes les contraintes d'optimisation.
- **Visualisation :** Une droite (forme linéaire) qui effleure une surface courbe (fonction convexe) sans jamais entrer dedans.

## 2. Formalisation

Soit $E$ un espace vectoriel sur $\mathbb{R}$.

### A. Fonctionnelle Sous-linéaire

> **Définition 1 :** Une application $p : E \to \mathbb{R}$ est dite **sous-linéaire** si :
> 1. $\forall x, y \in E, \quad p(x+y) \le p(x) + p(y)$ (Sous-additivité).
> 2. $\forall \lambda \ge 0, \forall x \in E, \quad p(\lambda x) = \lambda p(x)$ (Homogénéité positive).
> *Note :* Toute norme est une fonctionnelle sous-linéaire.

### B. Le Théorème de Hahn-Banach (Analytique)

> **Théorème :**
> Soit $M$ un sous-espace vectoriel de $E$. Soit $f : M \to \mathbb{R}$ une forme linéaire telle que :
> $$\forall x \in M, \quad f(x) \le p(x)$$
> Alors il existe une forme linéaire $F : E \to \mathbb{R}$ telle que :
> 1. $F|_M = f$ (C'est un prolongement).
> 2. $\forall x \in E, \quad F(x) \le p(x)$.

## 3. Démonstrations

### Démonstration : Le prolongement d'un pas (Dimension +1)

Soit $x_0 \in E \setminus M$. On veut étendre $f$ à $M \oplus \mathbb{R}x_0$. On cherche donc une valeur $c = F(x_0)$.
Pour tout $x \in M$ and $\lambda \in \mathbb{R}$, on veut $F(x + \lambda x_0) \le p(x + \lambda x_0)$.

1. **Conditions sur c :**
   - Pour $\lambda > 0$ : $f(x) + \lambda c \le p(x + \lambda x_0) \implies c \le \frac{1}{\lambda} [ p(x + \lambda x_0) - f(x) ] = p(\frac{x}{\lambda} + x_0) - f(\frac{x}{\lambda})$.
   - Pour $\lambda = -1$ : $f(y) - c \le p(y - x_0) \implies c \ge f(y) - p(y - x_0)$.
2. **Existence de c :** On a besoin de montrer que $\sup_{y \in M} [f(y) - p(y-x_0)] \le \inf_{x \in M} [p(x+x_0) - f(x)]$.
3. **Preuve de l'inégalité :** Pour tous $x, y \in M$ :
   $f(x) + f(y) = f(x+y) \le p(x+y) = p(x+x_0 + y-x_0) \le p(x+x_0) + p(y-x_0)$.
   D'où $f(y) - p(y-x_0) \le p(x+x_0) - f(x)$.
   Le membre de gauche est toujours inférieur à celui de droite. On peut donc choisir un $c$ entre les deux.
4. **Conclusion :** On peut prolonger de proche en proche. Pour le cas de dimension infinie quelconque, on utilise l'**Axiome du Choix** (sous la forme du Lemme de Zorn) pour montrer qu'il existe un prolongement maximal qui couvre tout $E$.

## 4. Exercices d'Application

### Exercice 1 : Existence de formes linéaires
**Énoncé :** Soit $E$ un espace vectoriel normé et $x \neq 0$. Montrer qu'il existe $L \in E^*$ telle que $\|L\|=1$ and $L(x) = \|x\|$.
**Correction Détaillée :**
1. On pose $M = \mathbb{R}x$ (la droite engendrée par $x$).
2. On définit $f(\lambda x) = \lambda \|x\|$ sur $M$.
3. $f$ est linéaire et vérifie $f(y) \le \|y\|$ pour tout $y \in M$.
4. Par Hahn-Banach (avec $p = \| \cdot \|$), il existe un prolongement $L$ à $E$ tel que $L(y) \le \|y\|$.
5. Cela implique $\|L\| \le 1$. Comme $L(x/\|x\|) = 1$, alors $\|L\|=1$.

### Exercice 2 : Niveau Avancé (Dualité et Distance)
**Énoncé :** Soit $M$ un sous-espace de $E$ and $x \in E$. Montrer que $dist(x, M) = \sup \{ L(x) \mid L \in M^\perp, \|L\| \le 1 \}$.
**Correction Détaillée :**
C'est une application directe de Hahn-Banach. On construit une forme linéaire qui vaut 0 sur $M$ et qui mesure l'écart de $x$ par rapport à $M$. C'est le fondement de la **Dualité de Fenchel** en optimisation.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Hahn-Banach garantit que les problèmes d'**Optimisation Convexe** sous contraintes ont des solutions duales (les multiplicateurs de Lagrange).
- **Example Concret :**
    - **Support Vector Machines (SVM) :** Pour trouver l'hyperplan séparateur optimal, on résout un problème dual. Hahn-Banach assure que cet hyperplan existe toujours si les données sont linéairement séparables.
    - **Théorie de la Robustesse :** Pour prouver qu'un réseau de neurones est robuste, on essaie de trouver une forme linéaire qui "borne" ses sorties. Hahn-Banach est utilisé pour prouver l'existence de telles bornes dans des espaces de fonctions complexes.
    - **Apprentissage de Mesures (GANS) :** La distance de Wasserstein peut s'écrire sous une forme duale (Kantorovich-Rubinstein) grâce à une variante de Hahn-Banach. C'est ce qui permet de transformer une intégrale difficile sur des joints de probabilités en une optimisation sur des fonctions lipschitziennes.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 97 (Espaces de Banach et Opérateurs Linéaires).md]], [[Jalon 11 (Formes linéaires).md]]
- **Concepts Futurs dépendants :** [[Jalon 99 (Théorème de Hahn-Banach).md]], [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]]
