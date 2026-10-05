# Exercice 3 : Action sur des suites de fonctions

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f_n(x) = n e^{-nx} \mathbf{1}_{[0, +\infty[}(x)$. Montrer que la suite de distributions régulières $(T_{f_n})$ converge au sens des distributions vers la distribution de Dirac $\delta_0$.

**Correction Détaillée :**
1. **Convergence au sens des distributions :**
   Il faut montrer que pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$, $\lim_{n \to \infty} \langle T_{f_n}, \phi \rangle = \langle \delta_0, \phi \rangle = \phi(0)$.

2. **Calcul de l'action :**
   $$ \langle T_{f_n}, \phi \rangle = \int_{-\infty}^{+\infty} f_n(x)\phi(x)dx = \int_0^{+\infty} n e^{-nx} \phi(x) dx $$
   Effectuons le changement de variable $u = nx$, $du = n dx$.
   $$ \langle T_{f_n}, \phi \rangle = \int_0^{+\infty} e^{-u} \phi\left(\frac{u}{n}\right) du $$

3. **Passage à la limite :**
   On a $\lim_{n \to \infty} e^{-u} \phi\left(\frac{u}{n}\right) = e^{-u} \phi(0)$ pour tout $u > 0$ par continuité de $\phi$ en 0.
   De plus, comme $\phi$ est à support compact, elle est bornée, disons par $M$.
   Donc $\left| e^{-u} \phi\left(\frac{u}{n}\right) \right| \le M e^{-u}$.
   La fonction $u \mapsto M e^{-u}$ est intégrable sur $[0, +\infty[$ ($\int_0^\infty M e^{-u} du = M$).
   Par le théorème de convergence dominée de Lebesgue, on peut intervertir limite et intégrale :
   $$ \lim_{n \to \infty} \langle T_{f_n}, \phi \rangle = \int_0^{+\infty} e^{-u} \phi(0) du = \phi(0) \left[ -e^{-u} \right]_0^{+\infty} = \phi(0)(0 - (-1)) = \phi(0) $$
   Ainsi, $T_{f_n} \to \delta_0$ dans $\mathcal{D}'(\mathbb{R})$.
