# Exercice 8 : Produit de convolution et inégalité de Young dans L2
$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f \in L^1(\mathbb{R})$ et $g \in L^2(\mathbb{R})$.
1. Rappeler pourquoi $f * g \in L^2(\mathbb{R})$.
2. Montrer rigoureusement que la transformée de Fourier de $f * g$ vérifie $\widehat{f * g}(\xi) = \hat{f}(\xi)\hat{g}(\xi)$ presque partout dans $L^2$.
3. Déduire que $\|\widehat{f * g}\|_2 \le \|f\|_1 \|\hat{g}\|_2$.
4. En conclure que $\|f * g\|_2 \le \|f\|_1 \|g\|_2$ (Cas particulier de l'inégalité de Young pour la convolution).

---
**Correction :**
**Question 1 : Appartenance de la convolution à $L^2$**
D'après l'inégalité de Young pour la convolution, si $f \in L^p(\mathbb{R})$ et $g \in L^q(\mathbb{R})$ avec $\frac{1}{p} + \frac{1}{q} = 1 + \frac{1}{r}$, alors $f * g \in L^r(\mathbb{R})$ et $\|f * g\|_r \le \|f\|_p \|g\|_q$.
En choisissant $p = 1$, $q = 2$, l'équation devient $1 + \frac{1}{2} = 1 + \frac{1}{r} \implies r = 2$.
Donc $f * g \in L^2(\mathbb{R})$ et $\|f * g\|_2 \le \|f\|_1 \|g\|_2$.

**Question 2 : Transformée de Fourier du produit de convolution**
Puisque $f * g \in L^2(\mathbb{R})$, on peut lui appliquer la transformée de Fourier sur $L^2$ (prolongée par densité).
Soit $g_n \in L^1 \cap L^2$ une suite convergeant vers $g$ dans $L^2$.
Pour $g_n$, le théorème usuel sur $L^1$ assure que $\widehat{f * g_n}(\xi) = \hat{f}(\xi)\hat{g_n}(\xi)$.
Or, par continuité de la convolution $L^1 \times L^2 \to L^2$, $f * g_n \to f * g$ dans $L^2$.
Par la continuité de l'opérateur de Plancherel sur $L^2$, $\widehat{f * g_n} \to \widehat{f * g}$ dans $L^2$.
De plus, $\hat{f}$ est bornée (car $f \in L^1$), on a $\|\hat{f}\|_{\infty} \le \|f\|_1$.
L'opérateur de multiplication par $\hat{f}$ est continu sur $L^2$, donc $\hat{f} \hat{g_n} \to \hat{f} \hat{g}$ dans $L^2$.
Par unicité de la limite dans $L^2$, $\widehat{f * g} = \hat{f}\hat{g}$ presque partout.

**Question 3 : Inégalité sur les normes $L^2$ des spectres**
Calculons la norme $L^2$ de $\widehat{f * g}$ :
$$ \|\widehat{f * g}\|_2^2 = \int_{-\infty}^{+\infty} |\hat{f}(\xi)\hat{g}(\xi)|^2 d\xi = \int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 |\hat{g}(\xi)|^2 d\xi $$
Puisque $f \in L^1(\mathbb{R})$, $|\hat{f}(\xi)| = |\int f(t)e^{-i\xi t}dt| \le \int |f(t)|dt = \|f\|_1$.
Ainsi, $|\hat{f}(\xi)|^2 \le \|f\|_1^2$ pour tout $\xi$.
Donc :
$$ \|\widehat{f * g}\|_2^2 \le \int_{-\infty}^{+\infty} \|f\|_1^2 |\hat{g}(\xi)|^2 d\xi = \|f\|_1^2 \int_{-\infty}^{+\infty} |\hat{g}(\xi)|^2 d\xi = \|f\|_1^2 \|\hat{g}\|_2^2 $$
En prenant la racine carrée, $\|\widehat{f * g}\|_2 \le \|f\|_1 \|\hat{g}\|_2$.

**Question 4 : Preuve de l'inégalité de Young (cas particulier)**
Par le théorème de Plancherel, $\|\widehat{f * g}\|_2 = \sqrt{2\pi} \|f * g\|_2$ et $\|\hat{g}\|_2 = \sqrt{2\pi} \|g\|_2$.
En remplaçant ces expressions dans l'inégalité de la question 3, on obtient :
$$ \sqrt{2\pi} \|f * g\|_2 \le \|f\|_1 (\sqrt{2\pi} \|g\|_2) $$
En simplifiant par $\sqrt{2\pi}$ (strictement positif), il reste :
$$ \|f * g\|_2 \le \|f\|_1 \|g\|_2 $$
On vient de redémontrer un cas particulier de l'inégalité de Young (souvent admise en analyse fonctionnelle) en utilisant la puissance de l'isométrie de Plancherel.
