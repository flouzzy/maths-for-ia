# Exercice 7 : Application à la série harmonique ★★★☆☆

**Énoncé :**
Etudier $\int_0^1 \sum_{n=1}^\infty x^n dx$ en justifiant chaque étape.

**Correction :**
1. On a une série de fonctions $u_n(x) = x^n$.
2. Sur l'intervalle $[0, 1]$, pour tout $n \ge 1$, $u_n(x) \ge 0$. Les fonctions sont mesurables car continues.
3. On peut appliquer le théorème de Beppo Levi pour intervertir somme et intégrale.
4. $\int_0^1 \sum_{n=1}^\infty x^n dx = \sum_{n=1}^\infty \int_0^1 x^n dx$.
5. On calcule l'intégrale : $\int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}$.
6. Donc l'intégrale de la somme vaut $\sum_{n=1}^\infty \frac{1}{n+1} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots$.
7. Il s'agit de la série harmonique tronquée, qui diverge vers $+\infty$. L'intégrale vaut donc $+\infty$.
