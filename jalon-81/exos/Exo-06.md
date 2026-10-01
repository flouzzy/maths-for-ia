# Exercice 6 : Dérivée au sens L2 et énergie spectrale
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in L^2(\mathbb{R})$ telle que sa dérivée faible $f'$ appartienne également à $L^2(\mathbb{R})$.
1. Exprimer $\widehat{f'}$ en fonction de $\hat{f}$.
2. Montrer que l'intégrale $\int_{-\infty}^{+\infty} \xi^2 |\hat{f}(\xi)|^2 d\xi$ est finie, et donner son interprétation physique en termes d'énergie de la dérivée.
3. Si $\|f\|_2 = 1$, prouver l'inégalité de Heisenberg-Weyl : $\left(\int_{-\infty}^{+\infty} t^2 |f(t)|^2 dt\right) \left(\int_{-\infty}^{+\infty} \xi^2 |\hat{f}(\xi)|^2 d\xi\right) \ge \frac{\pi}{2}$.

---
**Correction :**
**Question 1 : Transformée de $f'$**
Pour $f \in \mathcal{S}(\mathbb{R})$, l'intégration par parties montre que :
$$ \widehat{f'}(\xi) = \int_{-\infty}^{+\infty} f'(t) e^{-i\xi t} dt = \left[ f(t) e^{-i\xi t} \right]_{-\infty}^{+\infty} - \int_{-\infty}^{+\infty} f(t) (-i\xi) e^{-i\xi t} dt $$
Comme $f \in \mathcal{S}(\mathbb{R})$, le terme tout intégré s'annule à l'infini, d'où :
$$ \widehat{f'}(\xi) = i\xi \int_{-\infty}^{+\infty} f(t) e^{-i\xi t} dt = i\xi \hat{f}(\xi) $$
Ce résultat s'étend par densité aux fonctions $f \in L^2(\mathbb{R})$ admettant une dérivée faible dans $L^2(\mathbb{R})$.

**Question 2 : Finitude de l'intégrale et interprétation**
Par hypothèse, $f' \in L^2(\mathbb{R})$. D'après le théorème de Plancherel appliqué à $f'$, nous avons $\widehat{f'} \in L^2(\mathbb{R})$ et :
$$ \int_{-\infty}^{+\infty} |\widehat{f'}(\xi)|^2 d\xi = 2\pi \int_{-\infty}^{+\infty} |f'(t)|^2 dt $$
Or, $|\widehat{f'}(\xi)|^2 = |i\xi \hat{f}(\xi)|^2 = \xi^2 |\hat{f}(\xi)|^2$. En remplaçant, on obtient :
$$ \int_{-\infty}^{+\infty} \xi^2 |\hat{f}(\xi)|^2 d\xi = 2\pi \|f'\|_2^2 $$
Puisque $f' \in L^2(\mathbb{R})$, le terme de droite est fini.
*Interprétation physique :* L'énergie de la dérivée temporelle du signal (qui quantifie la vitesse de variation du signal) est proportionnelle au second moment (la variance) de sa densité spectrale d'énergie. Plus un signal varie vite, plus son énergie s'étale vers les hautes fréquences.

**Question 3 : Inégalité de Heisenberg-Weyl**
L'inégalité d'incertitude stipule que pour $f \in \mathcal{S}(\mathbb{R})$ avec $\|f\|_2 = 1$ :
$$ \left( \int_{-\infty}^{+\infty} t^2 |f(t)|^2 dt \right) \left( \int_{-\infty}^{+\infty} \omega^2 |F(\omega)|^2 d\omega \right) \ge \frac{1}{4} $$
où $F(\omega) = \frac{1}{\sqrt{2\pi}} \hat{f}(\omega)$ est la transformée normalisée pour que $\|F\|_2 = 1$.
Dans notre convention $\hat{f}(\xi)$, on a $F(\xi) = \frac{1}{\sqrt{2\pi}} \hat{f}(\xi)$. L'intégrale de droite devient $\frac{1}{2\pi} \int \xi^2 |\hat{f}(\xi)|^2 d\xi$.
Ainsi,
$$ \left( \int t^2 |f(t)|^2 dt \right) \left( \frac{1}{2\pi} \int \xi^2 |\hat{f}(\xi)|^2 d\xi \right) \ge \frac{1}{4} $$
Ce qui se réécrit, en multipliant par $2\pi$ :
$$ \left( \int t^2 |f(t)|^2 dt \right) \left( \int \xi^2 |\hat{f}(\xi)|^2 d\xi \right) \ge \frac{2\pi}{4} = \frac{\pi}{2} $$
La démonstration repose sur l'intégration par parties de $\|f\|_2^2 = \int f \bar{f} dt = \int t f(t) \bar{f}'(t) dt + \int t f'(t) \bar{f}(t) dt$, suivie d'une application de l'inégalité de Cauchy-Schwarz, puis de Plancherel.
