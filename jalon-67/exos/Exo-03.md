## Exercice 3 : Interversion pour une série double \quad $\bigstar\bigstar\star\star\star$

Soit $(a_{i,j})_{(i,j) \in \mathbb{N}^2}$ une suite double de réels positifs.
**Question :** Montrer formellement via Beppo Levi que $\sum_{i=0}^\infty \sum_{j=0}^\infty a_{i,j} = \sum_{j=0}^\infty \sum_{i=0}^\infty a_{i,j}$.

**Solution :**
1. Munissons $X = \mathbb{N}$ de la mesure de comptage $\mu$. L'intégrale sur cet espace est la somme discrète.
2. Posons pour $i \in \mathbb{N}$, $f_n(i) = \sum_{j=0}^n a_{i,j}$.
3. Comme $a_{i,j} \ge 0$, pour tout $i$, $f_{n+1}(i) \ge f_n(i)$. La suite $(f_n)$ est croissante et positive.
4. La limite ponctuelle est $f(i) = \sum_{j=0}^\infty a_{i,j}$.
5. D'après Beppo Levi, $\int_\mathbb{N} f d\mu = \lim_{n \to \infty} \int_\mathbb{N} f_n d\mu$.
6. Soit : $\sum_{i=0}^\infty \left( \sum_{j=0}^\infty a_{i,j} \right) = \lim_{n \to \infty} \sum_{i=0}^\infty \sum_{j=0}^n a_{i,j}$.
7. Par linéarité sur la somme finie, le membre de droite vaut $\lim_{n \to \infty} \sum_{j=0}^n \sum_{i=0}^\infty a_{i,j} = \sum_{j=0}^\infty \sum_{i=0}^\infty a_{i,j}$. $\blacksquare$
