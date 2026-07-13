---
uuid: "jalon-26-exo-05"
title: "Inégalité de Ptolémée (cas euclidien)"
difficulty: 3
---

# Exercice 5 : Inégalité de Ptolémée (cas euclidien) (Difficulté ★★★☆☆)

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace euclidien.
1. Montrer que pour tous $x, y \in E \setminus \{0\}$, $\left\| \frac{x}{\|x\|^2} - \frac{y}{\|y\|^2} \right\| = \frac{\|x - y\|}{\|x\| \|y\|}$.
2. En déduire, par l'inégalité triangulaire, l'inégalité de Ptolémée : pour tous $a, b, c, d \in E$,
$$ \|a - c\| \|b - d\| \le \|a - b\| \|c - d\| + \|b - c\| \|a - d\| $$

## Démonstration Rigoureuse à Blanc

1. Calculons le carré de la norme demandée :
   $$ \left\| \frac{x}{\|x\|^2} - \frac{y}{\|y\|^2} \right\|^2 = \langle \frac{x}{\|x\|^2} - \frac{y}{\|y\|^2}, \frac{x}{\|x\|^2} - \frac{y}{\|y\|^2} \rangle $$
   Par bilinéarité :
   $$ = \frac{\langle x, x \rangle}{\|x\|^4} - 2 \frac{\langle x, y \rangle}{\|x\|^2 \|y\|^2} + \frac{\langle y, y \rangle}{\|y\|^4} $$
   Or $\langle x, x \rangle = \|x\|^2$ et $\langle y, y \rangle = \|y\|^2$, donc :
   $$ = \frac{\|x\|^2}{\|x\|^4} - 2 \frac{\langle x, y \rangle}{\|x\|^2 \|y\|^2} + \frac{\|y\|^2}{\|y\|^4} $$
   $$ = \frac{1}{\|x\|^2} - 2 \frac{\langle x, y \rangle}{\|x\|^2 \|y\|^2} + \frac{1}{\|y\|^2} $$
   Mettons tout au même dénominateur $\|x\|^2 \|y\|^2$ :
   $$ = \frac{\|y\|^2 - 2\langle x, y \rangle + \|x\|^2}{\|x\|^2 \|y\|^2} $$
   Le numérateur est précisément le développement de $\|x - y\|^2$.
   $$ = \frac{\|x - y\|^2}{\|x\|^2 \|y\|^2} $$
   En prenant la racine carrée (quantités positives), on obtient le résultat :
   $$ \left\| \frac{x}{\|x\|^2} - \frac{y}{\|y\|^2} \right\| = \frac{\|x - y\|}{\|x\| \|y\|} $$

2. Soit $A, B, C, D$ quatre points. Posons l'origine en $D$, c'est-à-dire que nous travaillons avec les vecteurs $a = A-D$, $b = B-D$, $c = C-D$, et $d = 0_E$.
   - Soit $i(x) = \frac{x}{\|x\|^2}$ l'inversion géométrique.
   - Considérons les points inversés $a' = i(a)$, $b' = i(b)$, $c' = i(c)$.
   - Appliquons l'inégalité triangulaire dans l'espace aux points $a', b', c'$ :
     $$ \|a' - c'\| \le \|a' - b'\| + \|b' - c'\| $$
   - D'après la question 1, $\|a' - c'\| = \frac{\|a - c\|}{\|a\| \|c\|}$.
   - Remplaçons dans l'inégalité :
     $$ \frac{\|a - c\|}{\|a\| \|c\|} \le \frac{\|a - b\|}{\|a\| \|b\|} + \frac{\|b - c\|}{\|b\| \|c\|} $$
   - Multiplions le tout par $\|a\| \|b\| \|c\|$ (qui est strictement positif si les points sont non nuls et distincts) :
     $$ \|a - c\| \|b\| \le \|a - b\| \|c\| + \|b - c\| \|a\| $$
   - En revenant aux notations initiales, $\|a\| = \|a - 0_E\| = \|a - d\|$, $\|b\| = \|b - d\|$, etc.
     $$ \|a - c\| \|b - d\| \le \|a - b\| \|c - d\| + \|b - c\| \|a - d\| $$
   $\blacksquare$
