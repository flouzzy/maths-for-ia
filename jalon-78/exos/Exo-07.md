# Équation différentielle et Fourier

$\bigstar\bigstar\bigstar\bigstar\star$

Trouver toutes les solutions $2\pi$-périodiques et de classe $C^2$ de l'équation différentielle :
$$ y''(t) + 2y'(t) + 2y(t) = \sin^2(t) $$

**Correction détaillée :**
1. Étude du second membre. On linéarise $\sin^2(t) = \frac{1 - \cos(2t)}{2} = \frac{1}{2} - \frac{1}{2}\cos(2t)$.
2. Recherche de solutions en série de Fourier. Si $y$ est une solution $2\pi$-périodique $C^2$, elle se développe en série de Fourier (qui converge normalement vers $y$).
   Posons $y(t) = \sum_{n \in \mathbb{Z}} c_n e^{int}$.
   Alors $y'(t) = \sum_{n \in \mathbb{Z}} (in) c_n e^{int}$ et $y''(t) = \sum_{n \in \mathbb{Z}} (-n^2) c_n e^{int}$.
   L'équation devient :
   $$ \sum_{n \in \mathbb{Z}} c_n (-n^2 + 2in + 2) e^{int} = \frac{1}{2} e^{i0t} - \frac{1}{4} e^{i2t} - \frac{1}{4} e^{-i2t} $$
3. Par unicité des coefficients de Fourier, on identifie terme à terme.
   - Pour $n=0$ : $c_0(2) = 1/2 \implies c_0 = 1/4$.
   - Pour $n=2$ : $c_2(-4 + 4i + 2) = -1/4 \implies c_2(-2 + 4i) = -1/4 \implies c_2 = \frac{-1}{4(-2+4i)} = \frac{-1}{8(-1+2i)} = \frac{-( -1 - 2i )}{8(1^2 + 2^2)} = \frac{1+2i}{40}$.
   - Pour $n=-2$ : $c_{-2}(-4 - 4i + 2) = -1/4 \implies c_{-2} = \frac{-1}{4(-2-4i)} = \frac{1-2i}{40}$.
   - Pour $n \notin \{-2, 0, 2\}$ : le second membre est nul, donc $c_n(-n^2+2in+2) = 0$. Comme $-n^2+2$ n'est jamais nul pour $n$ entier, $c_n = 0$.
4. Recomposition de la solution réelle.
   $$ y(t) = \frac{1}{4} + c_2 e^{i2t} + c_{-2} e^{-i2t} = \frac{1}{4} + \frac{1+2i}{40}(\cos 2t + i\sin 2t) + \frac{1-2i}{40}(\cos 2t - i\sin 2t) $$
   $$ y(t) = \frac{1}{4} + 2 \text{Re}(c_2 e^{i2t}) = \frac{1}{4} + \frac{2}{40} (\cos(2t) - 2\sin(2t)) = \frac{1}{4} + \frac{1}{20}\cos(2t) - \frac{1}{10}\sin(2t) $$
   L'unique solution périodique est $y(t) = \frac{1}{4} + \frac{1}{20}\cos(2t) - \frac{1}{10}\sin(2t)$.