# Exercice 7 : Lemme de Fatou vs TCM $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Montrer par un contre-exemple que si l'hypothèse de monotonie est violée, l'égalité $\int \lim f_n = \lim \int f_n$ peut être fausse, même pour des fonctions positives. Vérifier que l'inégalité de Fatou, elle, reste vraie.

## Correction Détaillée
1. Prenons l'espace $\mathbb{R}$ avec la mesure de Lebesgue.
2. Définissons la "bosse glissante" : $f_n(x) = n \mathbf{1}_{]0, 1/n[}(x)$.
3. Pour tout $n \ge 1$, $\int_{\mathbb{R}} f_n(x) dx = n \times (1/n) = 1$.
   Donc $\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) dx = 1$.
4. Limite ponctuelle :
   - Si $x \le 0$, $f_n(x) = 0$ pour tout $n$.
   - Si $x > 0$, il existe $N$ tel que $1/N < x$. Alors pour tout $n \ge N$, $x \notin ]0, 1/n[$, et $f_n(x) = 0$.
   Donc $\lim_{n \to \infty} f_n(x) = 0$ pour tout $x$. Soit $f(x) = 0$.
5. On calcule l'intégrale de la limite :
   $\int_{\mathbb{R}} f(x) dx = \int_{\mathbb{R}} 0 dx = 0$.
6. On a donc $0 = \int \lim f_n \neq \lim \int f_n = 1$. Le TCM ne s'applique pas car la suite $f_n(x)$ n'est pas croissante (elle augmente à $n$ puis retombe à 0).
7. Le Lemme de Fatou stipule que $\int \liminf f_n \le \liminf \int f_n$.
   Ici, $\liminf f_n = 0$, son intégrale est $0$. Et $\liminf \int f_n = \liminf 1 = 1$.
   L'inégalité $0 \le 1$ est bien vérifiée.
