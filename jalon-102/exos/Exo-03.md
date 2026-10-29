$\bigstar\bigstar\star\star\star$
**Énoncé :** Opérateur linéaire continu et convergence faible.
Soient $E$ et $F$ deux espaces de Banach, et $T : E \to F$ un opérateur linéaire continu.
Montrer que si $x_n \rightharpoonup x$ dans $E$, alors $T(x_n) \rightharpoonup T(x)$ dans $F$.

**Correction Détaillée :**
Soit $(x_n)$ une suite de $E$ convergeant faiblement vers $x$.
Pour montrer que $T(x_n) \rightharpoonup T(x)$ dans $F$, il faut montrer que pour toute forme linéaire continue $\phi \in F^*$, on a $\lim_{n \to \infty} \phi(T(x_n)) = \phi(T(x))$.
Considérons la composée $L = \phi \circ T$. Puisque $\phi$ et $T$ sont linéaires et continus, $L$ est une forme linéaire continue sur $E$, c'est-à-dire $L \in E^*$.
Par définition de la convergence faible de $x_n$ vers $x$ dans $E$, on sait que pour cette forme $L$ particulière :
$\lim_{n \to \infty} L(x_n) = L(x)$.
En remplaçant $L$ par son expression, on obtient :
$\lim_{n \to \infty} \phi(T(x_n)) = \phi(T(x))$.
Puisque cela est vrai pour tout $\phi \in F^*$, on conclut que $T(x_n)$ converge faiblement vers $T(x)$ dans $F$.
