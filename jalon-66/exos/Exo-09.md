# Exercice 9 : Inégalité de Chebyshev pour les moments d'ordre supérieur

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Généraliser l'inégalité de Markov pour démontrer l'inégalité de Chebyshev. Soit $f$ mesurable positive. Démontrer que pour tout $p > 0$ et $a > 0$, $\mu(\{f \geq a\}) \leq \frac{1}{a^p} \int_X f^p \, d\mu$.

**Démonstration :**
L'inégalité de Chebyshev est une conséquence directe de l'inégalité de Markov couplée à la stricte croissance de la fonction puissance sur les réels positifs.
Soit $f$ une fonction mesurable positive, et fixons des constantes $a > 0$ et $p > 0$.
Considérons l'événement (ou l'ensemble de niveau) $A = \{x \in X \mid f(x) \geq a\}$.
Puisque la fonction $t \mapsto t^p$ est strictement croissante et préserve l'ordre sur $[0, +\infty[$, l'inégalité logique suivante est une équivalence stricte :
$$f(x) \geq a \iff (f(x))^p \geq a^p$$
Par conséquent, l'ensemble $A$ peut être réécrit exactement sous la forme :
$$A = \{x \in X \mid f(x)^p \geq a^p\}$$
Posons la fonction $g(x) = (f(x))^p$. Puisque $f$ est mesurable et que $t \mapsto t^p$ est continue, la composition $g$ est une fonction mesurable positive.
Nous appliquons maintenant l'inégalité de Markov classique à la fonction $g$ avec la constante $a^p > 0$.
L'inégalité de Markov énonce que :
$$\mu(\{x \in X \mid g(x) \geq a^p\}) \leq \frac{1}{a^p} \int_X g \, d\mu$$
En remplaçant $g$ par son expression originale $f^p$, nous obtenons immédiatement :
$$\mu(\{x \in X \mid f(x)^p \geq a^p\}) \leq \frac{1}{a^p} \int_X f^p \, d\mu$$
Puisque les deux ensembles sont géométriquement identiques, la mesure de $A$ est strictement bornée par ce terme :
$$\mu(\{f \geq a\}) \leq \frac{1}{a^p} \int_X f^p \, d\mu$$
Cette généralisation montre que si une fonction possède un moment d'ordre élevé fini (par exemple $p=2$, variance en probabilités), la mesure des queues de distribution décroît extrêmement vite (polynomialement en $1/a^p$).
