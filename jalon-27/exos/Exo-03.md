---
uuid: "jalon-27-exo-03"
title: "Exercice 03 : Somme de projecteurs orthogonaux"
---
# Exercice 03 : Somme de projecteurs orthogonaux

**Difficulté :** ★★☆☆☆

## Énoncé

Soient $P$ et $Q$ deux projecteurs orthogonaux sur $E$. À quelle condition nécessaire et suffisante $P+Q$ est-il un projecteur orthogonal ?

## Démonstration sans ellipse

Par définition, un projecteur orthogonal $R$ vérifie $R^2 = R$ (idempotence) et $R^* = R$ (symétrie).
Puisque $P$ et $Q$ sont des projecteurs orthogonaux, on a $P^2=P$, $P^*=P$, et $Q^2=Q$, $Q^*=Q$.
L'opérateur $P+Q$ est toujours symétrique, car :
$$ (P+Q)^* = P^* + Q^* = P + Q $$
La question se réduit donc à savoir quand $P+Q$ est un projecteur, c'est-à-dire quand $(P+Q)^2 = P+Q$.
Développons $(P+Q)^2$ :
$$ (P+Q)^2 = (P+Q) \circ (P+Q) = P^2 + P \circ Q + Q \circ P + Q^2 $$
En utilisant $P^2=P$ et $Q^2=Q$, cela donne :
$$ (P+Q)^2 = P + P \circ Q + Q \circ P + Q = (P+Q) + P \circ Q + Q \circ P $$
Pour que $(P+Q)^2 = P+Q$, il faut et il suffit que :
$$ P \circ Q + Q \circ P = 0 \quad \text{(Équation 1)} $$
Multiplions l'Équation 1 à droite par $P$ :
$$ P \circ Q \circ P + Q \circ P^2 = 0 \implies P \circ Q \circ P + Q \circ P = 0 \quad \text{(car } P^2=P) $$
Multiplions l'Équation 1 à gauche par $P$ :
$$ P^2 \circ Q + P \circ Q \circ P = 0 \implies P \circ Q + P \circ Q \circ P = 0 $$
En soustrayant ces deux nouvelles relations :
$$ (P \circ Q + P \circ Q \circ P) - (P \circ Q \circ P + Q \circ P) = 0 \implies P \circ Q - Q \circ P = 0 \implies P \circ Q = Q \circ P $$
Remplaçons $Q \circ P$ par $P \circ Q$ dans l'Équation 1 :
$$ 2(P \circ Q) = 0 \implies P \circ Q = 0 $$
Par symétrie, $Q \circ P = 0$.
Ainsi, la condition nécessaire et suffisante est que $P \circ Q = Q \circ P = 0$, ce qui signifie géométriquement que les images de $P$ et $Q$ sont orthogonales. $\blacksquare$
