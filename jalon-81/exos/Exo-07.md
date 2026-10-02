# Exercice 7 : La Transformée de Fourier de la loi Normale
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f(t) = e^{-at^2}$ avec $a > 0$.
1. Calculer l'équation différentielle du premier ordre vérifiée par $f$.
2. En appliquant la transformée de Fourier sur cette équation différentielle (en supposant les propriétés d'échange dérivation/Fourier valides), déduire une équation différentielle pour $\hat{f}$.
3. Résoudre cette équation pour $\hat{f}(\xi)$ sachant que $\hat{f}(0) = \sqrt{\frac{\pi}{a}}$.
4. Vérifier que $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$ par le calcul explicite.

---
**Correction :**
**Question 1 : Équation différentielle pour $f$**
Dérivons $f(t) = e^{-at^2}$ par rapport à $t$ :
$f'(t) = -2at e^{-at^2} = -2at f(t)$.
Donc $f$ est solution de l'EDO linéaire : $y'(t) + 2at y(t) = 0$.

**Question 2 : Équation différentielle pour $\hat{f}$**
Appliquons la transformée de Fourier $\mathcal{F}$ à chaque terme de l'EDO $f'(t) = -2at f(t)$.
Nous savons que :
- $\mathcal{F}(f')(\xi) = i\xi \hat{f}(\xi)$
- $\mathcal{F}(tf(t))(\xi) = i \frac{d}{d\xi} \hat{f}(\xi)$
Donc :
$i\xi \hat{f}(\xi) = -2a \left( i \frac{d}{d\xi} \hat{f}(\xi) \right)$
En simplifiant par $i$ (non nul) :
$\xi \hat{f}(\xi) = -2a \hat{f}'(\xi) \implies \hat{f}'(\xi) = -\frac{\xi}{2a} \hat{f}(\xi)$
Ainsi, $\hat{f}$ vérifie une EDO du premier ordre similaire.

**Question 3 : Résolution de l'EDO pour $\hat{f}$**
L'équation $\hat{f}'(\xi) + \frac{\xi}{2a} \hat{f}(\xi) = 0$ est à variables séparables :
$$ \frac{\hat{f}'(\xi)}{\hat{f}(\xi)} = -\frac{\xi}{2a} \implies \ln(\hat{f}(\xi)) = -\frac{\xi^2}{4a} + C \implies \hat{f}(\xi) = K e^{-\frac{\xi^2}{4a}} $$
On détermine la constante $K$ avec la condition initiale en $\xi = 0$ :
$$ \hat{f}(0) = K e^0 = K $$
Or, par définition, $\hat{f}(0) = \int_{-\infty}^{+\infty} e^{-at^2} dt = \sqrt{\frac{\pi}{a}}$ (intégrale de Gauss).
Donc $K = \sqrt{\frac{\pi}{a}}$, et on obtient :
$$ \hat{f}(\xi) = \sqrt{\frac{\pi}{a}} e^{-\frac{\xi^2}{4a}} $$

**Question 4 : Vérification de Plancherel**
Calcul de $\|f\|_2^2$ :
$$ \|f\|_2^2 = \int_{-\infty}^{+\infty} (e^{-at^2})^2 dt = \int_{-\infty}^{+\infty} e^{-2at^2} dt $$
C'est l'intégrale de Gauss avec paramètre $2a$, donc $\|f\|_2^2 = \sqrt{\frac{\pi}{2a}}$.
Calcul de $\|\hat{f}\|_2^2$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} \left( \sqrt{\frac{\pi}{a}} e^{-\frac{\xi^2}{4a}} \right)^2 d\xi = \frac{\pi}{a} \int_{-\infty}^{+\infty} e^{-\frac{\xi^2}{2a}} d\xi $$
C'est l'intégrale de Gauss avec paramètre $\frac{1}{2a}$, dont la valeur est $\sqrt{\pi / (\frac{1}{2a})} = \sqrt{2\pi a}$.
Donc $\|\hat{f}\|_2^2 = \frac{\pi}{a} \sqrt{2\pi a} = \pi \sqrt{\frac{2\pi}{a}}$.
Vérifions $2\pi \|f\|_2^2$ :
$$ 2\pi \|f\|_2^2 = 2\pi \sqrt{\frac{\pi}{2a}} = \sqrt{4\pi^2 \frac{\pi}{2a}} = \sqrt{\frac{2\pi^3}{a}} = \pi \sqrt{\frac{2\pi}{a}} $$
Les deux quantités sont égales, Plancherel est respecté.
