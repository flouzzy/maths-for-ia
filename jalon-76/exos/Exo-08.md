## Exercice 8 : Théorème de Riesz-Fréchet (Cas simple) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $H = L^2([0,1])$. On définit l'application $\phi: H \to \mathbb{R}$ par $\phi(f) = \int_0^1 f(x) x dx$. Montrer que $\phi$ est une forme linéaire continue et trouver l'unique vecteur $g \in H$ tel que $\forall f \in H, \phi(f) = \langle f, g \rangle$.

**Correction Détaillée :**
1. **Linéarité :** $\phi(\lambda f + \mu h) = \int_0^1 (\lambda f(x) + \mu h(x))x dx = \lambda \int_0^1 f(x)x dx + \mu \int_0^1 h(x)x dx = \lambda \phi(f) + \mu \phi(h)$.
2. **Continuité :** Par l'inégalité de Cauchy-Schwarz :
   $$ |\phi(f)| = \left| \int_0^1 f(x) x dx \right| = |\langle f, \text{Id} \rangle| \le \|f\|_2 \|\text{Id}\|_2 $$
   où $\text{Id}(x) = x$. Comme $\|\text{Id}\|_2 = \sqrt{\int_0^1 x^2 dx} = \frac{1}{\sqrt{3}} < \infty$, l'application est continue.
3. **Application du Théorème de Riesz :** Puisque $\phi \in H^*$, le théorème de représentation de Riesz garantit l'existence et l'unicité de $g \in H$ tel que $\phi(f) = \langle f, g \rangle$.
4. **Identification de $g$ :**
   On a $\langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} dx$.
   Par définition $\phi(f) = \int_0^1 f(x) x dx$.
   En identifiant pour tout $f$, on trouve que $\overline{g(x)} = x$, et comme $x$ est réel, $g(x) = x$.
   Le vecteur de Riesz est donc la fonction identité $g(x) = x$.
