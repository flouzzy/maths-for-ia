---
uuid: "jalon-8-exo-02"
title: "Exercice 2 : Noyau, Image et Rang d'une application linéaire simple"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 2 : Noyau, Image et Rang d'une application linéaire simple (Difficulté : ★☆☆☆☆)

## Énoncé
Soit $f : \mathbb{R}^2 \to \mathbb{R}^2$ l'application définie pour tout $(x,y) \in \mathbb{R}^2$ par $f(x,y) = (2x - y, 4x - 2y)$.

1.  Démontrer que $f$ est une application linéaire.
2.  Déterminer le noyau $\ker f$ de $f$.
3.  Déterminer l'image $\text{Im } f$ de $f$.
4.  Calculer le rang de $f$ et vérifier le théorème du rang.

## Correction Détaillée

### 1. Démontrer que $f$ est une application linéaire

Pour démontrer que $f$ est une application linéaire, nous devons vérifier les deux propriétés suivantes :
   - Additivité : $\forall u, v \in \mathbb{R}^2, f(u + v) = f(u) + f(v)$.
   - Homogénéité : $\forall \lambda \in \mathbb{R}, \forall u \in \mathbb{R}^2, f(\lambda \cdot u) = \lambda \cdot f(u)$.

Soient $u = (x_1, y_1) \in \mathbb{R}^2$ et $v = (x_2, y_2) \in \mathbb{R}^2$. Soit $\lambda \in \mathbb{R}$.

**Vérification de l'additivité :**
Calculons $u + v$:
$u + v = (x_1 + x_2, y_1 + y_2)$.

Appliquons $f$ à $u + v$:
$f(u + v) = f(x_1 + x_2, y_1 + y_2)$
$f(u + v) = (2(x_1 + x_2) - (y_1 + y_2), 4(x_1 + x_2) - 2(y_1 + y_2))$
$f(u + v) = (2x_1 + 2x_2 - y_1 - y_2, 4x_1 + 4x_2 - 2y_1 - 2y_2)$
Réorganisons les termes :
$f(u + v) = ((2x_1 - y_1) + (2x_2 - y_2), (4x_1 - 2y_1) + (4x_2 - 2y_2))$

Calculons $f(u) + f(v)$:
$f(u) = (2x_1 - y_1, 4x_1 - 2y_1)$
$f(v) = (2x_2 - y_2, 4x_2 - 2y_2)$
$f(u) + f(v) = ((2x_1 - y_1) + (2x_2 - y_2), (4x_1 - 2y_1) + (4x_2 - 2y_2))$

Nous constatons que $f(u + v) = f(u) + f(v)$. L'additivité est vérifiée.

**Vérification de l'homogénéité :**
Calculons $\lambda \cdot u$:
$\lambda \cdot u = (\lambda x_1, \lambda y_1)$.

Appliquons $f$ à $\lambda \cdot u$:
$f(\lambda \cdot u) = f(\lambda x_1, \lambda y_1)$
$f(\lambda \cdot u) = (2(\lambda x_1) - (\lambda y_1), 4(\lambda x_1) - 2(\lambda y_1))$
$f(\lambda \cdot u) = (\lambda (2x_1 - y_1), \lambda (4x_1 - 2y_1))$

Calculons $\lambda \cdot f(u)$:
$f(u) = (2x_1 - y_1, 4x_1 - 2y_1)$
$\lambda \cdot f(u) = \lambda (2x_1 - y_1, 4x_1 - 2y_1)$
$\lambda \cdot f(u) = (\lambda (2x_1 - y_1), \lambda (4x_1 - 2y_1))$

Nous constatons que $f(\lambda \cdot u) = \lambda \cdot f(u)$. L'homogénéité est vérifiée.

Puisque $f$ satisfait les deux propriétés d'additivité et d'homogénéité, $f$ est bien une application linéaire de $\mathbb{R}^2$ dans $\mathbb{R}^2$.

### 2. Déterminer le noyau $\ker f$ de $f$

