\subsection*{Exercice 7 : La distribution Valeur Principale (vp) \quad $\bigstar\bigstar\bigstar\bigstar\star$}

On définit pour $\phi \in \mathcal{D}(\mathbb{R})$ la forme linéaire $\text{vp}(1/x)$ par :
$$\langle \text{vp}\left(\frac{1}{x}\right), \phi \rangle = \lim_{\epsilon \to 0^+} \int_{|x|>\epsilon} \frac{\phi(x)}{x} dx$$
Montrer que cette limite existe bien pour toute fonction test, démontrant ainsi qu'il s'agit d'une distribution.

**Correction Détaillée :**
Pour contourner la divergence au voisinage de zéro due à $1/x$, on exploite la symétrie.
L'intégrale se sépare sur deux domaines :
$\int_{|x|>\epsilon} \frac{\phi(x)}{x} dx = \int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} dx + \int_{\epsilon}^{+\infty} \frac{\phi(x)}{x} dx$
Dans la première intégrale, on effectue le changement de variable $x \to -x$ :
$\int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} dx = \int_{+\infty}^{\epsilon} \frac{\phi(-x)}{-x} (-dx) = -\int_{\epsilon}^{+\infty} \frac{\phi(-x)}{x} dx$
En recombinant avec la seconde intégrale :
$\int_{|x|>\epsilon} \frac{\phi(x)}{x} dx = \int_{\epsilon}^{+\infty} \frac{\phi(x) - \phi(-x)}{x} dx$
Par le théorème des accroissements finis appliqué entre $-x$ et $x$, $\phi(x) - \phi(-x) = 2x \phi'(c_x)$ avec $c_x \in [-x, x]$.
Puisque $\phi$ est $\mathcal{C}^\infty$, sa dérivée est bornée, disons par $M$.
Donc $\left| \frac{\phi(x) - \phi(-x)}{x} \right| \le \frac{2|x|M}{|x|} = 2M$.
La fonction intégrande $\frac{\phi(x) - \phi(-x)}{x}$ est bornée au voisinage de $0$.
De plus, son intégration se fait sur un ensemble compact puisque $\phi$ est à support compact. L'intégrale $\int_{0}^{+\infty} \frac{\phi(x) - \phi(-x)}{x} dx$ est donc parfaitement convergente (absolument convergente).
La limite quand $\epsilon \to 0^+$ existe donc bel et bien. $\text{vp}(1/x)$ est une distribution bien définie. $\blacksquare$
