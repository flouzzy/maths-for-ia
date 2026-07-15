---
title: "Exercice 5 : Valeurs propres d'une isométrie symétrique"
difficulty: "★★★☆☆"
---
# Exercice 5 : Valeurs propres d'une isométrie symétrique

## Énoncé
Soit $E$ un espace euclidien et $f \in \mathcal{L}(E)$.
Montrer que $f$ est à la fois symétrique et une isométrie si et seulement si $f$ est une symétrie orthogonale (c'est-à-dire un endomorphisme diagonalisable dont le spectre est inclus dans $\{-1, 1\}$).

## Correction Zéro Ellipse
**Définition préalable :**
Une symétrie est un endomorphisme $s$ tel que $s \circ s = \text{Id}_E$.
Une symétrie est orthogonale si ses sous-espaces $\text{Ker}(s - \text{Id}_E)$ et $\text{Ker}(s + \text{Id}_E)$ sont supplémentaires orthogonaux.

**Sens direct ($\implies$) : Symétrique + Isométrie implique Spectre $\subset \{-1, 1\}$**
Supposons que $f$ est symétrique ($f = f^*$) et que $f$ est une isométrie ($\forall x, \|f(x)\| = \|x\|$).
L'isométrie se traduit algébriquement par le fait que pour tout $x,y$, $\langle f(x), f(y) \rangle = \langle x, y \rangle$.
On peut réécrire ceci avec l'adjoint : $\langle x, f^*(f(y)) \rangle = \langle x, y \rangle$.
Par unicité, cela implique $f^* \circ f = \text{Id}_E$.
Mais par hypothèse, $f$ est symétrique, donc $f^* = f$.
L'équation devient $f \circ f = \text{Id}_E$, soit $f^2 = \text{Id}_E$.
Ainsi, le polynôme $X^2 - 1$ annule $f$. Or $X^2 - 1 = (X-1)(X+1)$. Ce polynôme est scindé à racines simples sur $\mathbb{R}$.
Cela prouve que $f$ est diagonalisable et que ses valeurs propres ne peuvent être que parmi les racines du polynôme annulateur, soit $\{-1, 1\}$.
De plus, $f$ étant symétrique, ses sous-espaces propres $E_1 = \text{Ker}(f - \text{Id})$ et $E_{-1} = \text{Ker}(f + \text{Id})$ sont nécessairement orthogonaux (cf. cours).
$E_1$ et $E_{-1}$ sont supplémentaires car le polynôme est scindé à racines simples et annulateur.
Ainsi, $f$ agit comme l'identité sur $E_1$ et l'opposé de l'identité sur $E_{-1}$, avec $E_1 \perp E_{-1}$. C'est la définition exacte d'une symétrie orthogonale par rapport à $E_1$.

**Sens réciproque ($\impliedby$) : Symétrie orthogonale implique Symétrique + Isométrie**
Supposons que $f$ est une symétrie orthogonale.
Alors l'espace se décompose en $E = E_1 \oplus^\perp E_{-1}$, où $f(x) = x$ pour $x \in E_1$ et $f(x) = -x$ pour $x \in E_{-1}$.
Soient $x, y \in E$. Écrivons $x = u_1 + v_1$ et $y = u_2 + v_2$ avec $u_i \in E_1$ et $v_i \in E_{-1}$.
- Montrons que $f$ est symétrique :
$\langle f(x), y \rangle = \langle u_1 - v_1, u_2 + v_2 \rangle = \langle u_1, u_2 \rangle - \langle v_1, v_2 \rangle$ (car les termes croisés $\langle u_i, v_j \rangle$ sont nuls grâce à l'orthogonalité des espaces).
D'autre part, $\langle x, f(y) \rangle = \langle u_1 + v_1, u_2 - v_2 \rangle = \langle u_1, u_2 \rangle - \langle v_1, v_2 \rangle$.
On obtient bien $\langle f(x), y \rangle = \langle x, f(y) \rangle$. $f$ est symétrique.
- Montrons que $f$ est une isométrie :
$\|f(x)\|^2 = \langle u_1 - v_1, u_1 - v_1 \rangle = \|u_1\|^2 - 2\langle u_1, v_1 \rangle + \|v_1\|^2 = \|u_1\|^2 + \|v_1\|^2$ (car $\langle u_1, v_1 \rangle = 0$).
Or par le théorème de Pythagore sur les composantes orthogonales, $\|x\|^2 = \|u_1 + v_1\|^2 = \|u_1\|^2 + \|v_1\|^2$.
Donc $\|f(x)\| = \|x\|$ pour tout $x$. $f$ est une isométrie.
