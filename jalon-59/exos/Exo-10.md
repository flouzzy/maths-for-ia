# Exercice 10 : Équicontinuité des primitives

## Énoncé
Soit $(f_n)$ une suite de fonctions continues sur $[0, 1]$ telles que la suite soit bornée dans $L^2([0, 1])$, c'est-à-dire qu'il existe $M > 0$ tel que $\int_0^1 |f_n(t)|^2 dt \le M$ pour tout $n$.
On pose $F_n(x) = \int_0^x f_n(t) dt$.
Montrer que la suite $(F_n)$ admet une sous-suite uniformément convergente.

## Correction Détaillée

Il s'agit d'appliquer le théorème d'Arzelà-Ascoli sur la famille $\mathcal{F} = \{F_n \mid n \in \mathbb{N}\}$.

1. **Équicontinuité par Cauchy-Schwarz :**
Pour $x, y \in [0, 1]$ avec $x \le y$ :
$|F_n(y) - F_n(x)| = \left|\int_x^y f_n(t) dt\right| = \left|\int_x^y 1 \cdot f_n(t) dt\right|$.
En appliquant l'inégalité de Cauchy-Schwarz :
$\left(\int_x^y 1 \cdot f_n(t) dt\right)^2 \le \left(\int_x^y 1^2 dt\right) \left(\int_x^y |f_n(t)|^2 dt\right) = (y-x) \int_x^y |f_n(t)|^2 dt$.
Or, $\int_x^y |f_n(t)|^2 dt \le \int_0^1 |f_n(t)|^2 dt \le M$.
Donc $|F_n(y) - F_n(x)| \le \sqrt{M(y-x)}$.
Pour $\epsilon > 0$, en prenant $\delta = \frac{\epsilon^2}{M}$, on a $|x-y| < \delta \implies |F_n(y) - F_n(x)| < \epsilon$.
L'équicontinuité est démontrée.

2. **Bornitude :**
$|F_n(x)| = |F_n(x) - F_n(0)| \le \sqrt{M x} \le \sqrt{M}$.
La famille est donc uniformément bornée par $\sqrt{M}$.

3. **Conclusion :**
Les fonctions $F_n$ sont définies sur un compact, sont équicontinues et ponctuellement bornées. D'après le théorème d'Arzelà-Ascoli, la suite $(F_n)$ admet une sous-suite uniformément convergente.
