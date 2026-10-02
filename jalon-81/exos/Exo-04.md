# Exercice 4 : Transformée inverse et fonctions à support compact
$\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $\hat{f}(\xi) = \mathbf{1}_{[-\Omega, \Omega]}(\xi)$.
1. Calculer la fonction $f(t)$ dont la transformée de Fourier est $\hat{f}$.
2. Vérifier que $f \notin L^1(\mathbb{R})$ mais que $f \in L^2(\mathbb{R})$.
3. Vérifier le théorème de Plancherel pour ce couple $(f, \hat{f})$.

---
**Correction :**
**Question 1 : Fonction originale $f(t)$**
La fonction $\hat{f}$ appartient à $L^2(\mathbb{R})$ car elle est à support compact et bornée. On applique la formule d'inversion de Plancherel :
$$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{f}(\xi) e^{i\xi t} d\xi = \frac{1}{2\pi} \int_{-\Omega}^{\Omega} e^{i\xi t} d\xi $$
Pour $t \neq 0$ :
$$ f(t) = \frac{1}{2\pi} \left[ \frac{e^{i\xi t}}{it} \right]_{-\Omega}^{\Omega} = \frac{1}{2\pi} \frac{e^{i\Omega t} - e^{-i\Omega t}}{it} = \frac{1}{2\pi} \frac{2i\sin(\Omega t)}{it} = \frac{\sin(\Omega t)}{\pi t} $$
Pour $t = 0$, $f(0) = \frac{1}{2\pi} \int_{-\Omega}^{\Omega} 1 d\xi = \frac{2\Omega}{2\pi} = \frac{\Omega}{\pi}$, ce qui prolonge continûment $\frac{\sin(\Omega t)}{\pi t}$ en $0$.

**Question 2 : Appartenance aux espaces $L^p$**
La fonction $|f(t)| = \frac{|\sin(\Omega t)|}{\pi |t|}$ se comporte asymptotiquement comme $\frac{1}{|t|}$.
On sait que l'intégrale $\int_{1}^{+\infty} \frac{|\sin(\Omega t)|}{t} dt$ diverge (intégrale de Dirichlet modifiée en valeur absolue). Ainsi, $f \notin L^1(\mathbb{R})$.
Cependant, $|f(t)|^2 = \frac{\sin^2(\Omega t)}{\pi^2 t^2} \le \frac{1}{\pi^2 t^2}$. L'intégrale $\int_{1}^{+\infty} \frac{1}{t^2} dt$ converge, et au voisinage de 0, la fonction est continue, donc bornée. Par conséquent, l'intégrale globale converge et $f \in L^2(\mathbb{R})$.

**Question 3 : Vérification de Plancherel**
D'une part, $\|\hat{f}\|_2^2 = \int_{-\Omega}^{\Omega} 1^2 d\xi = 2\Omega$.
D'autre part, $\|f\|_2^2 = \int_{-\infty}^{+\infty} \frac{\sin^2(\Omega t)}{\pi^2 t^2} dt$.
Effectuons le changement de variable $x = \Omega t$, $dx = \Omega dt$, d'où $dt = \frac{dx}{\Omega}$ :
$$ \|f\|_2^2 = \int_{-\infty}^{+\infty} \frac{\sin^2(x)}{\pi^2 (x/\Omega)^2} \frac{dx}{\Omega} = \frac{\Omega^2}{\pi^2 \Omega} \int_{-\infty}^{+\infty} \frac{\sin^2(x)}{x^2} dx = \frac{\Omega}{\pi^2} \times \pi = \frac{\Omega}{\pi} $$
On doit vérifier $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$.
On a bien $2\pi \|f\|_2^2 = 2\pi \frac{\Omega}{\pi} = 2\Omega = \|\hat{f}\|_2^2$. L'isométrie est vérifiée.
