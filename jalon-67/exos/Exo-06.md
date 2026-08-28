# Exercice 6 : Inégalité de Fatou stricte ★★☆☆☆

**Énoncé :**
Donner un exemple explicite d'une suite de fonctions positives $f_n$ telle que $\int \lim\inf f_n < \lim\inf \int f_n$.

**Correction :**
1. Le lemme de Fatou énonce que $\int \lim\inf f_n \le \lim\inf \int f_n$. Cherchons un cas d'inégalité stricte.
2. On prend l'espace $\mathbb{R}$ avec la mesure de Lebesgue. Soit la 'bosse glissante' : $f_n(x) = \chi_{[n, n+1]}(x)$.
3. Pour tout $x \in \mathbb{R}$, pour $n$ assez grand ($n > x$), $f_n(x) = 0$. Donc $\lim_{n \to \infty} f_n(x) = 0$. La limite inférieure est la fonction nulle $0$.
4. Son intégrale est $\int 0 d\lambda = 0$.
5. D'autre part, pour tout $n$, $\int f_n d\lambda = \lambda([n, n+1]) = 1$. Donc $\lim\inf \int f_n = 1$.
6. On a bien $0 < 1$. L'inégalité stricte se produit à cause de la perte de masse vers l'infini (non compacité). Ce problème n'apparaît jamais avec des suites croissantes.
