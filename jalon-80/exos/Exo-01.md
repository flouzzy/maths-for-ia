\subsection*{Exercice 1 : Transformée de Fourier d'une fonction constante par morceaux \quad $\bigstar\star\star\star\star$}

Soit la fonction $f$ définie sur $\mathbb{R}$ par $f(t) = 1$ si $t \in [0, 1]$ et $f(t) = 0$ sinon.

**1.** Montrer que $f \in L^1(\mathbb{R})$.
**2.** Calculer la transformée de Fourier $\hat{f}(\xi)$ pour tout $\xi \in \mathbb{R}$.
**3.** Déterminer $\lim_{|\xi| \to +\infty} \hat{f}(\xi)$. Ce résultat est-il cohérent avec le lemme de Riemann-Lebesgue ?

---
**Correction :**

**1.** La fonction $f$ est mesurable (fonction indicatrice d'un segment). On calcule son intégrale de Lebesgue :
$$ \int_{-\infty}^{+\infty} |f(t)| \, dt = \int_{0}^{1} 1 \, dt = 1 < +\infty $$
Donc $f \in L^1(\mathbb{R})$.

**2.** Soit $\xi \in \mathbb{R}$. Par définition de la transformée de Fourier :
$$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t)e^{-i\xi t} \, dt = \int_{0}^{1} e^{-i\xi t} \, dt $$
Si $\xi = 0$, l'intégrale vaut $\int_0^1 1 \, dt = 1$.
Si $\xi \neq 0$, une primitive de $t \mapsto e^{-i\xi t}$ est $t \mapsto \frac{e^{-i\xi t}}{-i\xi}$. On obtient :
$$ \hat{f}(\xi) = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_0^1 = \frac{e^{-i\xi} - 1}{-i\xi} = \frac{1 - e^{-i\xi}}{i\xi} $$
En factorisant par l'arc moitié $e^{-i\xi/2}$ :
$$ \hat{f}(\xi) = \frac{e^{-i\xi/2}(e^{i\xi/2} - e^{-i\xi/2})}{i\xi} = e^{-i\xi/2} \frac{2i\sin(\xi/2)}{i\xi} = e^{-i\xi/2} \frac{\sin(\xi/2)}{\xi/2} = e^{-i\xi/2} \text{sinc}(\xi/2) $$

**3.** Lorsque $|\xi| \to +\infty$, on a $|\hat{f}(\xi)| \le \left|\frac{1 - e^{-i\xi}}{i\xi}\right| \le \frac{1 + 1}{|\xi|} = \frac{2}{|\xi|}$.
Par le théorème des gendarmes, $\lim_{|\xi| \to +\infty} \hat{f}(\xi) = 0$. Ce résultat est en parfait accord avec le lemme de Riemann-Lebesgue stipulant que pour toute fonction de $L^1(\mathbb{R})$, sa transformée de Fourier s'annule à l'infini.
