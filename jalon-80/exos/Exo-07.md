\subsection*{Exercice 7 : Convolution de deux portes \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Soit $f(t) = \mathbf{1}_{[-a, a]}(t)$ (avec $a > 0$).
On note $h = f * f$ l'auto-convolution de la porte.
**1.** Calculer explicitement $h(t)$ par la définition de l'intégrale.
**2.** Calculer $\hat{h}(\xi)$ par application du théorème de convolution.
**3.** Vérifier la cohérence.

---
**Correction :**

**1.** $h(t) = (f * f)(t) = \int_{-\infty}^{+\infty} f(t-s)f(s) \, ds = \int_{-a}^{a} f(t-s) \, ds$.
La fonction $f(t-s)$ vaut $1$ si $-a \le t-s \le a$, c'est-à-dire si $t-a \le s \le t+a$. Sinon elle vaut $0$.
L'intégrale est donc la mesure de l'intersection des intervalles $[-a, a]$ et $[t-a, t+a]$.
- Si $t > 2a$ ou $t < -2a$, l'intersection est vide, $h(t) = 0$.
- Si $0 \le t \le 2a$, l'intersection est $[t-a, a]$. La longueur est $a - (t-a) = 2a - t$.
- Si $-2a \le t \le 0$, l'intersection est $[-a, t+a]$. La longueur est $(t+a) - (-a) = 2a + t$.
En résumé, $h(t) = (2a - |t|) \mathbf{1}_{[-2a, 2a]}(t)$. C'est une fonction triangle.

**2.** D'après l'exercice 1 (ou le cours), $\hat{f}(\xi) = 2a \, \text{sinc}(\xi a) = 2 \frac{\sin(\xi a)}{\xi}$.
Le théorème de convolution affirme que $\widehat{f * f}(\xi) = \hat{f}(\xi) \cdot \hat{f}(\xi) = (\hat{f}(\xi))^2$.
Donc $\hat{h}(\xi) = \left( 2 \frac{\sin(\xi a)}{\xi} \right)^2 = 4 \frac{\sin^2(\xi a)}{\xi^2}$.

**3.** Cohérence :
On pourrait recalculer $\hat{h}(\xi)$ directement à partir de la fonction triangle $h(t) = 2a - |t|$ sur $[-2a, 2a]$ par deux intégrations par parties. Le résultat redonnerait rigoureusement $4 \frac{\sin^2(\xi a)}{\xi^2}$. Le théorème de convolution offre un gain de temps majeur.
