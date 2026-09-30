## Exercice 10 : Inégalité de Wirtinger via Fourier \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f \in L^2(\mathbb{R})$ continûment dérivable, avec $f' \in L^2(\mathbb{R})$.
Supposons de plus que le spectre de $f$ ne contient pas de basses fréquences : $\hat{f}(\xi) = 0$ pour presque tout $\xi \in [-a, a]$ (avec $a > 0$).
Montrer que $\|f\|_2 \le \frac{1}{a} \|f'\|_2$.

**Correction :**
La condition "pas de basses fréquences" se traduit mathématiquement par $\text{supp}(\hat{f}) \subset ]-\infty, -a] \cup [a, +\infty[$.
Par l'isométrie de Plancherel, l'énergie de $f$ est donnée par :
$$ \|f\|_2^2 = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 d\xi = \frac{1}{2\pi} \int_{|\xi| \ge a} |\hat{f}(\xi)|^2 d\xi $$
D'autre part, la dérivation dans le domaine temporel correspond à une multiplication par $i\xi$ dans le domaine fréquentiel : $\mathcal{F}(f')(\xi) = i\xi \hat{f}(\xi)$.
L'énergie de la dérivée est, par Plancherel :
$$ \|f'\|_2^2 = \frac{1}{2\pi} \int_{\mathbb{R}} |i\xi \hat{f}(\xi)|^2 d\xi = \frac{1}{2\pi} \int_{\mathbb{R}} \xi^2 |\hat{f}(\xi)|^2 d\xi $$
Comme $\hat{f}(\xi) = 0$ pour $|\xi| < a$, l'intégration ne se fait que sur les domaines où $\xi^2 \ge a^2$.
On peut donc minorer l'intégrale de l'énergie de la dérivée :
$$ \|f'\|_2^2 = \frac{1}{2\pi} \int_{|\xi| \ge a} \xi^2 |\hat{f}(\xi)|^2 d\xi \ge \frac{1}{2\pi} \int_{|\xi| \ge a} a^2 |\hat{f}(\xi)|^2 d\xi $$
En factorisant $a^2$ qui est constant vis-à-vis de l'intégrale :
$$ \|f'\|_2^2 \ge a^2 \left( \frac{1}{2\pi} \int_{|\xi| \ge a} |\hat{f}(\xi)|^2 d\xi \right) = a^2 \|f\|_2^2 $$
Puisque $a > 0$, nous pouvons diviser par $a^2$ et prendre la racine carrée :
$$ \|f\|_2^2 \le \frac{1}{a^2} \|f'\|_2^2 \implies \|f\|_2 \le \frac{1}{a} \|f'\|_2 $$
*Conclusion physique :* Un signal dénué de basses fréquences oscille nécessairement très vite, ce qui se traduit par une "énergie de dérivée" importante proportionnellement à l'énergie du signal lui-même. C'est une forme d'inégalité de Poincaré-Wirtinger, démontrée de manière purement algébrique grâce à l'isométrie de l'espace de Hilbert sous la transformation de Fourier.
