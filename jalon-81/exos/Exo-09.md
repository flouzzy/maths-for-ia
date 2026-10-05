# Exercice 9 : Série de fonctions et Isométrie
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $\phi(t) = \text{sinc}(t)$. On définit $f_N(t) = \sum_{k=-N}^N c_k \phi(t - k\pi)$.
Exprimez $\|f_N\|_2^2$ en fonction des coefficients $c_k$ en utilisant la transformée de Fourier dans $L^2$.

**Correction :**
Calculons $\widehat{f_N}(\xi)$.
Nous savons que $\mathcal{F}(\text{sinc}(t)) = \pi \mathbf{1}_{[-1, 1]}(\xi)$.
Par la propriété de translation : $\mathcal{F}(\phi(t - k\pi)) = e^{-ik\pi\xi} \pi \mathbf{1}_{[-1, 1]}(\xi)$.
Par linéarité : $\widehat{f_N}(\xi) = \pi \mathbf{1}_{[-1, 1]}(\xi) \sum_{k=-N}^N c_k e^{-ik\pi\xi}$.
Appliquons l'identité de Plancherel :
$\|f_N\|_2^2 = \frac{1}{2\pi} \|\widehat{f_N}\|_2^2 = \frac{1}{2\pi} \int_{-1}^1 \pi^2 \left| \sum_{k=-N}^N c_k e^{-ik\pi\xi} \right|^2 d\xi$.
Remarquons que les fonctions $\xi \mapsto e^{-ik\pi\xi}$ forment une famille orthogonale sur $[-1, 1]$.
En effet, $\int_{-1}^1 e^{-in\pi\xi} e^{im\pi\xi} d\xi = \int_{-1}^1 e^{i(m-n)\pi\xi} d\xi = 2 \delta_{n,m}$.
Donc $\int_{-1}^1 \left| \sum c_k e^{-ik\pi\xi} \right|^2 d\xi = \sum_{k=-N}^N |c_k|^2 \cdot 2$.
Finalement, $\|f_N\|_2^2 = \frac{1}{2\pi} \pi^2 \cdot 2 \sum |c_k|^2 = \pi \sum_{k=-N}^N |c_k|^2$.
Les translations du sinus cardinal forment une base orthogonale.
