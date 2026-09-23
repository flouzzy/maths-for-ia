# Exercice 6 : Espace $L^2$ (★★★☆☆)

**Énoncé :**
On considère l'espace hilbertien $L^2(0, +\infty)$ muni de la mesure $e^{-x} dx$. Le produit scalaire est $\langle f, g \rangle = \int_0^{+\infty} f(x)g(x)e^{-x} dx$.
Vérifier que les polynômes $L_0(x) = 1$ et $L_1(x) = 1 - x$ forment une famille orthogonale de norme 1 (début de la famille des polynômes de Laguerre).

**Correction Détaillée :**
*Analyse de l'énoncé :* Il faut calculer la norme de $L_0$, la norme de $L_1$ et leur produit scalaire avec la mesure donnée (fonction de pondération $e^{-x}$). On rappelle que $\int_0^\infty x^n e^{-x} dx = n!$.

*Résolution pas-à-pas :*
1. **Norme de $L_0$ :**
   $$ \|L_0\|^2 = \int_0^{+\infty} 1^2 e^{-x} dx = [-e^{-x}]_0^{+\infty} = (0) - (-1) = 1 $$

2. **Orthogonalité :**
   $$ \langle L_0, L_1 \rangle = \int_0^{+\infty} 1 \cdot (1 - x) e^{-x} dx = \int_0^{+\infty} e^{-x} dx - \int_0^{+\infty} x e^{-x} dx $$
   La première intégrale vaut $1$. La seconde se fait par parties ($u=x, v'=-e^{-x}$) et vaut $1! = 1$.
   Donc $\langle L_0, L_1 \rangle = 1 - 1 = 0$.

3. **Norme de $L_1$ :**
   $$ \|L_1\|^2 = \int_0^{+\infty} (1 - x)^2 e^{-x} dx = \int_0^{+\infty} (1 - 2x + x^2) e^{-x} dx $$
   Par linéarité de l'intégrale :
   $$ \|L_1\|^2 = \int_0^{+\infty} e^{-x} dx - 2\int_0^{+\infty} x e^{-x} dx + \int_0^{+\infty} x^2 e^{-x} dx $$
   $$ \|L_1\|^2 = 1 - 2(1!) + 2! = 1 - 2 + 2 = 1 $$

La famille $(L_0, L_1)$ est donc bien orthonormale dans cet espace pondéré.
