# Exercice 10 : Égalité dans le Lemme de Fatou
$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $(f_n)$ une suite de fonctions positives intégrables sur $(X, \mathcal{A}, \mu)$ convergeant ponctuellement presque partout vers une fonction intégrable $f$.
Montrer l'équivalence suivante :
$$\int_X f d\mu = \lim_{n \to \infty} \int_X f_n d\mu \quad \iff \quad \lim_{n \to \infty} \int_X |f_n - f| d\mu = 0$$
(Ce résultat est un corollaire très puissant appelé Théorème de Scheffé, souvent prouvé via Fatou).

## Correction
Il s'agit de montrer que la convergence des intégrales (convergence en moyenne faible) équivaut à la convergence dans l'espace $L^1$ (convergence forte), sachant la convergence presque partout.

**Sens réciproque $(\impliedby)$ :**
Supposons que $\lim_{n \to \infty} \int_X |f_n - f| d\mu = 0$.
Par l'inégalité triangulaire inverse pour les intégrales :
$$\left| \int_X f_n d\mu - \int_X f d\mu \right| = \left| \int_X (f_n - f) d\mu \right| \leq \int_X |f_n - f| d\mu$$
En passant à la limite $n \to \infty$, le majorant tend vers $0$.
Donc le membre de gauche tend vers $0$, ce qui signifie que $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$.
Cette implication est triviale et n'utilise pas l'hypothèse de positivité.

**Sens direct $(\implies)$ :**
C'est ici que réside la difficulté.
Supposons que $\int_X f_n d\mu \to \int_X f d\mu$.
Considérons la suite de fonctions $g_n = (f_n - f)^-$, c'est-à-dire la partie négative de $f_n - f$.
On a $(f_n - f)^- = \max(0, -(f_n - f)) = \max(0, f - f_n)$.
Puisque les fonctions sont positives, $f_n \geq 0$, donc $f - f_n \leq f$.
Ainsi, $0 \leq g_n \leq f$ pour tout $n$.
La suite $(g_n)$ est dominée par $f$ (qui est intégrable par hypothèse) et $g_n(x) \to (f(x) - f(x))^- = 0$ p.p.
Par le Théorème de Convergence Dominée de Lebesgue (ou Fatou dominé), on a :
$$\lim_{n \to \infty} \int_X g_n d\mu = 0$$

Maintenant, rappelons que $f_n - f = (f_n - f)^+ - (f_n - f)^-$.
En intégrant :
$$\int_X (f_n - f) d\mu = \int_X (f_n - f)^+ d\mu - \int_X (f_n - f)^- d\mu$$
Par hypothèse, $\int_X f_n d\mu - \int_X f d\mu \to 0$, donc $\int_X (f_n - f) d\mu \to 0$.
Ainsi :
$$0 = \lim_{n \to \infty} \left( \int_X (f_n - f)^+ d\mu - \int_X g_n d\mu \right)$$
Comme $\lim \int_X g_n d\mu = 0$, on en déduit que :
$$\lim_{n \to \infty} \int_X (f_n - f)^+ d\mu = 0$$

Enfin, $|f_n - f| = (f_n - f)^+ + (f_n - f)^- = (f_n - f)^+ + g_n$.
En intégrant :
$$\int_X |f_n - f| d\mu = \int_X (f_n - f)^+ d\mu + \int_X g_n d\mu$$
Les deux termes de droite tendent vers $0$.
Donc $\lim_{n \to \infty} \int_X |f_n - f| d\mu = 0 + 0 = 0$.
La preuve est achevée.
