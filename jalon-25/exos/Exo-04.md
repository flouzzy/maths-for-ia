---
title: "Exercice 4 : Identités de polarisation"
difficulty: 2
---

## Énoncé Formel et Typage Rigoureux
Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel. L'enjeu est d'éprouver la consistance algébrique des formes bilinéaires.
Soit $E$ un espace vectoriel muni d'un produit scalaire $\langle \cdot, \cdot \rangle$ et $\| \cdot \|$ sa norme associée.
1. Si $E$ est un espace vectoriel sur $\mathbb{R}$, exprimer $\langle x, y \rangle$ uniquement en fonction de la norme (Identité de polarisation).
2. Même question si $E$ est un espace vectoriel sur $\mathbb{C}$.

## Preuve Analytique Pas-à-Pas (Zéro Ellipse)
La démarche déductive exige une formalisation intégrale sans ellipse.
**1. Cas Réel ($\mathbb{K} = \mathbb{R}$)**
Soient $x, y \in E$. Nous connaissons le développement de la norme au carré de la somme :
$$\|x + y\|^2 = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2$$
En isolant $\langle x, y \rangle$, on obtient la première forme de polarisation :
$$\langle x, y \rangle = \frac{1}{2} \left( \|x + y\|^2 - \|x\|^2 - \|y\|^2 \right)$$
Alternativement, on peut utiliser le développement de la différence :
$$\|x - y\|^2 = \|x\|^2 - 2\langle x, y \rangle + \|y\|^2$$
En soustrayant cette deuxième équation à la première :
$$\|x + y\|^2 - \|x - y\|^2 = (\|x\|^2 + 2\langle x, y \rangle + \|y\|^2) - (\|x\|^2 - 2\langle x, y \rangle + \|y\|^2)$$
$$\|x + y\|^2 - \|x - y\|^2 = 4\langle x, y \rangle$$
Soit la forme la plus symétrique :
$$\langle x, y \rangle = \frac{1}{4} \left( \|x + y\|^2 - \|x - y\|^2 \right)$$

**2. Cas Complexe ($\mathbb{K} = \mathbb{C}$)**
Le produit scalaire est sesquilinéaire (hermitien).
$$\|x + y\|^2 = \langle x+y, x+y \rangle = \|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2$$
Or $\langle y, x \rangle = \overline{\langle x, y \rangle}$. Donc $\langle x, y \rangle + \langle y, x \rangle = 2 \text{Re}(\langle x, y \rangle)$.
Ainsi, $\|x + y\|^2 = \|x\|^2 + 2\text{Re}(\langle x, y \rangle) + \|y\|^2$.
De même, $\|x - y\|^2 = \|x\|^2 - 2\text{Re}(\langle x, y \rangle) + \|y\|^2$.
Par soustraction, on trouve la partie réelle :
$$4\text{Re}(\langle x, y \rangle) = \|x + y\|^2 - \|x - y\|^2 \implies \text{Re}(\langle x, y \rangle) = \frac{1}{4} (\|x + y\|^2 - \|x - y\|^2)$$

Pour obtenir la partie imaginaire, considérons les combinaisons avec $i$ :
$$\|x + iy\|^2 = \langle x+iy, x+iy \rangle = \|x\|^2 + \langle x, iy \rangle + \langle iy, x \rangle + \|iy\|^2$$
Comme la forme est linéaire à droite, $\langle x, iy \rangle = i\langle x, y \rangle$.
Comme elle est antilinéaire à gauche, $\langle iy, x \rangle = -i\langle y, x \rangle$.
De plus, $\|iy\|^2 = \langle iy, iy \rangle = -i \cdot i \langle y, y \rangle = (-i^2) \|y\|^2 = \|y\|^2$.
$$\|x + iy\|^2 = \|x\|^2 + i\langle x, y \rangle - i\langle y, x \rangle + \|y\|^2$$
$$i\langle x, y \rangle - i\langle y, x \rangle = i(\langle x, y \rangle - \overline{\langle x, y \rangle}) = i(2i \text{Im}(\langle x, y \rangle)) = -2\text{Im}(\langle x, y \rangle)$$
Ainsi :
$$\|x + iy\|^2 = \|x\|^2 - 2\text{Im}(\langle x, y \rangle) + \|y\|^2$$
De même :
$$\|x - iy\|^2 = \|x\|^2 + 2\text{Im}(\langle x, y \rangle) + \|y\|^2$$
Par soustraction :
$$\|x + iy\|^2 - \|x - iy\|^2 = -4\text{Im}(\langle x, y \rangle)$$
$$\text{Im}(\langle x, y \rangle) = \frac{1}{4} (\|x - iy\|^2 - \|x + iy\|^2)$$

Le produit scalaire est $\langle x, y \rangle = \text{Re}(\langle x, y \rangle) + i\text{Im}(\langle x, y \rangle)$. En substituant les deux parties :
$$\langle x, y \rangle = \frac{1}{4} \left( \|x + y\|^2 - \|x - y\|^2 + i\|x - iy\|^2 - i\|x + iy\|^2 \right)$$
Ce qui est l'identité de polarisation complexe.
