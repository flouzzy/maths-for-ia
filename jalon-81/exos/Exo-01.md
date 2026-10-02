# Exercice 1 : Calcul de norme $L^2$ et application directe de Plancherel
$\bigstar\star\star\star\star$

**Énoncé :**
Soit la fonction $f(t) = e^{-2|t|}$.
1. Montrer que $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
2. Calculer sa transformée de Fourier $\hat{f}(\xi)$.
3. Vérifier explicitement l'égalité de Plancherel pour cette fonction.

---
**Correction :**
**Question 1 : Appartenance aux espaces $L^1$ et $L^2$**
La fonction $f(t) = e^{-2|t|}$ est paire et continue sur $\mathbb{R}$.
Calculons son intégrale sur $\mathbb{R}$ :
$$ \|f\|_1 = \int_{-\infty}^{+\infty} e^{-2|t|} dt = 2 \int_{0}^{+\infty} e^{-2t} dt = 2 \left[ \frac{e^{-2t}}{-2} \right]_0^{+\infty} = 2 \times \frac{1}{2} = 1 $$
Puisque $\|f\|_1 < +\infty$, $f \in L^1(\mathbb{R})$.
Calculons la norme $L^2$ de $f$ :
$$ \|f\|_2^2 = \int_{-\infty}^{+\infty} \left(e^{-2|t|}\right)^2 dt = \int_{-\infty}^{+\infty} e^{-4|t|} dt = 2 \int_{0}^{+\infty} e^{-4t} dt = 2 \left[ \frac{e^{-4t}}{-4} \right]_0^{+\infty} = 2 \times \frac{1}{4} = \frac{1}{2} $$
Puisque $\|f\|_2^2 < +\infty$, $f \in L^2(\mathbb{R})$. Ainsi, $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.

**Question 2 : Transformée de Fourier**
Par définition, $\hat{f}(\xi) = \int_{-\infty}^{+\infty} e^{-2|t|} e^{-i\xi t} dt$.
En séparant l'intégrale sur $\mathbb{R}^-$ et $\mathbb{R}^+$ :
$$ \hat{f}(\xi) = \int_{-\infty}^{0} e^{2t} e^{-i\xi t} dt + \int_{0}^{+\infty} e^{-2t} e^{-i\xi t} dt $$
$$ \hat{f}(\xi) = \int_{-\infty}^{0} e^{(2-i\xi)t} dt + \int_{0}^{+\infty} e^{-(2+i\xi)t} dt $$
$$ \hat{f}(\xi) = \left[ \frac{e^{(2-i\xi)t}}{2-i\xi} \right]_{-\infty}^0 + \left[ \frac{e^{-(2+i\xi)t}}{-(2+i\xi)} \right]_0^{+\infty} $$
$$ \hat{f}(\xi) = \frac{1}{2-i\xi} + \frac{1}{2+i\xi} = \frac{2+i\xi + 2-i\xi}{(2-i\xi)(2+i\xi)} = \frac{4}{4+\xi^2} $$

**Question 3 : Vérification de l'égalité de Plancherel**
Le théorème de Plancherel stipule que $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$.
Nous savons que $\|f\|_2^2 = \frac{1}{2}$, donc $2\pi \|f\|_2^2 = \pi$.
Calculons la norme $L^2$ de $\hat{f}$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} \left(\frac{4}{4+\xi^2}\right)^2 d\xi = 16 \int_{-\infty}^{+\infty} \frac{1}{(4+\xi^2)^2} d\xi $$
Effectuons le changement de variable $\xi = 2u$, $d\xi = 2du$ :
$$ \|\hat{f}\|_2^2 = 16 \int_{-\infty}^{+\infty} \frac{1}{16(1+u^2)^2} (2du) = 2 \int_{-\infty}^{+\infty} \frac{du}{(1+u^2)^2} $$
Utilisons la formule classique $\int_{-\infty}^{+\infty} \frac{du}{(1+u^2)^2} = \frac{\pi}{2}$ (obtenue par exemple par intégration par parties ou résidus) :
$$ \|\hat{f}\|_2^2 = 2 \times \frac{\pi}{2} = \pi $$
L'égalité $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$ est rigoureusement vérifiée.
