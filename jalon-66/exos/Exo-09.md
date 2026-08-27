# Exercice 9 : Intégrale avec une mesure à densité
$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ l'espace mesuré usuel.
Soit $h : \mathbb{R} \to \mathbb{R}_+$ une fonction mesurable positive fixée.
On définit une application $\mu : \mathcal{B}(\mathbb{R}) \to [0, +\infty]$ par :
$\mu(A) = \int_{\mathbb{R}} \mathbf{1}_A \cdot h \, d\lambda$.
1. On admet que $\mu$ est une mesure (mesure à densité).
2. Démontrer que pour toute fonction étagée positive $s$, $\int_{\mathbb{R}} s \, d\mu = \int_{\mathbb{R}} s \cdot h \, d\lambda$.

**Correction :**
1. Soit $s$ une fonction étagée positive, avec sa forme canonique $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$.
2. Par définition de l'intégrale d'une étagée selon la mesure $\mu$ :
   $$\int_{\mathbb{R}} s \, d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
3. On remplace $\mu(A_i)$ par sa définition $\mu(A_i) = \int_{\mathbb{R}} \mathbf{1}_{A_i} h \, d\lambda$ :
   $$\int_{\mathbb{R}} s \, d\mu = \sum_{i=1}^n a_i \left( \int_{\mathbb{R}} \mathbf{1}_{A_i} h \, d\lambda \right)$$
4. Utilisons la linéarité de l'intégrale de Lebesgue (par rapport à $\lambda$) pour faire rentrer la somme et les coefficients à l'intérieur de l'intégrale. Les fonctions $a_i \mathbf{1}_{A_i} h$ sont toutes mesurables positives.
   $$\int_{\mathbb{R}} s \, d\mu = \int_{\mathbb{R}} \left( \sum_{i=1}^n a_i \mathbf{1}_{A_i} h \right) d\lambda$$
5. On factorise la fonction $h$ dans l'intégrande :
   $$\int_{\mathbb{R}} s \, d\mu = \int_{\mathbb{R}} \left( \sum_{i=1}^n a_i \mathbf{1}_{A_i} \right) h \, d\lambda$$
6. Le terme entre parenthèses est exactement la fonction étagée $s$.
   On conclut :
   $$\int_{\mathbb{R}} s \, d\mu = \int_{\mathbb{R}} s \cdot h \, d\lambda$$
   *Ce processus s'étend par supremum, justifiant le calcul pratique des espérances via la densité $f_X$ en probabilités.*
