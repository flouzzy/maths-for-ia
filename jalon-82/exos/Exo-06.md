# Exercice 6 : Convergence vers Dirac via la Gaussienne

\subsection*{Exercice 6 : Convergence vers Dirac via la Gaussienne \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Soit $g_n(x) = \frac{n}{\sqrt{\pi}} e^{-n^2 x^2}$. Montrer que $T_{g_n} \to \delta_0$.

**Démonstration pas à pas :**
1. **Intégrale de Gauss :** On sait que $\int_{-\infty}^{+\infty} e^{-x^2} dx = \sqrt{\pi}$. Le changement de variable $y = nx$ donne $\int_{-\infty}^{+\infty} g_n(x) dx = 1$.
2. **Décomposition :** Pour $\phi \in \mathcal{D}(\mathbb{R})$ :
   $$ \langle T_{g_n}, \phi \rangle - \phi(0) = \int_{-\infty}^{+\infty} g_n(x) (\phi(x) - \phi(0)) dx $$
3. **Majoration :** Soit $\epsilon > 0$. La fonction $\phi$ est continue en 0, donc il existe $\delta > 0$ tel que $|x| < \delta \implies |\phi(x) - \phi(0)| < \epsilon$.
   On coupe l'intégrale en deux : $|x| < \delta$ et $|x| \ge \delta$.
   $$ \left| \int_{|x| < \delta} g_n(x)(\phi(x)-\phi(0)) dx \right| \le \epsilon \int_{-\infty}^{+\infty} g_n(x) dx = \epsilon $$
   Pour $|x| \ge \delta$, $\phi$ est bornée (soit $M = \sup |\phi|$).
   $$ \left| \int_{|x| \ge \delta} g_n(x)(\phi(x)-\phi(0)) dx \right| \le 2M \int_{|x| \ge \delta} g_n(x) dx $$
   Le changement $y = nx$ donne $2M \int_{|y| \ge n\delta} \frac{1}{\sqrt{\pi}} e^{-y^2} dy$, qui est le reste d'une intégrale convergente, et tend donc vers 0.
   Ainsi, pour $n$ assez grand, la différence totale est $\le 2\epsilon$.
   Donc $\langle T_{g_n}, \phi \rangle \to \phi(0)$. $\blacksquare$
