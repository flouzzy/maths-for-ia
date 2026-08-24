# Exercice 2 : Mesure de comptage et séries \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $\mathbb{N}$ muni de la mesure de comptage $\mu$. Calculer $\int_\mathbb{N} f \, d\mu$ pour la fonction $f(n) = \frac{1}{3^n}$.

**Correction :**
Pour la mesure de comptage sur $\mathbb{N}$, l'intégrale de Lebesgue coïncide exactement avec la somme de la série de terme général $f(n)$.
1. Par définition pour une fonction discrète positive, $\int_\mathbb{N} f \, d\mu = \sum_{n=0}^\infty f(n)$.
2. Ici, $\int_\mathbb{N} f \, d\mu = \sum_{n=0}^\infty \frac{1}{3^n}$.
3. On reconnaît une série géométrique de raison $q = 1/3$. Comme $|q| < 1$, la série converge.
4. La somme est $\frac{1}{1 - 1/3} = \frac{1}{2/3} = \frac{3}{2}$.
