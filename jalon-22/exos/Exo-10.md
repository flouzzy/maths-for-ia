# Exercice 10 : Un problème d'interversion subtil

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Soit $f_n(x) = n x e^{-n x^2}$.
1. Calculer $\lim_{n \to \infty} \int_0^1 f_n(x) dx$.
2. Calculer $\int_0^1 (\lim_{n \to \infty} f_n(x)) dx$.
3. Expliquer rigoureusement pourquoi les deux résultats diffèrent et analyser la convergence de $f_n$ sur $[0, 1]$.

**Démonstration :**
*Note : Ceci est une suite de fonctions, mais l'analyse du défaut d'interversion limite-intégrale est le pilier de la compréhension des séries de fonctions (via $S_n$).*
1. **Limite de l'intégrale :**
   Calculons l'intégrale pour un entier $n$ fixé :
   $$ \int_0^1 n x e^{-n x^2} dx $$
   On reconnaît la dérivée de $e^{-n x^2}$. En effet, la dérivée de $x \mapsto e^{-n x^2}$ est $-2n x e^{-n x^2}$.
   Donc, $\int_0^1 n x e^{-n x^2} dx = \left[ -\frac{1}{2} e^{-n x^2} \right]_0^1 = -\frac{1}{2} (e^{-n} - 1) = \frac{1}{2} (1 - e^{-n})$.
   En passant à la limite :
   $$ \lim_{n \to \infty} \int_0^1 f_n(x) dx = \lim_{n \to \infty} \frac{1}{2} (1 - e^{-n}) = \frac{1}{2} $$

2. **Intégrale de la limite :**
   Étudions la limite simple de $f_n(x)$ sur $[0, 1]$.
   - Si $x = 0$, $f_n(0) = 0$, donc $\lim_{n \to \infty} f_n(0) = 0$.
   - Si $x \in ]0, 1]$, l'exponentielle l'emporte sur toute puissance, donc $\lim_{n \to \infty} n x e^{-n x^2} = 0$.
   Donc, pour tout $x \in [0, 1]$, la limite ponctuelle est la fonction nulle $f(x) = 0$.
   L'intégrale de cette limite est donc :
   $$ \int_0^1 f(x) dx = \int_0^1 0 dx = 0 $$

3. **Analyse du défaut d'interversion :**
   On a $\lim \int f_n = 1/2 \neq 0 = \int \lim f_n$. Le théorème d'interversion ne s'applique pas. L'hypothèse manquante est la **convergence uniforme** de $f_n$ vers $0$ sur $[0, 1]$.
   Calculons la norme infinie de $f_n$. La dérivée est :
   $f_n'(x) = n e^{-n x^2} + n x (-2n x) e^{-n x^2} = n e^{-n x^2} (1 - 2n x^2)$.
   La dérivée s'annule en $x_n = \frac{1}{\sqrt{2n}}$.
   Le maximum est donc $f_n(x_n) = n \frac{1}{\sqrt{2n}} e^{-1/2} = \sqrt{\frac{n}{2}} e^{-1/2}$.
   La norme infinie $\|f_n\|_{\infty} = \sqrt{\frac{n}{2}} e^{-1/2}$ tend vers $+\infty$ quand $n \to \infty$.
   Elle ne tend pas vers 0, donc il n'y a pas convergence uniforme. La "bosse glissante" s'échappe vers la gauche et monte à l'infini, capturant une aire de $1/2$ qui échappe à la limite ponctuelle.
$\blacksquare$
