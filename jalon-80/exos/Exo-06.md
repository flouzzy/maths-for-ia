\subsection*{Exercice 6 : Transformée de Fourier de la Gaussienne \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Soit la fonction $g(t) = e^{-t^2/2}$.
On rappelle que $\int_{-\infty}^{+\infty} e^{-t^2/2} dt = \sqrt{2\pi}$.
**1.** Montrer que $g$ vérifie l'équation différentielle $g'(t) + t g(t) = 0$.
**2.** En déduire une équation différentielle vérifiée par sa transformée de Fourier $\hat{g}(\xi)$.
**3.** Résoudre cette équation pour trouver l'expression explicite de $\hat{g}(\xi)$.

---
**Correction :**

**1.** Calculons la dérivée de $g(t)$ :
$g'(t) = \frac{d}{dt}(e^{-t^2/2}) = -t e^{-t^2/2} = -t g(t)$.
Donc $g'(t) + t g(t) = 0$.

**2.** Appliquons la transformée de Fourier à cette équation différentielle.
$\mathcal{F}(g')(\xi) + \mathcal{F}(t \mapsto t g(t))(\xi) = 0$.
On sait que $\mathcal{F}(g')(\xi) = i\xi \hat{g}(\xi)$.
Pour le second terme, dérivons la définition de la transformée de Fourier de $g$ par rapport à $\xi$ :
$\frac{d}{d\xi} \hat{g}(\xi) = \frac{d}{d\xi} \int_{-\infty}^{+\infty} g(t) e^{-i\xi t} dt = \int_{-\infty}^{+\infty} g(t) (-it) e^{-i\xi t} dt = -i \mathcal{F}(t g(t))(\xi)$.
Donc $\mathcal{F}(t g(t))(\xi) = i \frac{d}{d\xi} \hat{g}(\xi) = i \hat{g}'(\xi)$.
L'équation devient :
$i\xi \hat{g}(\xi) + i \hat{g}'(\xi) = 0$.
En divisant par $i$ :
$\hat{g}'(\xi) + \xi \hat{g}(\xi) = 0$.

**3.** Nous avons une équation différentielle linéaire du premier ordre pour $\hat{g}$ : $\hat{g}'(\xi) = -\xi \hat{g}(\xi)$.
La solution générale est de la forme $\hat{g}(\xi) = K e^{-\xi^2/2}$ avec $K \in \mathbb{C}$.
Pour trouver la constante $K$, évaluons $\hat{g}$ en $\xi = 0$ :
$\hat{g}(0) = \int_{-\infty}^{+\infty} g(t) e^0 dt = \int_{-\infty}^{+\infty} e^{-t^2/2} dt = \sqrt{2\pi}$.
Or, $\hat{g}(0) = K e^0 = K$.
Donc $K = \sqrt{2\pi}$.
Ainsi, $\hat{g}(\xi) = \sqrt{2\pi} e^{-\xi^2/2}$.
La fonction Gaussienne est un point fixe (à une constante près) de la transformée de Fourier.
