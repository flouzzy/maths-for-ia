# Exercice 10 : Résolution d'une EDP via Fourier L2 (Équation de la Chaleur)
$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
On s'intéresse à l'équation de la chaleur unidimensionnelle sur la droite réelle entière :
$$ \frac{\partial u}{\partial t}(x,t) = \alpha \frac{\partial^2 u}{\partial x^2}(x,t) \quad \text{pour } x \in \mathbb{R}, t > 0 $$
avec condition initiale $u(x,0) = f(x) \in L^2(\mathbb{R})$.
On suppose que pour tout $t \ge 0$, la fonction $x \mapsto u(x,t)$ appartient à $L^2(\mathbb{R})$.
1. Appliquer la transformée de Fourier (par rapport à la variable spatiale $x$) pour convertir cette EDP en une famille d'équations différentielles ordinaires (EDO) dépendant du paramètre $\xi$.
2. Résoudre cette EDO pour obtenir $\hat{u}(\xi, t)$ en fonction de $\hat{f}(\xi)$.
3. Montrer que l'énergie spatiale de la solution, $E(t) = \int_{\mathbb{R}} |u(x,t)|^2 dx$, est une fonction décroissante du temps. Utiliser Plancherel.
4. (Optionnel) En déduire une expression de $u(x,t)$ sous forme de produit de convolution.

---
**Correction :**
**Question 1 : Transformation de Fourier spatiale**
Soit $\hat{u}(\xi, t) = \int_{-\infty}^{+\infty} u(x,t) e^{-i\xi x} dx$.
Appliquons la transformée de Fourier à l'EDP, en échangeant dérivation par rapport au temps et intégration spatiale (admis) :
$$ \mathcal{F}\left(\frac{\partial u}{\partial t}\right) = \frac{\partial \hat{u}}{\partial t}(\xi, t) $$
Pour la dérivée seconde spatiale, nous avons $\mathcal{F}(\frac{\partial^2 u}{\partial x^2}) = (i\xi)^2 \hat{u}(\xi, t) = -\xi^2 \hat{u}(\xi, t)$.
L'EDP devient donc l'EDO suivante pour chaque fréquence $\xi$ fixée :
$$ \frac{\partial \hat{u}}{\partial t}(\xi, t) = -\alpha \xi^2 \hat{u}(\xi, t) $$

**Question 2 : Résolution de l'EDO**
Pour $\xi$ fixé, c'est une EDO linéaire du premier ordre à coefficients constants. Sa solution générale est :
$$ \hat{u}(\xi, t) = C(\xi) e^{-\alpha \xi^2 t} $$
La condition initiale en $t=0$ donne $\hat{u}(\xi, 0) = \hat{f}(\xi)$. Ainsi, $C(\xi) = \hat{f}(\xi)$.
La solution fréquentielle est donc :
$$ \hat{u}(\xi, t) = \hat{f}(\xi) e^{-\alpha \xi^2 t} $$

**Question 3 : Décroissance de l'énergie (Dissipation)**
D'après le théorème de Plancherel :
$$ E(t) = \int_{\mathbb{R}} |u(x,t)|^2 dx = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{u}(\xi, t)|^2 d\xi $$
Substituons l'expression trouvée :
$$ E(t) = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 \left(e^{-\alpha \xi^2 t}\right)^2 d\xi = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 e^{-2\alpha \xi^2 t} d\xi $$
Puisque $f \in L^2(\mathbb{R})$, l'intégrale pour $t=0$ est finie et vaut $E(0)$.
Pour tout $t > 0$, la fonction exponentielle $e^{-2\alpha \xi^2 t}$ est strictement comprise entre 0 et 1 (pour $\xi \neq 0$). De plus, elle est strictement décroissante par rapport au temps $t$.
La fonction intégrée $|\hat{f}(\xi)|^2 e^{-2\alpha \xi^2 t}$ diminue ponctuellement avec $t$. Par le théorème de convergence dominée (ou simple monotonie de l'intégrale), l'énergie globale $E(t)$ est une fonction décroissante du temps. Le processus de chaleur est bien dissipatif et détruit les hautes fréquences (lissage exponentiel).

**Question 4 : Retour dans l'espace (Noyau de la Chaleur)**
Nous avons $\hat{u}(\xi, t) = \hat{f}(\xi) \cdot \hat{K_t}(\xi)$, avec $\hat{K_t}(\xi) = e^{-\alpha t \xi^2}$.
Nous reconnaissons la transformée de Fourier d'une gaussienne. On sait que $\mathcal{F}(e^{-ax^2}) = \sqrt{\frac{\pi}{a}} e^{-\frac{\xi^2}{4a}}$.
Identifions : $\frac{1}{4a} = \alpha t \implies a = \frac{1}{4\alpha t}$.
Donc $\hat{K_t}(\xi)$ est la transformée de Fourier de $K_t(x) = \sqrt{\frac{1}{4\pi \alpha t}} e^{-\frac{x^2}{4\alpha t}}$.
Par la propriété liant le produit de transformées de Fourier au produit de convolution, on en déduit que :
$$ u(x,t) = (f * K_t)(x) = \frac{1}{\sqrt{4\pi \alpha t}} \int_{\mathbb{R}} f(y) e^{-\frac{(x-y)^2}{4\alpha t}} dy $$
C'est la formule fondamentale de la chaleur par convolution avec le noyau de Gauss-Weierstrass.
