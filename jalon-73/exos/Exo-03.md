# Exercice 3 : Limite de normes Lp

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $f : [0, 1] \to \mathbb{R}$ définie par $f(x) = x$. L'espace $[0, 1]$ est muni de la mesure de Lebesgue $\lambda$.

1. Pour $p \ge 1$, calculer $\|f\|_p$.
2. Calculer le supremum essentiel $\|f\|_\infty$.
3. Montrer rigoureusement par le calcul que $\lim_{p \to +\infty} \|f\|_p = \|f\|_\infty$.

---

## Correction détaillée

1. **Calcul de $\|f\|_p$ :**
   Pour tout $p \ge 1$, la fonction $x \mapsto x^p$ est continue sur le segment $[0, 1]$, donc intégrable au sens de Riemann et de Lebesgue.
   $$ \|f\|_p = \left( \int_0^1 |x|^p \, dx \right)^{1/p} $$
   $$ \int_0^1 x^p \, dx = \left[ \frac{x^{p+1}}{p+1} \right]_0^1 = \frac{1}{p+1} $$
   Donc :
   $$ \|f\|_p = \left( \frac{1}{p+1} \right)^{1/p} $$

2. **Calcul de $\|f\|_\infty$ :**
   La fonction $f(x) = x$ est continue et strictement croissante sur $[0, 1]$. Son maximum est atteint en $x=1$ et vaut 1.
   Puisque l'ensemble $\{x \in [0, 1] \mid f(x) > 1\}$ est vide (donc de mesure nulle), et pour tout $\epsilon > 0$, l'ensemble $\{x \in [0, 1] \mid f(x) > 1 - \epsilon\} = ]1-\epsilon, 1]$ a une mesure strictement positive ($\epsilon$), on a :
   $$ \|f\|_\infty = 1 $$

3. **Preuve de la limite :**
   Étudions la limite de $\|f\|_p = (p+1)^{-1/p}$ lorsque $p \to +\infty$.
   Passons au logarithme :
   $$ \ln(\|f\|_p) = -\frac{1}{p} \ln(p+1) $$
   Par croissances comparées, on sait que $\lim_{p \to +\infty} \frac{\ln(p+1)}{p} = 0$.
   Donc $\lim_{p \to +\infty} \ln(\|f\|_p) = 0$.
   En composant par l'exponentielle (qui est continue) :
   $$ \lim_{p \to +\infty} \|f\|_p = e^0 = 1 = \|f\|_\infty $$
   Ceci est un cas particulier d'un théorème très général pour toute fonction $f \in L^\infty$ sur un espace de mesure finie.
