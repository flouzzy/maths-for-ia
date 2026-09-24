## Exercice 6 : Théorème de Riemann-Lebesgue \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
En utilisant la densité des fonctions en escalier, prouver le Lemme de Riemann-Lebesgue pour $L^1(\mathbb{R})$ :
Pour toute fonction $f \in L^1(\mathbb{R})$, on a $\lim_{|n| \to \infty} \int_{\mathbb{R}} f(x) e^{-inx} dx = 0$.

**Correction :**
Soit $f \in L^1(\mathbb{R})$ et $\epsilon > 0$.
L'ensemble des fonctions en escalier à support compact est dense dans $L^1(\mathbb{R})$.
Il existe donc une fonction en escalier $s = \sum_{j=1}^k c_j \mathbf{1}_{[a_j, b_j]}$ telle que $\| f - s \|_1 < \frac{\epsilon}{2}$.

Par linéarité, évaluons l'intégrale pour la fonction $s$ :
$I_n(s) = \int_{\mathbb{R}} s(x) e^{-inx} dx = \sum_{j=1}^k c_j \int_{a_j}^{b_j} e^{-inx} dx$.
Calculons l'intégrale pour un intervalle $[a_j, b_j]$ pour $n \neq 0$ :
$\int_{a_j}^{b_j} e^{-inx} dx = \left[ \frac{e^{-inx}}{-in} \right]_{a_j}^{b_j} = \frac{e^{-inb_j} - e^{-ina_j}}{-in}$.
La valeur absolue de ce terme est majorée par :
$\left| \frac{e^{-inb_j} - e^{-ina_j}}{-in} \right| \le \frac{|e^{-inb_j}| + |e^{-ina_j}|}{|n|} = \frac{2}{|n|}$.
Donc, $|I_n(s)| \le \sum_{j=1}^k |c_j| \frac{2}{|n|}$.
Il est évident que $\lim_{|n| \to \infty} |I_n(s)| = 0$. Il existe donc $N$ tel que pour tout $|n| \ge N$, $|I_n(s)| < \frac{\epsilon}{2}$.

Maintenant, appliquons l'inégalité triangulaire pour l'intégrale de $f$ :
$|I_n(f)| = \left| \int_{\mathbb{R}} f(x) e^{-inx} dx \right| \le \left| \int_{\mathbb{R}} (f(x) - s(x)) e^{-inx} dx \right| + \left| \int_{\mathbb{R}} s(x) e^{-inx} dx \right|$.
Le premier terme se majore en valeur absolue par l'intégrale de la valeur absolue :
$\int_{\mathbb{R}} |f(x) - s(x)| |e^{-inx}| dx = \int_{\mathbb{R}} |f(x) - s(x)| \times 1 dx = \| f - s \|_1 < \frac{\epsilon}{2}$.
Ainsi, pour tout $|n| \ge N$, $|I_n(f)| \le \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
La limite est bien $0$.
