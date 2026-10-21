# Exercice 10 : Inégalité de Gibbs et Borne de l'Entropie Croisée

$\bigstar\bigstar\bigstar\bigstar\bigstar$


Soit deux distributions de probabilité discrètes $P = (p_1, \dots, p_N)$ et $Q = (q_1, \dots, q_N)$ avec $p_i, q_i > 0$.
L'inégalité de Gibbs stipule que $-\sum_{i=1}^N p_i \ln p_i \le -\sum_{i=1}^N p_i \ln q_i$.

**1.** Démontrer cette inégalité de manière élémentaire, en utilisant l'inégalité fondamentale $\ln x \le x - 1$ pour tout $x > 0$.
**2.** Déterminer le cas précis où l'égalité est vérifiée.

**Correction :**

**1.** Soit l'expression de la différence entre l'entropie et l'entropie croisée (qui n'est autre que l'opposé de la divergence KL) :
$$-\sum_{i=1}^N p_i \ln q_i - \left( - \sum_{i=1}^N p_i \ln p_i \right) = - \sum_{i=1}^N p_i (\ln q_i - \ln p_i) = - \sum_{i=1}^N p_i \ln\left(\frac{q_i}{p_i}\right)$$
Nous utilisons l'inégalité fondamentale pour le logarithme népérien : $\ln(x) \le x - 1$ (c'est une propriété de la concavité du logarithme : la tangente en $x=1$ est $y=x-1$).
Ainsi, $\ln\left(\frac{q_i}{p_i}\right) \le \frac{q_i}{p_i} - 1$.
En introduisant cela dans la somme :
$$- \sum_{i=1}^N p_i \ln\left(\frac{q_i}{p_i}\right) \ge - \sum_{i=1}^N p_i \left( \frac{q_i}{p_i} - 1 \right)$$
Développons le terme de droite :
$$- \sum_{i=1}^N p_i \left( \frac{q_i}{p_i} - 1 \right) = - \sum_{i=1}^N (q_i - p_i) = - \left( \sum_{i=1}^N q_i - \sum_{i=1}^N p_i \right)$$
Puisque $P$ et $Q$ sont des distributions de probabilité valides, la somme de leurs composantes vaut 1 : $\sum p_i = 1$ et $\sum q_i = 1$.
Par conséquent, la différence vaut :
$$- (1 - 1) = 0$$
Nous avons donc démontré que la différence entre l'entropie croisée et l'entropie est toujours positive ou nulle, soit :
$$H(P, Q) \ge H(P)$$

**2.** L'égalité $\ln x = x - 1$ n'est vérifiée que si et seulement si $x = 1$.
Dans notre cas, cela signifie que pour chaque $i \in \{1, \dots, N\}$, nous devons avoir $\frac{q_i}{p_i} = 1$, ce qui équivaut à $q_i = p_i$.
L'égalité est donc vérifiée si et seulement si les deux distributions sont strictement identiques p.p.
