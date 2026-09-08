# Exercice 2 : Intégrale de la série géométrique pondérée

**Difficulté :** $\bigstar\bigstar\☆☆\☆☆$

## Énoncé

Calculer la limite $\lim_{n \to \infty} \int_{0}^1 \sum_{k=1}^n x^k (-\ln(x)) dx$ en justifiant l'interversion limite-intégrale.

## Démonstration rigoureuse pas à pas

La fonction $f_n(x) = \sum_{k=1}^n x^k (-\ln(x))$ est positive sur $]0, 1[$ car $-\ln(x) > 0$. La suite $(f_n)$ est une somme de termes positifs, donc la suite des sommes partielles croît vers la série $f(x) = \sum_{k=1}^\infty -x^k \ln(x)$. Par le corollaire de convergence monotone, $\int \lim f_n = \sum_{k=1}^\infty \int -x^k \ln(x) dx$. Une IPP donne $\int_0^1 -x^k \ln(x) dx = \frac{1}{(k+1)^2}$. La somme est donc $\sum_{k=1}^\infty \frac{1}{(k+1)^2} = \frac{\pi^2}{6}-1$ (somme de Bâle sans le premier terme).
