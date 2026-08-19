# Exercice 5 : Régularité intérieure

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

Démontrer que pour tout ensemble mesurable $E$ et $\epsilon > 0$, il existe un fermé $F \subset E$ tel que $\lambda(E \setminus F) \le \epsilon$. On suppose $E$ borné.

## Correction Détaillée

1. **Régularité extérieure :** Par définition de la mesure extérieure (qui coïncide avec la mesure sur $E$), $\lambda(E) = \inf \{ \sum \ell(I_n) \mid E \subset \bigcup I_n \}$.
Il existe donc une union dénombrable d'ouverts $O = \bigcup I_n$ contenant $E$ telle que $\lambda(O) \le \lambda(E) + \epsilon$.
Ainsi, $\lambda(O \setminus E) = \lambda(O) - \lambda(E) \le \epsilon$ (car $E$ est mesurable et $\lambda(E)$ fini car $E$ borné).
2. **Passage au complémentaire :** Considérons un grand segment fermé $K = [-M, M]$ contenant $E$. L'ensemble $K \setminus E$ est mesurable.
Par la régularité extérieure appliquée à $K \setminus E$, il existe un ouvert $V$ contenant $K \setminus E$ tel que $\lambda(V \setminus (K \setminus E)) \le \epsilon$.
3. **Construction du fermé :** Posons $F = K \setminus V$.
Puisque $V$ est ouvert, son complémentaire $F$ dans le fermé $K$ est fermé.
Comme $V \supset K \setminus E$, le passage au complémentaire dans $K$ donne $F \subset E$.
De plus, $E \setminus F = E \cap V = V \setminus (K \setminus E)$.
Donc $\lambda(E \setminus F) = \lambda(V \setminus (K \setminus E)) \le \epsilon$.
