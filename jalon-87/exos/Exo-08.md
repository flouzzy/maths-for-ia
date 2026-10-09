# Exercice 8 : Calcul de moments par fonction génératrice

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

La fonction génératrice des moments d'une variable aléatoire $X$ est définie par $M_X(t) = \mathbb{E}[e^{tX}]$.
On considère $X$ suivant une loi normale centrée réduite $\mathcal{N}(0,1)$, de densité $f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$.
1. Calculer $M_X(t)$.
2. En utilisant le fait que $\mathbb{E}[X^n] = M_X^{(n)}(0)$ (la $n$-ième dérivée évaluée en 0), calculer $\mathbb{E}[X]$ et $\mathbb{E}[X^2]$.

### Correction détaillée

1. Calcul de la fonction génératrice $M_X(t)$ via le théorème de transfert :
   $$ M_X(t) = \int_{-\infty}^{+\infty} e^{tx} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \, \mathrm{d}x $$
   $$ M_X(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} e^{-\frac{x^2}{2} + tx} \, \mathrm{d}x $$
   On complète le carré dans l'exponentielle :
   $$ -\frac{x^2}{2} + tx = -\frac{1}{2}(x^2 - 2tx) = -\frac{1}{2}( (x - t)^2 - t^2 ) = -\frac{1}{2}(x - t)^2 + \frac{t^2}{2} $$
   En remplaçant :
   $$ M_X(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} e^{-\frac{1}{2}(x - t)^2 + \frac{t^2}{2}} \, \mathrm{d}x = e^{t^2/2} \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}(x - t)^2} \, \mathrm{d}x $$
   L'intégrale restante est l'intégrale de la densité d'une loi normale $\mathcal{N}(t, 1)$ sur $\mathbb{R}$, elle vaut donc $1$.
   On obtient $M_X(t) = e^{t^2/2}$.

2. Dérivons $M_X(t)$ pour obtenir les moments.
   - Moment d'ordre 1 (Espérance) :
     $$ M'_X(t) = \frac{\mathrm{d}}{\mathrm{d}t} \left( e^{t^2/2} \right) = t e^{t^2/2} $$
     Évalué en $t=0$ : $\mathbb{E}[X] = M'_X(0) = 0 \times e^0 = 0$.
     La loi normale centrée réduite a bien une espérance nulle.

   - Moment d'ordre 2 :
     $$ M''_X(t) = \frac{\mathrm{d}}{\mathrm{d}t} \left( t e^{t^2/2} \right) = 1 \cdot e^{t^2/2} + t \cdot (t e^{t^2/2}) = (1 + t^2) e^{t^2/2} $$
     Évalué en $t=0$ : $\mathbb{E}[X^2] = M''_X(0) = (1 + 0^2) e^0 = 1$.
     La variance, $\mathbb{E}[X^2] - (\mathbb{E}[X])^2 = 1 - 0 = 1$, correspond bien au paramètre de la loi.
