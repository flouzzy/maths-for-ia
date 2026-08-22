# Exercice 7 : L'intégrale avec mesure pondérée $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$, on définit la mesure $\nu$ de densité (pondérée) telle que $\nu(A) = \int_A x^2 \, d\lambda(x)$ pour tout borélien $A$, où $\lambda$ est la mesure de Lebesgue.
Soit $s(x) = \mathbf{1}_{[0, 2]}(x) + 3 \cdot \mathbf{1}_{]2, 3]}(x)$.
Calculer $\int_{\mathbb{R}} s \, d\nu$.

**Correction Détaillée :**
1. $s$ est une fonction étagée positive avec $A_1 = [0, 2]$ et $a_1 = 1$, puis $A_2 = ]2, 3]$ et $a_2 = 3$.
2. Par définition de l'intégrale étagée par rapport à la mesure $\nu$ :
   $$\int_{\mathbb{R}} s \, d\nu = 1 \cdot \nu([0, 2]) + 3 \cdot \nu(]2, 3])$$
3. Calculons les mesures pondérées de ces deux ensembles. Par définition de $\nu$ (qui s'appuie sur une intégrale de Riemann/Lebesgue classique de la fonction continue $x^2$) :
   $$\nu([0, 2]) = \int_{[0, 2]} x^2 \, d\lambda(x) = \left[ \frac{x^3}{3} \right]_0^2 = \frac{8}{3}$$
   $$\nu(]2, 3]) = \int_{]2, 3]} x^2 \, d\lambda(x) = \left[ \frac{x^3}{3} \right]_2^3 = \frac{27}{3} - \frac{8}{3} = \frac{19}{3}$$
4. En injectant ces résultats dans la formule de l'intégrale :
   $$\int_{\mathbb{R}} s \, d\nu = 1 \times \frac{8}{3} + 3 \times \frac{19}{3}$$
5. Le calcul final donne :
   $$\int_{\mathbb{R}} s \, d\nu = \frac{8}{3} + 19 = \frac{8 + 57}{3} = \frac{65}{3}$$
