# Exercice 1 : Application directe sur un intervalle borné ★

## Énoncé
Soit $f_n(x) = \left( 1 - \frac{x}{n} \right)^n \mathbf{1}_{[0, n]}(x)$.
Montrer que $f_n$ est croissante et trouver la limite de $\int_0^\infty f_n(x) dx$.

## Correction Détaillée
1. **Mesurabilité et positivité** : Chaque $f_n$ est mesurable et positive sur $\mathbb{R}_+$.
2. **Croissance de la suite** : Pour tout $x \in \mathbb{R}_+$, on a $\ln(f_n(x)) = n \ln(1 - x/n)$. Par concavité du log, la suite $n \mapsto n \ln(1 - x/n)$ est croissante pour $n > x$. Ainsi, $(f_n)_{n \in \mathbb{N}}$ est une suite croissante presque partout.
3. **Limite simple** : Par développement limité, $\lim_{n \to \infty} n \ln(1 - x/n) = -x$, donc $f_n(x) \to e^{-x}$.
4. **Application du TCM** : Le TCM s'applique, donc $\lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty e^{-x} dx = 1$.
