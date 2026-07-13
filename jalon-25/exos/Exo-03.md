---
title: "Exercice 3 : Identité du parallélogramme"
difficulty: 2
---

## Énoncé
Soit $E$ un espace préhilbertien sur $\mathbb{R}$ ou $\mathbb{C}$, et $\| \cdot \|$ la norme induite par son produit scalaire $\langle \cdot, \cdot \rangle$.
Démontrer l'identité du parallélogramme :
$$\forall x, y \in E, \|x + y\|^2 + \|x - y\|^2 = 2(\|x\|^2 + \|y\|^2)$$
Interpréter géométriquement ce résultat.

## Correction Détaillée
**Preuve algébrique :**
Soient $x, y \in E$. Par définition de la norme :
$$\|x + y\|^2 = \langle x + y, x + y \rangle$$
Par bilinéarité (ou sesquilinéarité si le corps est $\mathbb{C}$) :
$$\|x + y\|^2 = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle$$
$$\|x + y\|^2 = \|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2$$
De manière analogue pour $\|x - y\|^2$ :
$$\|x - y\|^2 = \langle x - y, x - y \rangle$$
$$\|x - y\|^2 = \langle x, x \rangle - \langle x, y \rangle - \langle y, x \rangle + \langle y, y \rangle$$
(Attention ici : dans le cas complexe, $-\langle y, x \rangle$ vient de la combinaison de la linéarité à droite avec la semi-linéarité à gauche du signe $-$, car le produit de $-1$ avec la conjugaison de $-1$ reste $1$ pour le dernier terme).
$$\|x - y\|^2 = \|x\|^2 - \langle x, y \rangle - \langle y, x \rangle + \|y\|^2$$

Ajoutons les deux expressions membres à membres :
$$\|x + y\|^2 + \|x - y\|^2 = (\|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2) + (\|x\|^2 - \langle x, y \rangle - \langle y, x \rangle + \|y\|^2)$$
Les termes croisés $\langle x, y \rangle$ et $\langle y, x \rangle$ s'annulent :
$$\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2 = 2(\|x\|^2 + \|y\|^2)$$
Ce qui achève la démonstration.

**Interprétation géométrique :**
Dans un parallélogramme défini par les vecteurs $x$ et $y$ :
- Les longueurs des côtés sont $\|x\|$ et $\|y\|$.
- Les vecteurs diagonaux sont $x+y$ et $x-y$.
- Leurs longueurs (au carré) sont $\|x+y\|^2$ et $\|x-y\|^2$.
L'identité stipule que la somme des carrés des longueurs des deux diagonales d'un parallélogramme est égale à la somme des carrés des longueurs de ses quatre côtés. C'est une caractérisation fondamentale des espaces de Hilbert par rapport aux espaces de Banach quelconques (théorème de Jordan-von Neumann).
