## Bande Passante et conservation d'énergie partielle

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$


Soit $f \in L^2(\mathbb{R})$. On fait passer ce signal dans un filtre passe-bas idéal de fréquence de coupure $\Omega$. Le signal filtré $f_{\Omega}$ est défini par sa transformée de Fourier :
$$ \widehat{f_{\Omega}}(\xi) = \hat{f}(\xi) \mathbb{1}_{[-\Omega, \Omega]}(\xi) $$
1. Exprimer $\|f_{\Omega}\|_{L^2}^2$ sous forme d'intégrale.
2. Montrer que $\lim_{\Omega \to \infty} \|f - f_{\Omega}\|_{L^2} = 0$. (Indication : Utiliser le théorème de convergence dominée et Plancherel).
3. En déduire que le signal filtré converge en norme $L^2$ vers le signal d'origine.

### Correction :

1. Par le théorème de Plancherel appliqué à $f_{\Omega}$ :
$$ \|f_{\Omega}\|_{L^2}^2 = \frac{1}{2\pi} \int_{\mathbb{R}} |\widehat{f_{\Omega}}(\xi)|^2 d\xi = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 \mathbb{1}_{[-\Omega, \Omega]}(\xi)^2 d\xi $$
Puisque l'indicatrice au carré vaut l'indicatrice, on obtient l'énergie contenue dans la bande de fréquences :
$$ \|f_{\Omega}\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\Omega}^{\Omega} |\hat{f}(\xi)|^2 d\xi $$

2. Intéressons-nous à la différence temporelle $e_{\Omega} = f - f_{\Omega}$.
Sa transformée de Fourier, par linéarité, est :
$$ \widehat{e_{\Omega}}(\xi) = \hat{f}(\xi) - \widehat{f_{\Omega}}(\xi) = \hat{f}(\xi) (1 - \mathbb{1}_{[-\Omega, \Omega]}(\xi)) $$
Ce qui correspond aux fréquences extérieures à la bande passante :
$$ |\widehat{e_{\Omega}}(\xi)|^2 = |\hat{f}(\xi)|^2 \mathbb{1}_{|\xi| > \Omega} $$
Par Plancherel, on a :
$$ \|f - f_{\Omega}\|_{L^2}^2 = \frac{1}{2\pi} \int_{|\xi| > \Omega} |\hat{f}(\xi)|^2 d\xi $$
Posons la suite de fonctions intégrables $g_n(\xi) = |\hat{f}(\xi)|^2 \mathbb{1}_{|\xi| > n}$.
- Pour presque tout $\xi \in \mathbb{R}$, il existe $N$ tel que pour $n > N$, $n > |\xi|$. Ainsi, $\mathbb{1}_{|\xi| > n} = 0$. Donc $g_n(\xi) \to 0$ ponctuellement.
- On a la majoration uniforme par une fonction intégrable : $|g_n(\xi)| \le |\hat{f}(\xi)|^2$ pour tout $n$. Et $|\hat{f}|^2 \in L^1(\mathbb{R})$ car $\hat{f} \in L^2(\mathbb{R})$.
Par le théorème de convergence dominée de Lebesgue :
$$ \lim_{n \to \infty} \int_{\mathbb{R}} g_n(\xi) d\xi = \int_{\mathbb{R}} 0 d\xi = 0 $$
Ainsi, $\lim_{\Omega \to \infty} \frac{1}{2\pi} \int_{|\xi| > \Omega} |\hat{f}(\xi)|^2 d\xi = 0$.
Ce qui prouve que $\lim_{\Omega \to \infty} \|f - f_{\Omega}\|_{L^2}^2 = 0$.

3. Le résultat de la question 2 implique directement que la limite de l'erreur en norme $L^2$ est nulle. Ainsi, lorsque la largeur de la bande passante tend vers l'infini, le signal filtré $f_{\Omega}$ converge vers le signal original $f$ dans l'espace de Hilbert $L^2(\mathbb{R})$.
