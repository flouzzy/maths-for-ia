## Exercice 5 : Dualité temporelle-fréquentielle et inégalité d'Heisenberg \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Considérons l'espace de Hilbert $L^2(\mathbb{R})$. Soit $f \in \mathcal{S}(\mathbb{R})$ telle que $\|f\|_2 = 1$.
1. Rappeler les expressions de la variance en position $V_x$ et la variance en impulsion (fréquence) $V_\xi$, pour une fonction centrée en $0$ dans les deux domaines.
2. Démontrer le principe d'incertitude d'Heisenberg : $V_x V_\xi \ge \frac{1}{4}$.
*(Indication : Utiliser l'intégration par parties sur l'intégrale $\int t f(t) f'(t) dt$ et Cauchy-Schwarz)*

**Correction :**
1. **Variances :**
Comme $\|f\|_2 = 1$ et l'identité de Plancherel stipule $\|\hat{f}\|_2^2 = 2\pi$, la densité de probabilité dans l'espace des positions est $|f(t)|^2$, et dans l'espace des fréquences $\frac{1}{2\pi} |\hat{f}(\xi)|^2$.
Pour des densités centrées en zéro :
$$ V_x = \int_{\mathbb{R}} t^2 |f(t)|^2 dt = \| t \mapsto t f(t) \|_2^2 $$
$$ V_\xi = \frac{1}{2\pi} \int_{\mathbb{R}} \xi^2 |\hat{f}(\xi)|^2 d\xi $$
Or, on sait que $\mathcal{F}(f')(\xi) = i\xi \hat{f}(\xi)$. Par suite, $|\mathcal{F}(f')(\xi)|^2 = \xi^2 |\hat{f}(\xi)|^2$.
En appliquant Plancherel à $f'$ : $\frac{1}{2\pi} \int |\mathcal{F}(f')(\xi)|^2 d\xi = \int |f'(t)|^2 dt$.
Donc, $V_\xi = \|f'\|_2^2 = \int_{\mathbb{R}} |f'(t)|^2 dt$.

2. **Démonstration de l'inégalité d'Heisenberg :**
Considérons l'intégrale de $t (f(t) \overline{f'(t)} + \overline{f(t)} f'(t)) = t \frac{d}{dt} |f(t)|^2$.
Intégrons par parties sur $[-R, R]$ :
$$ \int_{-R}^{R} t \frac{d}{dt} |f(t)|^2 dt = \left[ t |f(t)|^2 \right]_{-R}^{R} - \int_{-R}^{R} |f(t)|^2 dt $$
Comme $f \in \mathcal{S}$, $|f(t)|^2$ décroît plus vite que tout polynôme, donc $\lim_{R \to \infty} R|f(\pm R)|^2 = 0$.
Par passage à la limite :
$$ \int_{\mathbb{R}} t (f(t) \overline{f'(t)} + \overline{f(t)} f'(t)) dt = - \int_{\mathbb{R}} |f(t)|^2 dt = - \|f\|_2^2 = -1 $$
La quantité sous l'intégrale de gauche est $2 \text{Re}(t f(t) \overline{f'(t)})$.
Ainsi, $2 \text{Re} \int_{\mathbb{R}} t f(t) \overline{f'(t)} dt = -1$.
Le module d'un nombre réel est égal au module de sa partie réelle (au signe près), et la partie réelle est inférieure au module du nombre complexe global :
$$ 1 = \left| 2 \text{Re} \int_{\mathbb{R}} t f(t) \overline{f'(t)} dt \right| \le 2 \int_{\mathbb{R}} |t f(t) \overline{f'(t)}| dt $$
Par l'inégalité de Cauchy-Schwarz appliquée aux fonctions $t f(t)$ et $f'(t)$ :
$$ 1 \le 2 \left( \int_{\mathbb{R}} |t f(t)|^2 dt \right)^{1/2} \left( \int_{\mathbb{R}} |f'(t)|^2 dt \right)^{1/2} = 2 \sqrt{V_x} \sqrt{V_\xi} $$
En élevant au carré et en divisant par 4, nous obtenons l'inégalité stricte :
$$ V_x V_\xi \ge \frac{1}{4} $$
Cela signifie physiquement qu'il est impossible qu'un signal soit arbitrairement concentré simultanément dans le temps (petite $V_x$) et dans la fréquence (petite $V_\xi$).
