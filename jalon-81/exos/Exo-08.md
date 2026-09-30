## Exercice 8 : Valeurs propres de l'opérateur de Fourier \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit l'opérateur $U = \frac{1}{\sqrt{2\pi}} \mathcal{F}$ sur $L^2(\mathbb{R})$.
1. Montrer que $U^4 = Id$.
2. En déduire les valeurs propres possibles de $U$.
3. Vérifier que la fonction $f(t) = e^{-t^2/2}$ est un vecteur propre et donner sa valeur propre.

**Correction :**
1. **Périodicité d'ordre 4 :**
Pour $f \in L^2(\mathbb{R})$, $U(f)(\xi) = \frac{1}{\sqrt{2\pi}} \int f(t) e^{-i\xi t} dt$.
Appliquons l'opérateur une seconde fois : $U^2(f)(x) = U(Uf)(x) = \frac{1}{\sqrt{2\pi}} \int Uf(\xi) e^{-ix\xi} d\xi$.
Par la formule d'inversion, $\frac{1}{2\pi} \int \hat{f}(\xi) e^{i x \xi} d\xi = f(x)$.
L'expression de $U^2$ a un signe négatif dans l'exponentielle, ce qui correspond à évaluer la fonction inverse en $-x$.
Donc $U^2(f)(x) = f(-x) = \check{f}(x)$.
Appliquons $U^2$ une nouvelle fois :
$U^4(f)(x) = U^2(U^2 f)(x) = U^2(\check{f})(x) = \check{f}(-x) = f(x)$.
Donc $U^4 = Id$.

2. **Valeurs propres :**
Le polynôme annulateur de l'opérateur $U$ est $P(X) = X^4 - 1$.
Les valeurs propres de $U$ doivent être des racines de ce polynôme.
Les racines de $X^4 - 1 = 0$ sur $\mathbb{C}$ sont $\{1, -1, i, -i\}$.
Donc, le spectre de l'opérateur de Fourier (normalisé) est inclus dans $\{1, -1, i, -i\}$.

3. **Vecteur propre gaussien :**
Soit $f(t) = e^{-t^2/2}$.
Nous savons que la transformée de Fourier (non normalisée) de la gaussienne est :
$\mathcal{F}(e^{-t^2/2})(\xi) = \sqrt{2\pi} e^{-\xi^2/2}$.
Calculons l'action de $U$ sur $f$ :
$U(f)(\xi) = \frac{1}{\sqrt{2\pi}} \mathcal{F}(f)(\xi) = \frac{1}{\sqrt{2\pi}} \sqrt{2\pi} e^{-\xi^2/2} = e^{-\xi^2/2} = f(\xi)$.
Ainsi, $U(f) = 1 \cdot f$.
La fonction $f(t) = e^{-t^2/2}$ est donc un vecteur propre de $U$ associé à la valeur propre $\lambda = 1$.
*(Les fonctions de Hermite-Gauss forment une base de Hilbert complète de vecteurs propres pour la transformée de Fourier).*
