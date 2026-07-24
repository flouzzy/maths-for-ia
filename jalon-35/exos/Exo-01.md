# Exercice 1 : ★

**Énoncé :**
L'ensemble $\emptyset$ et l'espace entier $E$ sont à la fois ouverts et fermés.

**Correction (Zéro Ellipse) :**
Soit $(E, \| \cdot \|)$ un espace normé.

1. **Cas de l'ensemble vide $\emptyset$ :**
- *Fermé :* Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\emptyset$ convergeant vers $x \in E$. Comme il n'existe aucune suite d'éléments dans l'ensemble vide, l'implication "si $(x_n) \in \emptyset^\mathbb{N}$ converge vers $x$, alors $x \in \emptyset$" est vraie par vacuité. Donc $\emptyset$ est fermé.
- *Ouvert :* Soit $x \in \emptyset$. Il n'y a aucun point, donc la condition "il existe une boule $B(x, r) \subset \emptyset$" est trivialement vérifiée. Plus rigoureusement, le complémentaire de $\emptyset$ est $E$, qui est fermé (voir ci-dessous), donc $\emptyset$ est ouvert.

2. **Cas de l'espace $E$ :**
- *Fermé :* Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments de $E$ convergeant vers $x \in E$. Par définition, la limite $x$ appartient à l'espace d'arrivée $E$. Donc $E$ contient ses limites. $E$ est fermé.
- *Ouvert :* Soit $(x_n)_{n \in \mathbb{N}}$ une suite quelconque de $E$ convergeant vers $x \in E$. Tous les termes de la suite sont dans $E$, donc ils y sont à partir d'un certain rang (dès le rang 0). $E$ est ouvert. $\blacksquare$
