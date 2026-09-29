\subsection*{Exercice 3 : Transformée de Fourier d'une fonction exponentielle symétrique \quad $\bigstar\bigstar\star\star\star$}

Soit $a > 0$. On considère la fonction $f(t) = e^{-a|t|}$.
**1.** Vérifier que $f \in L^1(\mathbb{R})$.
**2.** Calculer explicitement $\hat{f}(\xi)$.

---
**Correction :**

**1.** La fonction $f$ est positive, paire et mesurable.
$$ \int_{-\infty}^{+\infty} |f(t)| \, dt = 2 \int_{0}^{+\infty} e^{-at} \, dt = 2 \left[ \frac{e^{-at}}{-a} \right]_0^{+\infty} = 2 \left( 0 - \left(-\frac{1}{a}\right) \right) = \frac{2}{a} < +\infty $$
Donc $f \in L^1(\mathbb{R})$.

**2.** Par définition :
$$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} e^{-a|t|} e^{-i\xi t} \, dt $$
Puisque $f$ est paire et à valeurs réelles, d'après l'exercice précédent, la partie imaginaire de l'intégrale s'annule et on a :
$$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} e^{-a|t|} \cos(\xi t) \, dt = 2 \int_{0}^{+\infty} e^{-at} \cos(\xi t) \, dt $$
Calculons l'intégrale en repassant en complexe (pour faciliter la primitive) :
$$ \int_{0}^{+\infty} e^{-at} e^{i\xi t} \, dt = \int_{0}^{+\infty} e^{(i\xi - a)t} \, dt $$
La primitive est $\frac{e^{(i\xi - a)t}}{i\xi - a}$.
À la limite $t \to +\infty$, comme $\text{Re}(i\xi - a) = -a < 0$, $|e^{(i\xi - a)t}| = e^{-at} \to 0$.
Donc $\left[ \frac{e^{(i\xi - a)t}}{i\xi - a} \right]_0^{+\infty} = 0 - \frac{1}{i\xi - a} = \frac{1}{a - i\xi}$.
On cherche la partie réelle de cette intégrale complexe (qui correspond à l'intégrale avec le cosinus).
$$ \frac{1}{a - i\xi} = \frac{a + i\xi}{(a - i\xi)(a + i\xi)} = \frac{a + i\xi}{a^2 + \xi^2} $$
La partie réelle est $\frac{a}{a^2 + \xi^2}$.
Ainsi, $\int_0^{+\infty} e^{-at} \cos(\xi t) \, dt = \frac{a}{a^2 + \xi^2}$.
On conclut que :
$$ \hat{f}(\xi) = 2 \frac{a}{a^2 + \xi^2} = \frac{2a}{a^2 + \xi^2} $$
