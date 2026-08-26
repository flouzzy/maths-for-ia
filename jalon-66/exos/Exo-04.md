### Linéarité de l'intégrale pour des fonctions mesurables (cas simple) \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f$ une fonction mesurable positive, et $\alpha \ge 0$ une constante.
Démontrer rigoureusement à partir de la définition que $\int_X (\alpha f) d\mu = \alpha \int_X f d\mu$.
(Homogénéité de l'intégrale).

**Correction Détaillée :**
**Étape 1 : Traitement du cas trivial $\alpha = 0$.**
Si $\alpha = 0$, alors $\alpha f = 0 \cdot f = 0$.
L'intégrale de la fonction nulle est $0$.
De l'autre côté, $0 \cdot \int_X f d\mu = 0$ (avec la convention $0 \cdot \infty = 0$).
L'égalité est donc vérifiée.

**Étape 2 : Cas $\alpha > 0$.**
Par définition :
$$\int_X (\alpha f) d\mu = \sup \left\{ \int_X t d\mu \mid 0 \le t \le \alpha f, t \text{ simple} \right\}$$
Puisque $\alpha > 0$, la condition $t \le \alpha f$ est équivalente à $\frac{1}{\alpha} t \le f$.
Remarquons que $t$ est une fonction simple si et seulement si $s = \frac{1}{\alpha} t$ est une fonction simple.
Ainsi, lorsque $t$ parcourt l'ensemble des fonctions simples telles que $t \le \alpha f$, la fonction $s = \frac{1}{\alpha} t$ parcourt l'ensemble des fonctions simples telles que $s \le f$.

**Étape 3 : Substitution et propriété du supremum.**
On peut donc réécrire l'ensemble sur lequel on prend le supremum :
$$\int_X (\alpha f) d\mu = \sup \left\{ \int_X (\alpha s) d\mu \mid 0 \le s \le f, s \text{ simple} \right\}$$
Or, on sait déjà que pour une fonction simple $s = \sum a_i \mathbf{1}_{A_i}$, $\alpha s = \sum (\alpha a_i) \mathbf{1}_{A_i}$.
Son intégrale est $\int_X (\alpha s) d\mu = \sum (\alpha a_i) \mu(A_i) = \alpha \sum a_i \mu(A_i) = \alpha \int_X s d\mu$.
L'équation devient :
$$\int_X (\alpha f) d\mu = \sup \left\{ \alpha \int_X s d\mu \mid 0 \le s \le f, s \text{ simple} \right\}$$

**Étape 4 : Sortie de la constante du supremum.**
Puisque $\alpha > 0$, la constante $\alpha$ peut être sortie du supremum : $\sup(c \cdot A) = c \cdot \sup(A)$.
$$\int_X (\alpha f) d\mu = \alpha \sup \left\{ \int_X s d\mu \mid 0 \le s \le f, s \text{ simple} \right\}$$
Le supremum n'est autre que la définition de l'intégrale de $f$ :
$$\int_X (\alpha f) d\mu = \alpha \int_X f d\mu$$

**Conclusion :**
L'homogénéité positive est vérifiée rigoureusement.
