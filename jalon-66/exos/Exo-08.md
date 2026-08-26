### Support d'une fonction et mesure nulle \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+$. Soit $E = \{x \in X \mid f(x) > 0\}$ le support strict de $f$.
Montrer que si $\mu(E) = 0$, alors $\int_X f d\mu = 0$.

**Correction Détaillée :**
**Étape 1 : Les fonctions simples minorantes.**
Soit $s$ une fonction simple telle que $0 \le s \le f$.
$s$ s'écrit $s = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$, où on suppose que $a_i > 0$ et les $A_i$ sont disjoints.
Puisque $s(x) \le f(x)$, si $s(x) > 0$, alors on a obligatoirement $f(x) > 0$.
Donc pour tout $x \in A_i$, on a $f(x) \ge a_i > 0$, d'où $x \in E$.
Cela implique que $A_i \subset E$ pour tout $i$.

**Étape 2 : Mesure des ensembles de niveau de s.**
Par la propriété de monotonie de la mesure, si $A_i \subset E$, alors $\mu(A_i) \le \mu(E)$.
Par hypothèse, $\mu(E) = 0$. Donc $\mu(A_i) \le 0$.
Comme une mesure est positive, on a $\mu(A_i) = 0$ pour tout $i$.

**Étape 3 : Intégrale de s.**
L'intégrale de la fonction simple est :
$$\int_X s d\mu = \sum_{i=1}^k a_i \mu(A_i) = \sum_{i=1}^k a_i \cdot 0 = 0$$

**Étape 4 : Passage au supremum.**
Par définition, l'intégrale de $f$ est le supremum de ces intégrales :
$$\int_X f d\mu = \sup_{0 \le s \le f} \int_X s d\mu = \sup_{0 \le s \le f} 0 = 0$$

**Conclusion :**
Une fonction qui est non-nulle uniquement sur un ensemble de mesure nulle a une intégrale nulle. Combiné au résultat du cours, on a l'équivalence : $\int f d\mu = 0 \iff f = 0$ presque partout.
