## Exercice 6 : Résolution d'une équation différentielle via Fourier \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Résoudre l'équation différentielle suivante dans $L^2(\mathbb{R})$ :
$$ -u''(t) + u(t) = e^{-|t|} $$

**Correction :**
Supposons que $u \in L^2$ est solution et que ses dérivées ont un sens tel que l'on puisse appliquer la transformée de Fourier.
Appliquons la transformée de Fourier (dans $L^2$, par prolongement de $L^1$) des deux côtés de l'équation.
Notons $\hat{u} = \mathcal{F}(u)$.
On a $\mathcal{F}(u'')(\xi) = (i\xi)^2 \hat{u}(\xi) = -\xi^2 \hat{u}(\xi)$.
L'équation devient dans le domaine fréquentiel :
$$ -(-\xi^2 \hat{u}(\xi)) + \hat{u}(\xi) = \mathcal{F}(e^{-|t|})(\xi) $$
$$ (\xi^2 + 1)\hat{u}(\xi) = \mathcal{F}(e^{-|t|})(\xi) $$
Nous avons calculé précédemment que pour $a=1$, $\mathcal{F}(e^{-|t|})(\xi) = \frac{2}{1+\xi^2}$.
L'équation algébrique est donc :
$$ (\xi^2 + 1)\hat{u}(\xi) = \frac{2}{1+\xi^2} $$
D'où l'on isole $\hat{u}$ :
$$ \hat{u}(\xi) = \frac{2}{(1+\xi^2)^2} $$
Pour revenir dans le domaine temporel, on remarque que $\frac{2}{(1+\xi^2)^2}$ peut être vu via la propriété de dérivation par rapport aux fréquences, ou par la convolution.
En effet, $\hat{u}(\xi) = \frac{1}{2} \times \frac{2}{1+\xi^2} \times \frac{2}{1+\xi^2} = \frac{1}{2} \mathcal{F}(e^{-|t|})(\xi) \mathcal{F}(e^{-|t|})(\xi)$.
Par la propriété liant produit fréquentiel et convolution temporelle :
$$ \mathcal{F}(u) = \frac{1}{2} \mathcal{F}(e^{-|\cdot|} * e^{-|\cdot|}) $$
L'inversion donne $u(t) = \frac{1}{2} (e^{-|\cdot|} * e^{-|\cdot|})(t)$.
Calculons cette convolution :
$$ v(t) = \int_{-\infty}^{+\infty} e^{-|\tau|} e^{-|t-\tau|} d\tau $$
Pour $t \ge 0$, séparons l'intégrale en trois régions par rapport aux valeurs absolues :
- Pour $\tau < 0$, $v_1(t) = \int_{-\infty}^0 e^\tau e^{-(t-\tau)} d\tau = e^{-t} \int_{-\infty}^0 e^{2\tau} d\tau = e^{-t} \left[\frac{e^{2\tau}}{2}\right]_{-\infty}^0 = \frac{e^{-t}}{2}$.
- Pour $0 \le \tau \le t$, $v_2(t) = \int_0^t e^{-\tau} e^{-(t-\tau)} d\tau = \int_0^t e^{-t} d\tau = t e^{-t}$.
- Pour $\tau > t$, $v_3(t) = \int_t^{+\infty} e^{-\tau} e^{t-\tau} d\tau = e^t \int_t^{+\infty} e^{-2\tau} d\tau = e^t \left[ \frac{e^{-2\tau}}{-2} \right]_t^{+\infty} = e^t \frac{e^{-2t}}{2} = \frac{e^{-t}}{2}$.
Sommons les trois contributions pour $t \ge 0$ :
$$ v(t) = \frac{e^{-t}}{2} + t e^{-t} + \frac{e^{-t}}{2} = (1+t)e^{-t} $$
Par symétrie évidente de la convolution de fonctions paires, $v(-t) = v(t)$.
Donc $v(t) = (1+|t|)e^{-|t|}$.
Finalement, $u(t) = \frac{1}{2} v(t) = \frac{1}{2} (1+|t|)e^{-|t|}$.
Cette fonction est bien dans $L^2(\mathbb{R})$, valide notre résolution et prouve la surjectivité de l'opérateur pour ce membre de droite.
