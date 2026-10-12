# Indépendance d'un événement avec son complémentaire

**Difficulté :** $\bigstar\star\star\star\star$

Soit un événement $A$ de probabilité $p = \mathbb{P}(A)$.
Déterminer à quelle condition nécessaire et suffisante l'événement $A$ est indépendant de son propre complémentaire $A^c$.

### Correction

Soit $A$ un événement. Notons $p = \mathbb{P}(A)$. La probabilité de son complémentaire est $\mathbb{P}(A^c) = 1 - p$.

1. Traduisons l'hypothèse d'indépendance entre $A$ et $A^c$. Par définition, cela signifie que :
   $\mathbb{P}(A \cap A^c) = \mathbb{P}(A) \mathbb{P}(A^c)$.
2. Or, par la définition même du complémentaire, $A$ et $A^c$ sont disjoints, donc $A \cap A^c = \emptyset$.
3. Ainsi, la probabilité de leur intersection est toujours nulle : $\mathbb{P}(A \cap A^c) = 0$.
4. L'équation de l'indépendance devient donc :
   $0 = \mathbb{P}(A) \mathbb{P}(A^c)$
   $0 = p(1 - p)$
5. Les solutions de cette équation du second degré sont trivialement $p = 0$ ou $1 - p = 0 \iff p = 1$.

En conclusion, un événement $A$ est indépendant de son complémentaire $A^c$ si et seulement si $\mathbb{P}(A) = 0$ ou $\mathbb{P}(A) = 1$ (événements presque certains ou presque impossibles).
