# Exercice 6 : $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $C \subset \mathbb{R}^n$ un cône convexe fermé pointé (c'est-à-dire $C \cap (-C) = \{0\}$).
Montrer qu'il existe un vecteur $v \in \mathbb{R}^n$ tel que pour tout $x \in C \setminus \{0\}$, $\langle v, x \rangle > 0$.

## Correction

**Étape 1 : Section compacte**
Considérons la sphère unité $S = \{x \in \mathbb{R}^n \mid ||x|| = 1\}$. L'intersection $K = C \cap S$ est un compact (intersection d'un fermé et d'un compact) et ne contient pas l'origine. $K$ représente toutes les directions (rayons) de $C$. L'enveloppe convexe $Conv(K)$ est compacte. De plus $0 \notin Conv(K)$ (car le cône est saillant).

**Étape 2 : Séparation stricte**
Séparons le singleton $\{0\}$ du convexe compact $Conv(K)$.
D'après Hahn-Banach (forme stricte), il existe un hyperplan affine défini par un vecteur normal $v$ et une constante $\alpha$ tel que :
$\langle v, 0 \rangle = 0 < \alpha < \langle v, y \rangle$ pour tout $y \in Conv(K)$.
En particulier, pour tout $y \in K$, $\langle v, y \rangle > \alpha > 0$.

**Étape 3 : Extension au cône entier**
Soit $x \in C \setminus \{0\}$. Alors $x = ||x|| \cdot y$ où $y = x / ||x|| \in K$.
Donc $\langle v, x \rangle = ||x|| \cdot \langle v, y \rangle > ||x|| \cdot \alpha > 0$.
Le vecteur $v$ définit donc un hyperplan strict d'appui à l'origine. $\blacksquare$
