## La fonction maximum de deux fonctions mesurables \quad $\bigstar\bigstar\star\star\star$

Soient $f$ et $g$ deux fonctions mesurables définies sur un espace mesurable $(X, \mathcal{F})$ et à valeurs dans $\mathbb{R}$.
Démontrez que la fonction $h(x) = \max(f(x), g(x))$ est mesurable.

### Correction Détaillée

Pour montrer que $h$ est mesurable, il suffit de prouver que pour tout réel $a \in \mathbb{R}$, l'ensemble $h^{-1}(]a, +\infty[) = \{x \in X \mid h(x) > a\} \in \mathcal{F}$.

Analysons la condition : $h(x) > a \iff \max(f(x), g(x)) > a$.
Le maximum de deux nombres est strictement supérieur à $a$ si et seulement si l'un au moins des deux nombres est strictement supérieur à $a$.
Par conséquent, logiquement :
$$ \max(f(x), g(x)) > a \iff (f(x) > a) \text{ ou } (g(x) > a) $$

Traduisons cette équivalence logique en termes ensemblistes :
$$ \{x \in X \mid h(x) > a\} = \{x \in X \mid f(x) > a\} \cup \{x \in X \mid g(x) > a\} $$
Soit :
$$ h^{-1}(]a, +\infty[) = f^{-1}(]a, +\infty[) \cup g^{-1}(]a, +\infty[) $$

Analysons les propriétés des ensembles impliqués :
1. Puisque $f$ est mesurable, $f^{-1}(]a, +\infty[) \in \mathcal{F}$.
2. Puisque $g$ est mesurable, $g^{-1}(]a, +\infty[) \in \mathcal{F}$.
3. Par définition (Axiome 3), une tribu est stable par union. Donc l'union de ces deux ensembles appartient à $\mathcal{F}$.

Conclusion : Pour tout $a$, $h^{-1}(]a, +\infty[) \in \mathcal{F}$, ce qui prouve que $h = \max(f, g)$ est mesurable.
