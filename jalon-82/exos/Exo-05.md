\subsection*{Exercice 5 : Convergence de suite de fonctions vers un Dirac \quad $\bigstar\bigstar\bigstar\star\star$}

Soit la suite de fonctions $f_n(x) = \frac{n}{\pi (1 + n^2 x^2)}$.
Montrer que $f_n \to \delta_0$ au sens des distributions quand $n \to +\infty$.

**Correction Détaillée :**
Soit $\phi \in \mathcal{D}(\mathbb{R})$. Nous devons montrer que $\lim_{n \to +\infty} \int_{-\infty}^{+\infty} f_n(x) \phi(x) dx = \phi(0)$.
Séparons l'intégrale en deux parties (on injecte $\phi(0)$) :
$\int_{-\infty}^{+\infty} f_n(x) \phi(x) dx = \int_{-\infty}^{+\infty} \frac{n}{\pi (1 + n^2 x^2)} (\phi(x) - \phi(0) + \phi(0)) dx$
$ = \phi(0) \int_{-\infty}^{+\infty} \frac{n}{\pi (1 + n^2 x^2)} dx + \int_{-\infty}^{+\infty} \frac{n}{\pi (1 + n^2 x^2)} (\phi(x) - \phi(0)) dx$

Calculons la première intégrale (on effectue $y = nx$, $dy = n dx$) :
$\int_{-\infty}^{+\infty} \frac{n}{\pi (1 + n^2 x^2)} dx = \frac{1}{\pi} \int_{-\infty}^{+\infty} \frac{1}{1 + y^2} dy = \frac{1}{\pi} [\arctan(y)]_{-\infty}^{+\infty} = \frac{1}{\pi} \left( \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) \right) = 1$.
La première partie vaut donc exactement $\phi(0)$.

Il reste à montrer que le second terme tend vers 0. Soit $I_n = \int_{-\infty}^{+\infty} \frac{n}{\pi (1 + n^2 x^2)} (\phi(x) - \phi(0)) dx$.
Par le théorème des accroissements finis, puisque $\phi \in \mathcal{C}^\infty$ et est à support compact, sa dérivée $\phi'$ est bornée sur $\mathbb{R}$. Soit $M = \sup_{\mathbb{R}} |\phi'(x)|$.
On a $|\phi(x) - \phi(0)| \le M |x|$ pour tout $x$.
On scinde l'intégrale en $|x| \le A/\sqrt{n}$ et $|x| > A/\sqrt{n}$ pour un $A>0$ bien choisi.
Alternativement (plus rapide), on effectue le changement de variable $y = nx$ :
$I_n = \frac{1}{\pi} \int_{-\infty}^{+\infty} \frac{1}{1 + y^2} \left( \phi\left(\frac{y}{n}\right) - \phi(0) \right) dy$
Pour chaque $y$ fixé, la fonction intégrande tend vers $0$ car $\phi$ est continue en $0$.
De plus, la fonction intégrande est majorée en valeur absolue par $\frac{2 \|\phi\|_\infty}{1+y^2}$, qui est une fonction dans $L^1(\mathbb{R})$ indépendante de $n$.
On peut donc appliquer le Théorème de Convergence Dominée de Lebesgue : l'intégrale de la limite est la limite de l'intégrale, ce qui donne $0$.
Ainsi, $\lim_{n \to +\infty} \langle T_{f_n}, \phi \rangle = \phi(0) + 0 = \langle \delta_0, \phi \rangle$.
La suite converge bien vers $\delta_0$. $\blacksquare$
