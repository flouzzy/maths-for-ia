## Exercice 2 : Topologie discrète \quad $\bigstar$

**Énoncé :** Démontrer rigoureusement que la distance discrète $d(x, y) = 1$ si $x \neq y$, et $0$ sinon, induit la topologie discrète (où toute partie est un ouvert).

**Correction :** Considérons la boule ouverte $B(x, 1/2)$.
Par définition, $B(x, 1/2) = \{ y \in X \mid d(x, y) < 1/2 \}$.
Puisque la distance ne prend que les valeurs $0$ et $1$, la condition $d(x, y) < 1/2$ équivaut strictement à $d(x, y) = 0$.
Par l'axiome de séparation, cela équivaut à $y = x$. Donc $B(x, 1/2) = \{x\}$.
Puisqu'une boule ouverte est un ouvert pour la topologie induite, le singleton $\{x\}$ est un ouvert.
Toute partie $A \subset X$ peut s'écrire comme l'union de ses points : $A = \bigcup_{x \in A} \{x\}$.
Une union quelconque d'ouverts étant un ouvert, la partie $A$ est un ouvert. Ainsi, toute partie de $X$ est ouverte, c'est la topologie discrète.
