---
uuid: "jalon-8-exo-06"
title: "Exercice 6 : Noyau, Image et Théorème du Rang pour un Opérateur Différentiel sur les Polynômes"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 6 : Noyau, Image et Théorème du Rang pour un Opérateur Différentiel sur les Polynômes (Difficulté : ★★★☆☆)

## Énoncé
Soit $E = \mathbb{R}_3[X]$ l'espace vectoriel des polynômes à coefficients réels de degré inférieur ou égal à 3.
On considère l'application $f: E \to E$ définie pour tout polynôme $P \in E$ par $f(P) = P' - P''$, où $P'$ et $P''$ désignent respectivement la dérivée première et la dérivée seconde de $P$.

1.  Démontrer que $f$ est une application linéaire.
2.  Déterminer le noyau $\ker f$ de $f$ et en donner une base ainsi que sa dimension.
3.  Déterminer l'image $\text{Im } f$ de $f$ et en donner une base ainsi que sa dimension.
4.  Vérifier le théorème du rang pour l'application $f$.

## Correction Détaillée

### 1. Démonstration de la linéarité de $f$

Pour montrer que $f$ est une application linéaire, nous devons vérifier deux propriétés : l'additivité et l'homogénéité.

Soient $P, Q \in E = \mathbb{R}_3[X]$ et $\lambda \in \mathbb{R}$.

**a) Additivité :** Montrons que $f(P+Q) = f(P) + f(Q)$.
Par définition de $f$:
$f(P+Q) = (P+Q)' - (P+Q)''$.
En utilisant la linéarité de l'opérateur de dérivation (la dérivée d'une somme est la somme des dérivées) :
$(P+Q)' = P' + Q'$.
$(P+Q)'' = P'' + Q''$.
En substituant ces expressions dans l'équation de $f(P+Q)$ :
$f(P+Q) = (P' + Q') - (P'' + Q'')$.
En regroupant les termes relatifs à $P$ et $Q$ :
$f(P+Q) = (P' - P'') + (Q' - Q'')$.
Par définition de $f$, nous reconnaissons $f(P)$ et $f(Q)$ :
$f(P+Q) = f(P) + f(Q)$.
L'additivité est vérifiée.

