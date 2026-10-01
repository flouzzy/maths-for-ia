## Principe d'Incertitude de Heisenberg (Version L2)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$


Soit $f \in L^2(\mathbb{R})$ telle que $f \in \mathcal{S}(\mathbb{R})$ et $\|f\|_{L^2} = 1$.
On pose la dispersion temporelle $\Delta x^2 = \int_{\mathbb{R}} x^2 |f(x)|^2 dx$ et la dispersion fréquentielle $\Delta \xi^2 = \frac{1}{2\pi} \int_{\mathbb{R}} \xi^2 |\hat{f}(\xi)|^2 d\xi$.
1. Montrer en intégrant par parties que $\int_{\mathbb{R}} (x f'(x) \overline{f(x)} + x \overline{f'(x)} f(x)) dx = -1$.
2. En déduire que $\left| \int_{\mathbb{R}} x (f'(x) \overline{f(x)} + \overline{f'(x)} f(x)) dx \right| = 1$.
3. Utiliser l'inégalité de Cauchy-Schwarz sur $x f(x)$ et $f'(x)$ pour minorer le produit $\Delta x^2 \Delta \xi^2$. (On rappelle que $\widehat{f'}(\xi) = i\xi \hat{f}(\xi)$).

### Correction :

1. L'expression $f'(x) \overline{f(x)} + \overline{f'(x)} f(x)$ n'est autre que la dérivée de $|f(x)|^2$.
On doit évaluer $I = \int_{\mathbb{R}} x \frac{d}{dx}(|f(x)|^2) dx$.
Réalisons une intégration par parties. Posons $u(x) = x \implies u'(x) = 1$ et $v'(x) = \frac{d}{dx}(|f(x)|^2) \implies v(x) = |f(x)|^2$.
$$ I = \left[ x |f(x)|^2 \right]_{-\infty}^{+\infty} - \int_{\mathbb{R}} 1 \cdot |f(x)|^2 dx $$
Puisque $f \in \mathcal{S}(\mathbb{R})$, $f$ décroît très rapidement, donc $\lim_{x \to \pm\infty} x |f(x)|^2 = 0$.
Il reste :
$$ I = 0 - \|f\|_{L^2}^2 $$
Comme on a supposé $\|f\|_{L^2} = 1$, on a $I = -1$.

2. Il découle trivialement de la question précédente que :
$$ \left| \int_{\mathbb{R}} x (f'(x) \overline{f(x)} + \overline{f'(x)} f(x)) dx \right| = |-1| = 1 $$

3. Remarquons que $x (f'(x) \overline{f(x)} + \overline{f'(x)} f(x)) = 2 \text{Re}(x f(x) \overline{f'(x)})$.
Donc :
$$ 1 = \left| \int_{\mathbb{R}} 2 \text{Re}(x f(x) \overline{f'(x)}) dx \right| \le 2 \int_{\mathbb{R}} |x f(x)| |f'(x)| dx $$
Appliquons l'inégalité de Cauchy-Schwarz dans $L^2$ sur les fonctions $x \mapsto x f(x)$ et $x \mapsto f'(x)$ :
$$ 1 \le 2 \|x f\|_{L^2} \|f'\|_{L^2} \implies \frac{1}{4} \le \|x f\|_{L^2}^2 \|f'\|_{L^2}^2 $$
Or, par définition, $\|x f\|_{L^2}^2 = \int_{\mathbb{R}} x^2 |f(x)|^2 dx = \Delta x^2$.
D'autre part, selon le théorème de Plancherel appliqué à la dérivée $f'$ :
$$ \|f'\|_{L^2}^2 = \frac{1}{2\pi} \|\widehat{f'}\|_{L^2}^2 $$
Puisque $\widehat{f'}(\xi) = i\xi \hat{f}(\xi)$, on a $|\widehat{f'}(\xi)|^2 = \xi^2 |\hat{f}(\xi)|^2$.
Donc :
$$ \|f'\|_{L^2}^2 = \frac{1}{2\pi} \int_{\mathbb{R}} \xi^2 |\hat{f}(\xi)|^2 d\xi = \Delta \xi^2 $$
En substituant ces identités dans l'inégalité issue de Cauchy-Schwarz, on obtient le principe d'incertitude de Heisenberg :
$$ \Delta x^2 \Delta \xi^2 \ge \frac{1}{4} $$
Cela prouve qu'un signal ne peut pas être simultanément arbitrairement concentré dans le domaine temporel et dans le domaine fréquentiel.
