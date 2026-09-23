## Exercice 1 : Produit scalaire usuel et orthogonalité \quad $\bigstar\star\star\star\star$

**Énoncé :**
Dans $L^2([0, \pi])$, on considère les fonctions $f(x) = \sin(x)$ et $g(x) = \cos(x)$. Montrer que $f$ et $g$ sont orthogonales pour le produit scalaire standard de $L^2$.

**Correction Détaillée :**
1. **Analyse de l'énoncé :** L'espace est $L^2([0, \pi])$ muni de la mesure de Lebesgue. Le produit scalaire est donné par $\langle f, g \rangle = \int_0^\pi f(x)\overline{g(x)}dx$. Les fonctions étant à valeurs réelles, la conjugaison disparaît.
2. **Calcul de l'intégrale :**
   $$ \langle f, g \rangle = \int_0^\pi \sin(x)\cos(x) dx $$
3. **Astuce trigonométrique :** On utilise l'identité $\sin(2x) = 2\sin(x)\cos(x)$, d'où $\sin(x)\cos(x) = \frac{1}{2}\sin(2x)$.
4. **Intégration pas-à-pas :**
   $$ \langle f, g \rangle = \int_0^\pi \frac{1}{2}\sin(2x) dx = \frac{1}{2} \left[ -\frac{1}{2}\cos(2x) \right]_0^\pi $$
   $$ \langle f, g \rangle = -\frac{1}{4} ( \cos(2\pi) - \cos(0) ) = -\frac{1}{4} (1 - 1) = 0 $$
5. **Conclusion :** Le produit scalaire est nul, donc les fonctions $f(x) = \sin(x)$ et $g(x) = \cos(x)$ sont orthogonales dans $L^2([0, \pi])$.
