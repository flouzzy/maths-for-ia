# Exercice 4 : Interversion limite et intégrale

**Difficulté :** $\star\star\star$

**Énoncé :**
Montrer que $\int_0^1 \sum_{n=1}^\infty \frac{x^n}{n^3} dx = \sum_{n=1}^\infty \frac{1}{n^3(n+1)}$.

**Démonstration :**
1. Soit $f_n(x) = \frac{x^n}{n^3}$. Les fonctions $f_n$ sont continues sur le segment $[0, 1]$.
2. Étudions la convergence normale de la série $\sum f_n$ sur $[0, 1]$.
   La fonction $f_n$ est croissante sur $[0, 1]$, donc son supremum est atteint en $x=1$ :
   $$ \|f_n\|_{\infty, [0, 1]} = f_n(1) = \frac{1}{n^3} $$
3. La série numérique $\sum \frac{1}{n^3}$ est une série de Riemann convergente ($\alpha = 3 > 1$).
   Donc la série de fonctions $\sum f_n$ converge normalement, et a fortiori uniformément, sur le segment $[0, 1]$.
4. D'après le théorème d'intégration terme à terme sur un segment (justifié par la convergence uniforme de fonctions continues), on peut intervertir la série et l'intégrale :
   $$ \int_0^1 \left( \sum_{n=1}^\infty f_n(x) \right) dx = \sum_{n=1}^\infty \int_0^1 f_n(x) dx $$
5. Calculons l'intégrale du terme général :
   $$ \int_0^1 \frac{x^n}{n^3} dx = \frac{1}{n^3} \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n^3(n+1)} $$
6. On obtient bien :
   $$ \int_0^1 \sum_{n=1}^\infty \frac{x^n}{n^3} dx = \sum_{n=1}^\infty \frac{1}{n^3(n+1)} $$
$\blacksquare$