Par définition, le noyau de $f$ est l'ensemble des vecteurs $u = (x,y) \in \mathbb{R}^2$ tels que $f(u) = 0_{\mathbb{R}^2}$.
$f(x,y) = (0,0)$.
Cela nous donne le système d'équations suivant :
$$
\begin{cases}
2x - y = 0 \\
4x - 2y = 0
\end{cases}
$$

De la première équation, nous obtenons $y = 2x$.
Substituons cette expression de $y$ dans la deuxième équation :
$4x - 2(2x) = 0$
$4x - 4x = 0$
$0 = 0$

Cette dernière équation est toujours vraie, ce qui signifie que la deuxième équation est une conséquence de la première (elles sont linéairement dépendantes).
Les vecteurs $(x,y)$ dans le noyau sont ceux pour lesquels $y = 2x$.
Donc, un vecteur $(x,y)$ dans $\ker f$ peut s'écrire sous la forme $(x, 2x)$.
Nous pouvons factoriser $x$ :
$(x, 2x) = x(1, 2)$.

Ainsi, le noyau de $f$ est l'ensemble des multiples scalaires du vecteur $(1, 2)$.
$\ker f = \{ x(1, 2) \mid x \in \mathbb{R} \}$.
C'est la droite vectorielle engendrée par le vecteur $(1, 2)$.
$\ker f = \text{Vect}((1, 2))$.

Le vecteur $(1, 2)$ est non nul, il forme donc une base de $\ker f$.
Par conséquent, la dimension du noyau est $\dim(\ker f) = 1$.

### 3. Déterminer l'image $\text{Im } f$ de $f$

Par définition, l'image de $f$ est l'ensemble des vecteurs $w \in \mathbb{R}^2$ tels qu'il existe un vecteur $u = (x,y) \in \mathbb{R}^2$ avec $w = f(u)$.
$w = (w_1, w_2) = (2x - y, 4x - 2y)$.

Nous pouvons écrire $w$ comme une combinaison linéaire des vecteurs colonnes de la matrice associée à $f$ (si on considère la base canonique).
$f(x,y) = x(2,4) + y(-1,-2)$.
Donc, l'image de $f$ est l'espace vectoriel engendré par les vecteurs $(2,4)$ et $(-1,-2)$.
$\text{Im } f = \text{Vect}((2,4), (-1,-2))$.

Vérifions si ces vecteurs sont linéairement indépendants.
Le vecteur $(2,4)$ est un multiple du vecteur $(-1,-2)$ :
$(2,4) = -2(-1,-2)$.
Puisque $(2,4)$ est un multiple non nul de $(-1,-2)$, ces deux vecteurs sont linéairement dépendants.
Par conséquent, l'un des vecteurs est redondant pour générer l'espace. Nous pouvons choisir l'un d'eux comme base.
Par exemple, $\text{Im } f = \text{Vect}((2,4))$.
Ou, de manière équivalente, $\text{Im } f = \text{Vect}((1,2))$ puisque $(2,4) = 2(1,2)$.

L'image de $f$ est la droite vectorielle engendrée par le vecteur $(1,2)$.
Le vecteur $(1,2)$ est non nul, il forme donc une base de $\text{Im } f$.
Par conséquent, la dimension de l'image est $\dim(\text{Im } f) = 1$.

### 4. Calculer le rang de $f$ et vérifier le théorème du rang

Le rang de $f$, noté $\text{rg } f$, est par définition la dimension de son image.
D'après la question précédente, nous avons trouvé $\dim(\text{Im } f) = 1$.
Donc, $\text{rg } f = 1$.

Vérifions le théorème du rang. Le théorème du rang stipule que pour une application linéaire $f : E \to F$ où $E$ est de dimension finie, on a :
$\dim E = \dim(\ker f) + \text{rg } f$.

Dans notre cas, $E = \mathbb{R}^2$, donc $\dim E = 2$.
Nous avons trouvé $\dim(\ker f) = 1$.
Nous avons trouvé $\text{rg } f = 1$.

Substituons ces valeurs dans le théorème du rang :
$2 = 1 + 1$.
$2 = 2$.

Le théorème du rang est bien vérifié pour cette application linéaire.