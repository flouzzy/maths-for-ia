# Exercice 7 : Convergence d'une suite de tirages de Bernoulli exponentiels
$\bigstar\bigstar\bigstar\bigstar\star$


Soit $(X_n)$ une suite de variables aléatoires indépendantes telles que $X_n \sim \mathcal{B}(p_n)$ avec $p_n = e^{-n}$.
On définit $Y_n = \max_{1 \leq k \leq n} X_k$.
Montrez, via le lemme de Borel-Cantelli, que $X_n$ converge presque sûrement vers $0$.

**Correction :**
1. L'événement on considère est $A_n = \{ X_n = 1 \} = \{ |X_n - 0| \geq 1 \}$.
2. Calculons la somme des probabilités de ces événements :
$$ \sum_{n=1}^\infty \mathbb{P}(A_n) = \sum_{n=1}^\infty e^{-n} $$
3. Il s'agit d'une série géométrique de raison $q = e^{-1} < 1$. Cette série est donc absolument convergente (la somme finie vaut $\frac{e^{-1}}{1 - e^{-1}}$).
4. Puisque $\sum_{n=1}^\infty \mathbb{P}(A_n) < \infty$, le premier lemme de Borel-Cantelli (Jalon 89) s'applique.
5. Il affirme que la probabilité que les événements $A_n$ se réalisent une infinité de fois est nulle :
$$ \mathbb{P}(\limsup A_n) = \mathbb{P}\left(\bigcap_{n=1}^\infty \bigcup_{k=n}^\infty \{ X_k = 1 \} \right) = 0 $$
6. En passant au complémentaire, avec une probabilité $1$, l'événement $X_k = 1$ ne se réalise qu'un nombre fini de fois. Donc pour tout $\omega$ dans cet ensemble de probabilité $1$, il existe un rang $N(\omega)$ à partir duquel pour tout $n \geq N(\omega)$, $X_n(\omega) = 0$.
7. La suite des valeurs est donc constante égale à $0$ pour $n$ grand. Elle converge vers $0$. On a bien prouvé $X_n \xrightarrow{\text{p.s.}} 0$.
