---
title: "Exercice 4 : Identités de polarisation"
difficulty: 2
---

### Exercice 4 : Identité du parallélogramme
**Niveau : \star \star**

**Énoncé :**
Montrer que dans tout espace préhilbertien réel $(E, \langle \cdot, \cdot \rangle)$, pour tous $x, y \in E$, on a :
\[ \|x + y\|^2 + \|x - y\|^2 = 2(\|x\|^2 + \|y\|^2) \]

**Correction (Zéro Ellipse) :**
Fixons $x, y \in E$. Développons le terme $\|x + y\|^2$ en utilisant la bilinéarité et la symétrie du produit scalaire :
\[ \|x + y\|^2 = \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 \]
Développons de la même manière le terme $\|x - y\|^2$ :
\[ \|x - y\|^2 = \langle x - y, x - y \rangle = \langle x, x \rangle - \langle x, y \rangle - \langle y, x \rangle + \langle -y, -y \rangle = \|x\|^2 - 2\langle x, y \rangle + \|y\|^2 \]
Sommons les deux identités rigoureusement établies :
\[ \|x + y\|^2 + \|x - y\|^2 = (\|x\|^2 + 2\langle x, y \rangle + \|y\|^2) + (\|x\|^2 - 2\langle x, y \rangle + \|y\|^2) \]
Les termes croisés $+2\langle x, y \rangle$ et $-2\langle x, y \rangle$ s'annulent exactement.
Il reste donc :
\[ \|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2 = 2(\|x\|^2 + \|y\|^2) \]
Cette démonstration algébrique confirme l'identité géométrique classique liant les diagonales et les côtés d'un parallélogramme.
