\subsection*{Exercice 6 : Convergence de mesures vers une distribution \quad $\bigstar\bigstar\bigstar\bigstar\star$}

**Énoncé :**
Soit $f_n(x) = \frac{n}{2} \mathbf{1}_{[-1/n, 1/n]}(x)$. Montrer que la suite de distributions régulières associées converge vers la distribution de Dirac en $0$.

**Correction :**
Il s'agit de montrer que pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$, $\lim_{n \to \infty} \langle T_{f_n}, \phi \rangle = \langle \delta_0, \phi \rangle = \phi(0)$.
Par définition de la distribution régulière :
$$\langle T_{f_n}, \phi \rangle = \int_{-\infty}^{+\infty} f_n(x) \phi(x) dx = \frac{n}{2} \int_{-1/n}^{1/n} \phi(x) dx$$
Ceci représente la moyenne de $\phi$ sur l'intervalle $[-1/n, 1/n]$.
Puisque $\phi$ est de classe $C^\infty$, elle est en particulier continue en $0$. Par le théorème de la moyenne, il existe un point $c_n \in [-1/n, 1/n]$ tel que :
$$\int_{-1/n}^{1/n} \phi(x) dx = \left( \frac{1}{n} - \left(-\frac{1}{n}\right) \right) \phi(c_n) = \frac{2}{n} \phi(c_n)$$
Ainsi, $\langle T_{f_n}, \phi \rangle = \frac{n}{2} \times \frac{2}{n} \phi(c_n) = \phi(c_n)$.
Quand $n \to +\infty$, l'intervalle $[-1/n, 1/n]$ se réduit à $\{0\}$, donc $c_n \to 0$. Par continuité de $\phi$, $\phi(c_n) \to \phi(0)$.
Donc $\lim_{n \to \infty} \langle T_{f_n}, \phi \rangle = \phi(0)$.
On a bien la convergence au sens des distributions : $T_{f_n} \to \delta_0$.
