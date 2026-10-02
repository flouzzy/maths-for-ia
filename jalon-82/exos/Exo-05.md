# Exercice 5 : Convergence vers Dirac via des portes

\subsection*{Exercice 5 : Convergence vers Dirac via des portes \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Soit $f_n(x) = \frac{n}{2} \mathbf{1}_{[-1/n, 1/n]}(x)$. Montrer que la suite de distributions régulières $T_{f_n}$ converge vers $\delta_0$ dans $\mathcal{D}'(\mathbb{R})$.

**Démonstration pas à pas :**
1. **Action de $T_{f_n}$ :** Pour $\phi \in \mathcal{D}(\mathbb{R})$,
   $$ \langle T_{f_n}, \phi \rangle = \int_{-1/n}^{1/n} \frac{n}{2} \phi(x) dx $$
2. **Théorème de la moyenne :** La fonction $\phi$ est continue. Par le théorème de la moyenne, il existe $c_n \in [-1/n, 1/n]$ tel que :
   $$ \int_{-1/n}^{1/n} \phi(x) dx = \frac{2}{n} \phi(c_n) $$
3. **Passage à la limite :** On a donc $\langle T_{f_n}, \phi \rangle = \frac{n}{2} \cdot \frac{2}{n} \phi(c_n) = \phi(c_n)$.
   Lorsque $n \to +\infty$, l'intervalle $[-1/n, 1/n]$ se réduit à $\{0\}$, donc $c_n \to 0$.
   Par continuité de $\phi$, $\phi(c_n) \to \phi(0) = \langle \delta_0, \phi \rangle$.
   La convergence au sens des distributions est établie. $\blacksquare$
