# Exercice 5 : Translation et modulation dans L2
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $f \in L^2(\mathbb{R})$. On définit $g(t) = f(t - a)$ et $h(t) = f(t) e^{ibt}$ pour $a,b \in \mathbb{R}$.
1. Justifier que $g$ et $h$ sont dans $L^2(\mathbb{R})$.
2. Montrer que $\hat{g}(\xi) = e^{-ia\xi}\hat{f}(\xi)$ et $\hat{h}(\xi) = \hat{f}(\xi - b)$ au sens de $L^2$.

**Correction :**
1. $\|g\|_2^2 = \int |f(t-a)|^2 dt$. Par le changement de variable $u = t-a$ (qui préserve la mesure de Lebesgue), $\|g\|_2^2 = \|f\|_2^2 < \infty$.
$\|h\|_2^2 = \int |f(t) e^{ibt}|^2 dt = \int |f(t)|^2 |e^{ibt}|^2 dt = \int |f(t)|^2 \cdot 1 dt = \|f\|_2^2 < \infty$.
2. Puisque $f \in L^2$, il existe une suite $f_n \in \mathcal{S}$ telle que $f_n \to f$ dans $L^2$.
Soit $g_n(t) = f_n(t-a)$. Alors $g_n \in \mathcal{S}$ et $g_n \to g$ dans $L^2$.
Pour $g_n \in \mathcal{S}$, l'intégrale classique donne $\hat{g}_n(\xi) = \int f_n(t-a) e^{-i\xi t} dt = \int f_n(u) e^{-i\xi (u+a)} du = e^{-ia\xi} \hat{f}_n(\xi)$.
L'opérateur de multiplication par $e^{-ia\xi}$ est continu sur $L^2$. Par unicité de la limite dans Plancherel, on obtient $\hat{g}(\xi) = e^{-ia\xi}\hat{f}(\xi)$.
De même pour $h_n(t) = f_n(t) e^{ibt}$, $\hat{h}_n(\xi) = \hat{f}_n(\xi - b)$, ce qui passe à la limite $L^2$.
