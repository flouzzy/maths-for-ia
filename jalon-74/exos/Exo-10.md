### Exercice 10 : Inégalité de Clarkson (Introduction) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Dans un espace de Hilbert ($p=2$), l'identité du parallélogramme stipule que $\|f+g\|_2^2 + \|f-g\|_2^2 = 2(\|f\|_2^2 + \|g\|_2^2)$. Montrer comment Minkowski permet de borner par le bas $\|f+g\|_p^p + \|f-g\|_p^p$ pour $p \ge 2$.

**Correction Détaillée :**
1. L'identité du parallélogramme est une propriété géométrique stricte de la norme 2 induite par un produit scalaire.
2. Pour $p \ge 2$, l'inégalité de Clarkson stipule que pour $f, g \in L^p$ :
$$\|f+g\|_p^p + \|f-g\|_p^p \le 2^{p-1}(\|f\|_p^p + \|g\|_p^p)$$
3. Utilisons la convexité de la fonction $\phi(x) = |x|^p$ pour $p \ge 2$.
4. $\left| \frac{f+g}{2} \right|^p \le \frac{1}{2}|f|^p + \frac{1}{2}|g|^p$ par convexité (Jensen discrète).
5. De même, $\left| \frac{f-g}{2} \right|^p \le \frac{1}{2}|f|^p + \frac{1}{2}|-g|^p = \frac{1}{2}|f|^p + \frac{1}{2}|g|^p$.
6. En sommant ces deux inégalités :
$$\left| \frac{f+g}{2} \right|^p + \left| \frac{f-g}{2} \right|^p \le |f|^p + |g|^p$$
7. En multipliant par $2^p$ de chaque côté :
$$|f+g|^p + |f-g|^p \le 2^p(|f|^p + |g|^p)$$
(Note: La véritable inégalité de Clarkson offre une borne plus serrée avec $2^{p-1}$ pour $p \ge 2$, prouvable en utilisant des arguments de calcul différentiel sur les exposants, mais l'inégalité basique ci-dessus illustre comment Jensen et Minkowski s'entremêlent pour étudier la géométrie des boules dans les espaces $L^p$).
