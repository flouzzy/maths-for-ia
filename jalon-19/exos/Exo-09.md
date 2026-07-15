---
titre: "Exercice 9 : Dérivabilité"
difficulte: "★★★★★"
---

# Exercice 9 : Pratique et maîtrise conceptuelle

**Énoncé :**
Fonction de dérivée non Riemann-intégrable : Soit la fonction de Volterra $V(x)$. Construire formellement l'argument montrant qu'une fonction dérivable peut posséder une dérivée bornée non intégrable au sens de Riemann.

**Résolution Zéro Ellipse :**
1. La construction canonique repose sur l'ensemble de Smith-Volterra-Cantor (un ensemble de Cantor de mesure de Lebesgue strictement positive).
2. L'ensemble triadique classique de Cantor retire des intervalles ouverts de taille $\frac{1}{3}, \frac{2}{9}$, etc., conduisant à une mesure totale retirée de $1$, donc une mesure résiduelle nulle.
3. Construisons un ensemble "gras" $K$ en retirant au milieu de chaque composante connexe, à l'étape $n$, un intervalle de longueur $\frac{1}{4^n}$.
4. La somme des longueurs des intervalles retirés est $\sum_{n=1}^\infty 2^{n-1} \frac{1}{4^n} = \frac{1}{2} \sum (\frac{1}{2})^{n-1} = 1 \times \frac{1}{2} \times 2 = \frac{1}{2}$.
5. La mesure de Lebesgue de l'ensemble résiduel compact $K$ est donc $1 - \frac{1}{2} = \frac{1}{2} > 0$. L'ensemble $K$ est de plus nulle part dense.
6. Sur chaque intervalle ouvert retiré $]u, v[$, définissons une fonction dérivable oscillante semblable à $x^2 \sin(1/x)$, ajustée pour être nulle et de dérivée nulle aux bords $u$ et $v$.
7. Soit $V(x)$ la fonction globale ainsi construite par recollement. $V$ est dérivable partout.
8. Sur $K$, la dérivée s'annule par continuité des raccordements. La fonction dérivée $V'$ existe partout et est bornée.
9. Cependant, $V'$ est discontinue sur les bords des intervalles retirés. L'ensemble des points de discontinuité de $V'$ contient le compact $K$.
10. Le critère de Lebesgue-Vitali stipule qu'une fonction bornée est Riemann-intégrable si et seulement si l'ensemble de ses points de discontinuité est de mesure de Lebesgue nulle.
11. Or, les points de discontinuité de $V'$ contiennent $K$ qui a une mesure $\frac{1}{2} > 0$.
12. Par conséquent, la fonction $V'$, bien qu'étant l'exacte dérivée d'une fonction partout dérivable, n'est pas Riemann-intégrable. L'intégrale de Lebesgue supplantera l'intégrale de Riemann pour pallier cette défaillance de symétrie avec la dérivation. $\blacksquare$
