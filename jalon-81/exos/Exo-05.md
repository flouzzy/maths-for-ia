## La gaussienne, vecteur propre de la transformée de Fourier

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$


Soit $f(x) = e^{-x^2/2}$.
1. Montrer que $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
2. On admet que $\hat{f}(\xi) = \sqrt{2\pi} e^{-\xi^2/2}$. En utilisant l'opérateur unitaire $\widetilde{\mathcal{F}} : f \mapsto \frac{1}{\sqrt{2\pi}} \hat{f}$, calculer $\widetilde{\mathcal{F}}(f)$.
3. Calculer $\|f\|_{L^2}^2$ et vérifier l'isométrie.
4. Quel est le sens géométrique du résultat de la question 2 ?

### Correction :

1. La fonction $f(x) = e^{-x^2/2}$ est continue sur $\mathbb{R}$ et décroît plus vite que n'importe quelle puissance de $x$ à l'infini (elle est dans l'espace de Schwartz). Ainsi, les intégrales $\int_{\mathbb{R}} e^{-x^2/2} dx$ et $\int_{\mathbb{R}} (e^{-x^2/2})^2 dx = \int_{\mathbb{R}} e^{-x^2} dx$ sont convergentes. Donc $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.

2. Par définition, l'opérateur unitaire de Fourier est $\widetilde{\mathcal{F}}(f) = \frac{1}{\sqrt{2\pi}} \hat{f}$.
En utilisant la formule admise pour la transformée de la gaussienne :
$$ \widetilde{\mathcal{F}}(f)(\xi) = \frac{1}{\sqrt{2\pi}} \left( \sqrt{2\pi} e^{-\xi^2/2} \right) = e^{-\xi^2/2} = f(\xi) $$
On obtient que $\widetilde{\mathcal{F}}(f) = f$.

3. Calculons l'énergie de $f$ :
$$ \|f\|_{L^2}^2 = \int_{\mathbb{R}} e^{-x^2} dx $$
On sait que l'intégrale de Gauss est $\int_{\mathbb{R}} e^{-u^2} du = \sqrt{\pi}$. Donc $\|f\|_{L^2}^2 = \sqrt{\pi}$.
Vérifions l'isométrie : $\|\widetilde{\mathcal{F}}(f)\|_{L^2}^2 = \|f\|_{L^2}^2 = \sqrt{\pi}$.
C'est trivialement vérifié puisque $\widetilde{\mathcal{F}}(f) = f$.

4. Sur le plan géométrique et en algèbre linéaire infinie-dimensionnelle, l'égalité $\widetilde{\mathcal{F}}(f) = f$ signifie que la fonction gaussienne est un **vecteur propre** de l'opérateur de transformée de Fourier $\widetilde{\mathcal{F}}$, associé à la **valeur propre** $1$. La gaussienne ne change pas de forme en passant du domaine temporel au domaine spectral.
