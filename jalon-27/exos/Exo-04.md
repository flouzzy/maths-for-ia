---
title: "Exercice 4 : Projecteur orthogonal et symétrie"
difficulty: "★★★☆☆"
---
# Exercice 4 : Projecteur orthogonal et symétrie

## Énoncé
Soit $E$ un espace euclidien. Soit $p \in \mathcal{L}(E)$ un projecteur, c'est-à-dire tel que $p \circ p = p$.
Démontrer que $p$ est un projecteur orthogonal si et seulement si $p$ est un endomorphisme symétrique ($p = p^*$).

## Correction Zéro Ellipse
Un projecteur $p$ est caractérisé par la décomposition de l'espace en somme directe : $E = \text{Ker}(p) \oplus \text{Im}(p)$.
Pour tout $x \in E$, on peut écrire de manière unique $x = u + v$ avec $u \in \text{Im}(p)$ et $v \in \text{Ker}(p)$.
Par définition, $p(x) = p(u+v) = p(u) + p(v) = u + 0 = u$.
Un projecteur est dit "orthogonal" si et seulement si $\text{Ker}(p) \perp \text{Im}(p)$.

**Sens direct ($\implies$) : Projecteur orthogonal implique symétrique**
Supposons que $p$ soit un projecteur orthogonal.
Soient $x, y \in E$. Décomposons-les : $x = x_1 + x_2$ et $y = y_1 + y_2$ avec $x_1, y_1 \in \text{Im}(p)$ et $x_2, y_2 \in \text{Ker}(p)$.
Évaluons $\langle p(x), y \rangle$ :
$\langle p(x), y \rangle = \langle x_1, y_1 + y_2 \rangle = \langle x_1, y_1 \rangle + \langle x_1, y_2 \rangle$.
Puisque le projecteur est orthogonal, $\text{Ker}(p) \perp \text{Im}(p)$, donc le vecteur $x_1 \in \text{Im}(p)$ est orthogonal au vecteur $y_2 \in \text{Ker}(p)$.
Ainsi $\langle x_1, y_2 \rangle = 0$.
Il reste $\langle p(x), y \rangle = \langle x_1, y_1 \rangle$.

Évaluons maintenant $\langle x, p(y) \rangle$ :
$\langle x, p(y) \rangle = \langle x_1 + x_2, y_1 \rangle = \langle x_1, y_1 \rangle + \langle x_2, y_1 \rangle$.
De même, $x_2 \in \text{Ker}(p)$ et $y_1 \in \text{Im}(p)$ sont orthogonaux, donc $\langle x_2, y_1 \rangle = 0$.
Il reste $\langle x, p(y) \rangle = \langle x_1, y_1 \rangle$.

On constate que $\forall x, y \in E, \langle p(x), y \rangle = \langle x, p(y) \rangle$. Donc $p$ est symétrique.

**Sens réciproque ($\impliedby$) : Projecteur symétrique implique orthogonal**
Supposons que $p$ soit symétrique ($p = p^*$).
Il faut montrer que $\text{Ker}(p) \perp \text{Im}(p)$.
Soit $u \in \text{Im}(p)$ et $v \in \text{Ker}(p)$.
Puisque $u \in \text{Im}(p)$, il existe $x \in E$ tel que $u = p(x)$. Mais plus simplement, puisqu'il est dans l'image d'un projecteur, $p(u) = u$.
Puisque $v \in \text{Ker}(p)$, par définition $p(v) = 0_E$.
Calculons leur produit scalaire $\langle u, v \rangle$.
Puisque $p(u) = u$, on peut substituer :
$\langle u, v \rangle = \langle p(u), v \rangle$.
Utilisons la symétrie de $p$ :
$\langle p(u), v \rangle = \langle u, p(v) \rangle$.
Or $p(v) = 0_E$.
Donc $\langle u, 0_E \rangle = 0$.
Ainsi, tout vecteur de $\text{Im}(p)$ est orthogonal à tout vecteur de $\text{Ker}(p)$.
Le projecteur $p$ est bien un projecteur orthogonal.
