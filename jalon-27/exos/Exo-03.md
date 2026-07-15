---
uuid: "jalon-27-exo-03"
title: "Exercice 03 : Somme de projecteurs orthogonaux"
---
# Exercice 03 : Somme de projecteurs orthogonaux

**Difficulté :** ★★☆☆☆

## Énoncé

Soient $P$ et $Q$ deux projecteurs orthogonaux. À quelle condition $P+Q$ est-il un projecteur orthogonal ?

## Démonstration sans ellipse

Soient $P$ et $Q$ deux projecteurs orthogonaux. On sait que $P^2=P, P^*=P$ et $Q^2=Q, Q^*=Q$.
La somme $P+Q$ est symétrique car $(P+Q)^* = P^*+Q^* = P+Q$.
Il reste à vérifier la condition d'idempotence :
$$ (P+Q)^2 = P^2 + P \circ Q + Q \circ P + Q^2 = P + P \circ Q + Q \circ P + Q $$
Pour que $(P+Q)^2 = P+Q$, il faut et il suffit que $P \circ Q + Q \circ P = 0$.
En multipliant à droite par $P$, on obtient :
$$ P \circ Q \circ P + Q \circ P = 0 \quad \text{car } P^2=P $$
Et en multipliant à gauche par $P$, on obtient :
$$ P \circ Q + P \circ Q \circ P = 0 $$
En soustrayant ces deux relations, on a $P \circ Q - Q \circ P = 0$, soit $P \circ Q = Q \circ P$.
En remplaçant cela dans $2 P \circ Q = 0$, on obtient $P \circ Q = 0$.
La condition nécessaire et suffisante est que $P \circ Q = Q \circ P = 0$, c'est-à-dire que leurs images soient orthogonales. $\blacksquare$
