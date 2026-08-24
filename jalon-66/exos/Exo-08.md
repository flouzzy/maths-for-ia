# Exercice 8 : Calcul d'aire avec mesure pondérée \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ un espace mesuré où $\mu(\{n\}) = \frac{1}{n!}$. Calculer l'intégrale $\int_\mathbb{N} 2^n \, d\mu(n)$.

**Correction :**
Ici, la mesure $\mu$ n'est pas la mesure de comptage classique, mais une mesure pondérée (qui est finie d'ailleurs, car $\mu(\mathbb{N}) = e$).
1. Pour une fonction sur un ensemble dénombrable avec une mesure discrète, l'intégrale de Lebesgue est la somme de la série pondérée par la mesure des singletons.
2. $\int_\mathbb{N} f \, d\mu = \sum_{n=0}^\infty f(n) \mu(\{n\})$.
3. Remplaçons $f(n)$ et $\mu$ : $\int_\mathbb{N} 2^n \, d\mu = \sum_{n=0}^\infty 2^n \frac{1}{n!} = \sum_{n=0}^\infty \frac{2^n}{n!}$.
4. On reconnaît la série entière de l'exponentielle évaluée en $x = 2$ : $e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$.
5. La valeur de cette intégrale est donc exactement $e^2$.