**b) Homogénéité :** Montrons que $f(\lambda P) = \lambda f(P)$.
Par définition de $f$:
$f(\lambda P) = (\lambda P)' - (\lambda P)''$.
En utilisant la linéarité de l'opérateur de dérivation (la dérivée d'un scalaire fois une fonction est le scalaire fois la dérivée de la fonction) :
$(\lambda P)' = \lambda P'$.
$(\lambda P)'' = \lambda P''$.
En substituant ces expressions dans l'équation de $f(\lambda P)$ :
$f(\lambda P) = \lambda P' - \lambda P''$.
En factorisant par $\lambda$:
$f(\lambda P) = \lambda (P' - P'')$.
Par définition de $f$, nous reconnaissons $f(P)$ :
$f(\lambda P) = \lambda f(P)$.
L'homogénéité est vérifiée.

Puisque $f$ satisfait les propriétés d'additivité et d'homogénéité, $f$ est bien une application linéaire.

### 2. Détermination du noyau $\ker f$

Le noyau de $f$ est l'ensemble des polynômes $P \in E$ tels que $f(P) = 0_E$, où $0_E$ est le polynôme nul.
$P \in \ker f \iff P' - P'' = 0_E$.

Soit $P(X) \in \mathbb{R}_3[X]$. On peut écrire $P(X)$ sous la forme générale :
$P(X) = aX^3 + bX^2 + cX + d$, où $a, b, c, d \in \mathbb{R}$.

Calculons la première dérivée $P'(X)$ :
$P'(X) = \frac{d}{dX}(aX^3 + bX^2 + cX + d) = 3aX^2 + 2bX + c$.

Calculons la seconde dérivée $P''(X)$ :
$P''(X) = \frac{d}{dX}(3aX^2 + 2bX + c) = 6aX + 2b$.

Maintenant, calculons $P'(X) - P''(X)$:
$P'(X) - P''(X) = (3aX^2 + 2bX + c) - (6aX + 2b)$.
$P'(X) - P''(X) = 3aX^2 + (2b - 6a)X + (c - 2b)$.

Pour que $P'(X) - P''(X)$ soit le polynôme nul, tous ses coefficients doivent être nuls :
1. Coefficient de $X^2$: $3a = 0 \implies a = 0$.
2. Coefficient de $X$: $2b - 6a = 0$. Puisque $a=0$, cette équation devient $2b - 6(0) = 0 \implies 2b = 0 \implies b = 0$.
3. Terme constant: $c - 2b = 0$. Puisque $b=0$, cette équation devient $c - 2(0) = 0 \implies c = 0$.

Les coefficients $a, b, c$ doivent être nuls. Le coefficient $d$ n'apparaît pas dans les dérivées, il peut donc prendre n'importe quelle valeur réelle.
Ainsi, les polynômes $P(X)$ appartenant à $\ker f$ sont de la forme :
$P(X) = 0 \cdot X^3 + 0 \cdot X^2 + 0 \cdot X + d = d$, où $d \in \mathbb{R}$.

Le noyau $\ker f$ est donc l'ensemble des polynômes constants :
$\ker f = \{ d \mid d \in \mathbb{R} \} = \text{Vect}(1)$.

Une base de $\ker f$ est la famille $(1)$.
La dimension de $\ker f$ est le nombre de vecteurs dans cette base :
$\dim(\ker f) = 1$.

### 3. Détermination de l'image $\text{Im } f$

L'image de $f$ est l'ensemble des polynômes $Q \in E$ tels qu'il existe un $P \in E$ avec $Q = f(P)$.
$\text{Im } f = \{ f(P) \mid P \in E \}$.

L'espace $E = \mathbb{R}_3[X]$ a pour dimension $\dim E = 4$. Une base canonique de $E$ est $\mathcal{B}_E = (1, X, X^2, X^3)$.
L'image de $f$ est engendrée par l'image des vecteurs de cette base :
$\text{Im } f = \text{Vect}(f(1), f(X), f(X^2), f(X^3))$.

Calculons les images de ces polynômes :
- $f(1) = 1' - 1'' = 0 - 0 = 0_E$.
- $f(X) = X' - X'' = 1 - 0 = 1$.
- $f(X^2) = (X^2)' - (X^2)'' = 2X - 2$.
- $f(X^3) = (X^3)' - (X^3)'' = 3X^2 - 6X$.

Donc, $\text{Im } f = \text{Vect}(0_E, 1, 2X-2, 3X^2-6X)$.
On peut ignorer le vecteur nul dans la famille génératrice :
$\text{Im } f = \text{Vect}(1, 2X-2, 3X^2-6X)$.

Soit la famille $\mathcal{B}_{\text{Im } f} = (P_1, P_2, P_3)$ avec $P_1 = 1$, $P_2 = 2X-2$, $P_3 = 3X^2-6X$.
Cette famille est génératrice de $\text{Im } f$. Pour qu'elle soit une base, il faut qu'elle soit libre.
Supposons une combinaison linéaire nulle de ces polynômes :
$\alpha_1 P_1 + \alpha_2 P_2 + \alpha_3 P_3 = 0_E$, où $\alpha_1, \alpha_2, \alpha_3 \in \mathbb{R}$.
$\alpha_1(1) + \alpha_2(2X-2) + \alpha_3(3X^2-6X) = 0_E$.
Développons et regroupons par puissances de $X$:
$\alpha_1 - 2\alpha_2 + (2\alpha_2 - 6\alpha_3)X + 3\alpha_3 X^2 = 0_E$.

Pour que ce polynôme soit le polynôme nul, tous ses coefficients doivent être nuls :
1. Coefficient de $X^2$: $3\alpha_3 = 0 \implies \alpha_3 = 0$.
2. Coefficient de $X$: $2\alpha_2 - 6\alpha_3 = 0$. Puisque $\alpha_3=0$, cette équation devient $2\alpha_2 - 6(0) = 0 \implies 2\alpha_2 = 0 \implies \alpha_2 = 0$.
3. Terme constant: $\alpha_1 - 2\alpha_2 = 0$. Puisque $\alpha_2=0$, cette équation devient $\alpha_1 - 2(0) = 0 \implies \alpha_1 = 0$.

Tous les coefficients $\alpha_1, \alpha_2, \alpha_3$ sont nuls. La famille $\mathcal{B}_{\text{Im } f}$ est donc libre.
Puisqu'elle est à la fois génératrice et libre, c'est une base de $\text{Im } f$.
La dimension de $\text{Im } f$ est le nombre de vecteurs dans cette base :
$\dim(\text{Im } f) = 3$.
On appelle également cette dimension le rang de $f$, noté $\text{rg } f$.
$\text{rg } f = 3$.

### 4. Vérification du théorème du rang

Le théorème du rang stipule que pour toute application linéaire $f: E \to F$ où $E$ est de dimension finie, on a :
$\dim E = \dim(\ker f) + \text{rg}(f)$.

Dans notre cas :
- L'espace de départ est $E = \mathbb{R}_3[X]$, dont la dimension est $\dim E = 4$.
- Nous avons trouvé $\dim(\ker f) = 1$.
- Nous avons trouvé $\text{rg}(f) = \dim(\text{Im } f) = 3$.

Vérifions l'égalité :
$\dim E = \dim(\ker f) + \text{rg}(f)$
$4 = 1 + 3$
$4 = 4$.

L'égalité est vérifiée. Le théorème du rang est confirmé pour cette application linéaire.