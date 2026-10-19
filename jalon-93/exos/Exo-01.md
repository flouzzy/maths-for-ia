# Exercice 01 : Calcul basique : Loi uniforme
Difficulté : $\bigstar\star\star\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire suivant la loi uniforme sur l'intervalle $[-a, a]$ avec $a > 0$.
Calculez la fonction caractéristique $\phi_X(t)$ de $X$.

**Correction pas à pas :**
1. La densité de probabilité de $X$ est $f_X(x) = \frac{1}{2a} \mathbf{1}_{[-a, a]}(x)$.
2. Par définition, la fonction caractéristique est $\phi_X(t) = \mathbb{E}[e^{itX}] = \int_{\mathbb{R}} e^{itx} f_X(x) dx$.
3. On remplace $f_X(x)$ par son expression :
   $\phi_X(t) = \int_{-a}^{a} e^{itx} \frac{1}{2a} dx$.
4. Pour $t = 0$, $\phi_X(0) = \int_{-a}^{a} \frac{1}{2a} dx = 1$.
5. Pour $t \neq 0$, une primitive de $e^{itx}$ est $\frac{e^{itx}}{it}$. Ainsi :
   $\phi_X(t) = \frac{1}{2a} \left[ \frac{e^{itx}}{it} \right]_{-a}^{a} = \frac{1}{2ait} (e^{ita} - e^{-ita})$.
6. En utilisant la formule d'Euler $\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$, on obtient :
   $\phi_X(t) = \frac{1}{at} \frac{e^{ita} - e^{-ita}}{2i} = \frac{\sin(at)}{at}$.
7. On retrouve bien que $\lim_{t \to 0} \frac{\sin(at)}{at} = 1$.
La fonction caractéristique de la loi uniforme sur $[-a, a]$ est le sinus cardinal $\phi_X(t) = \text{sinc}(at)$.
