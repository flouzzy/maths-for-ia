# Exercice 6 : Convergence de Gaussiennes vers le Dirac

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f_n(x) = \frac{n}{\sqrt{\pi}} e^{-n^2 x^2}$. Montrer que $T_{f_n} \to \delta_0$ dans $\mathcal{D}'(\mathbb{R})$.

**Correction Détaillée :**
1. **Action sur une fonction test :**
   Soit $\phi \in \mathcal{D}(\mathbb{R})$. $\langle T_{f_n}, \phi \rangle = \int_{-\infty}^{+\infty} \frac{n}{\sqrt{\pi}} e^{-n^2 x^2} \phi(x) dx$.
2. **Changement de variable :**
   Posons $u = nx$, $du = n dx$. L'intégrale devient :
   $\langle T_{f_n}, \phi \rangle = \frac{1}{\sqrt{\pi}} \int_{-\infty}^{+\infty} e^{-u^2} \phi\left(\frac{u}{n}\right) du$.
3. **Application du théorème de Lebesgue :**
   Soit $g_n(u) = \frac{1}{\sqrt{\pi}} e^{-u^2} \phi\left(\frac{u}{n}\right)$.
   - Pour chaque $u \in \mathbb{R}$, par continuité de $\phi$, $\lim_{n \to \infty} g_n(u) = \frac{1}{\sqrt{\pi}} e^{-u^2} \phi(0)$.
   - $\phi$ est à support compact, donc bornée par $M = \sup_{x \in \mathbb{R}} |\phi(x)|$.
   - On a la majoration dominatrice : $|g_n(u)| \le \frac{M}{\sqrt{\pi}} e^{-u^2}$.
   - La fonction dominante $u \mapsto \frac{M}{\sqrt{\pi}} e^{-u^2}$ est intégrable sur $\mathbb{R}$ car $\int_{-\infty}^{+\infty} e^{-u^2} du = \sqrt{\pi}$.
   D'après le théorème de convergence dominée,
   $$ \lim_{n \to \infty} \langle T_{f_n}, \phi \rangle = \int_{-\infty}^{+\infty} \lim_{n \to \infty} g_n(u) du = \frac{\phi(0)}{\sqrt{\pi}} \int_{-\infty}^{+\infty} e^{-u^2} du = \phi(0) = \langle \delta_0, \phi \rangle $$
   La suite de distributions régulières tend bien vers la distribution de Dirac.
