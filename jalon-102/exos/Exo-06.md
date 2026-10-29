# Exercice 6

## Exercice 6 : Convergence faible et orthogonalité dans un Hilbert \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $H$ un espace de Hilbert et $(e_n)_{n \ge 1}$ un système orthonormé. Montrer que $(e_n)$ converge faiblement vers $0$.

**Correction :**
*Analyse de l'énoncé :* On utilise le théorème de représentation de Riesz pour un espace de Hilbert et l'inégalité de Bessel.
*Résolution pas-à-pas :*
1. **Étape 1 : Représentation des formes linéaires.**
   Soit $f \in H^*$. D'après le théorème de représentation de Riesz, il existe un unique vecteur $y \in H$ tel que pour tout $x \in H$, $f(x) = \langle y, x \rangle$.
2. **Étape 2 : Évaluation sur la famille orthonormée.**
   Nous devons évaluer $\lim_{n \to \infty} f(e_n) = \lim_{n \to \infty} \langle y, e_n \rangle$.
   Les scalaires $c_n = \langle y, e_n \rangle$ sont précisément les coefficients de Fourier du vecteur $y$ par rapport au système orthonormé $(e_n)$.
3. **Étape 3 : Inégalité de Bessel.**
   L'inégalité de Bessel stipule que pour tout vecteur $y$ et tout système orthonormé $(e_n)$, la série des carrés des modules des coefficients de Fourier converge et :
   $$\sum_{n=1}^\infty |\langle y, e_n \rangle|^2 \le \|y\|^2$$
   Puisque la série converge, son terme général tend nécessairement vers 0.
   Ainsi, $\lim_{n \to \infty} |\langle y, e_n \rangle|^2 = 0$, ce qui implique que $\lim_{n \to \infty} \langle y, e_n \rangle = 0$.
4. **Étape 4 : Conclusion.**
   Nous avons montré que pour tout $f \in H^*$, $\lim_{n \to \infty} f(e_n) = 0$.
   Cela signifie exactement que $e_n \rightharpoonup 0$ faiblement dans $H$.
