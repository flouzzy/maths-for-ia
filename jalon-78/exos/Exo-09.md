# Injectivité de la transformation de Fourier discrète

$\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f$ une fonction continue et $2\pi$-périodique. Montrer que si tous ses coefficients de Fourier $c_n(f)$ sont nuls pour tout $n \in \mathbb{Z}$, alors $f$ est la fonction nulle sur $\mathbb{R}$. (On pourra raisonner par l'absurde et construire un polynôme trigonométrique P tel que l'intégrale de fP soit strictement positive).

**Correction détaillée :**
1. Supposons qu'il existe un point $x_0 \in \mathbb{R}$ tel que $f(x_0) \neq 0$. Quitte à considérer $-f(x-x_0)$, on peut supposer $x_0 = 0$ et $f(0) > 0$.
2. Par continuité de $f$ en 0, il existe $\delta > 0$ et $\alpha > 0$ tels que $\forall x \in [-\delta, \delta]$, $f(x) \ge \alpha$.
   Quitte à restreindre $\delta$, on peut imposer $0 < \delta < \pi/2$.
3. On pose le polynôme trigonométrique $P(x) = 1 + \cos(x) - \cos(\delta)$.
   - Sur $[-\delta, \delta]$, $\cos(x) \ge \cos(\delta) \implies P(x) \ge 1$.
   - Sur $[-\pi, \pi] \setminus [-\delta, \delta]$, $\cos(x) < \cos(\delta) \implies P(x) < 1$. $|P(x)|$ peut être géré en ajustant la constante, prenons plutôt un polynôme $Q_k(x) = (P(x))^k$.
   Pour isoler l'intervalle $[-\delta, \delta]$, on considère $\int_{-\pi}^\pi f(x) Q_k(x) dx$.
4. Puisque tous les coefficients de Fourier de $f$ sont nuls, et que $Q_k$ est une combinaison linéaire finie d'exponentielles complexes, l'intégrale $\int_{-\pi}^\pi f(x) Q_k(x) dx$ est une combinaison linéaire des $c_n(f)$, donc elle est NULLE pour tout entier $k$.
5. Or, écrivons l'intégrale : $\int_{-\pi}^\pi f(x) Q_k(x) dx = \int_{-\delta}^\delta f(x) Q_k(x) dx + \int_{[-\pi, \pi] \setminus [-\delta, \delta]} f(x) Q_k(x) dx$.
   - Sur $[-\delta/2, \delta/2]$, $P(x) \ge 1 + \eta$ (avec $\eta > 0$). Donc $Q_k(x) \ge (1+\eta)^k$. Et $f(x) \ge \alpha$.
     L'intégrale sur ce sous-intervalle tend vers $+\infty$.
   - Sur $[-\pi, \pi] \setminus [-\delta, \delta]$, $|P(x)| \le 1$, donc $|Q_k(x)| \le 1$. La fonction $f$ étant bornée (disons par $M$), le reste de l'intégrale est borné par $2\pi M$.
   Par conséquent, pour $k$ assez grand, l'intégrale globale devient strictement positive.
6. C'est une contradiction avec le fait que l'intégrale de $f Q_k$ soit systématiquement nulle. L'hypothèse $f(x_0) \neq 0$ est donc fausse. La fonction est identiquement nulle.
Ce résultat est un cas particulier du théorème d'unicité (les polynômes trigonométriques sont denses dans les fonctions continues).