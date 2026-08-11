---
uuid: "exo-55-05"
title: "Produit d'espaces connexes"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : Produit d'espaces connexes

**Énoncé :**
Soient $X$ et $Y$ deux espaces topologiques connexes. Montrer que leur espace produit $X \times Y$ est connexe.

**Solution :**
1. Fixons un point $(x_0, y_0) \in X \times Y$.
2. Pour chaque point $(x, y) \in X \times Y$, on considère l'ensemble $T_{x,y} = (X \times \{y\}) \cup (\{x_0\} \times Y)$.
3. L'espace $X \times \{y\}$ est homéomorphe à $X$ donc est connexe. L'espace $\{x_0\} \times Y$ est homéomorphe à $Y$ donc est connexe.
4. L'intersection de ces deux ensembles est $\{(x_0, y)\}$, qui est non vide. Or, la réunion de deux connexes d'intersection non vide est connexe. Donc $T_{x,y}$ est connexe.
5. Remarquons que pour tout $(x, y)$, le point $(x_0, y_0)$ appartient à $T_{x,y}$ (précisément dans la partie $\{x_0\} \times Y$).
6. L'espace complet $X \times Y$ peut s'écrire comme la réunion de tous ces $T_{x,y}$ : $X \times Y = \bigcup_{(x,y)} T_{x,y}$.
7. C'est une réunion de parties connexes qui ont toutes un point commun, le point $(x_0, y_0)$.
8. Par un théorème du cours, la réunion d'une famille de connexes d'intersection globale non vide est un connexe. Ainsi, $X \times Y$ est connexe.
