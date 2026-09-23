# Exercice 1 : Espace $L^2$ (★☆☆☆☆)

**Énoncé :**
Considérons l'espace $L^2([0, 1])$ muni de la mesure de Lebesgue et de son produit scalaire standard $\langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} dx$.
Montrer que les fonctions $f(x) = 1$ et $g(x) = \sqrt{3}(2x - 1)$ sont orthonormales dans $L^2([0, 1])$.

**Correction Détaillée :**
*Analyse de l'énoncé :* Il faut vérifier que $\|f\|^2 = 1$, $\|g\|^2 = 1$ et $\langle f, g \rangle = 0$.

*Résolution pas-à-pas :*
1. **Norme de $f$ :**
   $$ \|f\|^2 = \int_0^1 1^2 dx = [x]_0^1 = 1 $$
   Donc $\|f\| = 1$.

2. **Norme de $g$ :**
   $$ \|g\|^2 = \int_0^1 (\sqrt{3}(2x - 1))^2 dx = 3 \int_0^1 (4x^2 - 4x + 1) dx $$
   $$ \|g\|^2 = 3 \left[ \frac{4x^3}{3} - 2x^2 + x \right]_0^1 = 3 \left( \frac{4}{3} - 2 + 1 \right) = 3 \left( \frac{4}{3} - 1 \right) = 3 \times \frac{1}{3} = 1 $$
   Donc $\|g\| = 1$.

3. **Orthogonalité :**
   $$ \langle f, g \rangle = \int_0^1 1 \cdot \sqrt{3}(2x - 1) dx = \sqrt{3} \left[ x^2 - x \right]_0^1 = \sqrt{3}(1 - 1) = 0 $$

Conclusion : Les fonctions sont orthonormales.
