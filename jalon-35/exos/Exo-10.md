# Exercice 10 : ★★★★★

**Énoncé :**
Théorème des bornes atteintes

**Correction (Zéro Ellipse) :**
Soit $(E, \|\cdot\|_E)$ et $(F, \|\cdot\|_F)$ deux espaces normés. Soit $K \subset E$ un compact non vide et $f : K \to F$ une application continue. Montrer que l'image $f(K)$ est un compact de $F$.

Soit $(y_n)_{n \in \mathbb{N}}$ une suite quelconque d'éléments de $f(K)$.
Par définition de l'image, pour chaque entier $n$, il existe au moins un antécédent $x_n \in K$ tel que $y_n = f(x_n)$.
La suite $(x_n)_{n \in \mathbb{N}}$ est à valeurs dans le compact $K$.
Par la caractérisation de Bolzano-Weierstrass de la compacité, on peut en extraire une sous-suite $(x_{\phi(n)})_{n \in \mathbb{N}}$ qui converge vers un point $x \in K$.
L'application $f$ est continue sur tout $K$, et en particulier en $x$.
La convergence $x_{\phi(n)} \to x$ implique donc la convergence des images : $f(x_{\phi(n)}) \to f(x)$.
C'est-à-dire que $y_{\phi(n)} \to f(x)$.
Comme $x \in K$, on a bien $f(x) \in f(K)$.
Nous avons ainsi montré que de toute suite $(y_n)$ de $f(K)$, on peut extraire une sous-suite $(y_{\phi(n)})$ qui converge vers un élément de $f(K)$.
Ceci est exactement la définition séquentielle d'un ensemble compact.
Par suite, $f(K)$ est compact. $\blacksquare$
