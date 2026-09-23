## Exercice 9 : Base hilbertienne et identité de Parseval \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Dans $L^2([-\pi, \pi])$, la famille $e_n(x) = \frac{1}{\sqrt{2\pi}} e^{inx}$ pour $n \in \mathbb{Z}$ est une base hilbertienne. Soit $f(x) = x$. Calculer les coefficients de Fourier $c_n = \langle f, e_n \rangle$ et en déduire la valeur de la série $\sum_{n=1}^\infty \frac{1}{n^2}$.

**Correction Détaillée :**
1. **Calcul des coefficients de Fourier :**
   $$ c_n = \langle f, e_n \rangle = \int_{-\pi}^\pi x \frac{1}{\sqrt{2\pi}} e^{-inx} dx $$
   Pour $n=0$ : $c_0 = \frac{1}{\sqrt{2\pi}} \int_{-\pi}^\pi x dx = 0$ (impaire).
   Pour $n \ne 0$ : Intégration par parties avec $u=x, dv=e^{-inx}dx \implies du=dx, v=\frac{e^{-inx}}{-in}$.
   $$ c_n = \frac{1}{\sqrt{2\pi}} \left( \left[ x \frac{e^{-inx}}{-in} \right]_{-\pi}^\pi - \int_{-\pi}^\pi \frac{e^{-inx}}{-in} dx \right) $$
   L'intégrale de droite est nulle car on intègre une période complète.
   $$ c_n = \frac{1}{\sqrt{2\pi}} \frac{1}{-in} ( \pi e^{-in\pi} - (-\pi) e^{in\pi} ) $$
   Puisque $e^{in\pi} = e^{-in\pi} = (-1)^n$, on a $c_n = \frac{1}{\sqrt{2\pi}} \frac{2\pi (-1)^n}{-in} = i \sqrt{2\pi} \frac{(-1)^n}{n}$.
2. **Calcul de la norme de $f$ :**
   $$ \|f\|_2^2 = \int_{-\pi}^\pi x^2 dx = \left[ \frac{x^3}{3} \right]_{-\pi}^\pi = \frac{2\pi^3}{3} $$
3. **Application de l'identité de Parseval :**
   $\|f\|_2^2 = \sum_{n \in \mathbb{Z}} |c_n|^2$.
   $|c_n|^2 = \left| i \sqrt{2\pi} \frac{(-1)^n}{n} \right|^2 = 2\pi \frac{1}{n^2}$ pour $n \ne 0$.
   Donc $\frac{2\pi^3}{3} = \sum_{n \in \mathbb{Z}, n \ne 0} \frac{2\pi}{n^2} = 4\pi \sum_{n=1}^\infty \frac{1}{n^2}$ (par symétrie).
4. **Conclusion :**
   $$ \sum_{n=1}^\infty \frac{1}{n^2} = \frac{2\pi^3 / 3}{4\pi} = \frac{\pi^2}{6} $$
   C'est la résolution du célèbre problème de Bâle !
