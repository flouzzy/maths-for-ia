# Exercice 2 : Convergence uniforme et intégration

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit $f_n(x) = \frac{x}{1 + n^2 x^2}$ définie sur $[0, 1]$.
1. Montrer que $(f_n)$ converge uniformément vers $0$ sur $[0, 1]$.
2. Vérifier que $\lim_{n \to \infty} \int_0^1 f_n(x) dx = \int_0^1 \lim_{n \to \infty} f_n(x) dx$.

## Résolution Détaillée

### 1. Convergence uniforme

Pour étudier la convergence uniforme de $(f_n)$ vers la fonction nulle $f(x)=0$, nous étudions la norme infinie.
Calculons la dérivée de $f_n$ :
$$ f_n'(x) = \frac{1(1 + n^2 x^2) - x(2n^2 x)}{(1 + n^2 x^2)^2} = \frac{1 - n^2 x^2}{(1 + n^2 x^2)^2} $$
La dérivée s'annule lorsque $1 - n^2 x^2 = 0$, soit pour $x = \frac{1}{n}$ (puisque $x \in [0, 1]$ et $n \ge 1$).
Le tableau de variation montre que $f_n$ est croissante sur $[0, 1/n]$ et décroissante sur $[1/n, 1]$.
Le maximum global sur $[0, 1]$ est donc atteint en $x = \frac{1}{n}$.
$$ f_n\left(\frac{1}{n}\right) = \frac{\frac{1}{n}}{1 + n^2 \frac{1}{n^2}} = \frac{\frac{1}{n}}{2} = \frac{1}{2n} $$
Ainsi, $\sup_{x \in [0, 1]} |f_n(x) - 0| = \frac{1}{2n}$.
Puisque $\lim_{n \to \infty} \frac{1}{2n} = 0$, la suite $(f_n)$ converge uniformément vers la fonction nulle sur $[0, 1]$.

### 2. Interversion limite et intégrale

Puisque les $f_n$ sont continues sur le segment compact $[0, 1]$ et convergent uniformément vers la fonction nulle qui est continue, le théorème d'interversion limite-intégrale (convergence uniforme sur un segment) s'applique.
Calculons explicitement l'intégrale pour vérifier.
$$ \int_0^1 f_n(x) dx = \int_0^1 \frac{x}{1 + n^2 x^2} dx $$
On remarque la forme $\frac{u'}{u}$. En posant $u = 1 + n^2 x^2$, on a $du = 2n^2 x dx$.
Donc $x dx = \frac{du}{2n^2}$.
$$ \int_0^1 f_n(x) dx = \frac{1}{2n^2} \left[ \ln(1 + n^2 x^2) \right]_0^1 = \frac{\ln(1 + n^2)}{2n^2} $$
Par croissance comparée (le polynôme $n^2$ croît plus vite que le logarithme), on a :
$$ \lim_{n \to \infty} \frac{\ln(1 + n^2)}{2n^2} = 0 $$
Et d'autre part, l'intégrale de la limite simple est :
$$ \int_0^1 0 \, dx = 0 $$
L'égalité est bien vérifiée. $\blacksquare$
