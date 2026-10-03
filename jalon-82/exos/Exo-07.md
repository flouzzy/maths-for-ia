\subsection*{Exercice 7 : Approximation gaussienne de l'identité \quad $\bigstar\bigstar\bigstar\bigstar\star$}

**Énoncé :**
Soit $g_n(x) = \frac{n}{\sqrt{\pi}} e^{-n^2 x^2}$. Montrer que $g_n$ converge vers $\delta_0$ au sens des distributions.

**Correction :**
Rappelons que l'intégrale de Gauss donne $\int_{-\infty}^{+\infty} e^{-u^2} du = \sqrt{\pi}$, donc $\int_{-\infty}^{+\infty} g_n(x) dx = 1$ pour tout $n$.
Soit $\phi \in \mathcal{D}(\mathbb{R})$. Evaluons :
$$\langle T_{g_n}, \phi \rangle = \int_{-\infty}^{+\infty} \frac{n}{\sqrt{\pi}} e^{-n^2 x^2} \phi(x) dx$$
Effectuons le changement de variable $u = nx$, $dx = \frac{du}{n}$ :
$$\langle T_{g_n}, \phi \rangle = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{\pi}} e^{-u^2} \phi(u/n) du$$
La fonction $u \mapsto \frac{1}{\sqrt{\pi}} e^{-u^2} \phi(u/n)$ est majorée en valeur absolue par $C e^{-u^2}$ (où $C = \frac{1}{\sqrt{\pi}} \sup |\phi|$). Cette majorante est intégrable et indépendante de $n$.
On peut donc appliquer le théorème de convergence dominée de Lebesgue pour inverser limite et intégrale.
Pour chaque $u$ fixé, par continuité de $\phi$, $\lim_{n \to \infty} \phi(u/n) = \phi(0)$.
$$\lim_{n \to \infty} \langle T_{g_n}, \phi \rangle = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{\pi}} e^{-u^2} \lim_{n \to \infty} \phi(u/n) du$$
$$\lim_{n \to \infty} \langle T_{g_n}, \phi \rangle = \phi(0) \int_{-\infty}^{+\infty} \frac{1}{\sqrt{\pi}} e^{-u^2} du = \phi(0) \times 1 = \phi(0)$$
C'est exactement la définition de la convergence vers $\delta_0$.
