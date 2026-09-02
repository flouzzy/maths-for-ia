# Exercice 4 : Série de fonctions mesurables ★★★

## Énoncé
Montrer que l'intégrale $\int_0^1 \frac{x \ln(x)}{1-x} dx$ est égale à $-\sum_{n=1}^\infty \frac{1}{(n+1)^2}$.

## Correction Détaillée
1. **Développement en série** : Pour $x \in ]0, 1[$, on a $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
2. **Positivité** : La fonction est négative sur l'intervalle. On va donc étudier $f(x) = \frac{-x \ln(x)}{1-x}$, qui est positive, et l'écrire comme la somme de la série $u_n(x) = -x^{n+1} \ln(x)$, toutes positives sur $]0, 1[$.
3. **Application du corollaire du TCM (intégration terme à terme)** : L'intégrale de la somme est la somme des intégrales : $\int_0^1 \sum_{n=0}^\infty u_n(x) dx = \sum_{n=0}^\infty \int_0^1 -x^{n+1} \ln(x) dx$.
4. **Calcul de l'intégrale** : Par intégration par parties, $\int_0^1 x^{n+1} \ln(x) dx = \left[ \frac{x^{n+2}}{n+2} \ln(x) \right]_0^1 - \int_0^1 \frac{x^{n+1}}{n+2} dx = 0 - \frac{1}{(n+2)^2}$.
5. **Conclusion** : $\int_0^1 f(x) dx = \sum_{n=0}^\infty \frac{1}{(n+2)^2} = \sum_{k=2}^\infty \frac{1}{k^2}$.
