# Exercice 7 : Espace de suites à poids

## Énoncé

Soit l'espace $\ell^2_w$ des suites telles que $\sum n |x_n|^2 < \infty$. Quel est son dual ?

*Niveau de difficulté :* $\bigstar\bigstar\bigstar\bigstar\star$

## Correction

1. **Isométrie :** Considérons l'application $T : \ell^2_w \to \ell^2$ définie par $T(x_n) = (\sqrt{n} x_n)$. Elle est bijective et préserve la norme. C'est une isométrie.
2. **Théorème de Riesz :** Tout espace de Hilbert s'identifie isométriquement à son dual via $x \mapsto \langle \cdot, x \rangle$.
3. **Forme explicite :** Une forme linéaire sur $\ell^2_w$ s'écrit $L(x) = \sum x_n y_n$. Pour que $L$ soit continue, il faut utiliser Cauchy-Schwarz : $|L(x)| \le \sum |\sqrt{n} x_n| |\frac{y_n}{\sqrt{n}}| \le (\sum n |x_n|^2)^{1/2} (\sum \frac{|y_n|^2}{n})^{1/2}$.
4. **Conclusion :** L'espace dual de $\ell^2_w$ peut s'identifier à l'espace des suites $(y_n)$ telles que $\sum \frac{|y_n|^2}{n} < \infty$. C'est un espace de suites avec un poids inverse.
