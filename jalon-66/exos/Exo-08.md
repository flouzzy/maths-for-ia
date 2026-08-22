# Exercice 8 : Égalité presque partout et intégrale $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré, et $f, g \in \mathcal{M}_+(X, \mathcal{F})$ deux fonctions mesurables positives.
Prouver rigoureusement que si $f = g$ $\mu$-presque partout, alors $\int_X f \, d\mu = \int_X g \, d\mu$.

**Correction Détaillée :**
1. Dire que $f = g$ presque partout signifie qu'il existe un ensemble mesurable $N \in \mathcal{F}$ tel que $\mu(N) = 0$ et pour tout $x \in X \setminus N$, $f(x) = g(x)$.
2. Nous utilisons la linéarité (pas encore démontrée dans le cours général, donc on va le faire par construction étagée).
   Écrivons la décomposition disjointe de l'espace : $X = (X \setminus N) \cup N$.
3. Une fonction étagée $s \le f$ peut s'écrire $s = s \cdot \mathbf{1}_{X \setminus N} + s \cdot \mathbf{1}_N$.
   Son intégrale est $\int s \, d\mu = \int s \cdot \mathbf{1}_{X \setminus N} \, d\mu + \int s \cdot \mathbf{1}_N \, d\mu$.
4. Or, $s \cdot \mathbf{1}_N \le \|s\|_{\infty} \mathbf{1}_N$, donc son intégrale est majorée par $C \cdot \mu(N) = 0$.
   Ainsi, $\int s \, d\mu = \int s \cdot \mathbf{1}_{X \setminus N} \, d\mu$.
5. Sur l'ensemble $X \setminus N$, on a $f = g$. Donc si $s \le f$ sur $X$, alors $s \le g$ sur $X \setminus N$.
   Soit la fonction $\tilde{s} = s \cdot \mathbf{1}_{X \setminus N}$. On a $\tilde{s} \in \mathcal{E}_+$ et $\tilde{s} \le g$ sur $X$ entier (car sur $N$, $\tilde{s}=0 \le g$).
6. L'intégrale de $\tilde{s}$ est exactement la même que l'intégrale de $s$.
   Donc $\int s \, d\mu = \int \tilde{s} \, d\mu \le \int g \, d\mu$ (puisque $\tilde{s}$ est une candidate pour le supremum définissant l'intégrale de $g$).
7. Comme ceci est vrai pour toute fonction étagée $s \le f$, on passe au supremum à gauche :
   $$\int_X f \, d\mu \le \int_X g \, d\mu$$
8. Par symétrie (les rôles de $f$ et $g$ sont totalement interchangeables car $g = f$ sur $X \setminus N$), on prouve de la même manière que $\int_X g \, d\mu \le \int_X f \, d\mu$.
9. Les deux intégrales (éventuellement infinies) sont donc égales.
