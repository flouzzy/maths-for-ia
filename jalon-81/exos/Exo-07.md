# Exercice 7 : Le principe d'Incertitude d'Heisenberg
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $f \in \mathcal{S}(\mathbb{R})$ telle que $\|f\|_2 = 1$. L'énergie est normalisée à 1.
Définissons les variances temporelle et spatiale : $V_t = \int t^2 |f(t)|^2 dt$ et $V_\xi = \int \xi^2 |\hat{f}(\xi)|^2 d\xi$.
En considérant l'intégrale $\int t f(t) f'(t) dt$ et Cauchy-Schwarz, prouver que $V_t \cdot V_\xi \geq \frac{\pi}{2}$.

**Correction :**
1. $\int \xi^2 |\hat{f}(\xi)|^2 d\xi = \int |\widehat{f'}(\xi)|^2 d\xi = 2\pi \int |f'(t)|^2 dt$ par Plancherel et les propriétés de dérivation de Fourier. Donc $V_\xi = 2\pi \int |f'(t)|^2 dt$.
2. Considérons $\int_{-\infty}^\infty t f(t) f'(t) dt$. (on suppose $f$ à valeurs réelles pour simplifier).
Par IPP : $\int t f(t) f'(t) dt = \left[ t \frac{f(t)^2}{2} \right]_{-\infty}^\infty - \int \frac{f(t)^2}{2} dt$.
Le terme de bord s'annule car $f \in \mathcal{S}$. Donc l'intégrale vaut $-1/2 \|f\|_2^2 = -1/2$.
3. Appliquons Cauchy-Schwarz :
$|-\frac{1}{2}|^2 \leq \left( \int |t f(t)| |f'(t)| dt \right)^2 \leq \left( \int t^2 |f(t)|^2 dt \right) \left( \int |f'(t)|^2 dt \right)$
$\frac{1}{4} \leq V_t \cdot \frac{V_\xi}{2\pi}$
Donc $V_t \cdot V_\xi \geq \frac{\pi}{2}$.
Un signal ne peut pas être à la fois très concentré dans le temps et dans les fréquences !
