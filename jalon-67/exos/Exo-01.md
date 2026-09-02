# Exo 01 : Introduction aux limites monotones simples ($\bigstar\star\star\star\star$)

## Énoncé
Soit la suite de fonctions $f_n : \mathbb{R}^+ \to \mathbb{R}$ définie par $f_n(x) = \mathbf{1}_{[0, n]}(x) \cdot e^{-x}$.
1. Montrer que la suite $(f_n)_{n \in \mathbb{N}}$ est positive et croissante.
2. Déterminer sa limite simple $f$.
3. Calculer $\int_{\mathbb{R}^+} f_n(x) \, dx$ et vérifier la conclusion du théorème de convergence monotone.

## Correction Détaillée
**Étape 1 : Positivité et croissance**
Pour tout $x \ge 0$ et $n \in \mathbb{N}$, l'exponentielle $e^{-x} > 0$ et la fonction indicatrice $\mathbf{1}_{[0, n]}(x) \in \{0, 1\}$. Ainsi $f_n(x) \ge 0$.
Soit $x \ge 0$ fixé. Puisque $[0, n] \subset [0, n+1]$, on a $\mathbf{1}_{[0, n]}(x) \le \mathbf{1}_{[0, n+1]}(x)$.
En multipliant par $e^{-x} > 0$, il vient $f_n(x) \le f_{n+1}(x)$. La suite est donc croissante.

**Étape 2 : Limite simple**
Pour tout $x \in \mathbb{R}^+$, il existe un entier $N \ge x$. Alors pour tout $n \ge N$, $x \in [0, n]$, donc $\mathbf{1}_{[0, n]}(x) = 1$.
Ainsi, $\lim_{n \to \infty} f_n(x) = e^{-x} \cdot 1 = e^{-x}$. On pose $f(x) = e^{-x}$.

**Étape 3 : Vérification du théorème**
Calculons l'intégrale de $f_n$ par rapport à la mesure de Lebesgue sur $\mathbb{R}^+$ :
$$ \int_0^{+\infty} f_n(x) \, dx = \int_0^n e^{-x} \, dx = \left[ -e^{-x} \right]_0^n = 1 - e^{-n} $$
La limite de ces intégrales est $\lim_{n \to \infty} (1 - e^{-n}) = 1$.
L'intégrale de la limite $f(x)$ est :
$$ \int_0^{+\infty} e^{-x} \, dx = \lim_{M \to \infty} \left[ -e^{-x} \right]_0^M = 1 $$
Les deux quantités coïncident, ce qui illustre le théorème de convergence monotone de Beppo Levi.
