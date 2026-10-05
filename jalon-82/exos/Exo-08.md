# Exercice 8 : Un Dirac décalé

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Déterminer la limite au sens des distributions de $g_n(x) = \frac{n}{2} \mathbf{1}_{[a - \frac{1}{n}, a + \frac{1}{n}]}(x)$.

**Correction Détaillée :**
1. **Évaluation :**
   Soit $\phi \in \mathcal{D}(\mathbb{R})$.
   $\langle T_{g_n}, \phi \rangle = \int_{-\infty}^{+\infty} g_n(x) \phi(x) dx = \frac{n}{2} \int_{a - 1/n}^{a + 1/n} \phi(x) dx$.
2. **Application du théorème de la moyenne :**
   La fonction $\phi$ est continue. D'après le théorème de la moyenne, il existe un point $c_n \in [a - 1/n, a + 1/n]$ tel que :
   $\int_{a - 1/n}^{a + 1/n} \phi(x) dx = \left( (a + 1/n) - (a - 1/n) \right) \phi(c_n) = \frac{2}{n} \phi(c_n)$.
3. **Passage à la limite :**
   $\langle T_{g_n}, \phi \rangle = \frac{n}{2} \cdot \frac{2}{n} \phi(c_n) = \phi(c_n)$.
   Lorsque $n \to \infty$, l'intervalle se resserre sur $a$, donc $c_n \to a$.
   Puisque $\phi$ est continue en $a$, $\lim_{n \to \infty} \phi(c_n) = \phi(a) = \langle \delta_a, \phi \rangle$.
   La suite de distributions régulières converge vers le Dirac en $a$, noté $\delta_a$.
