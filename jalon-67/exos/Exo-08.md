---
title: "TCM et limites presque partout"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---
# TCM et limites presque partout
**Énoncé :**
Montrer que si $f_n$ sont mesurables positives, et $\sum \int f_n < \infty$, alors $\sum f_n(x)$ converge (et donc est finie) pour presque tout $x$.

**Correction :**
1. Posons $S_N = \sum_{n=1}^N f_n$. La suite $(S_N)$ est croissante et positive.
2. Par le TCM, on peut intervertir limite et intégrale :
   $\int \left( \sum_{n=1}^\infty f_n \right) d\mu = \sum_{n=1}^\infty \int f_n d\mu < +\infty$.
3. La fonction limite $S = \sum_{n=1}^\infty f_n$ est positive et son intégrale est finie.
4. Par propriété de l'intégrale de Lebesgue, toute fonction positive dont l'intégrale est finie ne peut valoir $+\infty$ que sur un ensemble de mesure nulle.
5. Donc, $S(x) < +\infty$ pour presque tout $x$. Ainsi, la série $\sum f_n(x)$ converge $\mu$-presque partout.
