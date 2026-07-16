---
titre: "Exercice 8 : Dérivabilité"
difficulte: "★★★★☆"
---

# Exercice 8 : Pratique et maîtrise conceptuelle

**Énoncé :**
Démontrer le théorème de Darboux : Si $f$ est dérivable sur un intervalle $I$, alors sa fonction dérivée $f'$ vérifie la propriété des valeurs intermédiaires.

**Résolution Zéro Ellipse :**
1. Soient $a, b \in I$ avec $a < b$, et soit $y$ un réel strictement compris entre $f'(a)$ et $f'(b)$. Démontrons qu'il existe $c \in ]a,b[$ tel que $f'(c) = y$.
2. Supposons sans perte de généralité que $f'(a) < y < f'(b)$. Considérons la fonction auxiliaire $g(x) = f(x) - y x$.
3. La fonction $g$ est dérivable sur $I$, et $g'(x) = f'(x) - y$.
4. Évaluons la dérivée de $g$ aux bornes : $g'(a) = f'(a) - y < 0$ et $g'(b) = f'(b) - y > 0$.
5. Puisque $g$ est continue sur le compact $[a,b]$, elle y admet un minimum global en un point $c \in [a,b]$.
6. Montrons que $c$ ne peut être situé sur la frontière.
7. Comme $g'(a) < 0$, la limite du taux d'accroissement de $g$ en $a$ est strictement négative. Pour $x > a$ suffisamment proche, $g(x) - g(a) < 0 \implies g(x) < g(a)$. Le minimum n'est donc pas en $a$.
8. De même, $g'(b) > 0$. Pour $x < b$ suffisamment proche, $g(b) - g(x) > 0 \implies g(x) < g(b)$. Le minimum n'est donc pas en $b$.
9. Par conséquent, l'extremum $c$ est atteint à l'intérieur de l'ouvert $]a,b[$.
10. D'après la condition nécessaire d'optimalité du premier ordre (qui est un corollaire direct de la preuve de Rolle), la dérivée d'une fonction en un extremum local situé à l'intérieur d'un ouvert est nécessairement nulle.
11. Donc $g'(c) = 0$.
12. Or $g'(c) = f'(c) - y = 0 \implies f'(c) = y$. La dérivée atteint bien toutes ses valeurs intermédiaires. $\blacksquare$
