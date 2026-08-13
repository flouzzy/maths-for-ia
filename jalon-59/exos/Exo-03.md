# Exercice 3 : Convergence compacte

## Énoncé
Soit $f_n(x) = e^{-nx}$ sur $]0, +\infty[$.
Montrer que la convergence est compacte mais pas uniforme sur $]0, +\infty[$.

## Correction Détaillée

1. **Limite simple :**
Pour $x > 0$, $\lim_{n \to \infty} e^{-nx} = 0$. Donc la limite simple est $f = 0$.

2. **Convergence uniforme sur $]0, +\infty[$ :**
$\sup_{x \in ]0, +\infty[} |e^{-nx} - 0| = 1$ (obtenu lorsque $x \to 0$).
Puisque le supremum est constant égal à $1$, il ne tend pas vers 0. La convergence n'est pas uniforme.

3. **Convergence compacte (uniforme sur tout compact) :**
Soit $K \subset ]0, +\infty[$ un compact. $K$ est fermé et borné, donc il existe $a > 0$ tel que $K \subset [a, +\infty[$.
Pour tout $x \in K$, on a $x \ge a > 0$.
Donc $e^{-nx} \le e^{-na}$.
Ainsi, $\sup_{x \in K} |f_n(x) - f(x)| \le e^{-na}$.
Or $\lim_{n \to \infty} e^{-na} = 0$.
Donc $\lim_{n \to \infty} \sup_{x \in K} |f_n(x) - f(x)| = 0$.
La convergence est uniforme sur tout compact $K$, c'est-à-dire que la convergence est compacte.
